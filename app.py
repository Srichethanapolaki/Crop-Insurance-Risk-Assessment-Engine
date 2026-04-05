import streamlit as st
import pandas as pd
from risk_engine.risk_model import calculate_risk_score, get_factor_contributions
from risk_engine.insurance_recommender import recommend_insurance
from utils.visualization import create_risk_contribution_pie, create_risk_factors_bar_chart
from risk_engine.soil_ai import analyze_soil_health

# Page config
st.set_page_config(
    page_title="Crop Insurance Risk Engine",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS styling
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css('style.css')

# Commented out CSS block to avoid syntax errors
#     <style>
#     :root {
#         --primary-color: #2E7D32;
#         --secondary-color: #FFA726;
#         --danger-color: #D32F2F;
#         --success-color: #388E3C;
#     }

#     * {
#         margin: 0;
#         padding: 0;
#     }

#     body {
#         background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
#         font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#     }

#     .main {
#         background-color: #f8f9fa;
#     }
    
#     .stMetric {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#         padding: 20px;
#         border-radius: 10px;
#         color: white;
#         box-shadow: 0 4px 15px rgba(0,0,0,0.1);
#     }
    
#     .stButton > button {
#         width: 100%;
#         background: linear-gradient(135deg, #2E7D32 0%, #1B5E20 100%);
#         color: white;
#         border: none;
#         padding: 12px 24px;
#         border-radius: 8px;
#         font-weight: 600;
#         cursor: pointer;
#         transition: all 0.3s ease;
#         box-shadow: 0 4px 15px rgba(46, 125, 50, 0.3);
#     }
    
#     .stButton > button:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 6px 20px rgba(46, 125, 50, 0.4);
#     }
    
#     h1 {
#         color: #2E7D32;
#         text-align: center;
#         margin-bottom: 30px;
#         font-size: 2.5em;
#         text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
#     }

#     h2 {
#         color: #1B5E20;
#         margin-top: 25px;
#         margin-bottom: 15px;
#         border-bottom: 3px solid #FFA726;
#         padding-bottom: 10px;
#     }

#     h3 {
#         color: #2E7D32;
#         margin-top: 20px;
#     }
    
#     .feature-card {
#         background: white;
#         border-radius: 10px;
#         padding: 25px;
#         margin: 15px 0;
#         box-shadow: 0 4px 20px rgba(0,0,0,0.1);
#         border-left: 5px solid #2E7D32;
#         transition: all 0.3s ease;
#     }
    
#     .feature-card:hover {
#         transform: translateY(-5px);
#         box-shadow: 0 6px 30px rgba(0,0,0,0.15);
#     }

#     .risk-metric-high {
#         background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%);
#         padding: 20px;
#         border-radius: 10px;
#         color: white;
#         text-align: center;
#         font-size: 1.5em;
#         font-weight: bold;
#         box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
#     }
    
#     .risk-metric-medium {
#         background: linear-gradient(135deg, #ffa726 0%, #fb8c00 100%);
#         padding: 20px;
#         border-radius: 10px;
#         color: white;
#         text-align: center;
#         font-size: 1.5em;
#         font-weight: bold;
#         box-shadow: 0 4px 15px rgba(255, 167, 38, 0.3);
#     }
    
#     .risk-metric-low {
#         background: linear-gradient(135deg, #66bb6a 0%, #43a047 100%);
#         padding: 20px;
#         border-radius: 10px;
#         color: white;
#         text-align: center;
#         font-size: 1.5em;
#         font-weight: bold;
#         box-shadow: 0 4px 15px rgba(102, 187, 106, 0.3);
#     }
    
#     .input-section {
#         background: white;
#         padding: 25px;
#         border-radius: 10px;
#         box-shadow: 0 4px 15px rgba(0,0,0,0.1);
#         margin-bottom: 20px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# Title and header
st.markdown("<h1>🌾 Crop Insurance Risk Assessment Engine</h1>", unsafe_allow_html=True)

# Create tabs
tab1, tab2 = st.tabs(["🏠 Home", "📊 Risk Assessment"])

with tab1:
    # Display key metrics
    st.markdown("<h2>Platform Overview</h2>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Risk Factors", "5", "Analyzed")
        
    with col2:
        st.metric("Scenarios", "3", "Simulated")
        
    with col3:
        st.metric("Coverage Plans", "3", "Available")
        
    with col4:
        st.metric("Crop Types", "5", "Supported")

    # Main content
    st.markdown("<h2>About This Platform</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <h3>🎯 What We Do</h3>
#         <p>
        A comprehensive decision support system that evaluates agricultural risk using dynamic, 
        multi-factor analysis. Instead of relying on historical averages, our platform provides 
        transparent, explainable risk assessments that help farmers and insurance companies make 
        better decisions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Risk Score Ranges
    st.markdown("<h2>Risk Score Ranges</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="risk-metric-low">
            <h4>Low Risk (0-30)</h4>
            <p>Stable farming conditions with minimal exposure to agricultural risks.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="risk-metric-medium">
            <h4>Moderate Risk (31-60)</h4>
            <p>Average risk profile requiring balanced risk management strategies.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="risk-metric-high">
            <h4>High Risk (61-100)</h4>
            <p>Elevated exposure to multiple agricultural risks requiring comprehensive protection.</p>
        </div>
        """, unsafe_allow_html=True)

    # Features overview
    st.markdown("<h2>Core Features</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>📊 Multi-Factor Risk Scoring</h3>
            <p>Combines soil health, climate exposure, irrigation reliability, crop type, and pest risk into a comprehensive farm risk score.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>🔍 Explainability Engine</h3>
            <p>Understand exactly how each factor contributes to your risk score with detailed visual breakdowns.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>📈 Scenario Simulator</h3>
            <p>Test different environmental scenarios like drought, rainfall reduction, and pest outbreaks to see how your farm's risk changes.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>💡 Smart Recommendations</h3>
            <p>Get personalized insurance coverage suggestions based on your farm's unique risk profile.</p>
        </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 20px; color: #666;">
        <p>🌱 Empowering agricultural decision-making with transparent, data-driven risk assessment</p>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.title("📊 Risk Assessment Engine")

    st.markdown("Calculate your farm's comprehensive risk score based on multiple environmental and agricultural factors.")
    st.divider()
    st.subheader("🧠 AI Soil Health Analyzer")

    # Location and Image Upload Section
    st.markdown("### 📍 Location & Image Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        location = st.text_input("Farm Location", 
                                placeholder="Enter city, state, or coordinates",
                                help="Enter your farm's location for localized analysis")
    
    with col2:
        uploaded_image = st.file_uploader("Upload Soil Image", 
                                         type=['jpg', 'jpeg', 'png'],
                                         help="Upload a photo of your soil for AI analysis")
        
        if uploaded_image is not None:
            st.image(uploaded_image, caption="Uploaded Soil Image", use_column_width=True)
            st.success("Image uploaded successfully! AI analysis will consider visual soil characteristics.")

    st.divider()

    # Manual Input Section
    st.markdown("### 🔬 Soil Parameters")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        ph = st.slider("Soil pH", 0.0, 14.0, 6.5)

    with col2:
        nitrogen = st.slider("Nitrogen Level", 0, 100, 50)

    with col3:
        phosphorus = st.slider("Phosphorus Level", 0, 100, 50)

    col4, col5 = st.columns(2)

    with col4:
        potassium = st.slider("Potassium Level", 0, 100, 50)

    with col5:
        moisture = st.slider("Soil Moisture", 0, 100, 50)

    if st.button("🔬 Analyze Soil Health", use_container_width=True):

        score, recommendation = analyze_soil_health(
            ph,
            nitrogen,
            phosphorus,
            potassium,
            moisture,
            location
        )

        st.success(f"🌱 Soil Health Score: {score:.2f}/100")
        st.info(recommendation)
        
        # Display location if provided
        if location:
            st.info(f"📍 Analysis for location: {location}")
        
        # Additional analysis based on image
        if uploaded_image is not None:
            st.info("🖼️ Image analysis: Visual soil characteristics have been considered in the assessment.")

    # Load synthetic data
    @st.cache_data
    def load_synthetic_data():
        return pd.read_csv('data/syntheticdata.csv')

    synthetic_data = load_synthetic_data()

    # Data source selection
    st.markdown("### 📁 Data Source")
    data_source = st.radio("Choose input method:", 
                           ["🖊️ Manual Input", "📋 Load from Sample Data"],
                           horizontal=True)

    # Initialize session state
    if 'soil_health' not in st.session_state:
        st.session_state.soil_health = 50

    if data_source == "📋 Load from Sample Data":
        col1, col2 = st.columns([2, 1])
        with col1:
            farm_options = [f"Farm {int(row['farm_id'])} - {row['crop_type']} (Risk: {row['risk_score']:.0f})" 
                           for _, row in synthetic_data.iterrows()]
            selected_farm = st.selectbox("Select a farm:", farm_options)
            farm_id = int(selected_farm.split()[1])
            farm_data = synthetic_data[synthetic_data['farm_id'] == farm_id].iloc[0]
        
        with col2:
            if st.button("Load Data", use_container_width=True):
                st.session_state.soil_health = int(farm_data['soil_health'])
                st.session_state.climate_exposure = int(farm_data['climate_exposure'])
                st.session_state.irrigation_reliability = int(farm_data['irrigation_reliability'])
                st.session_state.crop_type = farm_data['crop_type']
                st.session_state.pest_risk = int(farm_data['pest_risk'])
                st.rerun()
    else:
        st.session_state.soil_health = 50
        st.session_state.climate_exposure = 50
        st.session_state.irrigation_reliability = 50
        st.session_state.crop_type = 'Rice'
        st.session_state.pest_risk = 50

    # Input section
    st.markdown("<div class='input-section'>", unsafe_allow_html=True)
    st.markdown("### 🌾 Farm Parameters")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<h4 style='color: #2E7D32;'>Soil Quality</h4>", unsafe_allow_html=True)
        soil_health = st.slider("Soil Health (0-100)", 0, 100, 
                               value=st.session_state.get('soil_health', 50),
                               help="Higher values indicate better soil quality")

    with col2:
        st.markdown("<h4 style='color: #2E7D32;'>Climate Conditions</h4>", unsafe_allow_html=True)
        climate_exposure = st.slider("Climate Exposure (0-100)", 0, 100,
                                    value=st.session_state.get('climate_exposure', 50),
                                    help="Higher values indicate more volatile climate conditions")

    with col3:
        st.markdown("<h4 style='color: #2E7D32;'>Water Management</h4>", unsafe_allow_html=True)
        irrigation_reliability = st.slider("Irrigation Reliability (0-100)", 0, 100,
                                          value=st.session_state.get('irrigation_reliability', 50),
                                          help="Higher values indicate more reliable irrigation systems")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h4 style='color: #2E7D32;'>Crop Selection</h4>", unsafe_allow_html=True)
        crop_type = st.selectbox("Crop Type", 
                                ['Rice', 'Wheat', 'Cotton', 'Maize', 'Soybean'],
                                index=['Rice', 'Wheat', 'Cotton', 'Maize', 'Soybean'].index(st.session_state.get('crop_type', 'Rice')))

    with col2:
        st.markdown("<h4 style='color: #2E7D32;'>Pest Management</h4>", unsafe_allow_html=True)
        pest_risk = st.slider("Pest Risk (0-100)", 0, 100,
                             value=st.session_state.get('pest_risk', 50),
                             help="Higher values indicate greater pest pressure")

    st.markdown("</div>", unsafe_allow_html=True)

    # Calculate button
    if st.button("🔍 Calculate Risk Score", use_container_width=True, key="calc_button"):
        # Prepare inputs
        inputs = {
            'soil_health': soil_health,
            'climate_exposure': climate_exposure,
            'irrigation_reliability': irrigation_reliability,
            'crop_type': crop_type,
            'pest_risk': pest_risk
        }

        # Calculate risk score
        risk_score = calculate_risk_score(**inputs)
        
        # Get contributions
        contributions = get_factor_contributions(**inputs)
        
        # Get insurance recommendation
        plan, reason, coverage_amount, premium = recommend_insurance(risk_score)

        # Store in session state
        st.session_state.risk_score = risk_score
        st.session_state.plan = plan
        st.session_state.reason = reason
        st.session_state.coverage_amount = coverage_amount
        st.session_state.premium = premium
        st.session_state.contributions = contributions

    # Display results if available
    if 'risk_score' in st.session_state:
        st.divider()
        st.markdown("### 📈 Assessment Results")
        
        risk_score = st.session_state.risk_score
        
        # Risk level classification
        if risk_score <= 30:
            risk_class = "risk-metric-low"
            status = "🟢 LOW RISK"
        elif risk_score <= 60:
            risk_class = "risk-metric-medium"
            status = "🟡 MODERATE RISK"
        else:
            risk_class = "risk-metric-high"
            status = "🔴 HIGH RISK"
        
        # Display risk score
        st.markdown(f"""
        <div class='{risk_class}'>
            {status}<br>
            Risk Score: {risk_score:.1f}/100
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        # Insurance recommendation
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 💼 Recommended Coverage")
            st.success(f"**{st.session_state.plan}**")
            st.info(f"_{st.session_state.reason}_")
            st.markdown(f"**Coverage Amount:** ${st.session_state.coverage_amount:,.0f}")
            st.markdown(f"**Annual Premium:** ${st.session_state.premium:,.0f}")
        
        with col2:
            st.markdown("### 📊 Risk Breakdown")
            pie_fig = create_risk_contribution_pie(st.session_state.contributions)
            st.plotly_chart(pie_fig, use_container_width=True)
        
        # Risk factor analysis
        st.divider()
        st.markdown("### 🔍 Factor Analysis")
        
        analysis_col1, analysis_col2 = st.columns(2)
        
        with analysis_col1:
            st.markdown("**Key Risk Drivers:**")
            sorted_contrib = dict(sorted(st.session_state.contributions.items(), 
                                        key=lambda x: x[1], reverse=True))
            for i, (factor, percent) in enumerate(sorted_contrib.items(), 1):
                st.write(f"{i}. {factor}: {percent:.1f}%")
        
        with analysis_col2:
            st.markdown("**Input Summary:**")
            st.json({
                "Soil Health": soil_health,
                "Climate Exposure": climate_exposure,
                "Irrigation": irrigation_reliability,
                "Crop": crop_type,
                "Pest Risk": pest_risk
            })
        
        # Risk factors bar chart
        st.divider()
        st.markdown("### 📊 Risk Factors Bar Chart")
        bar_fig = create_risk_factors_bar_chart(st.session_state.contributions)
        st.plotly_chart(bar_fig, use_container_width=True)
        
        # Download report
        st.divider()
        st.markdown("### 📄 Download Report")
        
        # Generate report content
        report_content = f"""
CROP INSURANCE RISK ASSESSMENT REPORT
=====================================

Assessment Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}

FARM RISK ASSESSMENT SUMMARY
-----------------------------
Risk Score: {st.session_state.risk_score:.1f}/100
Risk Level: {'Low' if st.session_state.risk_score <= 30 else 'Moderate' if st.session_state.risk_score <= 60 else 'High'}

INSURANCE RECOMMENDATION
-------------------------
Plan: {st.session_state.plan}
Coverage Amount: ${st.session_state.coverage_amount:,.0f}
Annual Premium: ${st.session_state.premium:,.0f}
Reason: {st.session_state.reason}

FARM PARAMETERS
---------------
Soil Health: {soil_health}/100
Climate Exposure: {climate_exposure}/100
Irrigation Reliability: {irrigation_reliability}/100
Crop Type: {crop_type}
Pest Risk: {pest_risk}/100

RISK FACTOR CONTRIBUTIONS
--------------------------
"""
        
        # Add contributions to report
        sorted_contrib = dict(sorted(st.session_state.contributions.items(), 
                                    key=lambda x: x[1], reverse=True))
        for factor, percent in sorted_contrib.items():
            report_content += f"{factor}: {percent:.1f}%\n"
        
        report_content += "\nGenerated by Crop Insurance Risk Engine\n"
        
        # Download button
        st.download_button(
            label="📥 Download Assessment Report",
            data=report_content,
            file_name=f"risk_assessment_report_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            use_container_width=True
        )