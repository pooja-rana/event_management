# Event Management API

A simplified Event Management API built with Django and Django REST Framework. This API supports role-based access control for Admin and User roles, allowing admins to manage events and users to purchase tickets.

## Features

- **User Management:**
  - Register users with roles (`Admin` or `User`).
  - Secure password handling with hashing.

- **Event Management (Admin Only):**
  - Create and manage events.
  - Fetch all events.

- **Ticket Management (User Only):**
  - Purchase tickets for events.
  - Validation to ensure ticket availability.

- **Authentication:**
  - JWT-based authentication for secure API access.

## Requirements

- Python 3.8+
- Django 4.0+
- Django REST Framework
- PostgreSQL or MySQL
- `djangorestframework-simplejwt`


## Installation

1. Clone the repository:
   ```bash
   git clone --branch develop https://github.com/pooja-rana/event_management.git

   ```
 2 Create a virtual environment and activate it:
   ```bash
   virtualenv -p python3.10 .venv
   source .venv/bin/activate 
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```plaintext
└── event_api
    ├── event_api
    │   ├── asgi.py
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-310.pyc
    │   │   ├── __init__.cpython-38.pyc
    │   │   ├── settings.cpython-310.pyc
    │   │   ├── settings.cpython-38.pyc
    │   │   ├── urls.cpython-310.pyc
    │   │   └── wsgi.cpython-310.pyc
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── events
    │   ├── admin.py
    │   ├── apps.py
    │   ├── constant.py
    │   ├── __init__.py
    │   ├── messages.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_alter_user_options_user_date_joined_user_email_and_more.py
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       ├── 0001_initial.cpython-310.pyc
    │   │       ├── 0002_alter_user_options_user_date_joined_user_email_and_more.cpython-310.pyc
    │   │       └── __init__.cpython-310.pyc
    │   ├── models
    │   │   ├── event_and_ticket_models.py
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── event_and_ticket_models.cpython-310.pyc
    │   │   │   ├── __init__.cpython-310.pyc
    │   │   │   └── user_models.cpython-310.pyc
    │   │   └── user_models.py
    │   ├── models.py
    │   ├── __pycache__
    │   │   ├── admin.cpython-310.pyc
    │   │   ├── apps.cpython-310.pyc
    │   │   ├── __init__.cpython-310.pyc
    │   │   ├── messages.cpython-310.pyc
    │   │   ├── urls.cpython-310.pyc
    │   │   └── views.cpython-310.pyc
    │   ├── serializers
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── __init__.cpython-310.pyc
    │   │   │   └── user_serializer.cpython-310.pyc
    │   │   └── user_serializer.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── __init__.py
    ├── manage.py
    └── requirements.txt
```


