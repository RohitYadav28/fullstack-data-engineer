# Django Demo App

## Setup

1. Clone the repo.
2. Activate venv: source venv/bin/activate
3. Install deps: pip install -r requirements.txt
4. Set up DB in settings.py.
5. Migrate: python manage.py migrate
6. Run: python manage.py runserver

## Features

- CRUD APIs at /api/books/
- External API integration at /api/fetch-external/
- Visualization at /

## Testing

Use Postman for APIs. Add data via POST, then view chart.
