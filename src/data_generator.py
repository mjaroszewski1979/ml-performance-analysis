import pandas as pd
import numpy as np

def generate_synthetic_data(n=200):
    np.random.seed(42)

    df = pd.DataFrame({
        "vu": np.random.randint(10, 300000, n),
        "attachment_size": np.random.uniform(0.1, 50, n),
        "test_duration": np.random.choice([300, 600, 900], n)
    })

    # syntetyczna logika KO (imitacja systemu)
    df["ko_flag"] = (
        (df["vu"] > 150000) &
        (df["attachment_size"] > 10)
    ).astype(int)

    return df