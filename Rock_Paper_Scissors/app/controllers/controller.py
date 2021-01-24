from app import app
from flask import render_template, request
from app.models.player import *
from app.models.game import *
from app.models.game_play import *

# @app.route('/')
# def index():
#     return "Hello World!"

# @app.route('/<choice1>/<choice2>')
# def player_choices(choice1, choice2):
#     return game_result(choice1, choice2)

@app.route('/game')
def index():
    return render_template('game_play.html') #gives the form on the page

@app.route('/game', methods = ['POST'])
def add_players():
    if request.method == 'POST':
        player1_name = request.form['name1']
        player1_choice = request.form['choice1']
        player2_name = request.form['name2']
        player2_choice = request.form['choice2'] #gives a form which takes inputs
        player1 = Player(player1_name, player1_choice)
        player2 = Player(player2_name, player2_choice)
        # add_player(player1)
        # add_player(player2) printed out players
        result = game_result(player1_choice, player2_choice)
        return render_template('game_play.html', result=result)
