# Password Manager

A password manager application built with Django and MongoDB to securely store and manage and evaluate strength of passwords.

---

## Features

- Add and store passwords with a title.
- View stored passwords, displayed as masked fields.
- Show passwords using a "View" button.
- Automatically records the date and time when passwords are stored.

---

## Requirements

- Python 3.10+
- Django 5.1.3
- MongoDB 

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ishijapriyansha/passw.git
   cd password-manager

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  

3. Install the required dependencies:
    ```bash
    pip install django pymongo

4. Configure the MongoDB connection:

- Open settings.py
- Add the MongoDB configuration

5. Run Database Migrations
    python manage.py makemigrations
    python manage.py migrate

6. Start the development server:
    ```bash
    python manage.py runserver

7. Open the app in your browser:
    ```bash
    http://127.0.0.1:8000/
    

## Usage
1. Add a password:
    - Enter a title and password in the form on the homepage and click 'Add'.

2. View Stored Passwords:
    - Stored passwords are displayed as masked fields.


## Technologies Used
- Frontend: HTML, CSS (Bootstrap 5)
- Backend: Django
- Database: MongoDB (pymongo)

## Future Enhancements
- Add encryption for stored passwords.
- Implement user authentication and authorization.
- Provide export/import functionality for passwords.
