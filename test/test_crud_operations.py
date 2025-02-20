import pytest
from src.crud_operations import read_all_clients, update_client_email, delete_client
from src.data_loader import create_table, load_sample_data

@pytest.fixture(autouse=True)
def setup_database():
    create_table()
    load_sample_data()

def test_read_all_clients():
    clients = read_all_clients()
    assert len(clients) == 3
    # Verificamos que los clientes estén ordenados por ID
    assert clients[0][0] == 1  # Primer cliente tiene ID 1
    assert clients[0][1] == 'Juan Perez'
    assert clients[1][0] == 2  # Segundo cliente tiene ID 2
    assert clients[2][0] == 3  # Tercer cliente tiene ID 3

def test_update_client_email():
    new_email = "nuevo@example.com"
    update_client_email(1, new_email)
    clients = read_all_clients()
    # Buscamos el cliente con ID 1
    client = next(c for c in clients if c[0] == 1)
    assert client[2] == new_email

def test_delete_client():
    delete_client(1)
    clients = read_all_clients()
    assert len(clients) == 2
    # Verificamos que el cliente con ID 1 ya no existe
    assert all(c[0] != 1 for c in clients)
