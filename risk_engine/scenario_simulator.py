import numpy as np
from .risk_model import calculate_risk_score

def simulate_scenario(base_inputs, scenario):
    """
    Simulate a scenario by adjusting the base inputs.

    Parameters:
    - base_inputs: dict with keys: soil_health, climate_exposure, irrigation_reliability, crop_type, pest_risk
    - scenario: str ('drought', 'rainfall_reduction', 'pest_outbreak')

    Returns:
    - simulated_risk_score: float
    - adjusted_inputs: dict
    """
    adjusted = base_inputs.copy()

    if scenario == 'drought':
        # Drought increases climate exposure and decreases irrigation reliability
        adjusted['climate_exposure'] = min(100, base_inputs['climate_exposure'] + 30)
        adjusted['irrigation_reliability'] = max(0, base_inputs['irrigation_reliability'] - 20)

    elif scenario == 'rainfall_reduction':
        # Rainfall reduction increases climate exposure
        adjusted['climate_exposure'] = min(100, base_inputs['climate_exposure'] + 25)

    elif scenario == 'pest_outbreak':
        # Pest outbreak increases pest risk
        adjusted['pest_risk'] = min(100, base_inputs['pest_risk'] + 40)

    else:
        # No change for unknown scenario
        pass

    simulated_risk_score = calculate_risk_score(
        adjusted['soil_health'],
        adjusted['climate_exposure'],
        adjusted['irrigation_reliability'],
        adjusted['crop_type'],
        adjusted['pest_risk']
    )

    return simulated_risk_score, adjusted

def get_scenario_comparison(base_inputs, scenarios=['drought', 'rainfall_reduction', 'pest_outbreak']):
    """
    Get risk scores for multiple scenarios compared to base.

    Returns:
    - dict with scenario: risk_score
    """
    comparison = {'Normal': calculate_risk_score(**base_inputs)}

    for scenario in scenarios:
        risk, _ = simulate_scenario(base_inputs, scenario)
        comparison[scenario.replace('_', ' ').title()] = risk

    return comparison
