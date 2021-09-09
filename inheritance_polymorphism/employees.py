class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department
    
    def get_name(self):
        return self.name

    def set_name(self, name):
       self.name = name 

    def get_department(self):
        return self.department 

    def set_department(self, department):
        self.department = department 

    def pay():
        return 0.0

    def __str__(self):
        return "Employee Class implements name and department and pay"


class CommissionPaid(Employee):
    def __init__(self, name, department, base_rate, sales):
        self.base_rate = base_rate
        self.sales = sales
        Employee.__init__(self, name, department)

    def get_base_rate(self):
        return self.base_rate

    def set_base_rate(self, base_rate):
        self.base_rate = base_rate

    def get_sales(self):
        return self.sales

    def set_sales(self, sales):
        self.sales = sales

    def pay(self):
        if self.sales > 30000:
            commission_rate = 0.03
        elif self.sales > 5000:
            commission_rate = 0.01
        else:
            commission_rate = 0.0
        pay = self.base_rate + commission_rate * self.sales
        return pay

    def __str__(self):
        return "Commission Paid"

class HourlyPaid(Employee):
    def __init__(self, name, department, hourly_rate, hours):
        self.hourly_rate = hourly_rate
        self.hours = hours
        super().__init__(name, department) 
    
    def get_hourly_rate(self):
        return self.hourly_rate

    def set_hourly_rate(self, hourly_rate):
        self.hourly_rate = hourly_rate

    def get_hours(self):
        return self.hours

    def set_hours(self, hours):
        self.hours = hours

    def pay(self):
        if self.hours > 40:
            pay = 40 * self.hourly_rate + (self.hours - 40) * self.hourly_rate * 1.5
        else:
            pay = self.hours * self.hourly_rate
        return pay

    def __str__(self):
        return "Hourly Paid"

class SalaryPaid(Employee):
    def __init__(self, name, department, salary):
        self.salary = salary
        super().__init__(name, department) 
    
    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def pay(self):
        return self.salary

    def __str__(self):
        return "Salary Paid"