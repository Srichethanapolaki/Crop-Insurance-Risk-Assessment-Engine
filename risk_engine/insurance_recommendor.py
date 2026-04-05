def recommend_insurance(risk_score):
    """
    Recommend insurance plan based on risk score.

    Parameters:
    - risk_score: float (0-100)

    Returns:
    - plan: str
    - reason: str
    - coverage_amount: float
    - premium: float
    """
    if risk_score <= 30:
        plan = "Basic Coverage"
        reason = "Low risk profile. Suitable for farms with stable conditions."
        coverage_amount = 50000  # $50,000 coverage
        premium = 2500  # $2,500 annual premium
    elif risk_score <= 60:
        plan = "Standard Coverage"
        reason = "Moderate risk. Balanced coverage for average agricultural risks."
        coverage_amount = 100000  # $100,000 coverage
        premium = 5000  # $5,000 annual premium
    else:
        plan = "Premium Coverage"
        reason = "High risk profile. Comprehensive coverage for volatile conditions."
        coverage_amount = 200000  # $200,000 coverage
        premium = 10000  # $10,000 annual premium

    return plan, reason, coverage_amount, premium
