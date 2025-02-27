"""
Module to define the Hand class.
"""

from flask import Flask, render_template, session, request, redirect, url_for, flash
from src.scoreboard import Scoreboard
from src.hand import Hand

app = Flask(__name__)

app.secret_key = 'zoeofilippaarsjalvmordsbenagnaochelinmed'

@app.route("/")
def main():
    """
    Main route for the Yahtzee web application.
    Creates a Hand object and renders the 'main.html' template with the hand.
    Returns:
        str: Rendered HTML template.
    """
    if 'reroll_count' not in session:
        session['reroll_count'] = 0
    if "scoreboard" not in session:
        # Skapa en ny Scoreboard om det inte finns i sessionen
        scoreboard = Scoreboard()
        session["scoreboard"] = scoreboard.to_json()  # Spara som JSON-sträng
    else:
        # Ladda Scoreboard från sessionen
        scoreboard_data = session["scoreboard"]
        scoreboard = Scoreboard.from_json(scoreboard_data)

    if "hand" not in session:
        session["hand"] = Hand().to_list()

    hand = Hand(dice_values=session["hand"])
    return render_template('index.html', hand=hand,
                           scoreboard=scoreboard, reroll_count=session['reroll_count'])

@app.route("/about")
def about():
    """
    About route for the Yahtzee web application.
    Renders the 'about.html' template.
    Returns:
        str: Rendered HTML template.
    """
    return render_template('about.html')

@app.route("/reset")
def reset():
    """
    session reset
    """
    session.clear()
    session['reroll_count'] = 0
    session['rule_selected'] = False
    session["hand"] = Hand().to_list()
    session["scoreboard"] = Scoreboard().to_json()
    return redirect(url_for("main"))

@app.route("/choose_rule", methods=["POST"])
def choose_rule():
    """
    flash om att man måste välja regel.
    sätter poäng för rule och tar bort valmöjligheten för den regeln man valt.
    """
    rule_name = request.form.get("chosen_rule")
    if not rule_name:
        flash("You must select a rule!", "error")
        return redirect(url_for("main"))

    scoreboard_data = session.get("scoreboard", "{}")
    scoreboard = Scoreboard.from_json(scoreboard_data)

    hand = Hand(dice_values=session.get("hand", []))

    try:
        scoreboard.add_points(rule_name, hand)
        session["scoreboard"] = scoreboard.to_json()
        session["hand"] = Hand().to_list()
        session['reroll_count'] = 0

        if scoreboard.finished():
            flash(f"""All rules have been selected! Game over!
            Your total score was {scoreboard.get_total_points()}.
            Great job!""", "end")
            return redirect(url_for("main"))

    except ValueError as e:
        flash(str(e), "error")

    return redirect(url_for("main"))

@app.route("/reroll", methods=["POST"])
def reroll():
    """
    räknar så man inte kan slå om mer än 2 gånger.
    """
    if 'reroll_count' not in session:
        session['reroll_count'] = 0

    if session['reroll_count'] < 2:
        session['reroll_count'] += 1
        session.modified = True
    hand = Hand(dice_values=session.get("hand", []))

    reroll_indices = request.form.getlist("reroll")
    reroll_indices = [int(i) for i in reroll_indices]

    hand.roll(reroll_indices)

    session["hand"] = hand.to_list()

    return redirect(url_for("main"))

if __name__ == '__main__':
    app.run(debug=True)
