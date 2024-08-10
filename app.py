import streamlit as st
import json
from modules.user_input import get_user_input
from modules.savings_projection import project_savings
from modules.retirement_planning import calculate_retirement_needs, retirement_savings_gap
from modules.investment_analysis import analyze_investments, calculate_risk_return
from modules.visualization import plot_savings_projection
from modules.reporting import generate_report


def main():
    st.title("Financial Planning Tool")

    # Get user data
    user_data = get_user_input()

    if user_data:
        # Display user data for debugging
        st.write("User Data:", user_data)

        # Project savings
        current_savings = user_data["current_savings"]
        annual_contribution = user_data["annual_contribution"]
        annual_rate = user_data["annual_rate"]
        years = user_data["years"]

        # Debugging: Print input values
        st.write("Current Savings:", current_savings)
        st.write("Annual Contribution:", annual_contribution)
        st.write("Annual Rate:", annual_rate)
        st.write("Years:", years)

        future_savings = project_savings(current_savings, annual_contribution, annual_rate, years)

        # Debugging: Print projected savings
        st.write("Future Savings:", future_savings)

        # Estimate retirement needs
        annual_expenses = user_data["annual_expenses"]
        retirement_years = user_data["retirement_years"]
        inflation_rate = user_data["inflation_rate"]

        required_savings = calculate_retirement_needs(annual_expenses, retirement_years, inflation_rate)
        savings_gap = retirement_savings_gap(future_savings, required_savings)

        # Analyze investments
        investment_details = user_data["investments"]  # No need to use json.loads here

        investments = analyze_investments(investment_details)
        risk, return_rate = calculate_risk_return(investments)

        # Visualization
        plot_savings_projection(years, future_savings)

        # Generate report
        report_path = generate_report(user_data, future_savings, required_savings, investments)
        st.success(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
