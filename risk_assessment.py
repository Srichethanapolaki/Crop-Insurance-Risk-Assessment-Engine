import pandas as pd
from risk_engine.risk_model import calculate_risk_score, get_factor_contributions
from risk_engine.insurance_recommender import recommend_insurance
from risk_engine.soil_ai import analyze_soil_health

def main():
    print("🌾 Crop Insurance Risk Assessment Engine")
    print("=" * 50)

    # Soil Health Analysis
    print("\n🧠 AI Soil Health Analyzer")
    print("-" * 30)

    ph = float(input("Enter soil pH (0.0-14.0): "))
    nitrogen = int(input("Enter nitrogen level (0-100): "))
    phosphorus = int(input("Enter phosphorus level (0-100): "))
    potassium = int(input("Enter potassium level (0-100): "))
    moisture = int(input("Enter soil moisture (0-100): "))

    soil_score, soil_recommendation = analyze_soil_health(ph, nitrogen, phosphorus, potassium, moisture)
    print(f"\n🌱 Soil Health Score: {soil_score:.2f}/100")
    print(f"Recommendation: {soil_recommendation}")

    # Farm Parameters
    print("\n🌾 Farm Parameters")
    print("-" * 20)

    soil_health = int(input("Enter soil health (0-100): "))
    climate_exposure = int(input("Enter climate exposure (0-100): "))
    irrigation_reliability = int(input("Enter irrigation reliability (0-100): "))

    crop_options = ['Rice', 'Wheat', 'Cotton', 'Maize', 'Soybean']
    print("Available crops:", ', '.join(crop_options))
    crop_type = input("Enter crop type: ").strip()

    pest_risk = int(input("Enter pest risk (0-100): "))

    # Calculate Risk Score
    print("\n🔍 Calculating Risk Score...")
    print("-" * 30)

    inputs = {
        'soil_health': soil_health,
        'climate_exposure': climate_exposure,
        'irrigation_reliability': irrigation_reliability,
        'crop_type': crop_type,
        'pest_risk': pest_risk
    }

    risk_score = calculate_risk_score(**inputs)
    contributions = get_factor_contributions(**inputs)
    plan, reason = recommend_insurance(risk_score)

    # Display Results
    print("\n📈 Assessment Results")
    print("-" * 25)

    if risk_score <= 30:
        status = "🟢 LOW RISK"
    elif risk_score <= 60:
        status = "🟡 MODERATE RISK"
    else:
        status = "🔴 HIGH RISK"

    print(f"Risk Status: {status}")
    print(f"Risk Score: {risk_score:.1f}/100")

    print("\n💼 Recommended Coverage")
    print("-" * 25)
    print(f"Plan: {plan}")
    print(f"Reason: {reason}")

    print("\n📊 Risk Breakdown")
    print("-" * 20)
    sorted_contrib = dict(sorted(contributions.items(), key=lambda x: x[1], reverse=True))
    for i, (factor, percent) in enumerate(sorted_contrib.items(), 1):
        print(f"{i}. {factor}: {percent:.1f}%")

    print("\n🔍 Input Summary")
    print("-" * 18)
    print(f"Soil Health: {soil_health}")
    print(f"Climate Exposure: {climate_exposure}")
    print(f"Irrigation Reliability: {irrigation_reliability}")
    print(f"Crop Type: {crop_type}")
    print(f"Pest Risk: {pest_risk}")

if __name__ == "__main__":
    main()
