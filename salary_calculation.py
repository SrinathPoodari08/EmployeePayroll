
def calculate_salary():
    basic = float(input("Enter Basic Salary: "))
    hra = float(input("Enter HRA: "))
    da = float(input("Enter DA: "))
    deductions = float(input("Enter Deductions: "))

    net_salary = basic + hra + da - deductions

    print("\nSalary Calculation")
    print("Basic Salary:", basic)
    print("Net Salary:", net_salary)

calculate_salary()
