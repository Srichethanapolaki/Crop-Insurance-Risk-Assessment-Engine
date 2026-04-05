import numpy as np

# Crop type to risk mapping (0-100 scale)
CROP_RISK_MAPPING = {
    "Rice": 40,
    "Wheat": 30,
    "Cotton": 50,
    "Maize": 35,
    "Soybean": 25
}


def calculate_risk_score(soil_health, climate_exposure, irrigation_reliability, crop_type, pest_risk):
    """
    Calculate the farm risk score based on multiple factors.
    """

    # Get crop risk from mapping
    crop_risk = CROP_RISK_MAPPING.get(crop_type, 30)

    # Risk score formula
    risk_score = (
        0.25 * soil_health
        + 0.30 * climate_exposure
        + 0.20 * irrigation_reliability
        + 0.15 * crop_risk
        + 0.10 * pest_risk
    )

    # Ensure value between 0-100
    risk_score = np.clip(risk_score, 0, 100)

    return risk_score


def get_factor_contributions(soil_health, climate_exposure, irrigation_reliability, crop_type, pest_risk):
    """
    Get the contribution of each factor to the risk score.
    """

    crop_risk = CROP_RISK_MAPPING.get(crop_type, 30)

    total_risk = calculate_risk_score(
        soil_health,
        climate_exposure,
        irrigation_reliability,
        crop_type,
        pest_risk
    )

    contributions = {
        "Soil Health": (0.25 * soil_health) / total_risk * 100 if total_risk > 0 else 0,
        "Climate Exposure": (0.30 * climate_exposure) / total_risk * 100 if total_risk > 0 else 0,
        "Irrigation Reliability": (0.20 * irrigation_reliability) / total_risk * 100 if total_risk > 0 else 0,
        "Crop Type": (0.15 * crop_risk) / total_risk * 100 if total_risk > 0 else 0,
        "Pest Risk": (0.10 * pest_risk) / total_risk * 100 if total_risk > 0 else 0
    }

    return contributions
