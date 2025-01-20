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
- PostgreSQL or MySQL (or SQLite for development/testing)
- `djangorestframework-simplejwt`
