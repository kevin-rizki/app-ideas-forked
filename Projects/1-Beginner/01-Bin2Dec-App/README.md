# Project Name

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## How to Run

To run the application, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/kevinrizki1019/app-ideas-forked.git
   ```

2. Navigate to the project directory:

   ```bash
   cd app-ideas-forked/Projects/1-Beginner/01-Bin2Dec-App
   ```

3. Build and run the Docker containers using Docker Compose:

   ```bash
   docker-compose run myapp python app.py
   ```

   Replace `myapp` with the name of your service defined in your `docker-compose.yml` file. This command will start the container and execute the Python script `app.py`.

4. You should see the output of the application in the terminal.

   Example:

   ```bash
    11
    Binary: 11
    Decimal:  3

   ```

5. To exit the container, press `Ctrl+C`.
