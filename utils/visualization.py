import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

def create_risk_contribution_pie(contributions):
    """
    Create a pie chart for risk factor contributions.

    Parameters:
    - contributions: dict with factor: percentage
    """
    labels = list(contributions.keys())
    values = list(contributions.values())

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, title="Risk Factor Contributions")])
    fig.update_layout(title="Risk Factor Contributions (%)")
    return fig

def create_scenario_comparison_bar(scenario_comparison):
    """
    Create a bar chart for scenario comparison.

    Parameters:
    - scenario_comparison: dict with scenario: risk_score
    """
    scenarios = list(scenario_comparison.keys())
    risks = list(scenario_comparison.values())

    fig = go.Figure(data=[go.Bar(x=scenarios, y=risks, marker_color='indianred')])
    fig.update_layout(
        title="Risk Score Comparison Across Scenarios",
        xaxis_title="Scenario",
        yaxis_title="Risk Score"
    )
    return fig

def create_risk_factors_bar_chart(contributions):
    """
    Create a horizontal bar chart for risk factor contributions.

    Parameters:
    - contributions: dict with factor: percentage
    """
    factors = list(contributions.keys())
    percentages = list(contributions.values())

    fig = go.Figure(data=[go.Bar(
        x=percentages,
        y=factors,
        orientation='h',
        marker_color=['#2E7D32', '#FFA726', '#D32F2F', '#1976D2', '#7B1FA2']
    )])

    fig.update_layout(
        title="Risk Factor Contributions",
        xaxis_title="Contribution (%)",
        yaxis_title="Risk Factors",
        height=400
    )
    return fig