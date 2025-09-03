# Full Stack Data Engineer Demo

Demo for Social Booster Media's Full Stack Data Engineer role: Django app with CRUD APIs, PostgreSQL/Supabase, third-party API integration, and data visualization.

## Setup

1. Clone: `git clone https://github.com/RohitYadav28/fullstack-data-engineer.git`
2. Activate venv: `venv\Scripts\activate` (Windows)
3. Install: `pip install -r requirements.txt`
4. Set up PostgreSQL/Supabase in `core/settings.py`.
5. Migrate: `python manage.py migrate`
6. Run: `python manage.py runserver`

## Features

- CRUD APIs: `/api/books/` (list/create), `/api/books/<id>/` (retrieve/update/delete)
- External API: `/api/fetch-external/` (fetches from JSONPlaceholder)
- Visualization: `/` (Chart.js bar chart of book prices)

## Testing

- Use Postman for APIs (e.g., POST/GET/PUT/DELETE to /api/books/).
- View chart at root URL after adding data.

## Decisions

- Used Django REST Framework for scalable APIs.
- JSONPlaceholder for simple external API integration.
- Chart.js for lightweight visualization.
