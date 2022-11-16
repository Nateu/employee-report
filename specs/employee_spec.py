from mamba import description, context, it, before
from expects import expect, equal, match, be_above_or_equal
from src.employee_listing import EmployeeListing

with description("Given a data set of employees") as self:
    with context("when requesting employees of age 18 and older"):
        with before.each:
            self.eightteen_and_older = EmployeeListing().list_18_and_older()
        
        with it("should list exactly 2 emoloyees of age 18 or older"):
            expect(self.eightteen_and_older[0].age).to(be_above_or_equal(18))
            expect(self.eightteen_and_older[1].age).to(be_above_or_equal(18))

        with it("should return first sepp and then mike"):
            expect(self.eightteen_and_older[0].name.casefold()).to(equal("Sepp".casefold()))
            expect(self.eightteen_and_older[1].name.casefold()).to(equal("Mike".casefold()))

        with it("should return the first names in all caps"):
            expect(self.eightteen_and_older[0].name).to(match(r"[A-Z]+"))
            expect(self.eightteen_and_older[1].name).to(match(r"[A-Z]+"))
