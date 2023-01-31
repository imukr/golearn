import re
def token_parser(s):
    print(re.findall(r"\d+|[()+\-*/]{1}", s))

token_parser('2 + 35 - 5')