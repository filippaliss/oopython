"""
Module to define the Hand class.
"""

from flask import Flask, render_template, session, request, redirect, url_for, flash
from src.scoreboard import Scoreboard
from src.hand import Hand
from src.leaderboard import Leaderboard

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
        scoreboard = Scoreboard()
        session["scoreboard"] = scoreboard.to_json()
    else:
        scoreboard_data = session["scoreboard"]
        scoreboard = Scoreboard.from_json(scoreboard_data)

    if "hand" not in session:
        session["hand"] = Hand().to_list()

    hand = Hand(dice_values=session["hand"])
    game_over = session.get('game_over', False)
    return render_template('index.html', hand=hand,
                           scoreboard=scoreboard, reroll_count=session['reroll_count'],
                           game_over=game_over)

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
            session['game_over'] = True
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


@app.route("/submit", methods=["POST"])
def submit_score():
    """
    Lägger till spelarens poäng i leaderboarden och sparar till filen.
    """
    name = request.form["name"]
    score = int(request.form["score"])

    game_leaderboard = Leaderboard()
    game_leaderboard.load("leaderboard.txt")
    game_leaderboard.add_player(name, score)
    game_leaderboard.save_to_file()

    session.clear()
    return redirect(url_for("main"))

@app.route('/leaderboard')
def leaderboard():
    """
    Visar leaderboard-sidan med spelarpoäng och ett formulär för att ta bort spelare.
    """
    game_leaderboard = Leaderboard()
    game_leaderboard.load("leaderboard.txt")
    players = game_leaderboard.get_players()  # Använd den nya metoden

    return render_template('leaderboard.html', players=players, num_entries=len(players))

@app.route('/remove_player/<player>', methods=['POST'])
def remove_player(player):
    """
    Removes a player from the leaderboard based on the user's choice.
    """
    game_leaderboard = Leaderboard()
    game_leaderboard.load("leaderboard.txt")

    game_leaderboard.remove_player(player)
    game_leaderboard.save_to_file()

    return redirect(url_for('leaderboard'))

if __name__ == '__main__':
    app.run(debug=True)
