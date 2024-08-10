def project_savings(current_savings, annual_contribution, annual_rate, years):
    future_savings = []
    for year in range(years + 1):
        if annual_rate != 0:
            future_value = current_savings * (1 + annual_rate/100)**year + annual_contribution * (((1 + annual_rate/100)**year - 1) / (annual_rate/100))
        else:
            future_value = current_savings + annual_contribution * year
        future_savings.append(future_value)
    return future_savings
