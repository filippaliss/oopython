"""
Module to define the Hand class.
"""

from flask import Flask, render_template, session
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
    scoreboard = Scoreboard()
    return render_template('index.html', hand=hand, scoreboard=scoreboard)

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
    hand = Hand()
    scoreboard = Scoreboard()
    return render_template('index.html', hand=hand, scoreboard=scoreboard)

@app.route("/choose_rule", methods=["POST"])
def choose_rule():
    rule_name = request.form.get("choose_rule")
    if rule_name:
        try:
            scoreboard.add_points(rule_name, hand)
        except ValueError as e:
            flash(str(e), "error")
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
