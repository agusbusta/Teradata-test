from data_loader import create_table, load_sample_data
from crud_operations import read_all_clients, update_client_email, delete_client

def main():
    # Crear tabla y cargar datos de ejemplo
    create_table()
    load_sample_data()

    # Ejemplo de lectura
    print("Todos los clientes:")
    for client in read_all_clients():
        print(client)

    # Ejemplo de actualización
    update_client_email(1, 'juan_nuevo@example.com')
    print("\nClientes después de la actualización:")
    for client in read_all_clients():
        print(client)

    # Ejemplo de borrado
    delete_client(2)
    print("\nClientes después del borrado:")
    for client in read_all_clients():
        print(client)

if __name__ == "__main__":
    main()
