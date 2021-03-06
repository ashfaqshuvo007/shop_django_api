"""
    Created by tareq on ২৭/৬/১৯
"""

__author__ = "Tareq"


def get_user_verification_email_content(name, verification_link):
    return "Dear {0},\n\n" \
           "Thank you for joining to Sol-Factory. Please verify your account by clicking this link: {1}.\n\n" \
           "Best regards.".format(name, verification_link)
