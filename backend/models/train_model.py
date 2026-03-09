import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Project root → FLOOD MANAGEMENT
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Model directory → backend/models
MODEL_DIR = os.path.join(BASE_DIR, "backend", "models")
MODEL_PATH = os.path.join(MODEL_DIR, "flood_model.pkl")

np.random.seed(42)

def train_model():

    os.makedirs(MODEL_DIR, exist_ok=True)

    # Generate 500 synthetic training samples
    n = 500

    rainfall = np.random.randint(10, 250, n)
    elevation = np.random.randint(170, 290, n)
    drain_capacity = np.random.uniform(0.1, 1.0, n)
    population_density = np.random.randint(1000, 50000, n)

    # Derive labels
    risk_score = (
        (rainfall / 250) * 0.4 +
        (1 - drain_capacity) * 0.35 +
        ((290 - elevation) / 120) * 0.25
    )

    labels = []
    for rs in risk_score:
        if rs > 0.55:
            labels.append("HIGH")
        elif rs > 0.35:
            labels.append("MEDIUM")
        else:
            labels.append("LOW")

    X = np.column_stack([rainfall, elevation, drain_capacity, population_density])
    y = np.array(labels)

    le = LabelEncoder()
    y_enc = le.fit_transform(y)

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y_enc)

    # Save model + encoder
    joblib.dump({"model": clf, "encoder": le}, MODEL_PATH)

    print(f"Model trained on {n} samples")
    print(f"Classes: {le.classes_}")
    print(f"Training accuracy: {clf.score(X, y_enc):.3f}")
    print(f"Model saved to: {MODEL_PATH}")

    return clf, le


if __name__ == "__main__":
    train_model()