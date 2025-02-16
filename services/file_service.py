import pandas as pd
from typing import List
from models.employee import Employee
from models.assignment import Assignment

class FileService:
    @staticmethod
    def load_employees(file_path: str) -> List[Employee]:
        df = pd.read_csv(file_path)
        return [
            Employee(name=row['Employee_Name'], email=row['Employee_EmailID'])
            for _, row in df.iterrows()
        ]

    @staticmethod
    def load_previous_assignments(file_path: str) -> List[Assignment]:
        df = pd.read_csv(file_path)
        return [
            Assignment(
                giver=Employee(row['Employee_Name'], row['Employee_EmailID']),
                receiver=Employee(row['Secret_Child_Name'], row['Secret_Child_EmailID'])
            )
            for _, row in df.iterrows()
        ]

    @staticmethod
    def save_assignments(assignments: List[Assignment], output_file: str) -> None:
        df = pd.DataFrame([a.to_dict() for a in assignments])
        df.to_csv(output_file, index=False)
