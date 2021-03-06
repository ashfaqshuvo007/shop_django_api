"""
    Created by tareq on 9/28/19
"""

import re
import string

__author__ = "Tareq"

all_cap_re = re.compile('([a-z0-9])([A-Z])')


def str_titleize(name):
    s2 = all_cap_re.sub(r'\1_\2', name)
    title = "".join([a if a.isupper() else b for a, b in zip(s2, string.capwords(s2))])
    return title.replace(r'_', r' ')
