class MyExeption(Exception):
    def __init__(self, value):
        self.value = value

def test(value: int):
    if value < 0:
            raise MyExeption(f'{value}<0')
    else:
        return value+100

try:
    test(-5)
except MyExeption as o:
    print (o)
