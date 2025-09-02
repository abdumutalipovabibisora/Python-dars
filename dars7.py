# 21-30. Meros Olish va Polimorfizm
# # 1
# class Vehicle:
#     def __init__(self, brend, model):
#         self.brend = brand
#         self.model = model

#     def display_info(self):
#         return f"{self.brend} {self.model}"

# class Car(Vehicle):
#     def __init__(self, brend, model, rang):
#         Vehicle.__init__(self,brend, model)
#         self.color = rang

#     def display_info(self):
#         return f"{self.brend} {self.model}, {self.color}"

# class Bike(Vehicle):
#     pass

# # 2
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def Name(self):
#         return f"{self.name}"

# class Dog(Animal):
#     def __init__(self, name, rangi):
#         Animal.__init__(self, name)
#         self.color = rangi 

#     def Color(self):
#         return f"{self.color}"

# d = Dog("it", "qora")
# print(d.Name())
# print(d.Color())

# # 3
# class Bird:
#     def speak(self):
#         print("Chirp chirp")

# class Parrot(Bird):
#     def speak(self):
#         print("chip chip")

# bird = Bird()
# parrot = Parrot()
# bird.speak()
# parrot.speak()

# # 4
# class Manager:
#     def __init__(self, ism, jamoa):
#         self.name = ism
#         self.team = jamoa
#         print(f"{self.name} of {self.team} team")

# class Employee(Manager):
#     def __init__(self, ism, jamoa, lavozim):
#         super().__init__(ism, jamoa)
#         self.position = lavozim
#         print(f"Employee: {self.name}, Position: {self.position}")

# emp = Employee("Ali", "IT", "Developer")

# # 5
# class Person:
#     def __init__(self, ism, yosh):
#         self.name = ism
#         self.age = yosh
#         print(f"Ismi: {self.name}, Yoshi: {self.age}")

# class Employee(Person):
#     def __init__(self, ism, yosh, lavozim):
#         super().__init__(ism, yosh)
#         self.job_title = lavozim
#         print(f"Ismi: {self.name}, Lavozimi: {self.job_title}")

# emp = Employee("Ali", 30, "Software Developer")

# # 6
# class Shape:
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2 

# class Square(Shape):
#     def __init__(self, a):
#         self.a = a

#     def area(self):
#         return self.a ** 2

# circle = Circle(5)
# square = Square(4)

# print(f"Circle area: {circle.area()}")
# print(f"Square area: {square.area()}")

# # 7
# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")

# dog = Dog()
# animal = Animal()

# print(isinstance(dog, Dog))
# print(isinstance(dog, Animal))
# print(isinstance(animal, Dog))
# print(isinstance(animal, Animal))

# # 8
# class Bird:
#     def __init__(self, name):
#         self.name = name

#     def fly(self):
#         print(f"{self.name} is flying.")

# class Penguin(Bird):
#     def __init__(self, name):
#         super().__init__(name)

#     def fly(self):
#         print(f"{self.name} can not fly.")

# qush = Bird("qaldirg'och")
# penguin = Penguin("Penguin")
# qush.fly()
# penguin.fly() 

# # 9
# class Mashina:
#     def __init__(self, brend, narx):
#         self.brend = brend
#         self.narx = narx

#     def narxni_solishtir(self, boshqa_mashina):
#         if self.narx < boshqa_mashina.narx:
#             return f"{self.brend} arzonroq."
#         elif self.narx > boshqa_mashina.narx:
#             return f"{self.brend} qimmatroq."
#         else:
#             return f"{self.brend} va {boshqa_mashina.brend} ning narxi bir xil."

# mashina1 = Mashina("BMW", 25000)
# mashina2 = Mashina("Tesla", 23000)
# print(mashina1.narxni_solishtir(mashina2))

# # 10
class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, s):
        self.balance += s
        return self

    def withdraw(self, s):
        if self.balance >= s:
            self.balance -= s
        else:
            print("Yetarli mablag' yo'q!")
        return self

    def get_balance(self):
        print(f"Joriy balans: {self.balance}")
        return self

account = Account(1000)
account.deposit(500).withdraw(200).get_balance()
