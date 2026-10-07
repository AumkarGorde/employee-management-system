import pytest
from service.employee_service import EmployeeService
from model.employee import Employee, Department
from datetime import datetime
from unittest.mock import patch

@pytest.fixture
def employees():
    emp = [
        {
            "id": "EMP-1",
            "name": "Omkar Gorde",
            "email": "omkarpgorde@morningstar.com",
            "department": "1",
            "salary": "11200",
            "updated_at": None,
            "created_at": "2026-10-04T17:23:00",
            "deleted_at": None
        },
        {
            "id": "EMP-2",
            "name": "Vaibhav D,",
            "email": "vaibhavd@morningstar.com",
            "department": "1",
            "salary": "11200",
            "updated_at": None,
            "created_at": "2026-10-04T17:24:00",
            "deleted_at": None
        }
    ]
    return emp

@patch("service.employee_service.load")
@patch("service.employee_service.save")
def test_add(mock_save, mock_load, employees):
    service = EmployeeService()
    mock_load.return_value = employees
    mock_save.return_value = True

    res = service.add(
        "Sapna",
        "snap@123.com",
        "1",
        13000
    )

    assert res == "New Employee is added"