from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    Message: str


class UserSchema(BaseModel):
    user_name: str
    user_email: EmailStr
    user_password: str


class UserPublic(BaseModel):
    user_name: str
    user_email: EmailStr
    id: int


class UserDB(UserSchema):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]
