# API Design

## 1. API Overview

The backend API will be implemented using FastAPI.

The API will follow REST-oriented conventions and use JSON
for request and response payloads unless a different protocol
is required.

The API base path will be:

    /api/v1

Versioning the API allows future versions to be introduced
without immediately breaking existing clients.

---

## 2. Authentication

### POST /api/v1/auth/login

Authenticates a user.

Request:

```json
{
  "email": "employee@example.com",
  "password": "password"
}