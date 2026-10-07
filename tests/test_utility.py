import pytest
from utility.json_utility import save, load
from model.employee import Employee, Department
from datetime import datetime
from pathlib import Path
from constants.constants import TEST_FILE_PATH

@pytest.fixture
def employee():
    return Employee(
        id = 'EMP-1',
        name = 'Omkar Gorde',
        email = 'omkarpgorde@morningstar.com',
        department = Department.IT,
        salary = 11200,
        updated_at = None,
        created_at = datetime.now(),
        deleted_at = None
    )

@pytest.fixture
def file_path():
    return str(Path(__file__).resolve().parent.parent / "data" / TEST_FILE_PATH)

def test_save(employee, file_path):
    result = save([employee], file_path)
    assert result == True

def test_load(file_path):
    result = load(file_path)
    assert result[0]["id"] == "EMP-1"
