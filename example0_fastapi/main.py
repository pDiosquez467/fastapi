from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


class Alumno(BaseModel):
    padron: int
    nombre: str
    apelido: str
    edad: int | None = None


class AlumnoUpsert(BaseModel):
    nombre: str
    apellido: str
    edad: int | None = None


alumnos: list[Alumno] = [
    Alumno(padron=1015, nombre="Walter", apelido="White", edad=52),
    Alumno(padron=1022, nombre="Jesse", apelido="Pinkman", edad=26),
    Alumno(padron=1039, nombre="Skyler", apelido="White", edad=45),
    Alumno(padron=1047, nombre="Saul", apelido="Goodman", edad=49),
    Alumno(padron=1054, nombre="Gustavo", apelido="Fring", edad=50),
]


@app.get("/")
def root():
    return {"message": "Hello, World!"}


@app.get("/alumnos")
def list() -> list[Alumno]:
    return alumnos


@app.get("/alumnos/{padron}")
def show(padron: int) -> Alumno:
    for alumno in alumnos:
        if alumno.padron == padron:
            return alumno
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Alumno NO encontrado"
    )


@app.post("/alumnos", status_code=status.HTTP_201_CREATED)
def create(alumnoUpsert: AlumnoUpsert) -> Alumno:
    alumno = Alumno(
        padron=alumnos[-1].padron + 1,
        nombre=alumnoUpsert.nombre,
        apelido=alumnoUpsert.apellido,
        edad=alumnoUpsert.edad,
    )
    alumnos.append(alumno)
    return alumno
