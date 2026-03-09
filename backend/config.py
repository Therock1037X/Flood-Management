import os

# Root project directory → FLOOD MANAGEMENT
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "delhi-flood-intelligence-2024"
    DEBUG = True

    # Delhi city bounds
    DELHI_CENTER_LAT = 28.6139
    DELHI_CENTER_LNG = 77.2090

    # Data directories
    DATA_DIR = os.path.join(BASE_DIR, "data")

    # Model directory (inside backend)
    MODEL_DIR = os.path.join(BASE_DIR, "backend", "models")

    # Files
    WARDS_CSV = os.path.join(DATA_DIR, "wards_data.csv")
    HOTSPOTS_CSV = os.path.join(DATA_DIR, "hotspot_data.csv")
    MODEL_PATH = os.path.join(MODEL_DIR, "flood_model.pkl")

    # ML Config
    N_TRAINING_SAMPLES = 500
    RISK_CLASSES = ["LOW", "MEDIUM", "HIGH"]

    # Simulation
    SIMULATION_STEPS = [0, 30, 60, 90]