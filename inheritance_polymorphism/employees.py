class Employee:
    def __init__(self, name, department):
        """
        This is a constructor for the Employee class
        :param name: name of employee
        :type name: str
        :param department: department of employee
        :type department: str
        :return: None
        """
        self.name = name
        self.department = department
        
    def get_name(self):
        """
        This method returns the name of the employee
        :return: name of employee
        :rtype: str
        """
        return self.name

    def set_name(self, name):
        """
        This method sets the name of the employee
        :param name: name of employee
        :type name: str
        :return: None
        """
        self.name = name 

    def get_department(self):
        """
        This method returns the department of the employee
        :return: department of employee
        :rtype: str
        """
        return self.department

    def set_department(self, department):
        """
        This method sets the department of the employee
        :param department: department of employee
        :type department: str
        :return: None
        """
        self.department = department

    def pay():
        """
        This method returns the pay of the employee
        :return: pay of employee
        :rtype: float
        """
        return 0.0

    def __str__(self):
        """
        This method returns a string representation of the employee
        :return: string representation of employee
        :rtype: str 
        """
        return "Employee Class implements name and department and pay"


class CommissionPaid(Employee):
    def __init__(self, name, department, base_rate, sales):
        """
        This is a constructor for the CommissionPaid class
        :param name: name of employee
        :type name: str
        :param department: department of employee
        :type department: str
        :param base_rate: base rate of employee
        :type base_rate: float
        :param sales: sales of employee
        :type sales: float
        :return: None
        """
        self.base_rate = base_rate
        self.sales = sales
        Employee.__init__(self, name, department)

    def get_base_rate(self):
        """
        This method returns the base rate of the employee
        :return: base rate of employee
        :rtype: float
        """
        return self.base_rate

    def set_base_rate(self, base_rate):
        """
        This method sets the base rate of the employee
        :param base_rate: base rate of employee
        :type base_rate: float
        :return: None
        """
        self.base_rate = base_rate

    def get_sales(self):
        """
        This method returns the sales of the employee
        :return: sales of employee
        :rtype: float
        """
        return self.sales

    def set_sales(self, sales):
        """
        This method sets the sales of the employee
        :param sales: sales of employee
        :type sales: float
        :return: None
        """
        self.sales = sales

    def __get_commission_rate__(self):
        """
        This method returns the commission rate of the employee
        :return: commission rate of employee
        :rtype: float
        """
        if self.sales > 30000:
            return 0.03
        elif self.sales > 5000:
            return  0.01
        else:
            return 0.0 

    def pay(self):
        """
        This method returns the pay of the employee
        :return: pay of employee
        :rtype: float
        """
        pay = self.base_rate + self.__get_commission_rate__() * self.sales
        return pay

    def __str__(self):
        """
        This method returns a string representation of the employee
        :return: string representation of employee
        :rtype: str
        """
        return "Commission Paid"

class HourlyPaid(Employee):
    def __init__(self, name, department, hourly_rate, hours):
        """
        This is a constructor for the HourlyPaid class
        :param name: name of employee
        :type name: str
        :param department: department of employee
        :type department: str
        :param hourly_rate: hourly rate of employee
        :type hourly_rate: float
        :param hours: hours of employee
        :type hours: float
        :return: None
        """
        self.hourly_rate = hourly_rate
        self.hours = hours
        super().__init__(name, department) 
    
    def get_hourly_rate(self):
        """
        This method returns the hourly rate of the employee
        :return: hourly rate of employee
        :rtype: float
        """
        return self.hourly_rate

    def set_hourly_rate(self, hourly_rate):
        """
        This method sets the hourly rate of the employee
        :param hourly_rate: hourly rate of employee
        :type hourly_rate: float
        :return: None
        """
        self.hourly_rate = hourly_rate

    def get_hours(self):
        """
        This method returns the hours of the employee
        :return: hours of employee
        :rtype: float
        """
        return self.hours

    def set_hours(self, hours):
        """
        This method sets the hours of the employee
        :param hours: hours of employee
        :type hours: float
        :return: None
        """
        self.hours = hours

    def pay(self):
        """
        This method returns the pay of the employee
        :return: pay of employee
        :rtype: float
        """
        if self.hours > 40:
            pay = 40 * self.hourly_rate + (self.hours - 40) * self.hourly_rate * 1.5
        else:
            pay = self.hours * self.hourly_rate
        return pay

    def __str__(self):
        return "Hourly Paid"

class SalaryPaid(Employee):
    def __init__(self, name, department, salary):
        """
        This is a constructor for the SalaryPaid class
        :param name: name of employee
        :type name: str
        :param department: department of employee
        :type department: str
        :param salary: salary of employee
        :type salary: float
        :return: None
        """
        self.salary = salary
        super().__init__(name, department) 
    
    def get_salary(self):
        """
        This method returns the salary of the employee
        :return: salary of employee
        :rtype: float
        """
        return self.salary

    def set_salary(self, salary):
        """
        This method sets the salary of the employee
        :param salary: salary of employee
        :type salary: float
        :return: None
        """
        self.salary = salary

    def pay(self):
        """
        This method returns the pay of the employee
        :return: pay of employee
        :rtype: float
        """
        return self.salary

    def __str__(self):
        """
        This method returns a string representation of the employee
        :return: string representation of employee
        :rtype: str
        """
        return "Salary Paid"