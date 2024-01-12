from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    role: str
    email: EmailStr
    password: str


class SUserRegister(BaseModel):
    email: EmailStr
    password: str
