#!/bin/bash

# Docker management scripts for Trading Card Vault

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Help function
show_help() {
    echo "Trading Card Vault - Docker Management Script"
    echo ""
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commands:"
    echo "  dev-up       Start development environment"
    echo "  dev-down     Stop development environment"
    echo "  prod-up      Start production environment"
    echo "  prod-down    Stop production environment"
    echo "  build        Build Docker images"
    echo "  logs         Show application logs"
    echo "  shell        Open Django shell in container"
    echo "  migrate      Run Django migrations"
    echo "  seed         Seed database with sample data"
    echo "  reset        Reset database (removes all data)"
    echo "  clean        Clean up Docker resources"
    echo "  help         Show this help message"
    echo ""
}

# Development environment
dev_up() {
    print_status "Starting development environment..."
    docker-compose -f docker-compose.dev.yml up --build -d
    print_success "Development environment started!"
    print_status "Application: http://localhost:8000"
    print_status "Admin: http://localhost:8000/admin (admin/admin123)"
}

dev_down() {
    print_status "Stopping development environment..."
    docker-compose -f docker-compose.dev.yml down
    print_success "Development environment stopped!"
}

# Production environment
prod_up() {
    print_status "Starting production environment..."
    docker-compose up --build -d
    print_success "Production environment started!"
    print_status "Application: http://localhost"
    print_status "Direct Django: http://localhost:8000"
}

prod_down() {
    print_status "Stopping production environment..."
    docker-compose down
    print_success "Production environment stopped!"
}

# Build images
build_images() {
    print_status "Building Docker images..."
    docker-compose build --no-cache
    print_success "Docker images built successfully!"
}

# Show logs
show_logs() {
    print_status "Showing application logs..."
    docker-compose logs -f web
}

# Django shell
django_shell() {
    print_status "Opening Django shell..."
    docker-compose exec web python manage.py shell
}

# Run migrations
run_migrations() {
    print_status "Running Django migrations..."
    docker-compose exec web python manage.py migrate
    print_success "Migrations completed!"
}

# Seed database
seed_database() {
    print_status "Seeding database with sample data..."
    docker-compose exec web python manage.py seed
    print_success "Database seeded successfully!"
}

# Reset database
reset_database() {
    print_warning "This will delete all data in the database!"
    read -p "Are you sure? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        print_status "Resetting database..."
        docker-compose down -v
        docker-compose up -d db
        sleep 5
        docker-compose exec web python manage.py migrate
        docker-compose exec web python manage.py seed
        print_success "Database reset completed!"
    else
        print_status "Database reset cancelled."
    fi
}

# Clean up Docker resources
clean_docker() {
    print_status "Cleaning up Docker resources..."
    docker-compose down -v --remove-orphans
    docker system prune -f
    print_success "Docker cleanup completed!"
}

# Main script logic
case "${1:-help}" in
    "dev-up")
        dev_up
        ;;
    "dev-down")
        dev_down
        ;;
    "prod-up")
        prod_up
        ;;
    "prod-down")
        prod_down
        ;;
    "build")
        build_images
        ;;
    "logs")
        show_logs
        ;;
    "shell")
        django_shell
        ;;
    "migrate")
        run_migrations
        ;;
    "seed")
        seed_database
        ;;
    "reset")
        reset_database
        ;;
    "clean")
        clean_docker
        ;;
    "help"|*)
        show_help
        ;;
esac 