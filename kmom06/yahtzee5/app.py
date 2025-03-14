"""
Module to define the Hand class.
"""
from flask import Flask, render_template, session, request, redirect, url_for, flash
from src.scoreboard import Scoreboard
from src.hand import Hand
from src.unorderedlist import UnorderedList
from src.sort import recursive_insertion
from src.queue import Queue
from src.leaderboard import Leaderboard


app = Flask(__name__)

app.secret_key = 'zoeofilippaarsjalvmordsbenagnaochelinmed'
players = {}  # Global dictionary för att lagra spelarnas scoreboards


@app.route("/")
def main():
    """
    Main route for the Yahtzee web application.
    Skapa en Hand och rendera 'main.html' med rätt Scoreboard.
    """
    if 'reroll_count' not in session:
        session['reroll_count'] = 0


    if "player_queue" in session:
        print(session["player_queue"])

    if "current_player" not in session:
        player_keys = list(players.keys())
        if len(player_keys) != 0:  # Se till att listan inte är tom
            session["current_player"] = player_keys[0]  # Första spelaren startar
        else:
            flash("No players found. Please add players.", "error")
            return redirect(url_for("choose_players"))

    print(players)
    print(session["player_queue"][0])
    print(session["player_queue"][0]["name"])
    scoreboard_json = session["player_queue"][0]["scoreboard"]
    scoreboard = Scoreboard().from_json(scoreboard_json)

    if "hand" not in session:
        session["hand"] = Hand().to_list()

    hand = Hand(dice_values=session["hand"])
    game_over = session.get('game_over', False)

    return render_template(
        'index.html', hand=hand, scoreboard=scoreboard,
         reroll_count=session['reroll_count'], game_over=game_over)

@app.route("/about")
def about():
    """
    About route for the Yahtzee web application.
    Renders the 'about.html' template.
    Returns:
        str: Rendered HTML template.
    """
    return render_template('about.html')

@app.route("/reset", methods=["GET"])
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
    Spelaren väljer en regel och turen går vidare.
    """
    rule_name = request.form.get("chosen_rule")
    if not rule_name:
        flash("You must select a rule!", "error")
        return redirect(url_for("main"))

    player_queue_list = session.get("player_queue")
    current_player = player_queue_list[0]
    scoreboard_data = current_player["scoreboard"]
    scoreboard = Scoreboard().from_json(scoreboard_data)
    player_queue = Queue()

    for player in player_queue_list:
        player_queue.enqueue(player)

    # Skapa en kopia av spelarlistan om den inte redan finns
    if "copy_player_list" not in session:
        session["copy_player_list"] = player_queue.to_list()

    player_queue.dequeue()

    hand = Hand(dice_values=session.get("hand", []))

    try:
        scoreboard.add_points(rule_name, hand)
        scoreboard_data = scoreboard.to_json()
        current_player["scoreboard"] = scoreboard_data  # Uppdatera aktuell spelares scoreboard

        # Uppdatera kopian med den nya scoreboarden
        for player in session["copy_player_list"]:
            if player["name"] == current_player["name"]:
                player["scoreboard"] = scoreboard_data  # Uppdatera spelarens scoreboard i kopian
                break  # Avsluta loopen när vi hittat rätt spelare

        session["hand"] = Hand().to_list()
        session['reroll_count'] = 0

        # Kontrollera om spelet är slut
        if scoreboard.finished() and len(player_queue.to_list()) == 0:
            session['game_over'] = True

            # Använd kopian för att hitta vinnaren
            highest_scoring_player = None
            highest_score = 0
            for player in session["copy_player_list"]:
                player_scoreboard = Scoreboard().from_json(player["scoreboard"])
                player_score = player_scoreboard.get_total_points()

                if player_score > highest_score:
                    highest_score = player_score
                    highest_scoring_player = player["name"]

            if highest_scoring_player:
                # Lägg till vinnaren i leaderboarden
                game_leaderboard = Leaderboard()
                game_leaderboard.load("leaderboard.txt")
                game_leaderboard.add_player(highest_scoring_player, highest_score)
                game_leaderboard.save_to_file()

            flash(f"""All rules have been selected! Game over!
            The winner is {highest_scoring_player} with {highest_score} points!
            """, "end")
            return redirect(url_for("main"))
        if scoreboard.finished():
            session["player_queue"] = player_queue.to_list()
            session["current_player"] = player_queue.peek()  # Uppdatera aktuell spelare
        else:
            player_queue.enqueue(current_player)  # Flytta första spelaren till slutet
            session["player_queue"] = player_queue.to_list()
            session["current_player"] = player_queue.peek()  # Uppdatera aktuell spelare

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

def load_leaderboard():
    """
    Läser in leaderboard.txt och returnerar en lista med tuples (namn, poäng).
    Hanterar felaktiga rader och saknad fil.
    """
    game_players = []
    game_leaderboard  = Leaderboard()
    try:
        game_leaderboard.load()
        game_players = game_leaderboard.get_players()
    except FileNotFoundError:
        pass

    unordered_list = UnorderedList()
    for player in game_players:
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
    game_players = load_leaderboard()

    return render_template('leaderboard.html', players=game_players, num_entries=len(players))

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

@app.route("/choose_players", methods=["GET", "POST"])
def choose_players():
    """
    Låt spelaren skriva in antal spelare och deras namn.
    """
    if request.method == "POST":
        try:
            num_players = int(request.form.get("num_players"))

            if num_players < 1:
                flash("Antalet spelare måste vara minst 1!", "error")
                return redirect(url_for("choose_players"))

            player_queue = Queue()

            for i in range(num_players):
                player_name = request.form.get(f"player_name_{i}")
                if not player_name:
                    flash("Alla spelare måste ha ett namn!", "error")
                    return redirect(url_for("choose_players"))

                player_object = {"name": player_name, "scoreboard": Scoreboard().to_json()}
                player_queue.enqueue(player_object)

            session["player_queue"] = player_queue.to_list()  # Spara kön i sessionen
            session["current_player"] = player_queue.peek()["name"]  # Första spelaren börjar
            #läga till scoreboard så att det görs
            session.pop("flashed_no_players", None)

            return redirect(url_for("main"))

        except ValueError:
            flash("Ange ett giltigt nummer!", "error")
            return redirect(url_for("choose_players"))

    return render_template("choose_players.html")

@app.route("/start_game", methods=["GET", "POST"])
def start_game():
    """
    Startar spelet
    """
    if request.method == "POST":
        player_name = request.form.get("player_names")

        if not player_name:
            flash("Du måste ange ett namn!", "error")
            return redirect(url_for("index"))  # Se till att den går tillbaka till huvudvyn

        if 'players' not in session:
            session['players'] = []

        session['players'].append(player_name)

    return redirect(url_for("main"))  # Korrekt endpoint för huvudsidan


@app.route("/end_turn")
def end_turn():
    """
    Slutför spelarens tur och gå till nästa spelare.
    """
    player_names = list(players.keys())
    current_player = session["current_player"]
    current_index = player_names.index(current_player)

    next_player = player_names[(current_index + 1) % len(player_names)]
    session["current_player"] = next_player  # Uppdatera till nästa spelare

    return redirect(url_for("main"))


if __name__ == '__main__':
    app.run(debug=True)
