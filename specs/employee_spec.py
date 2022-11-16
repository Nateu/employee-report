from mamba import describe, context, it

with describe("Given a data set of employees") as self:
    with context("when requesting employees of age 18 and older"):
        with it("should list exactly 2 emoloyees"):
            