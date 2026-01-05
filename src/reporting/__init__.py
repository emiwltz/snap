"""Reporting module for result presentation."""

from src.reporting.html_report import generate_html_report
from src.reporting.profile_card import generate_profile_card
from src.reporting.verdict import Verdict, compute_verdict

__all__ = [
    "generate_html_report",
    "generate_profile_card",
    "Verdict",
    "compute_verdict",
]
