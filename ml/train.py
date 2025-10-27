import os
import time
import joblib

import mlflow
import mlflow.sklearn
from pathlib import Path


# 极简：把 data.csv 的行数当作“指标”，把模型存个占位文件
DATA = Path("data/data.csv")
REG_DIR = Path("ml/registry")
REG_DIR.mkdir(parents=True, exist_ok=True)
MODEL_PATH = REG_DIR / "model.pkl"

mlflow.set_experiment("hello-mlops")

def run(exp_name="baseline"):
    with mlflow.start_run(run_name=exp_name):
        # 参数
        mlflow.log_param("exp_name", exp_name)
        # “指标”：行数（示意）
        lines = sum(1 for _ in open(DATA, "r", encoding="utf-8"))
        mlflow.log_metric("line_count", lines)
        # 伪“模型”文件
        joblib.dump({"note":"hello-model","lines":lines}, MODEL_PATH)
        mlflow.log_artifact(str(MODEL_PATH))
        print(f"✅ {exp_name} done. lines={lines}")

if __name__ == "__main__":
    run("baseline")
    time.sleep(1)
    run("improved")
