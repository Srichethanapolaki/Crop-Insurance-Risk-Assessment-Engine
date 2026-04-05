import numpy as np

def analyze_soil_health(ph, nitrogen, phosphorus, potassium, moisture, location=None):
    """
    AI Soil Health Analyzer

    Parameters:
    ph : float (0-14)
    nitrogen : float (0-100)
    phosphorus : float (0-100)
    potassium : float (0-100)
    moisture : float (0-100)
    location : str (optional) - Farm location for localized analysis

    Returns:
    soil_health_score (0-100)
    recommendation
    """

    # Normalize pH score (ideal range 6-7.5)
    if 6 <= ph <= 7.5:
        ph_score = 100
    else:
        ph_score = max(0, 100 - abs(ph - 6.5) * 20)

    # Nutrient score
    nutrient_score = (nitrogen + phosphorus + potassium) / 3

    # Moisture score
    moisture_score = moisture

    # AI Soil Health Score
    soil_health_score = (
        0.4 * ph_score +
        0.4 * nutrient_score +
        0.2 * moisture_score
    )

    soil_health_score = np.clip(soil_health_score, 0, 100)

    # Recommendation
    if soil_health_score > 75:
        recommendation = "Healthy soil. Suitable for most crops."
    elif soil_health_score > 50:
        recommendation = "Moderate soil health. Consider adding organic fertilizers."
    else:
        recommendation = "Poor soil health. Soil treatment required."

    return soil_health_score, recommendation