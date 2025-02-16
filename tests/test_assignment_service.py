import unittest
from models.employee import Employee
from models.assignment import Assignment
from services.assignment_service import AssignmentService

class TestAssignmentService(unittest.TestCase):
    def setUp(self):
        self.employees = [
            Employee("Test1", "test1@acme.com"),
            Employee("Test2", "test2@acme.com"),
            Employee("Test3", "test3@acme.com")
        ]
        self.previous_assignments = [
            Assignment(self.employees[0], self.employees[1])
        ]

    def test_no_self_assignments(self):
        service = AssignmentService(self.employees)
        assignments = service.create_assignments()
        
        for assignment in assignments:
            self.assertNotEqual(assignment.giver, assignment.receiver)

    def test_no_previous_assignments(self):
        service = AssignmentService(self.employees, self.previous_assignments)
        assignments = service.create_assignments()
        
        prev_receiver = self.previous_assignments[0].receiver
        prev_giver = self.previous_assignments[0].giver
        
        for assignment in assignments:
            if assignment.giver == prev_giver:
                self.assertNotEqual(assignment.receiver, prev_receiver)

    def test_all_employees_assigned(self):
        service = AssignmentService(self.employees)
        assignments = service.create_assignments()
        
        self.assertEqual(len(assignments), len(self.employees))
        assigned_givers = {a.giver for a in assignments}
        assigned_receivers = {a.receiver for a in assignments}
        
        self.assertEqual(assigned_givers, set(self.employees))
        self.assertEqual(assigned_receivers, set(self.employees))

if __name__ == '__main__':
    unittest.main()
