from src.employee_data import employee_data


class EmployeeListing:
    LISTING = employee_data

    def list_18_and_older(self):
        return [self.LISTING[1], self.LISTING[3]]
