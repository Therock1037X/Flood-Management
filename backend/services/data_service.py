from utils.data_loader import load_all_data


def get_all_data():
    """
    Load wards and hotspots data.
    """
    wards_df, hotspots_df = load_all_data()
    return wards_df, hotspots_df


def get_summary_stats():
    """
    Calculate summary statistics for dashboard.
    """
    wards_df, hotspots_df = load_all_data()

    stats = {
        "total_wards": len(wards_df),
        "high_risk": int((wards_df["risk_level"] == "HIGH").sum()),
        "medium_risk": int((wards_df["risk_level"] == "MEDIUM").sum()),
        "low_risk": int((wards_df["risk_level"] == "LOW").sum()),
        "affected_population": int(
            wards_df[wards_df["risk_level"] == "HIGH"]["population"].sum()
        ),
        "avg_rainfall": int(wards_df["rainfall"].mean()),
        "total_hotspots": len(hotspots_df),
    }

    return stats


def filter_hotspots(risk_level="ALL"):
    """
    Filter hotspot data by risk level.
    """
    _, hotspots_df = load_all_data()

    if risk_level != "ALL":
        hotspots_df = hotspots_df[hotspots_df["flood_risk_level"] == risk_level]

    return hotspots_df.to_dict(orient="records")