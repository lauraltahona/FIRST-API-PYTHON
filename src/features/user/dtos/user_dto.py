from pydantic import BaseModel, EmailStr, StringConstraints, ConfigDict
from typing import Annotated

class UserDtoRegister(BaseModel):
    email: EmailStr
    password: Annotated[str, StringConstraints(min_length=8, max_length=150)]

class UserDtoLogin(BaseModel):
    email: EmailStr
    password: Annotated[str, StringConstraints(min_length=8, max_length=150)]


class UserDtoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # ← esto le dice a Pydantic
    # "puedes leer atributos de objetos normales, no solo diccionarios"
    id: str
    email: EmailStr


class UserDtoUpdate(BaseModel):
    email: EmailStr | None = None
    password: Annotated[str, StringConstraints(min_length=8, max_length=150)] | None = None

