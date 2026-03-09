import numpy as np
from utils.model_loader import load_model

model, encoder = load_model()

def predict_flood_risk(rainfall, elevation, drain_capacity, population_density):

    X = np.array([[rainfall, elevation, drain_capacity, population_density]])

    prediction = model.predict(X)
    probabilities = model.predict_proba(X)

    risk_level = encoder.inverse_transform(prediction)[0]
    confidence = float(np.max(probabilities))

    return {
        "risk_level": risk_level,
        "confidence": round(confidence, 3)
    }