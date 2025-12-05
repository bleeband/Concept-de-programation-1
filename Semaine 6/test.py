a = 1
b = 2

def foo():
    print(a)
    print(b)

def fun():
    b = 4
    print(b)
    foo()

fun()
