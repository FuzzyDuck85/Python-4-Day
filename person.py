# Object Orientated Programming

class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def talk(self):
        return "Hi, my name is " + self.name + "!" + " I am " + str(self.age) + " years old."

class Employee(Person):

    def __init__(self, employee_number, name, age, height):
        self.employee_number = employee_number
        super().__init__(name, age, height)

    def get_employee_number(self):
        return self.employee_number

new_person = Person("Donald", 35, 183)
new_employee = Employee(9999, "Gavin", 34, 185)
print(new_person.name)
print(new_person.talk())
print(new_employee.name)
print(new_employee.talk())
