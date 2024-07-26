# For a gas station make a list of employees and print their salaries

# names = ["Baba", "Dada", "Sasa", "Haha", "Yaya", "Chaa", "Rara"]
# salaries = [4000, 5000, 8000, 9000, 12000, 7000, 6000]
#
# count = len(names)
#
# for c in range(count):
#     print(f"{names[c]}, ${salaries[c]}")

# -------------------------------------------------------------------------------------------------------------------


# this is good, but it is a fragile code
# to improve it we need to create a class that is like blueprint of the object
# we could create an object that could something like key value
# an employee and its salary

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary


# e = Employee("Dada", 5000)
# print(f"{e.name}, ${e.salary}")

# employees = [
#     Employee("Baba", 4000),
#     Employee("Dada", 5000),
#     Employee("Sasa", 8000),
#     Employee("Haha", 9000),
#     Employee("Yaya", 12000),
#     Employee("Chaa", 7000),
# ]
#
# for e in employees:
#     print(f"{e.name}, ${e.salary}")

# -------------------------------------------------------------------------------------------------------------------

# Now we got the new requirement to add the job_title of employees


# class Employee:
#     def __init__(self, name, salary, job_title):  # Adding an initializer/parameter/attributes and storing its value in self
#         self.name = name
#         self.salary = salary
#         self.job_title = job_title
#
#
# employees = [
#     Employee("Baba", 4000, "Manager"),
#     Employee("Dada", 5000, "Attendant"),
#     Employee("Sasa", 8000, "Cook"),
#     Employee("Haha", 9000, "Cook"),
#     Employee("Yaya", 12000, "Car Repair"),
#     Employee("Chaa", 7000, "Car Repair"),
# ]
#
# for e in employees:
#     print(f"{e.name}, ${e.salary}, {e.job_title}")

# -------------------------------------------------------------------------------------------------------------------

# New requirement to change two job titles
# Change Attendant to Station Attendant and Car Repair to Mechanic


# class Employee:
#     def __init__(self, name, salary,
#                  job_title):  # Adding an initializer/parameter/attributes and storing its value in self
#         self.name = name
#         self.salary = salary
#         self.job_title = job_title
#
#
# employees = [
#     Employee("Baba", 4000, "Manager"),
#     Employee("Dada", 5000, "Station Attendant"),
#     Employee("Sasa", 8000, "Cook"),
#     Employee("Haha", 9000, "Cook"),
#     Employee("Yaya", 12000, "Mechanic"),
#     Employee("Chaa", 7000, "Mechanic"),
# ]
#
# for e in employees:
#     print(f"{e.name}, ${e.salary}, {e.job_title}")

# -------------------------------------------------------------------------------------------------------------


# Here we see we had a duplicate code that can be solved by inheritance
# We can create a different subclass for attendant, mechanic, cook and manager and
# remove the job_title from main class each time we instantiate the employee object

from employee import Manager
from employee import Mechanic
from employee import Cook
from employee import Attendant
from reporting import AccountingReport
from reporting import StaffingReport
from reporting import ScheduleReport
from shift import MorningShift
from shift import EveningShift
from shift import NightShift
import datetime

# employees = [
#     Manager("Baba", 4000),
#     Mechanic("Dada", 5000),
#     Cook("Sasa", 8000),
#     Attendant("Haha", 9000),
#     Cook("Yaya", 12000),
#     Cook("Chaa", 7000),
#     Mechanic("Rara", 5000)
# ]
#
# for e in employees:
#     print(f"{e.name}, ${e.salary}, {e.job_title}")


# ----------------------------------------------------------------------------------------------

# New requirement to create a new report
# 1) For staffing
# 2) For accounting

employees = [
    Manager("Baba", "Left", 4000, EveningShift()),
    Mechanic("Dada", "Right", 5000, MorningShift()),
    Cook("Sasa", "Aaya", 8000, NightShift()),
    Attendant("Haha", "Gaya", 9000, MorningShift()),
    Cook("Yaya", "Naya", 12000, EveningShift()),
    Cook("Chaa", "Paya", 7000, EveningShift()),
    Mechanic("Rara", "Saya", 5000, MorningShift()),
    Attendant("Rama", "Shyama", 25000, MorningShift)
]

ar = AccountingReport(employees)
sr = StaffingReport(employees)
tr = ScheduleReport(employees)

reports = [ar, sr, tr,
           ]

for r in reports:
    r.print_report()  # used polymorphism to print both the reports
    print()
