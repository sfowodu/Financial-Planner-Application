import streamlit as st
import json


def get_user_input():
    st.sidebar.header("Input Your Financial Information")

    current_savings = st.sidebar.number_input("Current Savings ($)", min_value=0.0, value=10000.0)
    annual_contribution = st.sidebar.number_input("Annual Contribution ($)", min_value=0.0, value=5000.0)
    annual_rate = st.sidebar.number_input("Expected Annual Return (%)", min_value=0.0, value=5.0)
    years = st.sidebar.number_input("Number of Years", min_value=0, value=20)

    annual_expenses = st.sidebar.number_input("Estimated Annual Expenses in Retirement ($)", min_value=0.0,
                                              value=40000.0)
    retirement_years = st.sidebar.number_input("Years in Retirement", min_value=0, value=20)
    inflation_rate = st.sidebar.number_input("Expected Inflation Rate (%)", min_value=0.0, value=2.0)

    # Get investment details as a JSON string
    investments_json = st.sidebar.text_area("Investment Details (JSON format)",
                                            value='[{"name": "Stock A", "type": "stock", "amount_invested": 10000, "expected_annual_return": 7.5, "risk_level": "high"}]')

    # Parse the JSON string to a Python object
    try:
        investments = json.loads(investments_json)
    except json.JSONDecodeError as e:
        st.error(f"Invalid JSON format: {e}")
        investments = []

    user_data = {
        "current_savings": current_savings,
        "annual_contribution": annual_contribution,
        "annual_rate": annual_rate,
        "years": years,
        "annual_expenses": annual_expenses,
        "retirement_years": retirement_years,
        "inflation_rate": inflation_rate,
        "investments": investments
    }

    return user_data
