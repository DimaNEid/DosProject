# DosProject

This project is a **microservices-based application** that uses Docker to containerize individual services, ensuring isolation and easy deployment. The main components include:

1. **Catalog Service** - Manages the catalog of items (e.g., books) with a database to store information like titles, costs, stock levels, and more.
2. **Order Service** - Handles purchase requests, checking inventory from the catalog, updating stock, and processing transactions.
3. **Frontend Service** - Acts as an interface between the backend services and users, handling API requests to the catalog and order services.

## Key Features

- **Database Isolation**: Each service container operates with its own database instance (e.g., `db.sqlite3` in the Catalog service), ensuring changes are limited to the Docker environment and don't affect the host system.
- **Data Consistency**: The Docker setup preserves data state within each container, allowing the system to be moved or restarted without data loss.
- **Microservice Architecture**: The project uses a modular approach with services communicating over HTTP, providing flexibility for scaling and maintenance.
- **Reproducibility**: Docker containers ensure consistent environments, making it easy to deploy the same setup across different machines.
