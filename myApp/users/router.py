from fastapi import APIRouter, Response, Depends

from myApp.exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException
from myApp.users.auth import authenticate_user, create_access_token, get_password_hash
from myApp.users.dao import UsersDAO
from myApp.users.dependencies import get_current_user  # get_current_admin_user
from myApp.users.models import Users
from myApp.users.schemas import SUserAuth, SUserRegister

router_auth = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

router_users = APIRouter(
    prefix="/users",
    tags=["Пользователи"],
)


@router_auth.post("/register", status_code=201)
async def register_user(user_data: SUserRegister):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    new_user = await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)
    return {"new_user": user_data.email}


@router_auth.post("/login")
async def login_user(response: Response, user_data: SUserRegister):
    user = await authenticate_user(user_data.email, user_data.password)
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return {"access_token": access_token}


@router_auth.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("booking_access_token")


@router_users.get("/me")
async def read_users_me(current_user: Users = Depends(get_current_user)):
    return current_user

# @router.get("/all")
# async def read_users_all(current_user: Users = Depends(get_current_admin_user)):
#     return await UsersDAO.find_all()
