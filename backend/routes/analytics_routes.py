from flask import Blueprint, jsonify
from services.data_service import get_summary_stats, get_all_data

analytics_bp = Blueprint("analytics", __name__)


@analytics_bp.route("/analytics", methods=["GET"])
def get_analytics():

    wards_df, hotspots_df = get_all_data()

    # Risk distribution
    risk_counts = wards_df["risk_level"].value_counts().to_dict()

    # Top rainfall wards
    top_wards = wards_df.nlargest(
        10, "rainfall"
    )[["ward_name", "rainfall", "risk_level", "population"]].to_dict(orient="records")

    # Readiness score distribution
    readiness_bins = {"0-0.4": 0, "0.4-0.6": 0, "0.6-0.8": 0, "0.8-1.0": 0}

    for value in wards_df["readiness_score"]:
        if value < 0.4:
            readiness_bins["0-0.4"] += 1
        elif value < 0.6:
            readiness_bins["0.4-0.6"] += 1
        elif value < 0.8:
            readiness_bins["0.6-0.8"] += 1
        else:
            readiness_bins["0.8-1.0"] += 1

    return jsonify({
        "summary": get_summary_stats(),
        "risk_distribution": risk_counts,
        "top_rainfall_wards": top_wards,
        "readiness_distribution": readiness_bins,
        "total_population_at_risk": int(
            wards_df[wards_df["risk_level"] == "HIGH"]["population"].sum()
        ),
        "avg_drain_capacity": round(float(wards_df["drain_capacity"].mean()), 3)
    })