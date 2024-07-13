from calendar import month
from tkinter import Variable
from unittest import result
from networkx import out_degree_centrality
from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import pickle
import os

app = Flask(__name__)
model = pickle.load(open('Random_forest.pkl', 'rb'))
    

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods = ['POST', 'GET'])
def predict():
    try:
        
        Seller_Type_Individual = str(request.form["Seller_Type_Individual"])
        Car_Model = str(request.form["Car_Model"])
        Mileage = int(request.form["Mileage"])
        Fuel_Type_Petrol = str(request.form["Fuel_Type_Petrol"])
        Registration = str(request.form["Registration"])
        Year = int(request.form["Year"])

        prediction = model.predict([[Seller_Type_Individual, Car_Model, Mileage, Fuel_Type_Petrol, Registration, Year]])
        
        
        
        return render_template("index.html", prediction_text='{}'.format(prediction))
    except Exception as e:
        return jsonify({"error": str(e)})
if __name__ == '__main__':
    app.run(debug=True)
    
    