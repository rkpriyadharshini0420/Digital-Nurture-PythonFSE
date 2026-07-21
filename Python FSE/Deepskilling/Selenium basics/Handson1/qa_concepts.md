# QA Concepts, Functional Testing & Defect Lifecycle

## Task 1: Map Testing Types to a Real System

### 1. Test Levels for Course Management API
*   **Unit Testing:** Test the `calculate_course_duration()` function in isolation to ensure it returns the correct integer when given valid start and end dates.
*   **Integration Testing:** Test the `POST /api/courses/` endpoint with the database to ensure that when valid JSON data is submitted, the API successfully writes the record to the database.
*   **System Testing:** Test the complete end-to-end flow: Login as Admin -> Call `POST /api/courses/` -> Navigate to `GET /api/courses/` to verify the new course appears in the full system list.
*   **User Acceptance Testing (UAT):** As an actual college admin user, log in through the UI and verify that you can successfully create a course and that it meets the college's administrative needs.

### 2. Functional vs Non-Functional Classification
*   The test cases described above are **Functional** (they verify *what* the system does and if it behaves correctly).
*   **Non-Functional Test Example (Performance):** Ensure the `GET /api/courses/` endpoint successfully returns the course list in under 200 milliseconds when 500 users request it simultaneously.

### 3. Black-Box vs White-Box Testing
*   **Black-Box Testing:** Testing the software without any knowledge of the internal code structure or logic. The tester only cares about providing inputs and checking the outputs. **Typically performed by QA Testers.**
*   **White-Box Testing:** Testing with full knowledge of the internal code, branches, and logic structures. **Typically performed by Developers.**

### 4. Formal Test Cases for POST /api/courses/

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC_001 | Create course with valid data | Admin user is authenticated | 1. Send POST request with all mandatory fields populated correctly. | 201 Created and course is saved. | | |
| TC_002 | Create course with missing mandatory field | Admin user is authenticated | 1. Send POST request omitting the 'course_name' field. | 400 Bad Request error returned. | | |
| TC_003 | Unauthorized access attempt | User is NOT authenticated | 1. Send POST request with valid course data. | 401 Unauthorized error returned. | | |

---

## Task 2: Defect Lifecycle & Severity Classification

### 5. Defect Lifecycle
*   **New:** A bug is found and logged by QA.
*   **Assigned:** The bug is assigned to a developer to fix.
*   **Open:** The developer starts working on the bug.
*   **Fixed:** The developer resolves the issue and pushes the code.
*   **Retest:** QA tests the specific bug to see if the fix worked.
*   **Verified:** QA confirms the bug is fixed.
*   **Closed:** The bug lifecycle ends.
*   **Rejected Path:** The developer or product owner determines it is not a bug (e.g., it is a feature).
*   **Deferred Path:** The bug is valid but not important enough to fix in the current sprint/release, so it is postponed.

### 6. Severity and Priority Classification
*   **a) POST /api/courses/ returns 500 Internal Server Error:** 
    *   **Severity:** Critical
    *   **Priority:** P1
    *   **Justification:** The core functionality of creating a course is completely broken for all users, requiring immediate attention.
*   **b) Course names > 150 characters silently truncated:** 
    *   **Severity:** Medium
    *   **Priority:** P3
    *   **Justification:** It is a functional data-loss issue, but it only affects very long names and doesn't crash the system.
*   **c) /docs Swagger page has a typo:** 
    *   **Severity:** Low
    *   **Priority:** P4
    *   **Justification:** It is a cosmetic issue that does not impact the API's functionality at all.
*   **d) Login occasionally returns 401 on first attempt:** 
    *   **Severity:** High
    *   **Priority:** P1
    *   **Justification:** Even though it is intermittent, login is a critical path. A failure here causes major user frustration and blocks access.

### 7. Complete Defect Report (For Bug A)
*   **Defect ID:** BUG-101
*   **Title:** POST /api/courses/ returns 500 Internal Server Error for all requests
*   **Environment:** QA Environment, Windows 11, Chrome v120
*   **Build Version:** v1.0.5
*   **Severity:** Critical
*   **Priority:** P1
*   **Steps to Reproduce:**
    1. Log into the API client with Admin credentials.
    2. Send a POST request to `/api/courses/` with a valid JSON payload.
*   **Expected Result:** The server should return a `201 Created` status code and save the new course.
*   **Actual Result:** The server returns a `500 Internal Server Error` and the course is not saved.
*   **Attachments:** screenshot of 500 error.

### 8. Severity vs Priority
*   **Severity** refers to how much damage the bug causes to the system's functionality (technical impact). 
*   **Priority** refers to how urgently the business needs the bug fixed (business impact).
*   **Example where High Severity != High Priority:** An application crashes (High Severity) when a user clicks a very specific, hidden button on a legacy page that no one has used in 5 years. Because no one uses it, the business decides it can wait to be fixed (Low Priority).