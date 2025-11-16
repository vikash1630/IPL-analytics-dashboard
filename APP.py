from flask import Flask,render_template,request,jsonify
import API
app = Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html")

@app.route("/win-probability")
def prob():
    result = API.Teams()
    return render_template("challenge.html",teams = result['teams'])

@app.route("/teams")
def teams():
    result = API.Teams()
    return render_template('teams.html', teams = result['teams'])


@app.route("/team/<team>")
def team_profile(team):
    data = API.Team_Data(team)        # call your function

    if "error" in data:
        return f"<h1>{data['error']}</h1>"

    return render_template("team_profile.html", team=team, data=data)


@app.route("/win-probability/<t1>vs<t2>")
def TeamVsTeam(t1,t2):

    data = API.TeamVTeam(t1,t2)
    
    return render_template("TeamVsTeam.html", data = data)


@app.route("/<team>/players")
def players(team):

    data = API.Team_Players(team)

    return render_template("Players.html", data = data)


if __name__ == "__main__":
    app.run(debug = True)




