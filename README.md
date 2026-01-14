# Elevate Backend

## Overview
Elevate Backend is a FastAPI-based application for managing and serving backend services.
The goal of this Backend is be used in the Elevate Frontend.
This app contains interaction with three APIs:

**Employee Management API** (Created with FastAPI)
- Full CRUD operations for employees with relationships
- Manage job positions, nationalities, and seniority levels
- Search employees by name or last name
- Filter by job, country, or seniority level
- Includes authentication via JWT tokens

**Jokes API** (External Integration)
- Fetches random jokes from the Italian Jokes API
- Supports multiple joke subtypes: One-liner, Observational, Wordplay, Long, and Stereotype
- Provides a single random joke endpoint for variety

**Harry Potter API** (External Integration)
- Query three main data sources:
  - **Books**: Search and retrieve all Harry Potter books with metadata
  - **Characters**: Find characters by name with detailed information
  - **Spells**: Browse and search magical spells from the Harry Potter universe

## Setup

### Prerequisites
- Python 3.9+
- pip

### Installation

1. Create a virtual environment:
```bash
python -m venv .venv
```

2. Activate the virtual environment:
```bash
# On Linux/macOS
source .venv/bin/activate

# On Windows
.venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
# Or create the .venv with the VS Code tool including the requirements
```

## Environment Variables
Create a .env file with this content:
```bash
SECRET_KEY="GENERIC_SECRET_KEY_FOR_DEVELOPMENT_PURPOSES_ONLY"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

## Running the Application

Start the development server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

For API documentation, visit `http://localhost:8000/docs`

## Technical Information

### Core Technologies

- **FastAPI** - Modern, fast web framework for building APIs with Python
- **SQLAlchemy** - SQL toolkit and Object-Relational Mapping (ORM) library
- **SQLite** - Lightweight, file-based relational database
- **Uvicorn** - ASGI web server for running FastAPI applications
- **Alembic** - Database migration tool for SQLAlchemy

### Authentication & Security

- **python-jose** - Implementation of JOSE (JavaScript Object Signing and Encryption)
- **passlib** - Password hashing library with bcrypt support
- **bcrypt** - Secure password hashing algorithm
- **python-multipart** - Multipart form data parsing

### Additional Libraries

- **python-dotenv** - Load environment variables from .env files
- **requests** - HTTP library for making external API calls
- **pydantic** - Data validation using Python type annotations
- **pytest** - Testing framework for unit and integration tests

### External APIs Integrated

- **Jokes API** - Provides random jokes with different subtypes ["https://italian-jokes.vercel.app"]
- **Harry Potter API** - Provides Harry Potter books, characters, and spells data ["https://potterapi-fedeperin.vercel.app/en"]

### API Authentication

The API uses **OAuth2 with JWT tokens**. Most endpoints require authentication via Bearer token obtained from the `/auth/token` endpoint.

### Testing

Run tests with:
```bash
pytest
```