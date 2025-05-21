import os

import pandas as pd
from flask import Flask, jsonify, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_graph_data")
def get_graph_data():
    csv_path = os.path.join(app.static_folder, "data", "graph_data.csv")
    df = pd.read_csv(csv_path)
    data = {
        "Date": df["date"].tolist(),
        "AMZN Close": df["AMZN_adj_close"].tolist(),
        "SPX Close": df["SPX_adj_close"].tolist(),
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
