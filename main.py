from flask import Flask, redirect, send_from_directory

app = Flask(__name__)

@app.route('/team/<team_number>')
def redirect_to_team(team_number):
    print(f"Redirecting team {team_number} to FTCScout")
    return redirect(f'https://ftcscout.org/teams/{team_number}', code=301)

@app.route('/')
def homepage():
    return send_from_directory('.', 'index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('.', 'favicon.ico')

@app.route('/<path:path>')
def catch_all(path):
    print(f"Catching all for path: {path}")
    return redirect('/', code=301)
    