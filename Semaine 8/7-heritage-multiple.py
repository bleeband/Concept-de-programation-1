# ****  HERITAGE MULTIPLE  ***

class A():
    def __init__(self) -> None:
        super().__init__()
        print("A")

class B():
    def __init__(self) -> None:
        super().__init__()
        print("B")

class D():
    def __init__(self) -> None:
        super().__init__()
        print("D")

class C(A, B, D):
    def __init__(self) -> None:
        super().__init__()
        print("C")
        pass

c = C()

#  DE GAUCHE A DROITE  -->  METHOD RESOLUTION ORDER