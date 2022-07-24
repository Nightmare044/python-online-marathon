class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
    def from_string(self):
        '{}-{}-{}'.format(self.firstname, self.lastname, self.salary)


emp1 = Employee("Mary", "Sue", 60000)
print(emp1.firstname)
print(emp1.lastname)
print(emp1.salary)
print(isinstance(emp1.salary, int))


emp2 = Employee.from_string("John-Smith-55000")
print(emp2.firstname)
print(emp2.lastname)
print(emp2.salary)
print(isinstance(emp2.salary, int))