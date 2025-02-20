import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Teradata database configuration
DB_CONFIG = {
    'host': os.getenv('TERADATA_HOST'),
    'user': os.getenv('TERADATA_USER'),
    'password': os.getenv('TERADATA_PASSWORD'),
    'database': os.getenv('TERADATA_DATABASE')
}
