# Flask Application with Docker

## Prerequisites

- Docker
- Docker Compose

## Build and Run the Application with Docker

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-repo.git
    cd your-repo
    ```

2. **Build the Docker images and start the containers:**

    ```sh
    docker-compose up --build
    ```

    This command will build the Docker images and start the containers defined in `docker-compose.yml`.

3. **Access the application:**

    Open your web browser and go to `http://localhost:5000`.

## Running Tests

1. **Run the tests inside the container:**

    ```sh
    docker-compose run web pytest
    ```

## Cleaning Up

1. **Stop and remove the containers:**

    ```sh
    docker-compose down
    ```

2. **Remove the Docker volumes:**

    ```sh
    docker volume rm $(docker volume ls -q)
    ```

## Additional Information

- **Configuration:** Modify `config.py` to update database configurations or other settings.
- **Database:** The default database used is PostgreSQL. Modify the `docker-compose.yml` and `config.py` to change database settings.
