from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, mapped_column, Mapped

from myApp.database import Base

# if TYPE_CHECKING:
#     # Убирает предупреждения отсутствия импорта и неприятные подчеркивания в
#     # PyCharm и VSCode
#     from bookings.models import Bookings


# Модель написана в соответствии с современным стилем Алхимии (версии 2.x)
class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[str] = mapped_column(String(20), nullable=False, default='user')
    email: Mapped[str] = mapped_column(String, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)

    # bookings: Mapped[list["Bookings"]] = relationship(back_populates="user")

    # def __str__(self):
    #     return f"Пользователь {self.username}"
