from flask import Blueprint, jsonify
from courses.models import Course

# Define the blueprint
courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/', methods=['GET'])
def get_courses():
    # Fetch all records from the Course table
    courses = Course.query.all()
    
    # Return as JSON (assumes your Course model has a to_dict() method)
    return jsonify([c.to_dict() for c in courses]), 200