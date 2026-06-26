# 🎬 Movie Library Management System

A RESTful Movie Library Management API built with **FastAPI**, **SQLAlchemy**, and **SQLite**. The application supports secure user authentication using **JWT**, role-based authorization for **Admin** and **Consumer** users, and allows users to manage and rent movies.

---

# Features

## Authentication

* User Registration
* Secure Password Hashing using **Argon2**
* JWT-based Authentication
* OAuth2 Password Flow
* Protected Routes

---

## Role-Based Access Control (RBAC)

### Admin

* Create Movies
* Update Movies
* Delete Movies

### Consumer

* Rent Movies
* Return Movies
* View Personal Rental History

---

## Movie Management

* Add New Movie
* View All Movies
* View Movie by ID
* Update Movie Details
* Delete Movie
* Track Movie Availability

---

## Rental Management

* Rent Available Movies
* Return Rented Movies
* Maintain Rental History
* Automatic Movie Availability Update

---

# Tech Stack

| Technology      | Purpose                     |
| --------------- | --------------------------- |
| FastAPI         | REST API Framework          |
| SQLAlchemy      | ORM                         |
| SQLite          | Database                    |
| Pydantic        | Request Validation          |
| JWT             | Authentication              |
| OAuth2          | Authorization               |
| Argon2 (pwdlib) | Password Hashing            |
| Uvicorn         | ASGI Server                 |
| Swagger UI      | API Documentation & Testing |

---

# Project Structure

```text
movie_library/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── oauth2.py
├── utils.py
├── movies.db
├── requirements.txt
└── README.md
```

---

# Database Schema

## Users

| Field    | Type            |
| -------- | --------------- |
| id       | Integer         |
| username | String          |
| password | String (Hashed) |
| role     | String          |

---

## Movies

| Field     | Type    |
| --------- | ------- |
| id        | Integer |
| title     | String  |
| director  | String  |
| genre     | String  |
| year      | Integer |
| available | Boolean |

---

## Rentals

| Field       | Type              |
| ----------- | ----------------- |
| id          | Integer           |
| user_id     | Integer           |
| movie_id    | Integer           |
| rent_date   | String            |
| return_date | String (Nullable) |

---

# API Endpoints

## Authentication

### Register

```
POST /register
```

Creates a new consumer account with a securely hashed password.

---

### Login

```
POST /token
```

Authenticates the user and returns a JWT access token.

---

## User

### Current User

```
GET /me
```

Returns information about the currently authenticated user.

---

## Movies

### Create Movie (Admin)

```
POST /movies
```

---

### Get All Movies (Public)

```
GET /movies
```

---

### Get Movie By ID (Public)

```
GET /movies/{id}
```

---

### Update Movie (Admin)

```
PUT /movies/{id}
```

---

### Delete Movie (Admin)

```
DELETE /movies/{id}
```

---

## Rentals

### Rent Movie

```
POST /movies/{id}/rent
```

Allows authenticated consumers to rent an available movie.

---

### Return Movie

```
POST /movies/{id}/return
```

Returns a previously rented movie and updates its availability.

---

### My Rentals

```
GET /users/me/rentals
```

Returns the rental history of the authenticated user.

---

# Authentication Flow

```
User Login
      │
      ▼
Verify Username & Password
      │
      ▼
Generate JWT Token
      │
      ▼
Client Stores Token
      │
      ▼
Protected API Requests
      │
      ▼
Token Verification
      │
      ▼
Authorized Access
```

---

# Authorization

| Endpoint        | Admin | Consumer |
| --------------- | :---: | :------: |
| Register        |   ✅   |     ✅    |
| Login           |   ✅   |     ✅    |
| Get Movies      |   ✅   |     ✅    |
| Get Movie       |   ✅   |     ✅    |
| Create Movie    |   ✅   |     ❌    |
| Update Movie    |   ✅   |     ❌    |
| Delete Movie    |   ✅   |     ❌    |
| Rent Movie      |   ❌   |     ✅    |
| Return Movie    |   ❌   |     ✅    |
| View My Rentals |   ❌   |     ✅    |

---

# Security Features

* Argon2 Password Hashing
* JWT Authentication
* OAuth2 Password Flow
* Protected Endpoints
* Role-Based Authorization
* Password Verification
* Secure User Authentication

---

# How to Run

## Clone Repository

```bash
git clone <repository-url>
cd movie_library
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Server

```bash
uvicorn main:app --reload
```

---

## Open Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# Sample Workflow

1. Register a user.
2. Login to receive a JWT token.
3. Authorize using Swagger.
4. Admin creates movies.
5. Consumer rents a movie.
6. Consumer views rental history.
7. Consumer returns the movie.
8. Movie becomes available again.

---

# Learning Outcomes

This project demonstrates practical implementation of:

* RESTful API Development
* FastAPI Framework
* SQLAlchemy ORM
* SQLite Database Management
* JWT Authentication
* OAuth2 Authorization
* Password Hashing using Argon2
* Role-Based Access Control (RBAC)
* CRUD Operations
* Database Relationships
* Secure Backend Development

---

# Future Improvements

The next version of this project will include:

* PostgreSQL Integration
* Alembic Database Migrations
* Modular Router Architecture
* Service & Repository Pattern
* Environment Variables (.env)
* Docker Support
* Search & Filtering
* Pagination & Sorting
* Unit Testing with Pytest
* Deployment on Cloud Platforms

---

# Author

**Samyak Rawat**

Backend Developer | AI & Software Engineering Enthusiast
