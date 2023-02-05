# class Web:
#     def __init__(self, name,lastname,login,password,phone,email):
#         self.name = name,
#         self.lastname = lastname,
#         self.login = login,
#         self.password = password,
#         self.phone = phone,
#         self.email = email
#     def get_name(self):
#         return self.name

#     def get_lastname(self):
#         return self.lastname

#     def get_login(self):
#         return self.login

#     def get_password(self):
#         return self.password

#     def get_phone(self):
#         return self.phone
    
#     def get_email(self):
#         return self.email

#     def get_info(self):
#         return f" Name: {self.get_name()}, Lastname: {self.get_lastname()}, login: {self.get_login()}"
# user1 = Web('John', 'Alex', 'John_07', 'john0221', 10124397007, 'john00@gmail.com')

# print(user1.get_info())


# class Avto():
#     def __init__(self, nomi, rangi, karobka):
#         self.nomi = nomi
#         self.rangi = rangi
#         self.karobka = karobka
#         self.km = 0
#         self.yil = 2020

#     def get_info(self):
#         return f"Moshina nomi {self.nomi}, rangi {self.rangi}, uzatma {self.karobka}, prpbegi {self.km} kilpometr va {self.yil}da ishlab chiqarilgan "
    
#     def update_info(self):
#         self.km += 100
#         return self.km 
# mashina1 = Avto('Malibu', 'Qora', 'Aftomat')
# mashina2 = Avto('Gentra', 'Oq', 'Aftomat')
# mashina3 = Avto('Nexia 3', 'Space grey', 'Mexanika')
# # print(mashina1.update_info())
# # print(mashina1.get_info())


# class Aftosalon():
#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.mashinalar_soni = 0
#         self.mashinalar = [] 
#     def add_students(self, mashina):
#         self.mashinalar.append(mashina)
#         self.mashinalar_soni += 1
#     def get_students(self):
#         return [mashina.get_info() for mashina in self.mashinalar]

# gm = Aftosalon('uzmotors')
# mashina1 = Avto('Malibu', 'Qora', 'Aftomat')
# mashina2 = Avto('Gentra', 'Oq', 'Aftomat')
# mashina3 = Avto('Nexia 3', 'Space grey', 'Mexanika')


# gm.add_students(mashina1)
# gm.add_students(mashina2)
# gm.add_students(mashina3)

# add_moshinalar = gm.get_students()
# print(add_moshinalar)

# print(gm.mashinalar_soni)

# print(gm.mashinalar)

# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]

# print(see_methods(Aftosalon))

# class Shaxs:
#     """Shaxslar haqida ma'lumot"""

#     def __init__(self, ism, familiya, passport, tyil):
#         """Shaxsning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil

#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info

#     def get_age(self, yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil


# class Talaba(Shaxs):
#     """Talaba klassi"""

#     def __init__(self, ism, familiya, passport, tyil, idraqam, fan):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
#         self.fan = fan

#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam

#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich

#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
#         return info
    
        


# # Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.
# class Fan:
#     def __init__(self, fan1, fan2, fan3):
#         self.fan1 =fan1
#         self.fan2 =fan2
#         self.fan3 = fan3
#     def get_fan(self):
#         fan = f"Birinchi fanning nomi {self.fan1}, ikkinchi fanning nomi {self.fan2}, uchinchi fanning nomi {self.fan3}"
#         return fan
    

# fan_nomi = Fan('Natematika', 'Fizika', 'Ingliz tili')
# talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012",fan_nomi)

# print(talaba.fan.get_fan())


# def __init__(self, ism, familiya, passport, tyil):
#     """Shaxsning xususiyatlari"""
#     self.ism = ism
#     self.familiya = familiya
#     self.passport = passport
#     self.tyil = tyil

# def get_info(self):
#     """Shaxs haqida ma'lumot"""
#     info = f"{self.ism} {self.familiya}. "
#     info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#     return info

# def get_age(self, yil):
#     """Shaxsning yoshini qaytaruvchi metod"""
#     return yil - self.tyil

# talabalar = []

# def __init__(self, ism, familiya, passport, tyil, idraqam, fan):
#     """Talabaning xususiyatlari"""
#     super().__init__(ism, familiya, passport, tyil)
#     self.idraqam = idraqam
#     self.bosqich = 1
#     self.fan = fan

# def get_id(self):
#     """Talabaning ID raqami"""
#     return self.idraqam

# def get_bosqich(self):
#     """Talabaning o'qish bosqichi"""
#     return self.bosqich

# def get_info(self):
#     """Talaba haqida ma'lumot"""
#     info = f"{self.ism} {self.familiya}. "
#     info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
#     return info

# def fanga_yozil(self, fan):
#     """Fan objectini talaba listiga qo'shish"""
#     self.talabalar.append(fan)

    
