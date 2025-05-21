import json
import os
import random

import pandas as pd
from flask import Flask, jsonify, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

import graphscript

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_graph_data")
def get_graph_data():
    ## Open up the pairings file and select a random pair
    with open("static/data/pairings.json", "r") as f:
        pairings = json.load(f)
        selected = random.choice(pairings)
        ## Pass selected pair to graphscript to generate the graph
        names = graphscript.generate_graph(selected)

    ## Read in the graph_data.csv file
    csv_path = os.path.join(app.static_folder, "data", "merged_data.csv")
    df = pd.read_csv(csv_path)
    data = {
        "Date": df["date"].tolist(),
        names[0]: df[names[0]].tolist(),
        names[1]: df[names[1]].tolist(),
    }
    ## Return the data as a JSON object
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
