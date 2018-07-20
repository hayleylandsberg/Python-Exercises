# Create a class that contains information about employees of a company and define methods to get/set employee name, job title, and start date.

# Consider the concept of aggregation, and modify the Company class so that you assign employees to a company.

# Create a company, and three employees, and then assign the employees to the company.

class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = set()

    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name

class Employee(object):
    def __init__(self, employee_name, employee_title, employee_start_date):
        self.employee_name = employee_name
        self.employee_title = employee_title
        self.employee_start_date = employee_start_date

    def get_employee(self):
        return self.employee_name + employee_title + employee_start_date

#create company
Amazon = Company("Amazon", "1994")

#create employees
Eric = Employee("Eric Rivers", "Software Engineer", "01-09-13")
Joe = Employee("Joe Kline", "Communications Manager", "02-03-16")
Mary = Employee("Mary Peters", "Art Director", "03-20-12")

Amazon.employees.add(Eric)
Amazon.employees.add(Joe)
Amazon.employees.add(Mary)
