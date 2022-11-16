from expects import expect, equal
from src.employee_listing import EmployeeListing


def test_list_employees_18_and_older():
    eightteen_and_older = EmployeeListing().list_18_and_older()
    expect(len(eightteen_and_older)).to(equal(2))
