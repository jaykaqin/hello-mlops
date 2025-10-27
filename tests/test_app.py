from app.main import app


def client():
    app.testing = True
    return app.test_client()


def test_health():
    rv = client().get("/health")
    assert rv.status_code == 200 and rv.json["status"] == "ok"


def test_predict_typical():
    rv = client().post("/predict", json={"x": [1, 2, 3]})
    assert rv.status_code == 200 and rv.json["y"] == 3


def test_predict_edge_empty():
    rv = client().post("/predict", json={"x": []})
    assert rv.status_code == 200 and rv.json["y"] == 0
