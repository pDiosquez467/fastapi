from models.models import Alumno
from dependencies.dependencies import get_database


def seed():
    alumnos = [
        Alumno(padron=1, nombre="Juan", apellido="Perez", edad=20),
        Alumno(padron=2, nombre="Juan", apellido="Perez", edad=20),
        Alumno(padron=3, nombre="Juan", apellido="Perez", edad=20),
    ]
    get_database().cargar_alumnos(alumnos)
