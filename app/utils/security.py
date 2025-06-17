import bcrypt
import jwt

SECRET = "segredo"

def hash_password(pwd):
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

def verify_password(pwd, hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.encode())

def create_jwt(payload):
    return jwt.encode(payload, SECRET, algorithm="HS256")
