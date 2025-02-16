import pandas as pd
import random
from typing import List, Tuple, Dict

def create_assignments(employees: List[Tuple[str, str]], 
                      previous_assignments: Dict[str, str] = None) -> List[Dict]:
    """
    Create valid Secret Santa assignments following all constraints
    """

    max_attempts = 100
    attempt = 0
    
    """here this max_attempts is beacuse it will try to generate valid assignments
    until the maximum number of attempts is reached
    
    Here why i used this is:
    1. Prevent Infinite loop.
    2. To mae it controller on execution time

    by using this way i can ensure that the function behaves predicatably
    and can handle failures cases.
    
    
    """
    while attempt < max_attempts:
        try:
            assignments = []
            available_receivers = employees.copy()
            assigned_receivers = set()
            
            # Shuffle employees to randomize assignments
            givers = employees.copy()
            random.shuffle(givers)
            
            for giver in givers:
                valid_receivers = [
                    r for r in available_receivers
                    if (r[1] != giver[1]) and  # Can't assign to self
                    (r[1] not in assigned_receivers) and  # Receiver not already assigned
                    (previous_assignments is None or  # No previous assignments
                     giver[1] not in previous_assignments or  # Giver not in previous
                     r[1] != previous_assignments[giver[1]])  # Different from previous
                ]
                
                if not valid_receivers:
                    raise ValueError("No valid receivers available")
                
                receiver = random.choice(valid_receivers)
                assigned_receivers.add(receiver[1])
                assignments.append({
                    'Employee_Name': giver[0],
                    'Employee_EmailID': giver[1],
                    'Secret_Child_Name': receiver[0],
                    'Secret_Child_EmailID': receiver[1]
                })
            
            return assignments
            
        except ValueError:
            attempt += 1
            continue
    
    raise Exception("Could not generate valid assignments after maximum attempts")

def generate_sample_data():
    employees = [
        ("Hamish Murray", "hamish.murray@acme.com"),
        ("Layla Graham", "layla.graham@acme.com"),
        ("Matthew King", "matthew.king@acme.com"),
        ("Benjamin Collins", "benjamin.collins@acme.com"),
        ("Isabella Scott", "isabella.scott@acme.com"),
        ("Charlie Ross", "charlie.ross@acme.com"),
        ("Hamish Murray", "hamish.murray.sr@acme.com"),
        ("Piper Stewart", "piper.stewart@acme.com"),
        ("Spencer Allen", "spencer.allen@acme.com"),
        ("Charlie Wright", "charlie.wright@acme.com"),
        ("Hamish Murray", "hamish.murray.jr@acme.com"),
        ("Charlie Ross", "charlie.ross.jr@acme.com"),
        ("Ethan Murray", "ethan.murray@acme.com"),
        ("Matthew King", "matthew.king.jr@acme.com"),
        ("Mark Lawrence", "mark.lawrence@acme.com")
    ]

    # Generate current year employee list
    df_employees = pd.DataFrame(employees, columns=['Employee_Name', 'Employee_EmailID'])
    df_employees.to_csv('employees.csv', index=False)

    # First generate previous year assignments
    previous_assignments = create_assignments(employees)
    df_previous = pd.DataFrame(previous_assignments)
    df_previous.to_csv('previous_assignments.csv', index=False)



if __name__ == "__main__":
    generate_sample_data()
