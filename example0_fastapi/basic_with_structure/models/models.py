from pydantic import BaseModel


class Alumno(BaseModel):
    padron: int
    nombre: str
    apelido: str
    edad: int | None = None
    notas: list[int] = []


class AlumnoUpsert(BaseModel):
    nombre: str
    apellido: str
    edad: int | None = None


class Error(BaseModel):
    detail: str
