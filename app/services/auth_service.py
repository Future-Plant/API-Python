from app.models.user import UserCreate, UserLogin
from app.database.mongo import db
from app.utils.security import hash_password, verify_password, create_jwt

def signup_user(user: UserCreate):
    user_dict = user.dict()
    user_dict["password"] = hash_password(user.password)
    db.users.insert_one(user_dict)
    return {"msg": "Usuário cadastrado com sucesso"}

def login_user(user: UserLogin):
    found = db.users.find_one({"email": user.email})
    if not found or not verify_password(user.password, found["password"]):
        raise Exception("Credenciais inválidas")
    token = create_jwt({"email": user.email})
    return {"access_token": token}
