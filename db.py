import sqlite3

DB_NAME = "myDB.db"

# ----------------------------
# CONEXIÓN GENERAL
# ----------------------------
def connection():
    return sqlite3.connect(DB_NAME)


# ----------------------------
# CREATE
# ----------------------------
def post(data):
    try:
        conn = connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (nombre, correo) VALUES (?, ?)",
            (data["nombre"], data["correo"])
        )
        conn.commit()
        return {"message": "Usuario creado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conn.close()


# ----------------------------
# READ
# ----------------------------
def get():
    try:
        conn = connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        filas = cur.fetchall()

        resultado = []
        for f in filas:
            resultado.append({
                "id": f[0],
                "nombre": f[1],
                "correo": f[2]
            })
        return resultado
    except Exception as e:
        return {"error": str(e)}
    finally:
        conn.close()


# ----------------------------
# UPDATE
# ----------------------------
def put(user_id, data):
    try:
        conn = connection()
        cur = conn.cursor()

        cur.execute(
            "UPDATE users SET nombre = ?, correo = ? WHERE id = ?",
            (data["nombre"], data["correo"], user_id)
        )
        conn.commit()

        if cur.rowcount == 0:
            return {"error": "Usuario no encontrado"}

        return {"message": "Usuario actualizado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conn.close()


# ----------------------------
# DELETE
# ----------------------------
def delete(user_id):
    try:
        conn = connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()

        if cur.rowcount == 0:
            return {"error": "Usuario no encontrado"}

        return {"message": "Usuario eliminado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conn.close()
