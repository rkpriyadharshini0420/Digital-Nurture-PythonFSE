from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

@app.route('/api/students/<int:student_id>/enroll', methods=['POST'])
def enroll(student_id):
    data = request.json
    course_id = data.get('course_id')
    try:
        # Inter-service communication
        response = requests.get(f"http://localhost:5001/api/courses/{course_id}")
        if response.status_code == 200:
            return jsonify({"status": "Enrolled", "student": student_id, "course": course_id})
        return jsonify({"error": "Course not found"}), 404
    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Service Unavailable"}), 503

if __name__ == '__main__':
    app.run(port=5002)