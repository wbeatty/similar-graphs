import os

import pandas as pd

os.makedirs("static/data", exist_ok=True)


def generate_graph(pair):
    db1 = pd.read_csv(f"static/data/{pair[0]}")
    db2 = pd.read_csv(f"static/data/{pair[1]}")

    index1 = db1.columns[0]
    index2 = db2.columns[0]

    data1 = db1.columns[1:]
    data2 = db2.columns[1:]

    db1.rename(columns={index1: "date"}, inplace=True)
    db2.rename(columns={index2: "date"}, inplace=True)

    db1["date"] = pd.to_datetime(db1["date"], utc=True).dt.date
    db2["date"] = pd.to_datetime(db2["date"], utc=True).dt.date
    ## Drop the open, high, low, and volume columns
    db1.set_index("date", inplace=True)
    db2.set_index("date", inplace=True)

    shared_indices = db1.index.intersection(db2.index)

    db1_filtered = db1.loc[shared_indices]
    db2_filtered = db2.loc[shared_indices]

    merged_data = pd.concat(
        [
            db1_filtered[data1].rename(pair[0] + "_" + data1),
            db2_filtered[data2].rename(pair[1] + "_" + data2),
        ],
        axis=1,
    )

    merged_data.dropna(inplace=True)

    merged_data.to_csv("static/data/merged_data.csv")

    names = [pair[0] + "_" + data1, pair[1] + "_" + data2]
    return names
