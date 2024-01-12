from myApp.dao.base import BaseDAO
from myApp.users.models import Users


class UsersDAO(BaseDAO):
    model = Users
