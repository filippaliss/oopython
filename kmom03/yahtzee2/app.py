"""
Module to define the Hand class.
"""

from flask import Flask, render_template
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
    return render_template('index.html', hand=hand)

@app.route("/about")
def about():
    """
    About route for the Yahtzee web application.
    Renders the 'about.html' template.
    Returns:
        str: Rendered HTML template.
    """
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
