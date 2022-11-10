class EmployeeReport:
    def __init__(self):
        self.employees = []

    def report(self):
        return dict(sorted(self.employees.items()))

    def add(self, name: str, age: int) -> None:
        self.employees.append({"name": name, "age": age})

    def report_18_plus(self):
        return [employee for employee in self.employees if employee["age"] >= 18]
