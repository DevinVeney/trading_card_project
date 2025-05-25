# 🎴 Digital Trading Card Vault - Developer Documentation

A modern Django web application for managing and displaying trading card collections with a cyber-themed interface, particle effects, and advanced animations. This comprehensive guide will help developers understand, set up, and contribute to the project.

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Architecture & Technology Stack](#-architecture--technology-stack)
- [Features Documentation](#-features-documentation)
- [Getting Started](#-getting-started)
- [Development Setup](#-development-setup)
- [Project Structure](#-project-structure)
- [Database Schema](#-database-schema)
- [Frontend Architecture](#-frontend-architecture)
- [Backend Architecture](#-backend-architecture)
- [API Documentation](#-api-documentation)
- [Styling & Theming](#-styling--theming)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Contributing Guidelines](#-contributing-guidelines)
- [Troubleshooting](#-troubleshooting)

## 🎯 Project Overview

The Digital Trading Card Vault is a full-stack web application that demonstrates modern web development practices using Django, Bootstrap, Alpine.js, and HTMX. The project showcases:

- **Real-time interactions** without page refreshes
- **Advanced CSS animations** and particle effects
- **Responsive design** with mobile-first approach
- **Containerized deployment** with Docker
- **Modern Django patterns** and best practices

### Key Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| Django | 5.2.1 | Backend framework |
| Python | 3.13 | Programming language |
| PostgreSQL | 16 | Production database |
| Bootstrap | 5.3.0 | CSS framework |
| Alpine.js | 3.x | Reactive frontend |
| HTMX | 1.9.x | AJAX interactions |
| Particles.js | 2.x | Background effects |
| Docker | Latest | Containerization |
| Nginx | Alpine | Reverse proxy |

## 🏗️ Architecture & Technology Stack

### Backend Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Nginx         │    │   Django        │    │   PostgreSQL   │
│   (Reverse      │◄──►│   (Application  │◄──►│   (Database)    │
│    Proxy)       │    │    Server)      │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
    Static Files            Business Logic         Data Storage
    CSS, JS, Images         Views, Models,         Cards, Users,
                           Templates, APIs         Collections
```

### Frontend Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Frontend Layer                           │
├─────────────────┬─────────────────┬─────────────────────────┤
│   Bootstrap     │   Alpine.js     │   HTMX                  │
│   (Styling)     │   (Reactivity)  │   (AJAX)                │
├─────────────────┼─────────────────┼─────────────────────────┤
│   Particles.js  │   AOS           │   Custom CSS            │
│   (Effects)     │   (Animations)  │   (Cyber Theme)         │
└─────────────────┴─────────────────┴─────────────────────────┘
```

## 🚀 Features Documentation

### 1. Interactive Card Display System

**Location**: `cards/templates/cards/partials/card_grid.html`

The card display system features 3D flip animations powered by Alpine.js:

```html
<div class="vault-card" 
     x-data="{ flipped: false }" 
     @click="flipped = !flipped"
     :class="{ 'flipped': flipped }">
```

**Key Features**:
- **3D CSS Transforms**: Cards rotate 180° on Y-axis
- **Rarity-based Styling**: Different visual effects per rarity
- **Responsive Sizing**: Adaptive dimensions across devices
- **Hover Effects**: Elevation and glow on mouse over

**Technical Implementation**:
```css
.vault-card {
    transform-style: preserve-3d;
    transition: transform 0.6s cubic-bezier(0.4, 0.0, 0.2, 1);
}

.vault-card.flipped {
    transform: rotateY(180deg);
}
```

### 2. Real-time Search System

**Location**: `cards/views.py` (search_cards function)

HTMX-powered search with 300ms debouncing:

```html
<input type="text" 
       name="search" 
       hx-get="/cards/search/" 
       hx-target="#card-grid" 
       hx-trigger="keyup changed delay:300ms">
```

**Features**:
- **Debounced Input**: Prevents excessive API calls
- **Partial Page Updates**: Only updates card grid
- **Case-insensitive Search**: Searches card names and descriptions
- **Real-time Results**: No page refresh required

**Backend Implementation**:
```python
def search_cards(request):
    query = request.GET.get('search', '')
    cards = Card.objects.filter(
        Q(name__icontains=query) | 
        Q(description__icontains=query)
    )
    return render(request, 'cards/partials/card_grid.html', {'cards': cards})
```

### 3. Particle Effects System

**Location**: `cards/templates/cards/base.html`

Interactive particle background using particles.js:

```javascript
particlesJS('particles-js', {
    particles: {
        number: { value: 80 },
        color: { value: ['#00d4ff', '#8b5cf6', '#00ff88'] },
        shape: { type: 'circle' },
        opacity: { value: 0.6, random: true },
        size: { value: 3, random: true },
        line_linked: {
            enable: true,
            distance: 150,
            color: '#00d4ff',
            opacity: 0.4,
            width: 1
        },
        move: {
            enable: true,
            speed: 2,
            direction: 'none',
            random: false,
            straight: false,
            out_mode: 'out',
            bounce: false
        }
    },
    interactivity: {
        detect_on: 'canvas',
        events: {
            onhover: { enable: true, mode: 'repulse' },
            onclick: { enable: true, mode: 'push' },
            resize: true
        }
    }
});
```

**Features**:
- **Interactive Particles**: Respond to mouse movement
- **Click Effects**: Generate new particles on click
- **Network Connections**: Particles connect with lines
- **Color Theming**: Matches cyber vault aesthetic

### 4. Rarity System & Visual Effects

**Location**: `cards/static/cards/css/vault-theme.css`

Cards have different visual effects based on rarity:

```css
/* Epic Cards - Pulsing Glow */
.vault-card[data-rarity="epic"] {
    animation: epicPulse 2s ease-in-out infinite alternate;
    box-shadow: 0 0 30px rgba(139, 92, 246, 0.6);
}

/* Legendary Cards - Breathing Effect */
.vault-card[data-rarity="legendary"] {
    animation: legendaryBreathe 3s ease-in-out infinite;
    box-shadow: 0 0 40px rgba(255, 215, 0, 0.8);
}
```

**Rarity Levels**:
1. **Common**: Basic styling, gray badge
2. **Uncommon**: Green accent, subtle glow
3. **Rare**: Blue accent, moderate glow
4. **Epic**: Purple accent, pulsing animation
5. **Legendary**: Gold accent, breathing effect

### 5. Responsive Design System

**Breakpoints**:
```css
/* Mobile First Approach */
.vault-card { width: 280px; height: 420px; }

/* Tablet */
@media (max-width: 768px) {
    .vault-card { width: 260px; height: 390px; }
}

/* Mobile */
@media (max-width: 480px) {
    .vault-card { width: 320px; height: 480px; }
    .vault-grid { grid-template-columns: 1fr; }
}

/* Large Screens */
@media (min-width: 1200px) {
    .vault-card { width: 300px; height: 450px; }
}
```

### 6. Authentication System

**Location**: `trading_card_project/urls.py`, `cards/views.py`

Django's built-in authentication with custom templates:

```python
# URL Configuration
path('accounts/', include('django.contrib.auth.urls')),
path('admin/', admin.site.urls),

# View Protection
@login_required
def card_list(request):
    # Protected view logic
```

**Features**:
- **Login/Logout**: Standard Django auth
- **Admin Interface**: Full CRUD operations
- **User Sessions**: Persistent login state
- **Permission System**: Admin vs regular users

## 🛠️ Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Docker** (20.10+) and **Docker Compose** (2.0+)
- **Git** for version control
- **Code Editor** (VS Code recommended)
- **Web Browser** (Chrome/Firefox for best experience)

### Quick Start (5 minutes)

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd trading_card_project
   ```

2. **Start Development Environment**
   ```bash
   chmod +x docker-scripts.sh
   ./docker-scripts.sh dev-up
   ```

3. **Access the Application**
   - Main App: http://localhost:8000
   - Admin Panel: http://localhost:8000/admin
   - Login: admin / admin123

### Detailed Setup Process

#### Step 1: Environment Preparation

```bash
# Clone repository
git clone <repository-url>
cd trading_card_project

# Verify Docker installation
docker --version
docker-compose --version

# Make scripts executable
chmod +x docker-scripts.sh
```

#### Step 2: Configuration (Optional)

Create custom environment file:
```bash
cp env.example .env
# Edit .env with your preferred settings
```

#### Step 3: Build and Run

```bash
# Option 1: Using management script (recommended)
./docker-scripts.sh dev-up

# Option 2: Direct Docker Compose
docker-compose -f docker-compose.dev.yml up --build

# Option 3: Production setup
./docker-scripts.sh prod-up
```

#### Step 4: Verify Installation

1. **Check containers are running**:
   ```bash
   docker-compose -f docker-compose.dev.yml ps
   ```

2. **View logs**:
   ```bash
   ./docker-scripts.sh logs
   ```

3. **Test the application**:
   - Navigate to http://localhost:8000
   - You should see the cyber-themed homepage
   - Try logging in with admin/admin123

## 🏗️ Development Setup

### Local Development (Without Docker)

If you prefer local development:

```bash
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
```

### Development Tools

**Recommended VS Code Extensions**:
- Python
- Django
- Docker
- HTML CSS Support
- Auto Rename Tag
- Prettier

**Browser Developer Tools**:
- Chrome DevTools for debugging
- Vue.js devtools for Alpine.js
- Network tab for HTMX requests

### Hot Reloading

The Docker development setup includes hot reloading:
- **Python files**: Auto-reload on change
- **Templates**: Instant updates
- **Static files**: Collected automatically
- **Database**: Persistent across restarts

## 📁 Project Structure

```
trading_card_project/
├── 📁 cards/                          # Main Django app
│   ├── 📁 management/
│   │   └── 📁 commands/
│   │       └── 📄 seed.py             # Database seeding
│   ├── 📁 migrations/                 # Database migrations
│   ├── 📁 static/cards/
│   │   ├── 📁 css/
│   │   │   └── 📄 vault-theme.css     # Main stylesheet (695 lines)
│   │   └── 📁 images/                 # Card images
│   ├── 📁 templates/cards/
│   │   ├── 📄 base.html               # Base template with particles
│   │   ├── 📄 homepage.html           # Landing page (508 lines)
│   │   ├── 📄 card_list.html          # Card collection view
│   │   ├── 📄 card_detail.html        # Individual card view
│   │   └── 📁 partials/
│   │       └── 📄 card_grid.html      # HTMX partial
│   ├── 📄 models.py                   # Data models
│   ├── 📄 views.py                    # View logic
│   ├── 📄 urls.py                     # URL routing
│   └── 📄 admin.py                    # Admin configuration
├── 📁 trading_card_project/           # Django project settings
│   ├── 📄 settings.py                 # Configuration (192 lines)
│   ├── 📄 urls.py                     # Root URL config
│   └── 📄 wsgi.py                     # WSGI application
├── 📁 staticfiles/                    # Collected static files
├── 📁 media/                          # User uploads
├── 🐳 Dockerfile                      # Container definition
├── 🐳 docker-compose.yml             # Production setup
├── 🐳 docker-compose.dev.yml         # Development setup
├── 🌐 nginx.conf                      # Nginx configuration
├── 📄 requirements.txt                # Python dependencies
├── 📄 docker-scripts.sh               # Management scripts
├── 📄 env.example                     # Environment template
└── 📄 README.md                       # This file
```

### Key Files Explained

#### `cards/models.py`
```python
class Card(models.Model):
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=20, choices=RARITY_CHOICES)
    image = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class UserCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
```

#### `cards/views.py`
```python
@login_required
def card_list(request):
    """Main card collection view with search functionality"""
    
def search_cards(request):
    """HTMX endpoint for real-time search"""
    
def card_detail(request, card_id):
    """Individual card detail view"""
    
def homepage(request):
    """Landing page with feature demonstrations"""
```

## 🗄️ Database Schema

### Entity Relationship Diagram

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│      User       │    │ UserCollection  │    │      Card       │
├─────────────────┤    ├─────────────────┤    ├─────────────────┤
│ id (PK)         │◄──┤ user_id (FK)    │   ┌┤ id (PK)         │
│ username        │    │ card_id (FK)    ├──►│ name            │
│ email           │    │ quantity        │    │ rarity          │
│ password        │    │ created_at      │    │ image           │
│ is_staff        │    └─────────────────┘    │ description     │
│ date_joined     │                           │ created_at      │
└─────────────────┘                           └─────────────────┘
```

### Database Migrations

```bash
# Create new migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# View migration status
python manage.py showmigrations
```

### Sample Data

The `seed` command creates:
- **Admin user**: username=admin, password=admin123
- **Sample cards**: 5 trading cards with images
- **Rarity distribution**: Common cards for testing

## 🎨 Frontend Architecture

### CSS Architecture

The styling system uses a modular approach:

```css
/* 1. CSS Custom Properties (Variables) */
:root {
    --primary-color: #00d4ff;
    --secondary-color: #8b5cf6;
    --accent-color: #00ff88;
    --bg-dark: #0a0a0a;
    --card-width: 280px;
    --card-height: 420px;
}

/* 2. Base Styles */
.vault-theme { /* Global theme application */ }

/* 3. Component Styles */
.vault-card { /* Individual card styling */ }
.vault-grid { /* Grid layout system */ }
.vault-navbar { /* Navigation styling */ }

/* 4. Animation Definitions */
@keyframes floatCard { /* Floating animation */ }
@keyframes shimmer { /* Shimmer effect */ }
@keyframes epicPulse { /* Epic card glow */ }

/* 5. Responsive Breakpoints */
@media (max-width: 768px) { /* Tablet styles */ }
@media (max-width: 480px) { /* Mobile styles */ }
```

### Alpine.js Integration

Alpine.js provides reactive functionality:

```html
<!-- Card flip functionality -->
<div x-data="{ flipped: false }" 
     @click="flipped = !flipped"
     :class="{ 'flipped': flipped }">

<!-- Search state management -->
<div x-data="{ searching: false }" 
     @htmx:before-request="searching = true"
     @htmx:after-request="searching = false">
```

### HTMX Implementation

HTMX enables AJAX interactions:

```html
<!-- Real-time search -->
<input hx-get="/cards/search/" 
       hx-target="#card-grid" 
       hx-trigger="keyup changed delay:300ms">

<!-- Infinite scroll (future feature) -->
<div hx-get="/cards/load-more/" 
     hx-trigger="revealed" 
     hx-swap="afterend">
```

## 🔧 Backend Architecture

### Django Apps Structure

```python
# cards/apps.py
class CardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cards'
```

### URL Routing

```python
# trading_card_project/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('cards.urls')),
]

# cards/urls.py
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('cards/', views.card_list, name='card_list'),
    path('cards/<int:card_id>/', views.card_detail, name='card_detail'),
    path('cards/search/', views.search_cards, name='search_cards'),
]
```

### View Patterns

```python
# Function-based views with decorators
@login_required
def card_list(request):
    cards = Card.objects.all()
    return render(request, 'cards/card_list.html', {'cards': cards})

# HTMX partial views
def search_cards(request):
    query = request.GET.get('search', '')
    cards = Card.objects.filter(name__icontains=query)
    return render(request, 'cards/partials/card_grid.html', {'cards': cards})
```

### Model Patterns

```python
class Card(models.Model):
    RARITY_CHOICES = [
        ('common', 'Common'),
        ('uncommon', 'Uncommon'),
        ('rare', 'Rare'),
        ('epic', 'Epic'),
        ('legendary', 'Legendary'),
    ]
    
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=20, choices=RARITY_CHOICES)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
```

## 📡 API Documentation

### Search Endpoint

**URL**: `/cards/search/`
**Method**: GET
**Purpose**: Real-time card search

**Parameters**:
```
search (string): Search query for card names/descriptions
```

**Response**: HTML partial (card grid)

**Example**:
```bash
curl "http://localhost:8000/cards/search/?search=dragon"
```

### Future API Endpoints

Planned REST API endpoints:

```python
# api/urls.py (future)
urlpatterns = [
    path('api/cards/', CardListAPIView.as_view()),
    path('api/cards/<int:pk>/', CardDetailAPIView.as_view()),
    path('api/collections/', UserCollectionAPIView.as_view()),
]
```

## 🎨 Styling & Theming

### Color Palette

```css
:root {
    /* Primary Colors */
    --neon-blue: #00d4ff;
    --neon-purple: #8b5cf6;
    --neon-green: #00ff88;
    
    /* Background Colors */
    --bg-primary: #0a0a0a;
    --bg-secondary: #1a1a1a;
    --bg-tertiary: #2a2a2a;
    
    /* Text Colors */
    --text-primary: #ffffff;
    --text-secondary: #b0b0b0;
    --text-accent: #00d4ff;
}
```

### Typography

```css
/* Font Families */
--font-primary: 'Orbitron', monospace;  /* Headers */
--font-secondary: 'Rajdhani', sans-serif;  /* Body text */

/* Font Sizes */
--text-xs: 0.75rem;
--text-sm: 0.875rem;
--text-base: 1rem;
--text-lg: 1.125rem;
--text-xl: 1.25rem;
--text-2xl: 1.5rem;
--text-3xl: 1.875rem;
```

### Animation System

```css
/* Timing Functions */
--ease-out-cubic: cubic-bezier(0.4, 0.0, 0.2, 1);
--ease-in-out-cubic: cubic-bezier(0.4, 0.0, 0.6, 1);

/* Animation Durations */
--duration-fast: 0.15s;
--duration-normal: 0.3s;
--duration-slow: 0.6s;

/* Transform Origins */
--transform-card-flip: rotateY(180deg);
--transform-hover-lift: translateY(-10px) scale(1.05);
```

### Responsive Design Tokens

```css
/* Breakpoints */
--breakpoint-sm: 480px;
--breakpoint-md: 768px;
--breakpoint-lg: 1024px;
--breakpoint-xl: 1200px;

/* Container Sizes */
--container-sm: 100%;
--container-md: 768px;
--container-lg: 1024px;
--container-xl: 1200px;
```

## 🧪 Testing

### Test Structure

```bash
# Create test files
cards/tests/
├── __init__.py
├── test_models.py
├── test_views.py
├── test_forms.py
└── test_utils.py
```

### Model Tests

```python
# cards/tests/test_models.py
from django.test import TestCase
from cards.models import Card

class CardModelTest(TestCase):
    def setUp(self):
        self.card = Card.objects.create(
            name="Test Card",
            rarity="common",
            image="test.jpg",
            description="Test description"
        )
    
    def test_card_creation(self):
        self.assertEqual(self.card.name, "Test Card")
        self.assertEqual(self.card.rarity, "common")
    
    def test_string_representation(self):
        self.assertEqual(str(self.card), "Test Card")
```

### View Tests

```python
# cards/tests/test_views.py
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class CardViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
    
    def test_card_list_requires_login(self):
        response = self.client.get(reverse('card_list'))
        self.assertEqual(response.status_code, 302)
    
    def test_card_list_with_login(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('card_list'))
        self.assertEqual(response.status_code, 200)
```

### Running Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test cards

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html
```

### Frontend Testing

```javascript
// Test Alpine.js functionality
describe('Card Flip Functionality', () => {
    test('card flips on click', () => {
        // Test implementation
    });
});

// Test HTMX interactions
describe('Search Functionality', () => {
    test('search updates results', () => {
        // Test implementation
    });
});
```

## 🚀 Deployment

### Production Environment Variables

```bash
# Required for production
export DEBUG=0
export SECRET_KEY="your-super-secret-production-key"
export ALLOWED_HOSTS="yourdomain.com,www.yourdomain.com"
export DATABASE_URL="postgresql://user:pass@host:5432/dbname"
```

### Docker Production Deployment

```bash
# Build production images
docker-compose build

# Deploy with production settings
docker-compose up -d

# Check deployment status
docker-compose ps
docker-compose logs web
```

### SSL/HTTPS Setup

Update `nginx.conf` for SSL:

```nginx
server {
    listen 443 ssl http2;
    server_name yourdomain.com;
    
    ssl_certificate /path/to/certificate.crt;
    ssl_certificate_key /path/to/private.key;
    
    # SSL configuration
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512;
    
    # Rest of configuration...
}
```

### Performance Optimization

```python
# settings.py production optimizations
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'CONN_MAX_AGE': 600,
        'OPTIONS': {
            'MAX_CONNS': 20,
        }
    }
}

# Cache configuration
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}

# Static files optimization
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

## 🤝 Contributing Guidelines

### Development Workflow

1. **Fork the Repository**
   ```bash
   git clone https://github.com/yourusername/trading_card_project.git
   cd trading_card_project
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Set Up Development Environment**
   ```bash
   ./docker-scripts.sh dev-up
   ```

4. **Make Changes**
   - Follow coding standards
   - Add tests for new features
   - Update documentation

5. **Test Your Changes**
   ```bash
   python manage.py test
   ./docker-scripts.sh logs  # Check for errors
   ```

6. **Commit and Push**
   ```bash
   git add .
   git commit -m "feat: add new feature description"
   git push origin feature/your-feature-name
   ```

7. **Create Pull Request**
   - Describe your changes
   - Reference any issues
   - Include screenshots for UI changes

### Coding Standards

#### Python/Django

```python
# Follow PEP 8
# Use type hints where appropriate
def search_cards(request: HttpRequest) -> HttpResponse:
    """Search cards based on query parameters."""
    
# Use descriptive variable names
user_collection = UserCollection.objects.filter(user=request.user)

# Add docstrings to functions and classes
class Card(models.Model):
    """Represents a trading card in the collection."""
```

#### HTML/Templates

```html
<!-- Use semantic HTML -->
<main class="container">
    <section class="card-collection">
        <header class="collection-header">
            <h1>My Collection</h1>
        </header>
    </section>
</main>

<!-- Follow Django template conventions -->
{% load static %}
{% block content %}
    <!-- Content here -->
{% endblock %}
```

#### CSS

```css
/* Use BEM methodology */
.vault-card {}
.vault-card__header {}
.vault-card__body {}
.vault-card--flipped {}

/* Use CSS custom properties */
.vault-card {
    width: var(--card-width);
    height: var(--card-height);
}

/* Mobile-first responsive design */
.vault-grid {
    display: grid;
    grid-template-columns: 1fr;
}

@media (min-width: 768px) {
    .vault-grid {
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    }
}
```

#### JavaScript

```javascript
// Use modern ES6+ syntax
const initializeParticles = () => {
    // Implementation
};

// Use descriptive function names
const handleCardFlip = (event) => {
    // Implementation
};

// Add comments for complex logic
// Initialize particle system with cyber theme colors
particlesJS('particles-js', particleConfig);
```

### Commit Message Convention

Use conventional commits:

```
feat: add new card rarity system
fix: resolve card flip animation on mobile
docs: update API documentation
style: improve card hover effects
refactor: optimize database queries
test: add unit tests for card model
chore: update dependencies
```

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] Added tests for new functionality
- [ ] Manual testing completed

## Screenshots
(If applicable)

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No console errors
```

### Issue Templates

#### Bug Report
```markdown
**Describe the bug**
A clear description of the bug

**To Reproduce**
Steps to reproduce the behavior

**Expected behavior**
What you expected to happen

**Screenshots**
If applicable, add screenshots

**Environment:**
- OS: [e.g. macOS]
- Browser: [e.g. Chrome]
- Version: [e.g. 22]
```

#### Feature Request
```markdown
**Is your feature request related to a problem?**
A clear description of the problem

**Describe the solution you'd like**
A clear description of what you want to happen

**Additional context**
Any other context about the feature request
```

## 🔧 Troubleshooting

### Common Issues

#### 1. Docker Build Fails

**Problem**: Docker build fails with dependency errors

**Solution**:
```bash
# Clear Docker cache
docker system prune -a

# Rebuild without cache
docker-compose build --no-cache

# Check Docker version
docker --version  # Should be 20.10+
```

#### 2. Database Connection Issues

**Problem**: Can't connect to PostgreSQL

**Solution**:
```bash
# Check database container status
docker-compose ps

# View database logs
docker-compose logs db

# Reset database
./docker-scripts.sh reset
```

#### 3. Static Files Not Loading

**Problem**: CSS/JS files return 404

**Solution**:
```bash
# Collect static files
docker-compose exec web python manage.py collectstatic --noinput

# Check static files directory
docker-compose exec web ls -la /app/staticfiles/

# Verify STATIC_URL setting
docker-compose exec web python manage.py shell -c "from django.conf import settings; print(settings.STATIC_URL)"
```

#### 4. Admin User Login Issues

**Problem**: Can't login with admin/admin123

**Solution**:
```bash
# Create admin user manually
docker-compose exec web python manage.py createsuperuser

# Reset admin password
docker-compose exec web python manage.py shell -c "
from django.contrib.auth.models import User;
user = User.objects.get(username='admin');
user.set_password('admin123');
user.save();
print('Password reset successfully')
"
```

#### 5. Particle Effects Not Working

**Problem**: Background particles don't appear

**Solution**:
1. Check browser console for JavaScript errors
2. Verify particles.js is loaded:
   ```javascript
   // In browser console
   console.log(typeof particlesJS);  // Should be 'function'
   ```
3. Check network tab for failed resource loads
4. Ensure particles-js div exists in template

#### 6. Card Flip Animation Issues

**Problem**: Cards don't flip on click

**Solution**:
1. Verify Alpine.js is loaded:
   ```javascript
   // In browser console
   console.log(typeof Alpine);  // Should be 'object'
   ```
2. Check for CSS conflicts:
   ```css
   /* Ensure transform-style is preserved */
   .vault-card {
       transform-style: preserve-3d;
   }
   ```
3. Test on different browsers

#### 7. HTMX Search Not Working

**Problem**: Search doesn't update results

**Solution**:
1. Check HTMX is loaded:
   ```javascript
   // In browser console
   console.log(typeof htmx);  // Should be 'object'
   ```
2. Verify search endpoint:
   ```bash
   curl "http://localhost:8000/cards/search/?search=test"
   ```
3. Check network tab for AJAX requests

### Performance Issues

#### Slow Page Load

**Diagnosis**:
```bash
# Check container resources
docker stats

# Monitor database queries
docker-compose exec web python manage.py shell -c "
from django.db import connection;
print(len(connection.queries))
"
```

**Solutions**:
- Enable database query optimization
- Implement caching
- Optimize images
- Use CDN for static files

#### High Memory Usage

**Diagnosis**:
```bash
# Check memory usage
docker-compose exec web free -h

# Monitor Python memory
docker-compose exec web python -c "
import psutil;
print(f'Memory: {psutil.virtual_memory().percent}%')
"
```

**Solutions**:
- Implement pagination
- Optimize database queries
- Use lazy loading for images
- Configure proper cache settings

### Development Environment Issues

#### Hot Reload Not Working

**Solution**:
```bash
# Ensure volume mounting is correct
docker-compose -f docker-compose.dev.yml config

# Check file permissions
ls -la

# Restart development server
./docker-scripts.sh dev-down
./docker-scripts.sh dev-up
```

#### Port Conflicts

**Problem**: Port 8000 already in use

**Solution**:
```bash
# Find process using port
lsof -i :8000

# Kill process
kill -9 <PID>

# Or use different port
# Edit docker-compose.dev.yml ports section
```

### Getting Help

1. **Check Logs First**:
   ```bash
   ./docker-scripts.sh logs
   ```

2. **Search Issues**: Check GitHub issues for similar problems

3. **Create Detailed Bug Report**: Include:
   - Steps to reproduce
   - Error messages
   - Environment details
   - Screenshots

4. **Join Community**: Participate in discussions and help others

---

## 📚 Additional Resources

### Learning Resources

- **Django Documentation**: https://docs.djangoproject.com/
- **Alpine.js Guide**: https://alpinejs.dev/
- **HTMX Documentation**: https://htmx.org/docs/
- **Bootstrap Documentation**: https://getbootstrap.com/docs/
- **Docker Documentation**: https://docs.docker.com/

### Useful Tools

- **Django Debug Toolbar**: For development debugging
- **Django Extensions**: Additional management commands
- **Pre-commit Hooks**: Code quality enforcement
- **Black**: Python code formatting
- **Flake8**: Python linting

### Community

- **Django Community**: https://www.djangoproject.com/community/
- **Stack Overflow**: Tag questions with `django`, `htmx`, `alpine.js`
- **GitHub Discussions**: Project-specific discussions

---

**Happy coding! 🚀**

*This documentation is maintained by the development team. Please keep it updated as the project evolves.* 