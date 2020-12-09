# this is an example for cortex release 0.24 and may not deploy correctly on other releases of cortex

import mlflow.sklearn
import numpy as np


class PythonPredictor:
    def __init__(self, config, python_client):
        self.client = python_client

    def load_model(self, model_path):
        return mlflow.sklearn.load_model(model_path)

    def predict(self, payload, query_params):
        model_version = query_params.get("version")

        model = self.client.get_model(model_version=model_version)
        model_input = [
            payload["cylinders"],
            payload["displacement"],
            payload["horsepower"],
            payload["weight"],
            payload["acceleration"],
        ]
        result = model.predict([model_input]).item()

        return {"prediction": result, "model": {"version": model_version}}