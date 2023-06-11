def greet():
    print('hello')

def before(a):
    print('before...')
    a()
    print('after....')

before(greet)