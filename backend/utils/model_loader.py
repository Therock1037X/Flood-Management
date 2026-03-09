import joblib
from backend.config import Config

def load_model():
    """
    Load the trained flood prediction model and label encoder.
    """

    model_data = joblib.load(Config.MODEL_PATH)

    model = model_data["model"]
    encoder = model_data["encoder"]

    return model, encoder