# Book API

A Django REST Framework-based API for managing a book store. This API provides endpoints to create, retrieve, update, and delete books with full serialization support.

## Features

- ✅ RESTful API endpoints for book management
- ✅ Django ORM for database operations
- ✅ Django REST Framework serializers
- ✅ SQLite database (development)
- ✅ Clean project structure with separated concerns

## Project Structure

```
book_api/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database (development)
├── books/                   # Main app
│   ├── models.py            # Book model definition
│   ├── views.py             # API views/viewsets
│   ├── serializers.py       # DRF serializers
│   ├── admin.py             # Django admin config
│   ├── apps.py              # App configuration
│   ├── tests.py             # Unit tests
│   └── migrations/          # Database migrations
└── library_resource/        # Project settings
    ├── settings.py          # Django settings
    ├── urls.py              # URL routing
    ├── wsgi.py              # WSGI configuration
    └── asgi.py              # ASGI configuration
```

## Prerequisites

- Python 3.8+ 
- Django 3.2+
- Django REST Framework

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Kwesimk102/book_api.git
cd book_api
```

### 2. Create a virtual environment

```bash
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install manually:

```bash
pip install django djangorestframework
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

## Running the Server

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

### Admin Panel

Access the Django admin at: `http://localhost:8000/admin/`

## API Endpoints

### Books
- `GET /api/books/` - List all books
- `POST /api/books/` - Create a new book
- `GET /api/books/{id}/` - Retrieve a specific book
- `PUT /api/books/{id}/` - Update a book
- `DELETE /api/books/{id}/` - Delete a book

## Example Usage

### Get all books
```bash
curl http://localhost:8000/api/books/
```

### Create a new book
```bash
curl -X POST http://localhost:8000/api/books/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Django for Beginners",
    "author": "William Vincent",
    "isbn": "123-456-789",
    "pages": 350
  }'
```

### Get a specific book
```bash
curl http://localhost:8000/api/books/1/
```

### Update a book
```bash
curl -X PUT http://localhost:8000/api/books/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Advanced Django",
    "author": "William Vincent",
    "pages": 400
  }'
```

### Delete a book
```bash
curl -X DELETE http://localhost:8000/api/books/1/
```

## Testing

Run unit tests:

```bash
python manage.py test
```

## Configuration

### Database

Currently using SQLite for development. To use PostgreSQL or MySQL, update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'book_api_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}.

## Dependencies

Core dependencies (install with `pip install -r requirements.txt`):
- Django
- djangorestframework


## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or suggestions, please open an [issue](https://github.com/Kwesimk102/book_api/issues) on GitHub.

## Author

**Kwesimk102**  
GitHub: [@Kwesimk102](https://github.com/Kwesimk102)

---

**Last Updated:** December 1, 2025
