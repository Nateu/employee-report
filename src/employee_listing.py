from src.employee_data import employee_data


class EmployeeListing:
    LISTING = employee_data

    def list_18_and_older(self):
        list = [employee for employee in self.LISTING if employee["age"] >= 18]
        list.sort(key=self.employee_name)
        return list

    @staticmethod
    def employee_name(data):
        return data["name"]
