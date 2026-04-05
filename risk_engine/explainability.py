from .risk_model import get_factor_contributions

def explain_risk_score(soil_health, climate_exposure, irrigation_reliability, crop_type, pest_risk):
    """
    Provide explanation for the risk score.

    Returns:
    - contributions: dict
    """
    return get_factor_contributions(soil_health, climate_exposure, irrigation_reliability, crop_type, pest_risk)
