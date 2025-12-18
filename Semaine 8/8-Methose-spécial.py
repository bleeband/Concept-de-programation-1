

from typing import Any


class User():

    ban = False
    notes = [92, 45, 87]
    
    def __init__(self, name, email, age, notes) -> None:
        #  ATTRIBUTS
        print("A partir du user init")
        if age < 16:
            self.ban = True
        self.name = name
        self.email = email
        self.age = age      
        self.notes = notes  

    def _say_hi(self):
        print("Oh ! Hi !")
    
    def bonjour(self, short:bool=False) :
        if short:
            self._say_hi()
        else:
            print(f"Bonjour, je suis {self.name.title()} !")

    def __str__(self) -> str:
        return f"Nom: {self.name}, Email: {self.email}, Age: {self.age}"
    
    def __eq__(self, value) -> bool:
        return self.name == value.name and self.email == value.email and self.age == value.age
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(self.name)

    def __getitem__(self, cle):
        print(f"La reponse de la cle est {self.notes[cle]}")

un_user = User("Fabiola", "fb,2gmail.com", 22, [{"anglais": 82, "Math": 75, "Python": 98}])

# un_user2 = User("Fatima", "fa,2gmail.com", 29)
# un_user3 = User("Fabiola", "fb,2gmail.com", 22)

# print(dir(un_user))
# print(un_user.__dir__())
# print(un_user.__dict__)

# num = 45
# print(45+12)
# print(num.__add__(12))

print(un_user.__str__())
# print(un_user2.__str__())
# print(un_user.__eq__(un_user3))

un_user(2)