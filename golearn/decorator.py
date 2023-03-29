# decorator with inclosed func
def decorator(func):
    def inner(*args, **kwargs):
        print ('1')
        func()
        print('2')
    return inner

def inclosed():
    return print('inclosed func')

a=decorator(inclosed)
a()


def decator(func):
    def inner(*args, **kwargs):
        print ('1')
        func(*args, **kwargs)
        print('2')
    return inner

def inclosed(name):
    return print(f'inclosed func arg with:{name}')

a=decator(inclosed)
a('vasya')

def decorat(func):
    def inner(*args, **kwargs):
        print ('1')
        func(*args, **kwargs)
        print('2')
    return inner

@decorat
def inclosed():
    return print('func with decorator')

inclosed()