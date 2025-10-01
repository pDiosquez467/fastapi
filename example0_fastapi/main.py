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
    Alumno(padron=1016, nombre="Jesse", apelido="Pinkman", edad=26),
    Alumno(padron=1017, nombre="Skyler", apelido="White", edad=45),
    Alumno(padron=1018, nombre="Saul", apelido="Goodman", edad=49),
    Alumno(padron=1019, nombre="Gustavo", apelido="Fring", edad=50),
]


@app.get("/")
def root():
    return {"message": "Hello, World!"}


@app.get("/alumnos")
def list() -> list[Alumno]:
    return alumnos


@app.get("/alumnos/{padron}")
def show(padron: int) -> Alumno:
    return buscar_alumno(padron)


@app.post("/alumnos", status_code=status.HTTP_201_CREATED)
def create(alumno_upsert: AlumnoUpsert) -> Alumno:
    alumno = Alumno(
        padron=alumnos[-1].padron + 1,
        nombre=alumno_upsert.nombre,
        apelido=alumno_upsert.apellido,
        edad=alumno_upsert.edad,
    )
    alumnos.append(alumno)
    return alumno


@app.put("/alumnos/{padron}", status_code=status.HTTP_200_OK)
def update(padron: int, alumno_upsert: AlumnoUpsert) -> Alumno:
    alumno = buscar_alumno(padron)
    alumno.nombre = alumno_upsert.nombre
    alumno.apelido = alumno_upsert.apellido
    alumno.edad = alumno_upsert.edad
    return alumno


@app.delete("/alumnos/{padron}")
def delete(padron: int) -> Alumno:
    alumno = buscar_alumno(padron)
    alumnos.remove(alumno)
    return alumno


def buscar_alumno(padron: int) -> Alumno:
    for alumno in alumnos:
        if alumno.padron == padron:
            return alumno
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Alumno NO encontrado"
    )
