from src.employee_report import employee_data
from src.employee import Employee


class EmployeeList:

    def select(self):
        employees_18_and_over = [
            employee for employee in employee_data if employee.age >= 18
        ]
        employees_18_and_over.sort(key=lambda emp: emp.name)
        return [Employee(employee.name.upper(), employee.age) for employee in employees_18_and_over]
