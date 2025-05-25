# 🎴 Digital Trading Card Vault - Developer Documentation

A modern Django web application for managing and displaying trading card collections with a cyber-themed interface, particle effects, and advanced animations. This comprehensive guide will help developers understand, set up, and contribute to the project.

## 🏗️ Development Setup

### Local Development (Without Docker)

If you prefer local development:
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up database
python manage.py migrate
python manage.py seed

# Run development server
python manage.py runserver

### Local Development (With Docker)
// Builds the Docker image
docker-compose up
//run in separate terminal
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py seed