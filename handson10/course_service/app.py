from flask import Flask, jsonify
app = Flask(__name__)

courses = {1: {"name": "Python FSE", "code": "CS101"}}

@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    return jsonify(courses.get(course_id, {"error": "Not found"})), 200 if course_id in courses else 404

if __name__ == '__main__':
    app.run(port=5001)