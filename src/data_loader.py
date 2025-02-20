from src.database import get_connection

def create_table():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            # Primero intentamos eliminar la tabla si existe
            try:
                cursor.execute("DROP TABLE clientes")
            except:
                pass  # Ignoramos el error si la tabla no existe
            
            # Creamos la tabla
            cursor.execute("""
                CREATE TABLE clientes (
                    id INTEGER NOT NULL PRIMARY KEY,
                    nombre VARCHAR(100),
                    email VARCHAR(100),
                    telefono VARCHAR(20)
                )
            """)
        conn.commit()

def load_sample_data():
    sample_data = [
        (1, 'Juan Perez', 'juan@example.com', '555-0101'),
        (2, 'Maria Garcia', 'maria@example.com', '555-0102'),
        (3, 'Carlos Rodriguez', 'carlos@example.com', '555-0103')
    ]
    
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM clientes")  # Clear existing data
            cursor.executemany(
                "INSERT INTO clientes (id, nombre, email, telefono) VALUES (?, ?, ?, ?)",
                sample_data
            )
        conn.commit()
