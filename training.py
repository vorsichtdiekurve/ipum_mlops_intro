from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib


def load_data():
    return load_iris()


def train_model(data):
    x, y = data.data, data.target_names[data.target]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    model = DecisionTreeClassifier()
    model.fit(x_train, y_train)
    return model


def save_model(model):
    with open("ml/iris.mdl", "wb") as f:
        joblib.dump(model, f)
