from src.database import get_connection

def read_all_clients():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM clientes ORDER BY id")
            return cursor.fetchall()

def update_client_email(client_id, new_email):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE clientes SET email = ? WHERE id = ?", (new_email, client_id))
        conn.commit()

def delete_client(client_id):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM clientes WHERE id = ?", (client_id,))
        conn.commit()
