import pickle
from flask import Flask, render_template, request
 
app = Flask(__name__)

@app.route("/")
def home_view():
        return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
        t1 = int(request.form.get("team1"))
        t2 = int(request.form.get("team2"))
        tw = int(request.form.get("toss_winner"))
        td = int(request.form.get("toss_winner"))
        ht = int(request.form.get("home_team"))
        dm = int(request.form.get("is_death_match"))
        print(t1, t2, tw, '........... t1 ...........>>>>')
        model = pickle.load(open('model/model.pkl','rb'))
        team_names = ['Gujarat Lions', 'Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals', 'Mumbai Indians', 'Sunrisers Hyderabad', 'Kings XI Punjab', 'Royal Challengers Bangalore', 'Delhi Capitals', 'Rising Pune Supergiants']
        # t1 = 4
        # t2 = 9
        # tw = 9
        y_pred = model.predict([[t1,t2,tw,td,ht,dm]])[0]
        if y_pred != t1 or y_pred != t2:
                y_pred = tw
        print(y_pred, type(y_pred), '.....')
        winner = team_names[y_pred]
        # response_data = {'msg' : 'done..', 'winner': winner}
        # return response_data
        return render_template("result.html", result = winner)