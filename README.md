# Flix API 🎬

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.2-darkgreen.svg)
![Django REST Framework](https://img.shields.io/badge/DRF-3.16-red.svg)

A robust RESTful API built with Django and Django REST Framework, simulating the core features of a movie streaming service. This project showcases best practices in API development, including JWT authentication, custom permissions, and a professional code quality workflow.

## Core Features

* ✅ **Secure User Authentication:** Complete authentication system using JWT, with access and refresh tokens.
* ✅ **Entity Management:** Full CRUD operations for Genres, Actors, Movies, and Reviews.
* ✅ **Rating System:** Allows authenticated users to rate movies from 0 to 5 stars and add comments.
* ✅ **Platform Statistics:** A dedicated endpoint that returns aggregated metrics, such as total movies, count by genre, total reviews, and the overall average star rating.
* ✅ **Data Quality:** Implements validation at the serializer and model levels, including enforcing unique genre names to maintain data integrity.
* ✅ **Developer Tooling:** Includes custom management commands for administrative tasks, such as importing data from a CSV file.

## Tech Stack & Code Quality

* **Backend:** Python
* **Framework:** Django & Django REST Framework
* **Database:** SQLite3 (for development)
* **Authentication:** Simple JWT
* **Code Quality & Formatting:**
    * **Black:** For consistent, opinionated code formatting.
    * **isort:** For automatically organizing imports.
    * **Flake8:** For linting and enforcing PEP 8 style guide.

## API Endpoints (v1)

The base URL for all endpoints is `/api/v1/`. All routes (except for authentication) require a valid JWT in the `Authorization` header.

| Method               | Endpoint                        | Description                                     |
| :------------------- | :------------------------------ | :---------------------------------------------- |
| `POST`               | `/authentication/token/`        | Obtains a new token pair (access and refresh).  |
| `POST`               | `/authentication/token/refresh/`  | Refreshes an expired access token.              |
| `GET`, `POST`        | `/genres/`                      | Lists all genres or creates a new one.          |
| `GET`, `PUT`, `DELETE` | `/genres/<id>/`                 | Retrieves, updates, or deletes a specific genre. |
| `GET`, `POST`        | `/actors/`                      | Lists all actors or creates a new one.          |
| `GET`, `PUT`, `DELETE` | `/actors/<id>/`                 | Retrieves, updates, or deletes a specific actor. |
| `GET`, `POST`        | `/movies/`                      | Lists all movies or creates a new one.          |
| `GET`, `PUT`, `DELETE` | `/movies/<id>/`                 | Retrieves, updates, or deletes a specific movie. |
| `GET`                | `/movies/stats/`                | Returns statistics about movies and reviews.    |
| `GET`, `POST`        | `/reviews/`                     | Lists all reviews or creates a new one.         |
| `GET`, `PUT`, `DELETE` | `/reviews/<id>/`                | Retrieves, updates, or deletes a specific review.|

## How to Run the Project Locally

Follow these steps to set up and run the development environment.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Daniel-Q-Reis/flix-api.git](https://github.com/Daniel-Q-Reis/flix-api.git)
    cd flix-api
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install all dependencies:**
    *This command installs both production (`requirements.txt`) and development (`black`, `flake8`, `isort`) dependencies.*
    ```bash
    pip install -r requirements_dev.txt
    ```

4.  **Run the database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser to access the Admin panel:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **(Optional) Populate the database with initial actor data:**
    * Ensure the `actors.csv` file is in the project's root directory.
    * Run the management command:
    ```bash
    python manage.py import_actors actors.csv
    ```

7.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

The API will be available at `http://127.0.0.1:8000/`.

## Next Steps (Future Enhancements)

-   [ ] Containerize the application using Docker and Docker Compose.
-   [ ] Add automated tests with Pytest.
-   [ ] Set up a CI/CD pipeline for automated testing and deployment.
-   [ ] Implement a robust logging system for error monitoring.