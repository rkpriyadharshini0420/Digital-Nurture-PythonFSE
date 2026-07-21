from fastapi import FastAPI, HTTPException, Query, status
from fastapi.responses import JSONResponse
from typing import Optional

app = FastAPI()

# Mock Database
db = [{"id": i, "name": f"Course {i}", "code": f"CS{i}"} for i in range(1, 21)]

# Versioning: /api/v1/courses/
# Note: URL versioning (/v1/) is preferred for its simplicity and visibility. 
# Header-based versioning is an alternative but is harder to test directly in browsers.

@app.get("/api/v1/courses/", status_code=status.HTTP_200_OK)
def get_courses(
    page: int = Query(1, ge=1),
    page_size: int = Query(5, ge=1, le=20),
    search: Optional[str] = None
):
    # Filtering
    data = db
    if search:
        data = [c for c in db if search.lower() in c['name'].lower() or search.lower() in c['code'].lower()]
    
    # Pagination
    start = (page - 1) * page_size
    end = start + page_size
    results = data[start:end]
    
    return {
        "count": len(data),
        "next": f"/api/v1/courses/?page={page+1}&page_size={page_size}" if end < len(data) else None,
        "previous": f"/api/v1/courses/?page={page-1}&page_size={page_size}" if page > 1 else None,
        "results": results
    }

@app.post("/api/v1/courses/", status_code=status.HTTP_201_CREATED)
def create_course(name: str, code: str):
    new_course = {"id": len(db) + 1, "name": name, "code": code}
    db.append(new_course)
    # Location Header
    return JSONResponse(
        content=new_course,
        status_code=201,
        headers={"Location": f"/api/v1/courses/{new_course['id']}"}
    )

@app.patch("/api/v1/courses/{course_id}/")
def update_course_partial(course_id: int, name: Optional[str] = None):
    course = next((c for c in db if c['id'] == course_id), None)
    if not course:
        # Standardized Error Format
        return JSONResponse(
            status_code=404,
            content={"error": {"code": "NOT_FOUND", "message": f"Course with id {course_id} does not exist", "field": None}}
        )
    if name: course['name'] = name
    return course