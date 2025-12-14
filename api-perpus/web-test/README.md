# Web API Testing Interface

This is a simple web interface for testing the Library Management System API endpoints.

## Setup Instructions

1. Make sure the Django API server is running on `http://localhost:8000`
2. Open `index.html` in a web browser
3. For endpoints that require authentication, login first using a valid user account

## Available Tests

### Authentication
- Login with username (NIK) and password
- Stores the JWT token for subsequent authenticated requests

### Bibliography Endpoints
- Get all books (`/api/biblio/`)
- Get book by ID (`/api/biblio/{id}/`)
- Search books by term (`/api/biblio/?search={term}`)

### Publisher Endpoints
- Get all publishers (`/api/publishers/`)

### Author Endpoints
- Get all authors (`/api/authors/`)

## How to Use

1. **For public endpoints** (like getting all books):
   - Simply click the corresponding button
   
2. **For protected endpoints**:
   - First login using the Authentication section
   - Then click the buttons for protected endpoints

3. **For endpoints requiring parameters**:
   - Fill in the required fields (e.g., Book ID, Search term)
   - Click the corresponding button

## Results Display

- Success responses are displayed with green background
- Error responses are displayed with red background
- All JSON responses are formatted for readability

## Troubleshooting

1. If you get CORS errors, make sure the Django server has CORS configured properly
2. If authentication fails, verify the username and password are correct
3. If endpoints return 404 errors, check that the IDs exist in the database