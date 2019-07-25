# def age_program():
#     seconds_or_years = input("Give me seconds (s) or years (y)?")
#     if seconds_or_years == "s":
#             # Convert seconds to years
#             user_value = input("Enter the number of seconds you've lived for: ")
#             print("You have lived for {} years.".format(int(user_value) / 365 / 24 / 60 /60))
#     elif seconds_or_years == "y":
#             # Convert years to seconds
#             user_value = input("Enter the number of years you've lived for: ")
#             print("You have lived for {} seconds.".format(int(user_value) * 365 * 24 * 60 * 60))
#
# age_program()

owners_names = ['Jenny', 'Sam', 'Alexis']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter']
owners_dogs = zip(owners_names, dogs_names)
print(tuple(owners_dogs))
#Result: [('Jenny', 'Elphonse'), ('Sam', 'Dr.Doggy DDS'), ('Alexis', 'Carter')]

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
x = zip(a, b)
#use the tuple() function to display a readable version of the result:
print(tuple(x))


evens_to_10 = [x*2 for x in range(0, 10) if x % 2 == 0]
print(evens_to_10)

lst = []
for x in range(0,10):
  if x % 2 == 0:
    lst.append(x*2)
print(lst)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class People:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = People("Mary", 30)
p1.myfunc()

class Individual:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Individual("Max", 45)
p1.myfunc()


class Human:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
x = Human("John", "Doe")
x.printname()


#Create a class named Student, which will inherit the properties and methods from the Person class:
#Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
class Student(Human):
  pass
#Use the Student class to create an object, and then execute the printname method:
a = Student("Mike", "Olsen")
a.printname()

#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
#Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student(Human):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)


#Add a year parameter, and pass the correct year when creating objects:
class Student(Human):
  def __init__(self, fname, lname, year):
    Human.__init__(self, fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)


#Add a method called welcome to the Student class:
class Youth(Person):
  def __init__(self, fname, lname, year):
    Person.__init__(self, fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# =============== SUMMARIZE =================
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    Person.__init__(self, fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()