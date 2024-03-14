# Braden Jackson
# CIS261
# Week 7 Course Project Phase 3

def get_emp_name():
    emp_name = input("Enter employee name: ")
    return emp_name

def get_dates_worked():
    from_date = input("Enter Start Date (mm/dd/yyyy): ")
    to_date = input("Enter End Date (mm/dd/yyyy): ")
    return from_date, to_date

def get_hours_worked():
    while True:
        try:
            hours = float(input('Enter amount of hours worked: '))
            return hours
        except ValueError:
            print("Please enter a valid number.")

def get_hourly_rate():
    while True:
        try:
            hourly_rate = float(input("Enter hourly rate: "))
            return hourly_rate
        except ValueError:
            print("Please enter a valid number.")

def get_tax_rate():
    while True:
        try:
            tax_rate = float(input("Enter tax rate: "))
            return tax_rate
        except ValueError:
            print("Please enter a valid number.")

def calc_tax_and_net_pay(hours, hourly_rate, tax_rate):
    gross_pay = hours * hourly_rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def print_info(emp_detail_list):
    total_employees = 0
    total_hours = 0.00
    total_gross_pay = 0.00
    total_tax = 0.00
    total_net_pay = 0.00
    for emp_list in emp_detail_list:
        from_date, to_date, emp_name, hours, hourly_rate, tax_rate = emp_list

        gross_pay, income_tax, net_pay = calc_tax_and_net_pay(hours, hourly_rate, tax_rate)
        print(from_date, to_date, emp_name, f"{hours:,.2f}", f"{hourly_rate:,.2f}", f"{gross_pay:,.2f}", f"{tax_rate:,.1%}", f"{income_tax:,.2f}", f"{net_pay:,.2f}")

        total_employees += 1
        total_hours += hours
        total_gross_pay += gross_pay
        total_tax += income_tax
        total_net_pay += net_pay

    emp_totals = {"Total Employees": total_employees, "Total Hours": total_hours, "Total Gross Pay": total_gross_pay, "Total Tax": total_tax, "Total Net Pay": total_net_pay}
    print_totals(emp_totals)

def print_totals(emp_totals):
    print()
    for key, value in emp_totals.items():
        print(f"{key}: {value:,.2f}")

def write_employee_information(employee):
    with open("employeeinfo.txt", "a") as file:
        file.write('{}|{}|{}|{}|{}|{}\n'.format(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))

def get_from_date():
    while True:
        from_date = input("Enter From Date (mm/dd/yyyy): ")
        if len(from_date.split('/')) == 3 or from_date.upper() == 'ALL':
            return from_date
        else:
            print("Invalid Date Format.")

def read_employee_information(from_date):
    emp_detail_list = []
    with open("employeeinfo.txt", "r") as file:
        for line in file:
            employee = [x.strip() for x in line.strip().split("|")]
            if from_date.upper() == 'ALL' or from_date == employee[0]:
                emp_detail_list.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
    return emp_detail_list

if __name__ == "__main__":
    while True:
        emp_name = get_emp_name()
        if emp_name.upper() == "END":
            break
        from_date, to_date = get_dates_worked()
        hours = get_hours_worked()
        hourly_rate = get_hourly_rate()
        tax_rate = get_tax_rate()
        emp_detail = [from_date, to_date, emp_name, hours, hourly_rate, tax_rate]
        write_employee_information(emp_detail)

    from_date = get_from_date()
    emp_detail_list = read_employee_information(from_date)
    print()
    print_info(emp_detail_list)
