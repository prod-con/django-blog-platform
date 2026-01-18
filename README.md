# Django Blog Platform

A barebones Django blogging platform with user authentication and article management.

## Features

- User registration and login
- Create and delete articles
- View articles in reverse chronological order
- View articles by specific users

## Setup

The project is already set up with a virtual environment and migrations have been run.

## Running the Application

1. Activate the virtual environment:
```bash
source venv/bin/activate
```

2. Start the development server:
```bash
python manage.py runserver
```

3. Open your browser and navigate to: `http://127.0.0.1:8000/`

## Usage

1. Register a new account at `/register/`
2. Login with your credentials at `/login/`
3. Create articles at `/create/`
4. View all articles on the home page
5. View a specific user's articles at `/user/<username>/`
6. Delete your own articles using the delete button

## Admin Panel

To create a superuser for the admin panel:
```bash
python manage.py createsuperuser
```

Access the admin panel at `http://127.0.0.1:8000/admin/`

## Project Structure

- `blog/` - Main blog application
  - `models.py` - Article model with user relationship
  - `views.py` - Authentication and article views
  - `urls.py` - URL routing
  - `templates/blog/` - HTML templates
- `blogplatform/` - Project settings and configuration
