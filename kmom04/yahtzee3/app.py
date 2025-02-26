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
    return render_template('index.html', hand=hand, scoreboard=scoreboard, reroll_count=session['reroll_count'])

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
    session.clear()
    session['reroll_count'] = 0  # Återställ räknaren när en regel väljs
    session['rule_selected'] = False
    session["hand"] = Hand().to_list()  # Återställ tärningarna
    session["scoreboard"] = Scoreboard().to_json()
    return redirect(url_for("main"))

@app.route("/choose_rule", methods=["POST"])
def choose_rule():
    rule_name = request.form.get("chosen_rule")  # Fixad namnförvirring här
    if not rule_name:
        flash("You must select a rule!", "error")
        return redirect(url_for("main"))

    # Ladda scoreboard från session
    scoreboard_data = session.get("scoreboard", "{}")
    scoreboard = Scoreboard.from_json(scoreboard_data)

    # Ladda hand från session
    hand = Hand(dice_values=session.get("hand", []))

    try:
        scoreboard.add_points(rule_name, hand)
        session["scoreboard"] = scoreboard.to_json()  # Spara tillbaka i sessionen
        session["hand"] = Hand().to_list()  # Återställ handen för nästa runda
        session['reroll_count'] = 0  # Återställ räknaren när en regel väljs
    except ValueError as e:
        flash(str(e), "error")
    

    return redirect(url_for("main"))

@app.route("/reroll", methods=["POST"])
def reroll():
    if 'reroll_count' not in session:
        session['reroll_count'] = 0 

    if session['reroll_count'] < 2:
        session['reroll_count'] += 1
        session.modified = True
    # Hämta nuvarande hand från sessionen
    hand = Hand(dice_values=session.get("hand", []))

    # Hämta vilka tärningar som ska slås om (de markerade checkboxarna)
    reroll_indices = request.form.getlist("reroll")  # Hämtar lista med index (som strängar)
    reroll_indices = [int(i) for i in reroll_indices]  # Konvertera till heltal

    # Slå om de valda tärningarna
    hand.roll(reroll_indices)

    # Spara den uppdaterade handen i sessionen
    session["hand"] = hand.to_list()

    return redirect(url_for("main"))  # Ladda om sidan för att visa nya tärningar


if __name__ == '__main__':
    app.run(debug=True)
