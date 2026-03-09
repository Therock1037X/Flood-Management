from flask import Blueprint, request, jsonify
from services.prediction_service import predict_flood_risk

prediction_bp = Blueprint("prediction", __name__)


@prediction_bp.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    rainfall = float(data.get("rainfall", 80))
    elevation = float(data.get("elevation", 220))
    drain_capacity = float(data.get("drain_capacity", 0.6))
    population_density = float(data.get("population_density", 15000))

    result = predict_flood_risk(
        rainfall,
        elevation,
        drain_capacity,
        population_density
    )

    return jsonify(result)