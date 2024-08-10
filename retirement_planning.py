def calculate_retirement_needs(annual_expenses, retirement_years, inflation_rate):
    total_needs = 0
    for year in range(retirement_years):
        total_needs += annual_expenses * ((1 + inflation_rate / 100) ** year)
    return total_needs


def retirement_savings_gap(future_savings, required_savings):
    return required_savings - future_savings[-1]
