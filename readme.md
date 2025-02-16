# Secret Santa Assignment System

A Flask-based web application for managing Secret Santa assignments with support for previous year constraints.

## Project Structure

```
secret_santa_v1/
├── models/                 # Data models
│   ├── __init__.py
│   ├── employee.py        # Employee class definition
│   └── assignment.py      # Assignment class definition
├── services/              # Business logic services
│   ├── __init__.py
│   ├── file_service.py    # File handling operations
│   └── assignment_service.py  # Assignment generation logic
├── tests/                 # Unit tests
│   ├── __init__.py
│   └── test_assignment_service.py
├── templates/             # HTML templates
│   └── index.html
├── uploads/              # Temporary file storage (created automatically)
├── app.py                # Flask application
├── data_generator.py     # Sample data generator
└── requirements.txt      # Project dependencies
```

## Modules Used

- **Flask (2.0.1)**: Web framework for the application
- **Pandas (2.0.3)**: Data handling and CSV operations
- **Werkzeug (2.0.1)**: File handling and security utilities
- **Python Standard Library**:
  - random: For randomizing assignments
  - os: File system operations
  - typing: Type hints
  - unittest: Testing framework

## Setup and Installation

1. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```


## Running the Application

1. Generate sample data (optional):
```bash
python data_generator.py
```
This will create:
- current_employees.csv
- previous_assignments.csv

2. Start the Flask application:
```bash
python app.py
```

3. Access the application:
- Open web browser and go to `http://localhost:5000`
- Upload the required CSV files
- Download the generated assignments

## Running Tests

Execute the unit tests:
```bash
python -m unittest discover tests
```