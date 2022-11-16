from src.employee_data import employee_data
from src.employee import Employee


class EmployeeListing:
    LISTING = employee_data

    def list_18_and_older(self):
        list = [
            Employee(name=employee["name"].upper(), age=employee["age"])
            for employee in self.LISTING
            if employee["age"] >= 18
        ]
        list.sort(key=self.employee_name)
        return list

    @staticmethod
    def employee_name(employee: Employee):
        return employee.name
