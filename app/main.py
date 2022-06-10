import pickle
from flask import Flask
 
app = Flask(__name__)

@app.route("/", methods=['GET'])
def home_view():
        model = pickle.load(open('model/model.pkl','rb'))
        team_names = ['Gujarat Lions', 'Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals', 'Mumbai Indians', 'Sunrisers Hyderabad', 'Kings XI Punjab', 'Royal Challengers Bangalore', 'Delhi Capitals', 'Rising Pune Supergiants']
        t1 = 4
        t2 = 9
        tw = 9
        y_pred = model.predict([[t1,t2,tw,0,9,0]])[0]
        if y_pred != t1 or y_pred != t2:
                y_pred = tw
        winner = team_names[y_pred]
        response_data = {'msg' : 'done..', 'winner': winner}
        return response_data