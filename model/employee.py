from enum import Enum
from datetime import datetime
from dataclasses import dataclass

class Department(Enum):
    IT = 1
    SALES = 2
    HR = 3
    ADMIN = 4

@dataclass
class Employee:
    id: str
    name: str
    email: str
    department: Department
    salary: float
    updated_at: datetime | None
    created_at: datetime
    deleted_at: datetime | None

    @classmethod
    def from_dic(cls, data):
        return cls(
            id = data["id"],
            name = data["name"],
            email = data["email"],
            department = Department(int(data["department"])),
            salary = float(data["salary"]),
            updated_at = (
                datetime.fromisoformat(data["updated_at"])
                if data["updated_at"] is not None
                else None
            ),
            created_at = (
                datetime.fromisoformat(data["created_at"])
                if data["created_at"] is not None
                else None
            ),
            deleted_at = (
                datetime.fromisoformat(data["deleted_at"])
                if data["deleted_at"] is not None
                else None
            ),
        )

@dataclass
class EmployeeStatictics:
    total_employee: int
    it_employee: int
    hr_employee: int
    admin_employee: int
    sales_employee: int
    average_salary: float
    highest_salary: float
    lowest_salary: float