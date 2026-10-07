from utility.json_utility import (
    load,
    save
)
from model.employee import (
    Employee,
    Department,
    EmployeeStatictics
)
from datetime import datetime
from typing import List


class EmployeeService:

    def __init__(self):
        pass

    def __load_employees(
        self        
    )-> List[Employee]:
        load_previous_records = load()
        employees = [
            Employee.from_dic(record) 
            for record in load_previous_records
        ]
        return employees
        

    def add(
            self,
            name: str,
            email: str,
            department: str,
            salary: str
    ) -> str:
        employees = self.__load_employees()
        if employees:
            last_emp = max(
                employees,
                key = lambda emp: emp.created_at
            )
            unique_id, id = last_emp.id.split("-")
        else:
            unique_id, id = ("EMP", "0")


        
        employees.append(
            Employee(
                id= f"{unique_id}-{int(id)+1}",
                name=name,
                email=email,
                department=Department(int(department)),
                salary=float(salary),
                updated_at=None,
                created_at=datetime.now(),
                deleted_at=None
            )
        )
        save_emp = save(employees)

        if save_emp:
            return "New Employee is added"

        return "Fail to add new Employee"

    def get(
            self,
            emp_query: str,
    ):
        employees = self.__load_employees()

        if emp_query == "*":
            return employees

        if "EMP-".lower() in emp_query.lower():
            filtered = [
                emp for emp in employees
                if emp.id.lower() == emp_query.lower()
            ]
            return filtered


        if emp_query.lower() in [
            str(Department.IT.value),
            str(Department.SALES.value),
            str(Department.HR.value),
            str(Department.ADMIN.value)
        ]:
            filtered = [
                emp for emp in employees
                if emp_query.lower() == str(emp.department.value).lower()
            ]
            return filtered 
        elif emp_query.lower() in[
            Department.IT.name.lower(),
            Department.ADMIN.name.lower(),
            Department.HR.name.lower(),
            Department.SALES.name.lower()
        ]:
            filtered = [
                emp for emp in employees
                if emp_query.lower() == emp.department.name.lower()
            ]
            return filtered
        else:
            filtered = [
                emp for emp in employees
                if emp_query.lower() in emp.name.lower()
            ]
            return filtered

    def remove(
            self,
            emp_id: str
    ):
        employees = self.__load_employees()

        for emp in employees:
            if emp.id.lower() == emp_id.lower():
                employees.remove(emp)
                res = save(employees)
                if res:
                    return "Employee removed"
                else:
                    return "Issue removing employee"

        return "Employee not found"

    def update(
            self,
            employee: dict[str,str]
    ):
        employees = self.__load_employees()
        is_exist = False

        for emp in employees:
            if emp.id.lower() == employee["id"].lower():
                is_exist = True
                emp.name = employee["name"]
                emp.email = employee["email"]
                emp.department = Department(int(employee["department"]))
                emp.salary = float(employee["salary"])
                emp.updated_at = datetime.now()
                break

        if is_exist:
            res = save(employees)
            return res
        else:
            return f"No employee found for ID {employee.id}"

    def get_statistics(
            self
    )-> EmployeeStatictics:
        employees = self.__load_employees()
        if employees:
            sal = [emp.salary for emp in employees]
            return EmployeeStatictics(
                total_employee= len(employees),
                it_employee= sum(emp.department == Department.IT for emp in employees),
                hr_employee= sum(emp.department == Department.HR for emp in employees),
                admin_employee= sum(emp.department == Department.ADMIN for emp in employees),
                sales_employee= sum(emp.department == Department.SALES for emp in employees),
                average_salary=sum(sal) / len(sal),
                highest_salary= max(sal),
                lowest_salary=min(sal)
            )
        else:
            return EmployeeStatictics(
                total_employee=0,
                it_employee=0,
                hr_employee=0,
                admin_employee=0,
                sales_employee=0,
                average_salary=0,
                highest_salary=0,
                lowes_salary=0
            )

        




