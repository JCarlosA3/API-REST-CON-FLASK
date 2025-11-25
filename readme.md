
Descripción General del Proyecto:
Este proyecto consiste en la creación de una **API REST** utilizando el framework **Flask** y la base de datos **SQLite**.  
La API permite realizar operaciones **CRUD** (Crear, Leer, Actualizar y Eliminar) sobre un recurso llamado **users**, el cual contiene los campos:

- `id` (clave primaria)
- `nombre`
- `correo`

La API fue probada utilizando **Postman**, verificando su correcto funcionamiento mediante solicitudes HTTP.


Estructura del Proyecto
/api_flask
│── app.py
│── db.py
│── structureDB.sql
│── myDB.db
└── readme.md


Base de Datos

El archivo `structureDB.sql` contiene la estructura inicial de la tabla `users`:

```sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT NOT NULL UNIQUE
);

Para generar la base de datos:

import sqlite3

conn = sqlite3.connect("myDB.db")
f = open("structureDB.sql")
conn.executescript(f.read())
conn.commit()
conn.close()


Ejecutar Flask desde la terminal:
python app.py


La API se levanta en:
http://127.0.0.1:5000/


Endpoints Implementados

GET – Obtener todos los usuarios
GET /users
Ejemplo de respuesta:
[
    {
        "id": 1,
        "nombre": "Jose",
        "correo": "jose@gmail.com"
    }
]

POST – Crear un nuevo usuario
POST /users
Body (JSON):
{
    "nombre": "Jose",
    "correo": "jose@gmail.com"
}
Respuesta:
{
    "mensaje": "Usuario creado correctamente"
}

PUT – Actualizar un usuario existente
PUT /users/<id>
Body (JSON):
{
    "nombre": "Jose Editado",
    "correo": "nuevo@gmail.com"
}

DELETE – Eliminar un usuario
DELETE /users/<id>
Respuesta:
{
    "mensaje": "Usuario eliminado correctamente"
}
