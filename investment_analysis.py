def analyze_investments(investments):
    analysis = []
    for investment in investments:
        name = investment.get("name")
        investment_type = investment.get("type")
        amount_invested = investment.get("amount_invested", 0)
        expected_return = investment.get("expected_annual_return", 0)
        risk_level = investment.get("risk_level", "medium")

        analysis.append({
            "name": name,
            "type": investment_type,
            "amount_invested": amount_invested,
            "expected_annual_return": expected_return,
            "risk_level": risk_level
        })
    return analysis


def calculate_risk_return(investments):
    total_investment = sum(investment["amount_invested"] for investment in investments)
    weighted_return = sum((investment["amount_invested"] * investment["expected_annual_return"]) for investment in
                          investments) / total_investment
    # You can add more complex risk analysis based on `risk_level`

    return {
        "total_investment": total_investment,
        "weighted_return": weighted_return
    }
