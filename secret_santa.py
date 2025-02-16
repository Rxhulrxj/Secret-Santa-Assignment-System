import pandas as pd
import random
from typing import List, Tuple, Dict

class SecretSanta:
    def __init__(self):
        self.employees: pd.DataFrame = None
        self.previous_assignments: pd.DataFrame = None

    def load_employees(self, file_path: str) -> None:
        self.employees = pd.read_csv(file_path)

    def load_previous_assignments(self, file_path: str) -> None:
        self.previous_assignments = pd.read_csv(file_path)

    def assign_secret_santa(self) -> pd.DataFrame:
        if self.employees is None or self.employees.empty:
            raise ValueError("No employees loaded")

        employees_list = list(zip(self.employees['Employee_Name'], 
                                self.employees['Employee_EmailID']))
        available_receivers = employees_list.copy()
        assignments = []

        for giver in employees_list:
            # Create mask for valid receivers
            valid_receivers = [
                r for r in available_receivers
                if r != giver and (
                    giver[1] not in self.previous_assignments['Employee_EmailID'].values or 
                    r[1] not in self.previous_assignments[
                        self.previous_assignments['Employee_EmailID'] == giver[1]
                    ]['Secret_Child_EmailID'].values
                )
            ]

            if not valid_receivers:
                return self.assign_secret_santa()

            receiver = random.choice(valid_receivers)
            available_receivers.remove(receiver)
            assignments.append({
                'Employee_Name': giver[0],
                'Employee_EmailID': giver[1],
                'Secret_Child_Name': receiver[0],
                'Secret_Child_EmailID': receiver[1]
            })

        return pd.DataFrame(assignments)

    def save_assignments(self, assignments: pd.DataFrame, output_file: str) -> None:
        assignments.to_csv(output_file, index=False)
