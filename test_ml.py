import pytest

# TODO: add necessary import
import numpy as np 
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from ml.data import process_data
from ml.model import train_model, inference, compute_model_metrics

# TODO: implement the first test. Change the function name and input as needed
# Fixture to provide sample data for tests
@pytest.fixture
def sample_data():
    """
    Creates a small sample dataset to use in unit tests.
    Returns processed features, labels, encoder, and label binarizer.
    """
    data = pd.DataFrame({
        "age": [25, 30, 22, 40],
        "workclass": ["Private", "Self-emp", "Private", "Government"],
        "education": ["Bachelors", "HS-grad", "Masters", "PhD"],
        "marital-status": ["Never-married", "Married-civ-spouse", "Divorced", "Married-civ-spouse"],
        "occupation": ["Tech-support", "Exec-managerial", "Sales", "Prof-specialty"],
        "relationship": ["Not-in-family", "Husband", "Own-child", "Wife"],
        "race": ["White", "Black", "White", "Asian-Pac-Islander"],
        "sex": ["Male", "Female", "Male", "Female"],
        "native-country": ["United-States", "United-States", "United-States", "United-States"],
        "salary": [0, 1, 0, 1],
    })
    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]
    X, y, encoder, lb = process_data(
        data, categorical_features=cat_features, label="salary", training=True
    )
    return X, y, encoder, lb

def test_one(sample_data):
    """
    Test that train_model returns a RandomForestClassifier instance.
    """
    X, y, _, _ = sample_data
    model = train_model(X, y)
    assert isinstance(model, RandomForestClassifier), "Model should be RandomForestClassifier"


# TODO: implement the second test. Change the function name and input as needed
def test_two(sample_data):
    """
    Test that inference returns a numpy array with the correct length.
    """
    X, y, _, _ = sample_data
    model = train_model(X, y)
    preds = inference(model, X)
    assert isinstance(preds, np.ndarray), "Inference output should be a numpy array"
    assert preds.shape[0] == X.shape[0], "Predictions should have same length as input data"


# TODO: implement the third test. Change the function name and input as needed
def test_three(sample_data):
    """
    Test that compute_model_metrics returns precision, recall, and fbeta as floats.
    """
    X, y, _, _ = sample_data
    model = train_model(X, y)
    preds = inference(model, X)
    precision, recall, fbeta = compute_model_metrics(y, preds)
    for metric in [precision, recall, fbeta]:
        assert isinstance(metric, float), "Metrics should be floats"
