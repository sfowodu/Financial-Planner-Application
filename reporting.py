import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_report(user_data, projection, retirement, investment):
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)

    report_name = os.path.join(report_dir, "financial_report.pdf")
    c = canvas.Canvas(report_name, pagesize=letter)
    c.drawString(100, 750, "Financial Report")
    c.drawString(100, 730, f"User Data: {user_data}")
    c.drawString(100, 710, f"Savings Projection: {projection}")
    c.drawString(100, 690, f"Retirement Planning: {retirement}")
    c.drawString(100, 670, f"Investment Analysis: {investment}")
    c.save()
    return report_name
