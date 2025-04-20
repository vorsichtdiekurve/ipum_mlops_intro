import joblib


def load_model():
    with open("ml/iris.mdl", "rb") as f:
        model = joblib.load(f)
    return model


def predict(model, features):
    prediction = model.predict([features])[0]
    return prediction
