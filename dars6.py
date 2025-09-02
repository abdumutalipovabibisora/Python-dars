# mavzu: Python dasturlash tilida Sinflar davomi...

# 11-20. Sinf Metodlari va Inkapsulyatsiya

# # 11.	Metod bilan hisob-kitob qilish: Rectangle sinfini yarating va uning area() metodini yozing. 
# class Rectangle:
#     def __init__(self, eni, boyi):
#         self.width = eni
#         self.height = boyi

#     def area(self):
#         return self.width * self.height

# t = Rectangle(4, 5)
# print(t.area())

# # 12.	Statik metod yaratish: MathUtils sinfiga @staticmethod bilan add(a, b) metodini qo‘shing. 
# class MathUtils:
#     @staticmethod
#     def add(a,b):
#         return a + b
    
# m = MathUtils.add(64, 565)
# print(m)

# # 13.	Sinf metodidan foydalanish: Company sinfiga umumiy ishchilar sonini ko‘rsatuvchi @classmethod metodini qo‘shing. 
# class Company:
#     s = 0
#     def __init__(self, nomi):
#         self.nomi = nomi
#         Company.s += 1

#     @classmethod
#     def jami_ishchilar(cls):
#         return cls.s

# c = Company("ali")
# print(Company.jami_ishchilar())

# # 14.	Xususiy (private) atribut yaratish: BankAccount sinfiga hisob balansini __balance bilan himoyalang. 
# class BankAccount:
#     def __init__(self, balans):
#         self.__balance = balans

#     def depozit(self, miqdor):
#         if miqdor > 0:
#             self.__balance += miqdor
#         else:
#             print("Iltimos, ijobiy miqdor kiriting.")

#     def yechish(self, miqdor):
#         if miqdor > 0 and miqdor <= self.__balance:
#             self.__balance -= miqdor
#         else:
#             print("Balans yetarli emas.")
    
# h = BankAccount(2000)
# h.depozit(1000)
# hisob = h.yechish(500)

# # 15.	Inkapsulyatsiya qilingan ma’lumotlarga kirish: get_balance() metodi orqali __balance qiymatini qaytaring. 
# class BankAccount:
#     def __init__(self, balans):
#         self.__balance = balans

#     def depozit(self, miqdor):
#         if miqdor > 0:
#             self.__balance += miqdor
#         else:
#             print("Iltimos, ijobiy miqdor kiriting.")

#     def yechish(self, miqdor):
#         if miqdor > 0 and miqdor <= self.__balance:
#             self.__balance -= miqdor
#         else:
#             print("Balans yetarli emas.")

#     def get_balance(self):
#         return self.__balance
    
# h = BankAccount(2000)
# h.depozit(1000)

# h.yechish(500)
# hisob = h.get_balance()
# print(hisob)

# # 16.	O‘zgaruvchi nomlarini yashirish (__): User sinfiga maxfiy parol (__password) atributini qo‘shing.
# class User:
#     def __init__(self, nomi, parol):
#         self.username = nomi
#         self.__password = parol

#     def set_password(self, yangi_parol):
#         if len(yangi_parol) >= 8:
#             self.__password = yangi_parol
#         else:
#             print("Parol kamida 8 ta belgidan iborat bo'lishi kerak.")

#     def get_password(self):
#         return self.__password

# f = User("ali", "cisdjia2")
# print(f.get_password())
# f.set_password("jiajdIJDOai")
# print(f.get_password())

# # 17.	Setter va Getter metodlari: Temperature sinfiga get_celsius() va set_celsius() metodlarini yozing. 
# class Temperature:
#     def __init__(self, gradus):
#         self.__celsius = gradus

#     def set_celsius(self, yangi_celsius):
#         if isinstance(yangi_celsius, (int, float)):
#             self.__celsius = yangi_celsius
#         else:
#             print("Celsius qiymati son bo'lishi kerak.")

#     def get_celsius(self):
#         return self.__celsius

#     def __str__(self):
#         return f"Celsius: {self.__celsius}°C"

# t = Temperature(20)
# print(t.get_celsius())
# t.set_celsius(30)
# print(t.get_celsius())


# # 18.	Sinf ichida hisob-kitob: Circle sinfiga diameter() metodini qo‘shing. 
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def diameter(self):
#         return 2 * self.radius

# c = Circle(2)
# print(c.diameter())

# # 19.	Tashqaridan parametr olish: Car sinfiga speed atributini qo‘shing va increase_speed() metodi bilan tezligini oshiring. 
# class Car:
#     def __init__(self, model, tezlik):
#         self.model = model
#         self.speed = tezlik

#     def increase_speed(self, oshirish):
#         self.speed += oshirish

#     def __str__(self):
#         return f"{self.model} avtomobilning hozirgi tezligi: {self.speed} km/soat"

# c = Car("bmw", 28)
# print(c)
# c.increase_speed(30)
# print(c)

# # 20.	Obyektlarni ro‘yxat sifatida saqlash: Library sinfiga books nomli ro‘yxat qo‘shing va unga kitoblarni qo‘shadigan metod yozing. 
class Library:
    def __init__(self):
        self.books = []  # Kutubxona kitoblari ro'yxati

    def add_book(self, kitob_nomi):
        self.books.append(kitob_nomi)

    def __str__(self):
        return f"Kutubxonada {len(self.books)} ta kitob bor: {self.books}"

l = Library()
l.add_book("men") 
l.add_book("sir")
print(l)
