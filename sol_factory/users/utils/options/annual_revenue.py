"""
    Created by tareq on ৩০/৬/১৯
"""

__author__ = "Tareq"


def get_annual_revenue_options():
    options = [
        "Less than $100,000 / year",
        "$100,000 - $1M / year",
        "$1M - $5M / year",
        "$5M - $10M / year",
        "$10M - $100M / year",
        "$100M - $1B / year",
        "More than $1B / year"
    ]
    return tuple([(x, x) for x in options])
