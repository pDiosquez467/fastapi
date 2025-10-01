from fastapi import HTTPException, status
from models.models import Alumno, AlumnoUpsert


class Database:
    def __init__(self):
        self.alumnos = []

    def cargar_alumnos(self, alumnos: list[Alumno]):
        self.alumnos = alumnos

    def list(self) -> list[Alumno]:
        return self.alumnos

    def add(self, alumno_upsert: AlumnoUpsert) -> Alumno:
        padron = len(self.alumnos) + 1
        alumno = Alumno(padron=padron, **alumno_upsert.model_dump())
        self.alumnos.append(alumno)
        return alumno

    def find(self, padron: int) -> Alumno:
        for alumno in self.alumnos:
            if alumno.padron == padron:
                return alumno
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Alumno NO encontrado"
        )

    def update(self, padron: int, alumno_upsert: AlumnoUpsert) -> Alumno:
        alumno = self.find(padron)
        alumno.nombre = alumno_upsert.nombre
        alumno.apellido = alumno_upsert.apellido
        alumno.edad = alumno_upsert.edad
        return alumno

    def delete(self, padron: int) -> Alumno:
        alumno = self.find(padron)
        self.alumnos.remove(alumno)
        return alumno

    def cargar_nota(self, padron: int, nota: int) -> Alumno:
        alumno = self.find(padron)
        alumno.notas.append(nota)
        return alumno
