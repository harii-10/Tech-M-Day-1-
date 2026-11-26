"""
AI Suitability Advisor
A simple rule-based program to decide whether a business task needs AI.
Run: python ai_suitability_advisor.py
"""

import csv

# AI is the broad field of making computers perform intelligent tasks.
# ML is a part of AI that learns patterns from data.
# Deep Learning is ML that uses neural networks, often for images and audio.
# Generative AI creates content such as summaries and natural-language answers.
# Analytics/BI uses data, reports and dashboards. It does not always need AI.

# Each requirement is stored as data.
requirements = [
    {"name": "Validate PAN format", "rules": True, "learning": False, "unstructured": False, "generate": False, "data": True, "report": False, "image": False},
    {"name": "Predict customer cancellations", "rules": False, "learning": True, "unstructured": False, "generate": False, "data": True, "report": False, "image": False},
    {"name": "Summarise support emails", "rules": False, "learning": False, "unstructured": True, "generate": True, "data": True, "report": False, "image": False},
    {"name": "Detect defects in product photos", "rules": False, "learning": True, "unstructured": True, "generate": False, "data": True, "report": False, "image": True},
    {"name": "Calculate GST on an invoice", "rules": True, "learning": False, "unstructured": False, "generate": False, "data": True, "report": False, "image": False},
    {"name": "Forecast weekly product demand", "rules": False, "learning": True, "unstructured": False, "generate": False, "data": True, "report": False, "image": False},
    {"name": "Answer questions from HR policy PDF", "rules": False, "learning": False, "unstructured": True, "generate": True, "data": True, "report": False, "image": False},
    {"name": "Sort invoices by amount", "rules": True, "learning": False, "unstructured": False, "generate": False, "data": True, "report": False, "image": False},
    # Two additional examples
    {"name": "Show monthly sales performance", "rules": False, "learning": False, "unstructured": False, "generate": False, "data": True, "report": True, "image": False},
    {"name": "Classify incoming support tickets", "rules": False, "learning": True, "unstructured": True, "generate": False, "data": True, "report": False, "image": False},
]


def decide(item):
    """Choose the simplest suitable solution and explain the choice."""
    if item["rules"] and not item["learning"] and not item["generate"]:
        return "No AI (rules/code)", "Fixed rules can solve this task using normal Python code."
    if item["generate"]:
        return "Generative AI", "The task needs new text or a natural-language answer."
    if item["image"] and item["learning"]:
        return "Deep Learning", "A model must learn visual patterns from product images."
    if item["learning"]:
        return "Classical ML", "The task needs patterns to be learned from historical examples."
    if item["report"]:
        return "Analytics/BI", "The task is mainly reporting and analysing existing data."
    return "No AI (rules/code)", "A simple program is enough; AI has no clear advantage."


# One lifecycle plan is reused for every requirement in the same category.
# Each stage has one task and the role responsible.
lifecycle = {
    "Classical ML": [
        ("Problem framing", "Define prediction target and success measure", "Business analyst"),
        ("Data", "Collect and clean historical labelled data", "Data engineer"),
        ("Model", "Train and test a baseline prediction model", "Data scientist"),
        ("Deployment", "Make predictions available through an API or batch job", "ML engineer"),
        ("Monitoring", "Check model accuracy and data changes", "ML engineer"),
    ],
    "Deep Learning": [
        ("Problem framing", "Define defect types and acceptable error rate", "Quality engineer"),
        ("Data", "Collect and label product photos", "Data engineer"),
        ("Model", "Train and test an image recognition neural network", "ML engineer"),
        ("Deployment", "Connect the model to the photo inspection process", "ML engineer"),
        ("Monitoring", "Review missed defects and model performance", "Quality engineer"),
    ],
    "Generative AI": [
        ("Problem framing", "Define users, expected answers and safety rules", "Product owner"),
        ("Data", "Prepare approved emails or HR policy documents", "Data engineer"),
        ("Model", "Choose a language model and prepare prompts or document search", "AI engineer"),
        ("Deployment", "Add the assistant to the support or HR portal", "AI engineer"),
        ("Monitoring", "Check answer accuracy, privacy and user feedback", "AI engineer"),
    ],
    "Analytics/BI": [
        ("Problem framing", "Choose the business metrics to display", "Business analyst"),
        ("Data", "Collect and validate sales data", "Data engineer"),
        ("Model", "Create SQL calculations and dashboard charts", "BI analyst"),
        ("Deployment", "Publish the dashboard for business users", "BI developer"),
        ("Monitoring", "Check data refresh and dashboard accuracy", "BI developer"),
    ],
}


def make_report():
    rows = []
    for item in requirements:
        decision, reason = decide(item)
        risk = "Check rules and edge cases." if decision == "No AI (rules/code)" else "Check data quality, accuracy and privacy."
        next_step = "Confirm the business rule and write test cases." if decision == "No AI (rules/code)" else "Confirm the data and define how success will be measured."
        rows.append({
            "requirement": item["name"],
            "decision": decision,
            "reason": reason,
            "risk": risk,
            "first_next_step": next_step,
        })
    return rows


def save_report(rows):
    with open("decision_report.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def run_tests():
    # Basic tests for obvious cases.
    assert decide(requirements[0])[0] == "No AI (rules/code)"  # PAN
    assert decide(requirements[4])[0] == "No AI (rules/code)"  # GST
    assert decide(requirements[3])[0] == "Deep Learning"       # Photos
    assert decide(requirements[2])[0] == "Generative AI"       # Emails
    assert decide(requirements[8])[0] == "Analytics/BI"        # Sales report


if __name__ == "__main__":
    run_tests()
    report = make_report()
    save_report(report)

    print("AI Suitability Advisor")
    print("-" * 55)
    for row in report:
        print(row["requirement"], "->", row["decision"])

    print("\nLifecycle plan:")
    for row in report:
        category = row["decision"]
        if category in lifecycle:
            print("\n" + row["requirement"] + " (" + category + ")")
            for stage, task, role in lifecycle[category]:
                print(" ", stage, "-", task, "| Role:", role)

    print("\nTests passed. decision_report.csv created.")
