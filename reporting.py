# Report was tightly coupled to employee list and we wanted to decouple that dependency
# Now we can move the report code to any location we want by eliminating the dependency
# We did this by passing an emp_list in place of employees list
# We inject this dependency when we instantiate the object
# This is called dependency injection

from Report import Report


class AccountingReport(Report):

    def print_report(self):
        print("Accounting")
        print("============================")
        for e in self._emp_list:
            print(f"{e.get_full_name()},${e.salary}")


class StaffingReport(Report):

    def print_report(self):
        print("Staffing")
        print("===========================")
        for e in self._emp_list:
            print(f"{e.get_full_name()},{e.job_title}")


class ScheduleReport(Report):

    def print_report(self):
        print("Schedule")
        print("==============================")
        for e in self._emp_list:
            print(f"{e.get_full_name()},{e.shift.get_shift_info()}")

# We still have duplicate code in this class now we will go bottom up approach
# We will create a subclass Report which will be abstract
# This abstract class is never to be instantiated but always be inherited in the child class
