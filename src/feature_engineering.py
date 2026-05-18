import numpy as np
import pandas as pd

def add_features(df):
    df = df.copy()

    df["vu_x_attachment"] = df["vu"] * df["attachment_size"]
    df["attachment_log"] = np.log1p(df["attachment_size"])
    df["load_factor"] = df["vu"] * np.log1p(df["attachment_size"])

    df["vu_bin"] = pd.cut(
        df["vu"],
        bins=[0, 50, 100, 150, 200, 300],
        labels=False
    )

    return df
    