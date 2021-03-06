"""
    Created by tareq on ৫/৭/১৯
"""
from datetime import datetime

from settings import STATIC_UPLOAD_URL

__author__ = "Tareq"


def get_file_upload_path(instance, filename):
    today = datetime.today()
    return STATIC_UPLOAD_URL + "{}/{}/{}/{}".format(today.year, today.month, today.day, filename)
