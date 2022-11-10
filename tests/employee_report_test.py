from src.employee_list import EmployeeList
from src.employee import Employee


def test_select_employees_18_and_older():
    employees = EmployeeList()
    assert all(employee.age >= 18 for employee in employees.select())
    # assert employees.select()[0].age >= 18
    # assert employees.select()[1].age >= 18
    # assert len(employees.select()) == 2


def test_sort_employees_ascending():
    employees = EmployeeList()
    assert employees.select()[0].name < employees.select()[1].name


def test_employee_names_capitalized():
    employees = EmployeeList()
    assert employees.select() == [
        Employee("MIKE", age=51),
        Employee("SEPP", age=18),
    ]
