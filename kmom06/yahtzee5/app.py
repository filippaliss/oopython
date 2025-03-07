"""
Module to define the Hand class.
"""

from flask import Flask, render_template, session, request, redirect, url_for, flash
from src.scoreboard import Scoreboard
from src.hand import Hand
from src.unorderedlist import UnorderedList
from src.sort import recursive_insertion
from src.node import Node


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

    players = load_leaderboard()

    players.append((name, score))


    with open("leaderboard.txt", "w", encoding="utf-8") as f:
        for player in players:
            f.write(f"{player[0]}: {player[1]}\n")

    session.clear()
    return redirect(url_for("main"))


def load_leaderboard():
    """
    Läser in leaderboard.txt och returnerar en lista med tuples (namn, poäng).
    Hanterar felaktiga rader och saknad fil.
    """
    players = []
    try:
        with open("leaderboard.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(": ")
                if len(parts) == 2:  # Kolla att raden är korrekt formatterad
                    name, score = parts
                    try:
                        players.append((name, int(score)))  # Konvertera score till int
                    except ValueError:
                        print(f"Ogiltigt poängvärde, hoppar över: {line.strip()}")
                else:
                    print(f"Felaktigt format, hoppar över: {line.strip()}")

    except FileNotFoundError:
        pass

    unordered_list = UnorderedList()
    for player in players:
        unordered_list.add(player)

    recursive_insertion(unordered_list)

    sorted_players = []
    for i in range(unordered_list.size()):
        sorted_players.append(unordered_list.get(i))

    return sorted_players


@app.route('/leaderboard')
def leaderboard():
    """
    Visar leaderboard-sidan med spelarpoäng och ett formulär för att ta bort spelare.
    """
    players = load_leaderboard()
    return render_template('leaderboard.html', players=players, num_entries=len(players))

@app.route('/remove_player/<player>', methods=['POST'])
def remove_player(player):
    """
    Removes a player from the leaderboard based on the user's choice.
    """
    players = load_leaderboard()
    new_players = [(p, s) for p, s in players if p != player]

    with open("leaderboard.txt", "w", encoding="utf-8") as f:
        for name, score in new_players:
            f.write(f"{name}: {score}\n")

    return redirect(url_for('leaderboard'))


if __name__ == '__main__':
    app.run(debug=True)
