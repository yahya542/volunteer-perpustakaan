# API Permission Documentation

## Overview

This document explains the permission system implemented in the Library Management API. The system has been designed to allow public read access to bibliographic data while requiring authentication for operations involving loans, reservations, and fines.

## Permission Classes

### 1. ReadOnlyOrAuthenticated
- **Purpose**: Used for bibliographic data (books) and items
- **Behavior**: 
  - Allows read-only access (GET, HEAD, OPTIONS) to everyone
  - Requires authentication for write operations (POST, PUT, PATCH, DELETE)
- **Applied to**: 
  - BiblioViewSet (bibliography data)
  - ItemViewSet (library items)

### 2. LoanPermission
- **Purpose**: Used for loan operations
- **Behavior**: 
  - Requires authentication for all operations
- **Applied to**: 
  - LoanViewSet (loan transactions)

### 3. ReservePermission
- **Purpose**: Used for reservation operations
- **Behavior**: 
  - Requires authentication for all operations
- **Applied to**: 
  - ReserveViewSet (book reservations)

### 4. FinePermission
- **Purpose**: Used for fine operations
- **Behavior**: 
  - Requires authentication for all operations
- **Applied to**: 
  - FinesViewSet (library fines)

## Implementation Details

### Default Permissions
The API is configured with `AllowAny` as the default permission class in `settings.py`. This means that unless explicitly overridden in a ViewSet, all endpoints will be publicly accessible.

### Override Pattern
Each ViewSet specifies its own permission classes using the `permission_classes` attribute:

```python
class LoanViewSet(viewsets.ModelViewSet):
    permission_classes = [LoanPermission]
```

### How Authentication Works
- Authentication is handled via JWT tokens
- Users must obtain a token by logging in through the `/auth/login/` endpoint
- Tokens must be included in the Authorization header as `Bearer {token}`

## API Access Summary

| Endpoint | Read Access | Write Access | Authentication Required |
|----------|-------------|--------------|-------------------------|
| `/api/biblio/` | Public | Authenticated | Write only |
| `/api/items/` | Public | Authenticated | Write only |
| `/api/loans/` | Authenticated | Authenticated | Yes |
| `/api/reserves/` | Authenticated | Authenticated | Yes |
| `/api/fines/` | Authenticated | Authenticated | Yes |

## Testing Authentication

To test endpoints that require authentication:

1. Register a user: `POST /auth/register/`
2. Verify email: `POST /auth/verify-token/`
3. Login: `POST /auth/login/`
4. Use the returned token in the Authorization header:
   ```
   Authorization: Bearer {your_token_here}
   ```

## Master Data Access
Master data endpoints (publishers, authors, topics, etc.) inherit the default `AllowAny` permission, making them publicly accessible for read operations.