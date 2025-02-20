Teradata testing 
==========================================

Este proyecto implementa un sistema básico de gestión de clientes utilizando Teradata como base de datos.

Requisitos Previos
----------------
* Docker
* Docker Compose
* Git

Configuración Inicial
-------------------
1. Clonar el repositorio:
   git clone <url-del-repositorio>

2. Crear archivo de variables de entorno:
   .env

3. Editar el archivo .env con tus credenciales de Teradata:
   TERADATA_HOST=your_host
   TERADATA_USER=your_user
   TERADATA_PASSWORD=your_password
   TERADATA_DATABASE=your_database

Ejecutar Tests con Docker
-----------------------
1. Construir la imagen de Docker:
   docker-compose -f docker/docker-compose.yml build

2. Ejecutar todos los tests:
   docker-compose -f docker/docker-compose.yml run tests

3. Ejecutar tests específicos:
   docker-compose -f docker/docker-compose.yml run tests pytest test/test_crud_operations.py -v

Limpiar el Entorno Docker
-----------------------
Para remover contenedores y reconstruir desde cero:

1. Detener y remover contenedores:
   docker-compose -f docker/docker-compose.yml down

2. Remover todas las imágenes y volúmenes:
   docker-compose -f docker/docker-compose.yml down --rmi all --volumes

Estructura del Proyecto
---------------------
.
├── src/
│   ├── __init__.py
│   ├── config.py          # Configuración de la base de datos
│   ├── database.py        # Conexión a Teradata
│   ├── crud_operations.py # Operaciones CRUD
│   └── data_loader.py     # Carga inicial de datos
├── test/
│   └── test_crud_operations.py
├── docker/
│   └── docker-compose.yml
├── .env.example
├── .gitignore
├── Dockerfile
└── requirements.txt

Operaciones Disponibles
---------------------
* read_all_clients(): Obtiene todos los clientes
* update_client_email(client_id, new_email): Actualiza el email de un cliente
* delete_client(client_id): Elimina un cliente

Notas de Desarrollo
-----------------
* Los tests se ejecutan automáticamente al iniciar el contenedor
* La base de datos se recrea para cada ejecución de tests
* Las credenciales sensibles deben mantenerse en el archivo .env (no commitear)
* El sistema utiliza Python con el driver oficial de Teradata
* Todas las operaciones están cubiertas por tests automatizados

Solución de Problemas
-------------------
1. Si los tests fallan por conexión:
   - Verificar credenciales en .env
   - Comprobar acceso a Teradata
   - Verificar que el host sea accesible

2. Si Docker falla:
   - Verificar que Docker esté corriendo
   - Limpiar imágenes y volúmenes antiguos
   - Reconstruir la imagen desde cero 
