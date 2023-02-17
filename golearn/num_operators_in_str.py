'''
"2+ 34-5 * 3" => ['2', '+', '34', '-', '5', '*', '3']
'''

import re


def token_parser(s):
    return re.findall(r'\d+|[()/*\-+]{1}', s)

