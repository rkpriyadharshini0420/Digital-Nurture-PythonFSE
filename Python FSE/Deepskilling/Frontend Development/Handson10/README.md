# Hands-On 10: API Integration & Advanced State Management

This project implements a centralised API service layer and advanced state management patterns as part of the Digital Nurture 5.0 module.

## Tasks Completed
- **Task 1 (API Layer):** Built a centralised `apiClient` using Axios with request interceptors (for auth tokens) and response interceptors (for data standardisation and error handling).
- **Task 2 (Redux Toolkit):** Implemented `createAsyncThunk` for asynchronous API calls and used selectors to decouple components from the store structure.
- **Task 3 (Framework Comparison & Error Handling):** Documented state management patterns and implemented global error handling.

## Framework Comparison (Task 151)

| Framework | State Management | Key Characteristics |
| :--- | :--- | :--- |
| **React** | Redux Toolkit | Uses `createAsyncThunk` for async flows; decouples state via selectors. |
| **Angular** | NgRx | Strict architecture (Actions/Reducers/Effects); best for large enterprise applications. |
| **Vue** | Pinia | Lightweight, intuitive API; uses `storeToRefs` to maintain reactivity seamlessly. |

## How to Run
1. Install dependencies: `npm install`
2. Start the development server: `npm run dev`