import random
from typing import List, Dict
from models.employee import Employee
from models.assignment import Assignment

class AssignmentService:
    def __init__(self, employees: List[Employee], previous_assignments: List[Assignment] = None):
        self.employees = employees
        self.previous_assignments = self._create_previous_mapping(previous_assignments or [])

    def _create_previous_mapping(self, assignments: List[Assignment]) -> Dict[str, str]:
        return {a.giver.email: a.receiver.email for a in assignments}

    def create_assignments(self, max_attempts: int = 100) -> List[Assignment]:
        for _ in range(max_attempts):
            try:
                return self._try_create_assignments()
            except ValueError:
                continue
        raise Exception("Could not generate valid assignments after maximum attempts")

    def _try_create_assignments(self) -> List[Assignment]:
        available_receivers = self.employees.copy()
        assignments: List[Assignment] = []
        givers = self.employees.copy()
        random.shuffle(givers)

        for giver in givers:
            valid_receivers = [
                r for r in available_receivers
                if self._is_valid_assignment(giver, r)
            ]

            if not valid_receivers:
                raise ValueError("No valid receivers available")

            receiver = random.choice(valid_receivers)
            available_receivers.remove(receiver)
            assignments.append(Assignment(giver=giver, receiver=receiver))

        return assignments

    def _is_valid_assignment(self, giver: Employee, receiver: Employee) -> bool:
        return (
            giver != receiver and
            (giver.email not in self.previous_assignments or
             receiver.email != self.previous_assignments[giver.email])
        )
