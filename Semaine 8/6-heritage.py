# ****  HERITAGE  ***

class User():

    ban = False
    
    def __init__(self, name, email, age) -> None:
        #  ATTRIBUTS
        print("A partir du user init")
        if age < 16:
            self.ban = True
        self.name = name
        self.email = email
        self.age = age        

    def _say_hi(self):
        print("Oh ! Hi !")
    
    def bonjour(self, short:bool=False) :
        if short:
            self._say_hi()
        else:
            print(f"Bonjour, je suis {self.name.title()} !")

class Hacker():
    def __init__(self, attack_type: str) -> None:
        self.attack_type = attack_type

    def attack(self, ip:str):
        print(f"{self.attack_type} launch on {ip}")

class Admin(User, Hacker):
    def __init__(self, name, email, age, origine, attack_type) -> None:
        # super().__init__(name, email, age)
        User.__init__(self, name, email, age)
        Hacker.__init__(self, attack_type)
        self.origine = origine

    def delete_user(self, user:User):
        print(f"Le user {user.email} a ete supprime")

    def bonjour(self, short: bool = False):
        # return super().bonjour(short)
        print("Bonjour je suis l'admin")


class Entreprise(User):
    pass

admin = Admin("marc", "bb@bb.com", 41, "TI STM", "ddos")
user = User("Pierre", "qqewab@bb.com", 16)

admin.attack("127.0.0.0")

# user.bonjour()
# admin.bonjour()
# admin.delete_user(user)


# ***  FONCTION INTERNE  ***
#      isinstance issubclass

# print(isinstance(admin, Admin))
# print(isinstance(admin, User))
# print(isinstance(admin, object))

# a = 1
# print(isinstance(a, object))

# print(issubclass(Admin, User))
# print(issubclass(Admin, object))
# print(issubclass(User, object))
# print(issubclass(User, Admin))
