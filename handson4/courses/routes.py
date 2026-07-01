from flask import Blueprint, jsonify, request

# Define the Blueprint
courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

# In-memory list to store courses for now
courses = []

@courses_bp.route('/', methods=['GET'])
def get_courses():
    return jsonify(courses)

@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()
    courses.append(data)
    return jsonify(data), 201