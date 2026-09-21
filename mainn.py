from fastapi import FastAPI, HTTPException
from models import Libro, Editorial

app = FastAPI(title="API Biblioteca UNACH")

ed1 = Editorial(1, "McGraw Hill", "Estados Unidos")
ed2 = Editorial(2, "O'Reilly Media", "Estados Unidos")
ed3 = Editorial(3, "Ediciones de la U", "Colombia")
ed4 = Editorial(4, "Alfaomega", "México")

db_editoriales = {
    ed1.get_idEd(): ed1,
    ed2.get_idEd(): ed2,
    ed3.get_idEd(): ed3,
    ed4.get_idEd(): ed4
}

lib1 = Libro("978-3-16-148410-0", "Introducción a Python", "Guido van Rossum", 450.50)
lib2 = Libro("978-0-596-51649-9", "Learning Python", "Mark Lutz", 890.00)
lib3 = Libro("978-84-415-3210-6", "Estructuras de Datos", "Luis Joyanes", 600.00)
lib4 = Libro("978-607-15-0818-8", "Bases de Datos", "Silberschatz", 1200.75)
lib5 = Libro("978-1-491-95625-0", "Fluent Python", "Luciano Ramalho", 950.00)

db_libros = {
    lib1.get_ISBN(): lib1,
    lib2.get_ISBN(): lib2,
    lib3.get_ISBN(): lib3,
    lib4.get_ISBN(): lib4,
    lib5.get_ISBN(): lib5
}

@app.get("/editoriales/{id_ed}")
def obtener_editorial(id_ed: int):
    editorial = db_editoriales.get(id_ed)
    if editorial:
        return editorial.to_dict()
    raise HTTPException(status_code=404, detail="Editorial no encontrada")

@app.get("/libros/{isbn}")
def obtener_libro(isbn: str):
    libro = db_libros.get(isbn)
    if libro:
        return libro.to_dict()
    raise HTTPException(status_code=404, detail="Libro no encontrado")