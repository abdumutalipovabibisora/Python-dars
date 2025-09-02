# mavzu: Python dasturlash tilida Sinflar

# 1-10. Asosiy Sinflar va Obyektlar

# # 1.	Sinf yaratish: Book nomli sinf yarating va uning title va author atributlarini o‘rnating. 
# class Book:
#     def __init__(self, nomi, muallifi):
#         self.title = nomi
#         self.author = muallifi

# kitob1 = Book("Muqaddima", "Ibn Xaldun")
# print(f"{kitob1.author} {kitob1.title}")
        
# # 2.	Obyekt yaratish: Car sinfini yarating va undan 3 ta obyekt hosil qiling. 
# class Car:
#     def __init__(self, madel, rang):
#         self.madel = madel
#         self.rang = rang

# mashina1 = Car("BMW", "black")
# mashina2 = Car("Tesla", "black")
# mashina3 = Car("Ferrari", "white")

# print(f"{mashina1.madel} {mashina1.rang}")
# print(f"{mashina2.madel} {mashina2.rang}")
# print(f"{mashina3.madel} {mashina3.rang}")

# # 3.	Metod qo‘shish: Person sinfiga greet() metodini qo‘shing, u ismni ekranga chiqarishi kerak
# class Person:
#     def __init__(self, ism, fam, yosh):
#         self.name = ism
#         self.surname = fam
#         self.age = yosh
#     def greet(self):
#         print(self.name)

# odam = Person("Ali", "Valiyev", 20)
# odam.greet()

# # 4.	Obyekt atributlarini o‘zgartirish: Laptop sinfida brand va price atributlari bo‘lsin, ularning qiymatini o‘zgartiring. 
# class Laptop:
#     def __init__(self, brand, narx):
#         self.brand = brand
#         self.price = narx
#     def yangi(self, brand_y, narx_y):
#         self.brand = brand_y
#         self.price = narx_y

# komp = Laptop("hp", "380$")
# print(f"{komp.brand} {komp.price}")
# komp.yangi("apple", "1100$")
# print(f"{komp.brand} {komp.price}")
    
# # 5.	__init__ metodini ishlatish: Student sinfi yaratib, uning ism va yosh atributlarini __init__ metodi orqali o‘rnating. 
# class Student:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh

# student = Student("Ali", 20)
# print(f"{student.ism} {student.yosh}")

# # 6.	Xususiyatni o‘zgartirish: Phone sinfini yaratib, color atributini tashqaridan o‘zgartiring. 
# class Phone:
#     def __init__(self, nomi, xotirasi, rangi):
#         self.name = nomi
#         self.memory = xotirasi
#         self.color = rangi

# tel = Phone("A05s", 128, "seriy")
# print(f"{tel.name} {tel.memory} {tel.color}")

# tel.color = "White"
# print(f"{tel.name} {tel.memory} {tel.color}")

# # 7.	Obyekt ma’lumotlarini chiqarish: Movie sinfida display_info() metodini qo‘shing. 
# class Movie:
#     def __init__(self, nomi, janri):
#         self.name = nomi
#         self.janr = janri
#     def info(self):
#         print(f"{self.name} {self.janr}")

# kino = Movie("Kalmar oyini", "Dorama")
# kino.info()  

# # 8.	Xususiyatni qo‘shish: Animal sinfini yaratib, unga age atributini qo‘shing. 
# class Animal:
#     def __init__(self, age):
#         self.age = age

# hayvon = Animal(5)
# print(hayvon.age)

# # 9.	Foydalanuvchi kiritgan ma’lumot bilan obyekt yaratish: House sinfida foydalanuvchidan uy turi va narxi ni kiritishni so‘rang. 
# class House:
#     def __init__(self, turi, narx):
#         self.house = turi
#         self.price = narx

# house = input("Uy turini kiriting: ")
# price = int(input("Uy narxini kiriting: "))
# house1 = House(house, price)
# print(f"{house1.house} {house1.price}")

# 10.	Bir nechta obyekt yaratish va ularning ma’lumotlarini chiqarish: City sinfini yarating va 5 ta shahar obyektlarini saqlang. 
class City:
    def __init__(self, nomi, joylashgan_joyi):
        self.name = nomi
        self.manzil = joylashgan_joyi

shahar1 = City("Andijon", "Andijon viloyati" )
shahar2 = City("Toshkent", "O'zbekiston")
shahar3 = City("Navoiy", "Navoiy viloyati")
shahar4 = City("Buxoro", "Buxoro vilyati")
shahar5 = City("Shaxrisabz", "Qashqadaryo viloyati")

print(f"{shahar1.name} {shahar1.manzil}")
print(f"{shahar2.name} {shahar2.manzil}")
print(f"{shahar3.name} {shahar3.manzil}")
print(f"{shahar4.name} {shahar4.manzil}")
print(f"{shahar5.name} {shahar5.manzil}")
