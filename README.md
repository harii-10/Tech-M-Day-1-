# AI Suitability Advisor

## What it does
This Python program checks 10 business requirements and recommends whether to use normal code, Analytics/BI, Classical ML, Deep Learning, or Generative AI. It also explains each decision, shows a five-stage project lifecycle for AI/analytics tasks, runs basic tests, and creates a CSV report.

## Concepts
- **AI:** The broad field of making computers perform tasks that normally need human intelligence.
- **ML:** A part of AI that learns patterns from data.
- **Deep Learning:** A type of ML using neural networks, useful for complex images and similar data.
- **Generative AI:** AI that creates new content such as text and summaries.
- **Analytics/BI:** Uses data, reports and dashboards to understand business performance. It does not always require AI.

## Requirements covered
1. Validate PAN format
2. Predict customer cancellations
3. Summarise support emails
4. Detect defects in product photos
5. Calculate GST
6. Forecast weekly product demand
7. Answer questions from HR policy PDF
8. Sort invoices by amount
9. Show monthly sales performance (extra)
10. Classify incoming support tickets (extra)

## How to run
Python 3 is required. No extra packages are needed.

```bash
python ai_suitability_advisor.py
```

The program runs its tests and creates `decision_report.csv` in the same folder.

## Sample output

```text
AI Suitability Advisor
-------------------------------------------------------
Validate PAN format -> No AI (rules/code)
Predict customer cancellations -> Classical ML
Summarise support emails -> Generative AI
Detect defects in product photos -> Deep Learning
Calculate GST on an invoice -> No AI (rules/code)
Forecast weekly product demand -> Classical ML
Answer questions from HR policy PDF -> Generative AI
Sort invoices by amount -> No AI (rules/code)
Show monthly sales performance -> Analytics/BI
Classify incoming support tickets -> Classical ML

Tests passed. decision_report.csv created.
```

The program also prints the five lifecycle stages, one task and responsible role for every AI/analytics recommendation.

## Note
This is a first decision guide. Before building a real system, confirm the business need, check data quality, protect private information, and test the result with real users.
