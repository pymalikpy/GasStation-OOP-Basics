# name and salary will be different for each instance of the class
# if we want to make anything private we indicate it by adding an underscore but it is not hidden, it means
# these attributes should not be accessed and technically this is called encapsulation
# which means no one needs to know about implementation of the variable or method
class Employee:
    def __init__(self, first_name, last_name,
                 salary, shift):  # Adding an initializer/parameter/attributes and storing its value in self
        self._first_name = first_name
        self._last_name = last_name
        self.salary = salary
        self.shift = shift

    def get_full_name(self):
        return f"{self._last_name} {self._first_name}"

    def raise_salary(self, amount):
        self.salary = self.salary + amount


# This means that Manager is inherited from Employee
# job_title is directly declared in the class, it is called class variable
# Here we have also used polymorphism, where job_title is decided based on the subclass value for the variable
class Manager(Employee):
    job_title = "Manager"


class Mechanic(Employee):
    job_title = "Mechanic"


class Attendant(Employee):
    job_title = "Station Attendant"


class Cook(Employee):
    job_title = "Cook"
