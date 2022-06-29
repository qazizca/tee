# class Student:
#     id = 0
#     name = ""
#     surname = ""
#     gpa = 0
#
#     def __init__(self, id, name, surname, gpa):
#         self.id = id
#         self.name = name
#         self.surname = surname
#         self.gpa = gpa
#
#     def getStudentData(self):
#         return self.id, self.name, self.surname, self.gpa
#
#
# class Phone:
#     name = ""
#     model = ""
#     price = 0
#     def __init__(self, name, model, price):
#         self.name = name
#         self.model = model
#         self.price = price
#
#     def getData(self):
#         return self.name, self.model, self.price
#
# class Student1:
#     name = ""
#     surname = ""
#     gpa = 0
#
#     def __init__(self, name, surname, gpa):
#         self.name = name
#         self.surname = surname
#         self.gpa = gpa
#
#     def getStudentData(self):
#         return self.name, self.surname, self.gpa
# class Employee:
#     name = ''
#     age = 0
#     salary = 0
#
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     def getEmployeeData(self):
#         return self.name, self.age, self.salary
#
# class Programmer(Employee):
#     programmingLanguage = ''
#     def __init__(self, name, age, salary, programmingLanguage):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.programmingLanguage = programmingLanguage
#     def getProgrammerData(self):
#         return self.name, self.age, self.salary, self.programmingLanguage
#
# class DataAnalitic(Employee):
#     databaseTool = ''
#     def __init__(self, name, age, salary, databaseTool):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.databaseTool = databaseTool
#     def getDataAnalytic(self):
#         return self.name, self.age, self.salary, self.databaseTool
#
#
# class Book:
#     number = 0
#     title = ''
#     author = ''
#     pages = 0
#
#     def __init__(self, number, title, author, pages):
#         self.number = number
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def getBookData(self):
#         return self.number, self.title, self.author, self.pages
#
#
# class User:
#     name = ''
#     surname = ''
#     age = 0
#
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def getUserData(self):
#         return self.name, self.surname, self.age
#
#
# 123123123
#
# class User1:
#     id = 0
#     login = ''
#     password = ''
#     name = ''
#     surname = ''
#
#     def __init__(self, id, login, password, name, surname):
#         self.id = id
#         self.login = login
#         self.__password = ""
#         self.name = name
#         self.surname = surname
#
# class Staff(User1):
#     id = 0
#     login = ''
#     password = ''
#     name = ''
#     surname = ''
#     salary = float
#     subjects = []
#
#     def __init__(self, id, login, password, name, surname, salary):
#         self.id = id
#         self.login = login
#         self.password = password
#         self.name = name
#         self.surname = surname
#         self.salary = salary
#
#     def getStaffData(self):
#         return self.id, self.login, self.password, self.name, self.surname, self.salary
#     def addSubject(self,subject):
#         for i in range(len(subject)):
#             newSub = input()
#             subject.append(newSub)
#
# # class Student(User1):
# #     id = 0
# #     login = ''
# #     password = ''
# #     name = ''
# #     surname = ''
# #     gpa = float
# #     course = []
# #
# #     def __init__(self, id, login, password, name, surname, gpa):
# #         self.id = id
# #         self.login = login
# #         self.password = password
# #         self.name = name
# #         self.surname = surname
# #         self.gpa = gpa
# #
# #     def getStudentData(self):
# #         return self.id, self.login, self.password, self.name, self.surname, self.gpa
# #     def getUser1Data(self, course):
# #         for i in range(len(course())):
# #             newCour = input()
# #             course.append(newCour)
# #
# #
# #
# #
# #
# #
# #
# #    #""" de set_password(self, password):
# #     #    low = False
# #      #   upper = False
# #       #  for i in password:
# #        #     if i.islower():
# #         #        low = True
# #          #       continue
# #           #  if i.isupper():
# #            #     upper = True
# #             #    break
# #
# #         #if 8 < len(password) < 16 and low == True and upper == True:
# #          #   self.__password = password"""
# #
# #
# #
# #
# #     def getUser1Data(self):
# #         return self.id, self.login, self.password, self.name, self.surname
# #
# #
# # class Student(User1):
# #     courses = []
# #     def __init__(self, id, login, password, name, surname, gpa):
# #         super().__init__(id, login, password, name, surname)
# #         self.gpa = gpa
# #         self.courses = []
# #
# #     def getStudentData(self):
# #         return self.id, self.login, self.password, self.name, self.surname, self.gpa
# #
# #     def addCourse(self, course):
# #         self.courses.append(course)
# #
# #
# # class Staff(User1):
# #     subjects = []
# #
# #     def __init__(self, id, login, password, name, surname, salary):
# #         super().__init__(id, login, password, name, surname)
# #         self.subjects = []
# #         self.salary = salary
# #
# #     def getStaffData(self):
# #         return self.id, self.login, self.password, self.name, self.surname, self.salary,
# #
# #     def addSubject(self, subject):
# #         self.subjects.append(subject)
# #
# #
# # staff1 = Staff(2, 'login2', 'pas', 'Stafname', 'Stafsurname', 3000)
# # staff2 = Staff(4, 'login', 'pas', 'Stafname', 'Stafsurname', 3000)
# #
# # student1 = Student(1, 'login1', 'password1', 'name1', 'surname1', 2.5)
# # student2 = Student(2, 'login2', 'password2', 'name2', 'surname2', 3.5)
# #
# # user1 = User1(1,1,'password','name','surname')
# # user1.set_password("text")
# # staff1.addSubject("Math")
# # student1.addCourse('math')
# #
# # arr = [staff1, staff2, student2, student1, user1]
# #
# # print(student1.courses)
# # print(staff1.subjects)
#
# class Car:
#     name = ''
#     model = ''
#     maxSpeed = ''
#     year = 0
#     volume = float
#
#     def __init__(self, name, model, maxSpeed, year, volume):
#         self.name = name
#         self.model = model
#         self.maxSpeed = maxSpeed
#         self.year = year
#         self.volume = volume
#
#     def ride(self):
#         print('Name:{0}, Model:{1}, MaxSpeed:{3}, Year:{4}, Volume:{5} is riding'.format(self.name, self.model, self.maxSpeed, self.year, self.year, self.volume))
#
#
# class Toyota(Car):
#     manufacturer = ""
#
#     def __init__(self, name, model, maxSpeed, year, volume, manufacturer):
#         super().__init__(name, model, maxSpeed, year, volume)
#         self.manufacturer = manufacturer
#
#     def ride(self):
#         print('Toyota by name:{0}, Model:{1}, MaxSpeed:{3}, Year:{4}, Volume:{5}, manufacturer: {6} is riding'.format(self.name, self.model,
#                                                                                         self.maxSpeed, self.year,
#                                                                                         self.year, self.volume, self.manufacturer))
#
#
# class Mercedes(Car):
#
#     def __init__(self, name, model, maxSpeed, year, volume, classType):
#         super().__init__(name, model, maxSpeed, year, volume)
#         self.classType = classType
#
#     def ride(self):
#         print('Mercedes by name:{0}, Model:{1}, MaxSpeed:{3}, Year:{4}, Volume:{5}, classType:{6} is riding'.format(self.name, self.model,
#                                                                                         self.maxSpeed, self.year,
#                                                                                         self.year, self.volume, self.classType))
#
class User:
    id = 0
    first_name = ""
    text_message = ""

    def __init__(self, id, first_name, text_message):
        self.id = id
        self.first_name = first_name
        self.text_message = text_message

    def get_user_data(self):
        return "ID is: {0} " \
               "first name is: {1}, " \
               "Message is: {2} \n".format(self.id,self.first_name, self.text_message)
