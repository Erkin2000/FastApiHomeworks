from pydantic import BaseModel, EmailStr, validator


class UserRequestAdd(BaseModel):
    email: EmailStr
    password: str

class UserAdd(BaseModel):
    email: EmailStr
    hash_password: str

class User(BaseModel):
    id: int
    email: EmailStr

