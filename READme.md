# 🎴 Digital Trading Card Vault - Developer Documentation

A modern Django web application for managing and displaying trading card collections with a cyber-themed interface, particle effects, and advanced animations. This comprehensive guide will help developers understand, set up, and contribute to the project.

# Install dependencies
```bash
pip install -r requirements.txt
```
## 🏗️ Development Setup

### Local Development (Without Docker)

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
# Setup the database
python manage.py migrate
python manage.py seed
# Run development server
python manage.py runserver
```
### Local Development (With Docker)
```bash
# Builds the Docker image
docker-compose up
# Run in separate terminal
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py seed
```
 
### Key Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| Django | 5.2.1 | Backend framework |
| Python | 3.13 | Programming language |
| sqlite3 | 3 | Database |
| Bootstrap | 5.3.0 | CSS framework |
| Alpine.js | 3.x | Reactive frontend |
| HTMX | 1.9.x | AJAX interactions |
