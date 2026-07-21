# handson9/main.py
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from security import get_password_hash, verify_password, create_access_token

app = FastAPI()

# 94. CORS Configuration: Allow requests from the frontend dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock Database
users_db = []
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login/")

class User(BaseModel):
    email: str
    password: str

# 88. Register Endpoint
@app.post("/api/v1/auth/register/")
def register(user: User):
    if any(u['email'] == user.email for u in users_db):
        raise HTTPException(status_code=409, detail="Email already registered")
    
    hashed_pw = get_password_hash(user.password)
    users_db.append({"email": user.email, "hashed_password": hashed_pw})
    return {"message": "User registered successfully"}

# 91. Login Endpoint
@app.post("/api/v1/auth/login/")
def login(user: User):
    db_user = next((u for u in users_db if u['email'] == user.email), None)
    if not db_user or not verify_password(user.password, db_user['hashed_password']):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

# 93. Protected Route Example
@app.post("/api/v1/courses/")
def add_course(token: str = Depends(oauth2_scheme)):
    # This route is now protected and requires a Bearer token
    return {"message": "You are authorized to add a course"}