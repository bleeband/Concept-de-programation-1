#  =======   CLOSER  ========

# def fonction_parent():
#     a = 2
#     def fun_enfant():
#         print(a)
#     return fun_enfant

# fun = fonction_parent()
# fun()

# =====================================================
# number = 2
# # power = 2

# def power_factor(power):
#     def power_by(number):
#         return number ** power
#     return power_by

# power_by_2 = power_factor(2)

# print(power_by_2(4))

# power_by_4 = power_factor(4)

# print(power_by_4(4))

#====================================================

# def foo():
#     liste=[]
#     for item in range(3):
#         def display():
#             print(item)
#         liste.append(display)
#     return liste

# a = foo()
# a[0]()
# a[1]()
# a[2]()

# print(a)

#====================================================
# ===== GLOBAL NON LOCAL ======

# a = 1

# def fun():
#     global a
#     a += 1

# fun()

# def fun_compteur():
#     total = 0
#     def foo():
#         nonlocal total
#         print(total)
#         total += 1
#     return foo()

# a = fun_compteur()
# b = fun_compteur()

#====================================================
# ===== Annotation de fonction ======

def additionner(a: int | float, b: int) -> int:
    return a + b

additionner(1, 2)

#====================================================
# ===== Chaine de documentation ======
Nombre = int | float
def la_func_additionner(a: Nombre, b: Nombre) -> Nombre:
    '''
    Description de la fonction > la_func_additionner
    
    :param a: nombre a
    :type a: Nombre
    :param b: nombre b
    :type b: Nombre
    :return: aditionne a + b
    :rtype: Any
    '''
    return a + b

la_func_additionner(1,2)