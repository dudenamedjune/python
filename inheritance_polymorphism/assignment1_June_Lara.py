import employees
import prettytable

def main():
    employees_list = []

    employees_list.append(employees.HourlyPaid("John Smith", "Accounting", 20.5, 55))
    employees_list.append(employees.SalaryPaid("Mary Smith", "Finance", 2500))
    employees_list.append(employees.CommissionPaid("Justin White", "Marketing", 500, 50000))

    table = prettytable.PrettyTable(["Employee Type", "Employee Name", "Department", "Pay"])

    for employee in employees_list:
        table.add_row([employee, employee.get_name(), employee.get_department(), "${:,.2f}".format(employee.pay())])
        
    print(table)
    print("Total pay for all employees:", "${:,.2f}".format(sum(employee.pay() for employee in employees_list)))
    
main()
