from expects import expect, equal, match, be_above_or_equal
from src.employee_listing import EmployeeListing


def test_list_employees_18_and_older():
    eightteen_and_older = EmployeeListing().list_18_and_older()
    expect(eightteen_and_older[0].age).to(be_above_or_equal(18))
    expect(eightteen_and_older[1].age).to(be_above_or_equal(18))


def test_list_employees_18_and_older_sorted_by_name():
    eightteen_and_older = EmployeeListing().list_18_and_older()
    expect(eightteen_and_older[0].name.casefold()).to(equal("Mike".casefold()))
    expect(eightteen_and_older[1].name.casefold()).to(equal("Sepp".casefold()))


def test_list_employees_18_and_older_sorted_by_capitalized_name():
    eightteen_and_older = EmployeeListing().list_18_and_older()
    expect(eightteen_and_older[0].name).to(match(r"[A-Z]+"))
    expect(eightteen_and_older[1].name).to(match(r"[A-Z]+"))
