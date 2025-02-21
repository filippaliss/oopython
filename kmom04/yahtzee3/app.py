"""
Module to define the Hand class.
"""

from flask import Flask, render_template
from src.scoreboard import Scoreboard
from src.hand import Hand

app = Flask(__name__)


@app.route("/")
def main():
    """
    Main route for the Yahtzee web application.
    Creates a Hand object and renders the 'main.html' template with the hand.
    Returns:
        str: Rendered HTML template.
    """
    hand = Hand()
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
    hand = Hand()
    return render_template('index.html', hand=hand)

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
