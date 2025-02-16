from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    email: str

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return False
        return self.email == other.email

    def __hash__(self):
        return hash(self.email)
