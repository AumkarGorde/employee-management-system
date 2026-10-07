from service.employee_service import (
    EmployeeService
)
from model.employee import Employee, Department, EmployeeStatictics
from tabulate import tabulate

def show_employee(
        employees: list[Employee]
):
    data = [
        [emp.id, emp.name, emp.email, emp.department.name, emp.salary]
        for emp in employees
    ]
    print(
        tabulate(
            data,
            headers=[
                "ID",
                "NAME",
                "EMAIL",
                "DEPARTMENT",
                "SALARY"
            ],
            tablefmt="grid"
        )
    )

def show_stats(
        stats: EmployeeStatictics
):
    data = [
        ["TOTAL EMPLOYEES", stats.total_employee],
        ["IT EMPLOYEES", stats.it_employee],
        ["HR EMPLOYEES", stats.hr_employee],
        ["ADMIN EMPLOYEES", stats.admin_employee],
        ["SALES EMPLOYEES", stats.sales_employee],
        ["AVG SALARY", stats.average_salary],
        ["HIGHEST SALARY", stats.highest_salary],
        ["LOWEST SALARY", stats.lowest_salary],
    ]
    print(
        tabulate(
            data,
            headers=[
                "STATS",
                "COUNT"
            ],
            tablefmt="grid"
        )
    )
    
def enter_details():
    name = input("Name: ")
    email = input("Email: ")
    print("Select One Option")
    print("1: IT")
    print("2: Salee")
    print("3: HR")
    print("4: Admin")
    while True:
        department = input("Department: ")
        if department not in ["1","2","3","4"]:
            print("Wrong Department Selected, Enter again")
        else:
            break
    salary = input("Salary: ")

    return (name, email, department, salary)

def show_menu() -> None:
    print("\n ========== Employee Management System ==========")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Update Employee")
    print("4. Search Employee")
    print("5. Show All Employees")
    print("6. Show Statistics")
    print("7. Exit")

def add_employee(service_emp: EmployeeService):
    print("\n Add Employee")

    (name, email, department, salary) = enter_details()

    result = service_emp.add(
        name=name,
        email=email,
        department=department,
        salary=salary
    )
    print(result)

def remove_employee(service: EmployeeService):
    print("Please find Employees")
    employees = service.get("*")
    show_employee(employees)
    print("Enter Employee Id you want to remove")
    emp_id = input("Employee ID: ")
    res = service.remove(emp_id)
    print(res)




def update_employee(service_emp: EmployeeService):
    employees = service_emp.get("*")
    show_employee(employees)
    id = input("Enter employee id forr update: ")
    (name, email, department, salary) = enter_details()

    emp_dict = {
        "id":id,
        "name":name,
        "email":email,
        "department":department,
        "salary":salary
    }
    res = service_emp.update(emp_dict)
    print(res)

    



def search_employee(service_emp: EmployeeService, all : bool = False):
    if all:
        print("Entire Employee In Records")
        employees = service_emp.get("*")
    else:
        print("Enter Id, Name or Department, Press * for all records")
        choice = input("Search term: ")
        employees = service_emp.get(choice)

    if employees:
        show_employee(employees)
    else:
        print(f"No records found for : {choice}")


def show_statistics(service_emp: EmployeeService):
    print("Employee Summary")
    stats = service_emp.get_statistics()
    show_stats(stats)

        
    

def run() -> None:

    while True:
        show_menu()

        inp = input("\n Choose Option: ")
        service_emp = EmployeeService()

        if inp == "1":
            add_employee(service_emp)
        elif inp == "2":
            remove_employee(service_emp)
        elif inp == "3":
            update_employee(service_emp)
        elif inp == "4":
            search_employee(service_emp)
        elif inp == "5":
            search_employee(service_emp,True)
        elif inp == "6":
            show_statistics(service_emp)
        elif inp == "7":
            print("Exit")
            break
        else:
            print("Invalid Selection")


            


