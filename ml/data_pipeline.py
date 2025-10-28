import pandas as pd
from pathlib import Path


def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def simple_transform(df: pd.DataFrame) -> pd.DataFrame:
    # 演示：加一列，y/x 的比值（避免除零）
    df = df.copy()
    df["ratio"] = df["y"] / df["x"].replace(0, 1)
    return df


if __name__ == "__main__":
    from pathlib import Path

    df = load_csv("data/data.csv")
    out = simple_transform(df)
    Path("data").mkdir(exist_ok=True)
    out.to_csv("data/data_transformed.csv", index=False)
    print("saved -> data/data_transformed.csv")
