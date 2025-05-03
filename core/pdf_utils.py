import pdfkit
from django.template.loader import render_to_string


def generate_pdf_report(score, questions, answers, skill_map):
    html = render_to_string(
        "report.html",
        {
            "score": score,
            "questions": questions,
            "answers": answers,
            "skill_map": skill_map,
        },
    )
    pdf = pdfkit.from_string(html, False)
    return pdf
