# Automation Strategy & Framework Planning

## Task 1: Automation Decision and Test Case Selection

### 17. Automation Criteria applied to POST /api/courses/
1. **Repetitiveness:** High. This is a core functionality that must be checked frequently.
2. **Regression Potential:** High. Code changes in the API often affect course creation.
3. **Data Dependency:** High. It requires specific JSON payloads.
4. **Stability:** High. The endpoint definition is clear and unlikely to change daily.
5. **Business Value:** High. If this fails, the core product is broken.

### 18. Manual vs. Automate Decisions
* (a) **Automate:** Regression testing is repetitive and prone to human error.
* (b) **Manual:** Exploratory testing requires human intuition to find unexpected bugs.
* (c) **Automate:** Requires specialized tools; impossible to test concurrency manually.
* (d) **Automate:** Essential for daily regression of the login flow.
* (e) **Manual:** Requires visual verification; hard to automate Swagger layout nuances.
* (f) **Automate:** Critical smoke test for deployment pipelines.

### 19. Test Automation ROI Calculation
* Automation Cost: 4 hours. Manual Run: 0.5 hours.
* Payback period (runs needed): 4 / 0.5 = 8 runs.
* With 20% maintenance (0.1 hours extra per run): 4 / (0.5 - 0.1) = 10 runs.
* **Conclusion:** It pays for itself after 10 runs.

### 20. Flaky Tests
* **Definition:** A test that exhibits different results (pass/fail) despite no changes to code.
* **Example:** A test that fails due to network latency when the server is slow.
* **Prevention:** (1) Implement explicit waits, (2) Avoid hard-coded sleeps, (3) Use isolated test data.

---

## Task 2: Framework Comparison

### 21. Framework Types
1. **Linear:** Record-and-playback. Adv: Fast to build. Disadv: Not reusable. Use: Small POCs.
2. **Modular:** Divide tests into small scripts. Adv: Reusable. Disadv: High maintenance. Use: Simple apps.
3. **Data-Driven:** Keep data in external files. Adv: High coverage. Disadv: Complex setup. Use: Login with 50 users.
4. **Keyword-Driven:** Uses action keywords. Adv: Non-technical users can write tests. Disadv: Complex framework. Use: Large corporate teams.
5. **Hybrid:** Combination of the above. Adv: Scalable and reusable. Disadv: High initial effort. Use: Our Course Management System.

### 22. Recommendation: Hybrid Framework
I recommend a **Hybrid Framework** (Modular + Data-Driven). It allows reusability of login steps (Modular) and testing 50 combinations (Data-Driven). It supports both developers and non-technical members by abstracting complex selectors.

### 23. Hybrid Folder Structure
```text
/selenium_project
  /data         (CSV/Excel files)
  /pages        (Page Object Model files)
  /tests        (Test scripts)
  /utils        (Driver setup, helpers)
  /config       (Environment settings)