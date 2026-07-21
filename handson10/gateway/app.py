from flask import Flask, request
import requests
app = Flask(__name__)

# This route captures everything after /api/
@app.route('/api/<path:subpath>', methods=['GET', 'POST'])
def gateway(subpath):
    # Check if the URL starts with 'courses'
    if subpath.startswith('courses'):
        # Forward to Course Service
        resp = requests.request(method=request.method, url=f"http://127.0.0.1:5001/api/{subpath}")
        return resp.json(), resp.status_code
    
    # Check if the URL starts with 'students'
    elif subpath.startswith('students'):
        # Forward to Student Service
        resp = requests.request(method=request.method, url=f"http://127.0.0.1:5002/api/{subpath}", json=request.json)
        return resp.json(), resp.status_code
    
    return {"error": "Route not found"}, 404

if __name__ == '__main__':
    app.run(port=5000)