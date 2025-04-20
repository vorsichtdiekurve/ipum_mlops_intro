import os.path

import numpy as np

import training
import inference

from fastapi import FastAPI
from api.models.iris import PredictRequest, PredictResponse


def create_model():
    data = training.load_data()
    model = training.train_model(data)
    training.save_model(model)


if not os.path.exists("ml/iris.mdl"):
    create_model()

model = inference.load_model()

app = FastAPI()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    input_features = np.array(
        [
            request.sepal_length,
            request.sepal_width,
            request.petal_length,
            request.petal_width,
        ]
    )
    prediction = inference.predict(model, input_features)
    return PredictResponse(prediction=prediction)
