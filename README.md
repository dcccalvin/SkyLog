# 🛩️ Pilot Logbook Management System

A web-based application for pilots to efficiently log flights, manage certifications, track training, and generate detailed reports. Built with Django and Bootstrap for reliability and ease of use.

---

## Table of Contents

- [Features](#features)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- **User Authentication**: Secure registration, login, and password management.
- **Flight Log Management**: Add, edit, view, and delete flight records with details such as date, aircraft, route, duration, and remarks.
- **Certification Tracking**: Manage pilot certifications, including expiry reminders.
- **Training Records**: Log and review training sessions and outcomes.
- **PDF Report Generation**: Export flight logs and summaries as PDF documents.
- **Responsive UI**: Mobile-friendly interface using Bootstrap.
- **Role-Based Access**: Admin and pilot roles for different access levels.
- **Error Handling**: User-friendly error messages and form validation.

---

## System Architecture

- **Backend**: Django 4.2 (Python 3.13)
- **Frontend**: Bootstrap 4, HTML5, CSS3, JavaScript
- **Database**: SQLite (default, can be switched to PostgreSQL/MySQL)
- **PDF Generation**: ReportLab or WeasyPrint (as configured)
- **Authentication**: Django’s built-in authentication system

---

## Installation

1. **Clone the Repository**
    ```sh
    git clone https://github.com/dcccalvin/logbook_project.git
    cd pilot_logbook
    ```

2. **Create a Virtual Environment**
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply Migrations**
    ```sh
    python manage.py migrate
    ```

5. **Create a Superuser (Admin)**
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the Development Server**
    ```sh
    python manage.py runserver
    ```

7. **Access the Application**
    - Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## Usage

- **Register** as a new pilot or log in as an existing user.
- **Add Flight Logs**: Enter details for each flight.
- **Manage Certifications**: Update and track your pilot certifications.
- **Log Training**: Record training sessions and outcomes.
- **Generate Reports**: Download your logs and summaries as PDFs.
- **Admin Panel**: Access via `/admin` for user and data management.

---

## Project Structure

```
pilot_logbook/
│
├── Pilot_Logbook/           # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── logbook/                 # Main app: models, views, templates
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## Database Schema

- **User**: username, email, password, role
- **FlightLog**: user, date, aircraft, route, duration, remarks
- **Certification**: user, type, issue_date, expiry_date
- **TrainingRecord**: user, session_type, date, outcome

See `corrected schema.png` for a visual representation.

---

## Testing

- **Run Unit Tests**
    ```sh
    python manage.py test
    ```
- **Test Coverage**: Ensure all models, views, and forms are covered.

---

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes.
4. Push to your fork and submit a pull request.
5. Report bugs or request features via Issues.

---

## License

This project is licensed under the MIT License.

---

## Contact

- **Author**: Calvin D.
- **Email**: [chumacalvin8@gmail.com]
- **GitHub**: [https://github.com/dcccalvin/logbook_project](https://github.com/dcccalvin/logbook_project)

---

*Happy flying and safe logging!*