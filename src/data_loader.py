from src.database import get_connection

def create_table():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            # En Teradata usamos DROP TABLE si existe
            cursor.execute("""
                DROP TABLE clientes
            """)
            
            # Creamos la tabla con sintaxis Teradata
            cursor.execute("""
                CREATE TABLE clientes (
                    id INTEGER NOT NULL,
                    nombre VARCHAR(100),
                    email VARCHAR(100),
                    telefono VARCHAR(20),
                    PRIMARY KEY (id)
                )
            """)
        conn.commit()

def load_sample_data():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            # Insertamos los 3 clientes que esperan los tests
            cursor.execute("""
                INSERT INTO clientes (id, nombre, email, telefono) 
                VALUES (?, ?, ?, ?)
            """, (1, 'Juan Perez', 'juan@example.com', '1234567890'))
            
            cursor.execute("""
                INSERT INTO clientes (id, nombre, email, telefono) 
                VALUES (?, ?, ?, ?)
            """, (2, 'Maria Garcia', 'maria@example.com', '0987654321'))
            
            cursor.execute("""
                INSERT INTO clientes (id, nombre, email, telefono) 
                VALUES (?, ?, ?, ?)
            """, (3, 'Pedro Lopez', 'pedro@example.com', '5555555555'))
        conn.commit()
