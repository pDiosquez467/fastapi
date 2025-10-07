from fastapi import APIRouter, status

from dependencies.dependencies import DatabaseDep
from models.models import Alumno, AlumnoUpsert, Error

router = APIRouter()


@router.get("/")
def list(db: DatabaseDep) -> list[Alumno]:
    return db.list()


@router.get("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(db: DatabaseDep, padron: int) -> Alumno:
    return db.find(padron)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(db: DatabaseDep, alumno_upsert: AlumnoUpsert) -> Alumno:
    alumno = db.add(alumno_upsert)
    return alumno


@router.put("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def update(db: DatabaseDep, padron: int, alumno_upsert: AlumnoUpsert) -> Alumno:
    alumno = db.update(padron, alumno_upsert)
    return alumno


@router.delete("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def delete(db: DatabaseDep, padron: int) -> Alumno:
    alumno = db.delete(padron)
    return alumno


@router.patch(
    "/{padron}/cargar_nota", responses={status.HTTP_404_NOT_FOUND: {"model": Error}}
)
def cargar_nota(db: DatabaseDep, padron: int, nota: int) -> Alumno:
    alumno = db.cargar_nota(padron, nota)
    return alumno
