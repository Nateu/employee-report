from expects import expect, equal
from src.employee_listing import EmployeeListing


def test_list_employees_18_and_older():
    eightteen_and_older = EmployeeListing().list_18_and_older()
    expect(len(eightteen_and_older)).to(equal(2))


def test_list_employees_18_and_older_sorted_by_name():
    eightteen_and_older = EmployeeListing().list_18_and_older()
    expect(eightteen_and_older[0]["name"]).to(equal("Mike"))
    expect(eightteen_and_older[1]["name"]).to(equal("Sepp"))
