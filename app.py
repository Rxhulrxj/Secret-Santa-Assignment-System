import os
from flask import Flask, request, render_template, send_file, flash
from werkzeug.utils import secure_filename
from services.file_service import FileService
from services.assignment_service import AssignmentService
import pandas as pd

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/assign', methods=['POST'])
def assign_secret_santa():
    try:
        current_file = request.files['current_employees']
        previous_file = request.files['previous_assignments']

        if not current_file or not previous_file:
            return 'Both files are required', 400

        # Save uploaded files
        current_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(current_file.filename))
        previous_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(previous_file.filename))
        
        current_file.save(current_path)
        previous_file.save(previous_path)

        # Load data using services
        file_service = FileService()
        employees = file_service.load_employees(current_path)
        previous_assignments = file_service.load_previous_assignments(previous_path)

        # Create new assignments
        assignment_service = AssignmentService(employees, previous_assignments)
        new_assignments = assignment_service.create_assignments()

        # Save results
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'new_assignments.csv')
        file_service.save_assignments(new_assignments, output_path)

        # Clean up
        os.remove(current_path)
        os.remove(previous_path)

        return send_file(output_path, as_attachment=True, download_name='new_assignments.csv')

    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True)
