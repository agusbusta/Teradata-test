import teradatasql
from src.config import DB_CONFIG

def get_connection():
    return teradatasql.connect(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        database=DB_CONFIG['database']
    )
