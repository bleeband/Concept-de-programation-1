#  premier exemple de portée

a = 1
b = 2
c = 3

def fonct1():
    print(a)
# fonct1()

# ------- EXEMPLE 2

def fonct2():
    b = 2
# fonct2()
# print(b)

# ------- EXEMPLE 3

def fonct3():
    print(sum([1, 2]))
# fonct3()

# ------- EXEMPLE 4

def fonct4():
    b = 1
    print(a)

    def fonct5():
        print(a)
        print(b)
        fonct5()
# fonct4()

# ------- EXEMPLE 5

def fun_6():
    def in_fun_6():
        print(a)
    in_fun_6()

# fun_6()

# ------- EXEMPLE 6

def foo():
    print(a)
    print(b)

def fun():
    b = 1
    print(a)
    foo()

# fun()

# ------- EXEMPLE 7

def fun_7():
    a = 2
    def in_fun_7():
        print(a)
    in_fun_7()

# fun_7()

# ------- EXEMPLE 8

def fun_8():

    def in_fun_8():
        d = 2
    in_fun_8()
    print(d)

# fun_8()