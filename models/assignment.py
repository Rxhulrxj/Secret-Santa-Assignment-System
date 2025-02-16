from dataclasses import dataclass
from .employee import Employee

@dataclass
class Assignment:
    giver: Employee
    receiver: Employee

    def to_dict(self):
        return {
            'Employee_Name': self.giver.name,
            'Employee_EmailID': self.giver.email,
            'Secret_Child_Name': self.receiver.name,
            'Secret_Child_EmailID': self.receiver.email
        }
