from flask import Flask, request, jsonify
import joblib, os

app = Flask(__name__)
MODEL_PATH = os.getenv("MODEL_PATH", "ml/registry/model.pkl")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict():
    data = request.get_json(force=True)
    x = data.get("x", [0])          # 极简示例：x 是一维或多维数值
    if not isinstance(x, list): x = [x]
    # 这里为了 Hello World，可不用真正模型：返回长度作为“预测”
    return jsonify({"y": len(x)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
