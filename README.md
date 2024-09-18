# FlyWithMe - Airline Management System

FlyWithMe is a web application developed using Django for managing flight details. It allows administrators to perform CRUD operations on flight records, view flight lists, and manage flight schedules.

## Features

- **Flight Management:** Create, read, update, and delete flight records.
- **User Authentication:** Secure login and registration for administrators.
- **Search Functionality:** Search for flights by Flight ID.
- **Responsive Design:** Designed for desktop and mobile use.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- MySQL

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/flywithme.git
    cd flywithme
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use: env\Scripts\activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the database:**

    Update the `DATABASES` settings in `settings.py` with your MySQL database credentials.

5. **Run migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    Visit `http://127.0.0.1:8000` in your web browser to see the application in action.

## Usage

- **Home Page:** Access the landing page of FlyWithMe.
- **Flight List:** View and search for flights.
- **Add Flight:** Add new flight records.
- **Edit Flight:** Modify existing flight records.
- **Delete Flight:** Remove flight records.

## URL Patterns

- **Landing Page:** `/`
- **Login:** `/login/`
- **Registration:** `/registration/`
- **Flight List:** `/flights/`
- **Add Flight:** `/flights/add/`
- **Edit Flight:** `/flights/edit/<flight_id>/`
- **Delete Flight:** `/flights/delete/<flight_id>/`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django for providing a robust framework for web development.
- MySQL for reliable database management.

