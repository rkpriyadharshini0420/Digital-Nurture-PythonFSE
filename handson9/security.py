# handson9/security.py
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "your-very-secret-key" 
ALGORITHM = "HS256"

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # bcrypt is preferred because it is intentionally slow (work factor),
    # making brute-force attacks computationally expensive compared to fast algorithms like MD5.
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    # Token expiry set to 30 minutes
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)