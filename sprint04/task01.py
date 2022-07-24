"""Define a class Employee. In the class Employee implement the instance attributes as firstname, lastname and salary.

Create the method from_string() which parses a string containing these attributes and assigns them to the correct properties. Properties will be separated by a dash.

Examples:
emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")
emp1.firstname ➞ "Mary"
emp1.salary ➞ 60000
emp2.firstname ➞ "John"
"""


class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = int(salary)
    #
    # def from_string(self, value):
    #     value.split("-")
    #     self.firstname = value[0]
    #     self.lastname = value[1]
    #     self.salary = int(value[2])


emp1 = Employee("Mary", "Sue", 60000)
print(emp1.firstname)
print(emp1.lastname)
print(emp1.salary)
print(isinstance(emp1.salary, int))

#
# emp2 = Employee.from_string("John-Smith-55000")
# print(emp2.firstname)
# print(emp2.lastname)
# print(emp2.salary)
# print(isinstance(emp2.salary, int))
