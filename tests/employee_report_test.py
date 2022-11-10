import pytest
from src.employee_report import EmployeeReport


@pytest.fixture
def base_4():
    employee_report = EmployeeReport()
    employee_report.add(name="Max", age=17)
    employee_report.add(name="Sepp", age=18)
    employee_report.add(name="Nina", age=15)
    employee_report.add(name="Mike", age=51)
    return employee_report


def test_an_empty_employee_report_should_be_an_empty_list():
    employee_report = EmployeeReport()
    assert employee_report.report() == []


def test_an_empty_employee_report_when_adding_max_age_17_it_should_report_max():
    employee_report = EmployeeReport()
    employee_report.add(name="Max", age=17)
    employee_report.add(name="Angie", age=21)
    assert employee_report.report() == [
        {"name": "Angie", "age": 21},
        {"name": "Max", "age": 17},
    ]


def test_employee_report_holding_2_employees_when_requesting_a_report_it_should_order_by_name():
    employee_report = EmployeeReport()
    employee_report.add(name="Max", age=17)
    assert employee_report.report() == [{"name": "Max", "age": 17}]
    


def test_employee_report_holding_4_employees_when_requesting_a_report_it_should_hold_all_4(
    base_4,
):
    assert base_4.report() == [
        {"name": "Max", "age": 17},
        {"name": "Sepp", "age": 18},
        {"name": "Nina", "age": 15},
        {"name": "Mike", "age": 51},
    ]


def test_employee_report_holding_4_employees_when_requesting_an_18_plus_report_it_should_hold_only_sepp_and_mike(
    base_4,
):
    assert base_4.report_18_plus() == [
        {"name": "Sepp", "age": 18},
        {"name": "Mike", "age": 51},
    ]
