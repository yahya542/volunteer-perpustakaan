# Perpustakaan API - Postman Testing Guide

## Konfigurasi Dasar Postman

```
Base URL: http://localhost:8000 (sesuaikan dengan port Django Anda)
Headers:
  Content-Type: application/json
  Authorization: Bearer {token} (untuk endpoint yang memerlukan autentikasi)
```

---

## 1. AUTHENTICATION ENDPOINTS

### Register User
```
Method: POST
URL: http://localhost:8000/auth/register/
```

**Request Body:**
```json
{
  "nama": "John Doe",
  "nik": "1234567890123456",
  "tempat_lahir": "Jakarta",
  "tanggal_lahir": "1990-05-15",
  "institusi": "Universitas Indonesia",
  "tipe_keanggotaan": "Mahasiswa",
  "jenis_kelamin": "L",
  "alamat": "Jl. Sudirman No. 123, Jakarta",
  "nomor_hp": "081234567890",
  "email": "john.doe@example.com",
  "password": "password123",
  "konfirmasi_password": "password123",
  "foto_diri": "",
  "foto_ktp": ""
}
```

**Expected Response:**
```json
{
  "message": "User created successfully"
}
```

**Catatan**: Setelah register, sistem akan mengirim email verifikasi. User harus verifikasi email terlebih dahulu sebelum bisa login.

## 📧 **Status Email Saat Ini:**
**Console Backend** - Email ditampilkan di terminal Django (untuk development)

## 🔄 **Untuk Mengirim Email ke Inbox User:**
1. Buka `backend/settings.py`
2. Comment out: `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`
3. Uncomment blok SMTP Gmail
4. Restart Django server
5. Email akan dikirim ke inbox user sesungguhnya!

### Verify Email Token
```
Method: POST
URL: http://localhost:8000/auth/verify-token/
```

**Request Body:**
```json
{
  "email": "john.doe@example.com",
  "token": "123456"
}
```

**Catatan**: Token adalah kode 6-digit yang dikirim ke email Anda.

**Expected Response:**
```json
{
  "message": "Email verified successfully! Your account is now active.",
  "member_id": "1234567890123456",
  "username": "1234567890123456"
}
```

### Login User
```
Method: POST
URL: http://localhost:8000/auth/login/
```

**Request Body:**
```json
{
  "username": "1234567890123456",
  "password": "password123"
}
```

**Expected Response:**
```json
{
  "message": "Login successful",
  "username": "1234567890123456"
}
```

**Catatan**: Username menggunakan NIK yang diinput saat register. Sistem akan membuat record Member dan User secara bersamaan saat registrasi.

---

## 2. USER MANAGEMENT ENDPOINTS

### List All Members
```
Method: GET
URL: http://localhost:8000/user/members/
```

### Create New Member
```
Method: POST
URL: http://localhost:8000/user/members/
```

**Request Body:**
```json
{
  "member_id": "MEM1234567890",
  "member_name": "Jane Smith",
  "gender": 2,
  "birth_date": "1992-08-20",
  "birth_place": "Bandung",
  "member_type_id": 1,
  "member_address": "Jl. Malioboro No. 45, Yogyakarta",
  "member_email": "jane.smith@example.com",
  "inst_name": "Universitas Gadjah Mada",
  "member_phone": "081987654321",
  "member_image": "",
  "ktp_image": "",
  "mpasswd": "hashed_password_here",
  "register_date": "2024-01-15",
  "expire_date": "2025-01-15"
}
```

### Member Check-in
```
Method: POST
URL: http://localhost:8000/user/members/{member_id}/check_in/
```

---

## 3. LIBRARY MANAGEMENT ENDPOINTS

### Create Bibliography
```
Method: POST
URL: http://localhost:8000/api/biblio/
```

**Request Body:**
```json
{
  "title": "Introduction to Computer Science",
  "isbn_issn": "978-0123456789",
  "publisher_id": 1,
  "publish_year": "2023",
  "collation": "450 pages",
  "notes": "A comprehensive guide to computer science fundamentals",
  "gmd_id": 1,
  "language_id": "en"
}
```

### Create Library Item
```
Method: POST
URL: http://localhost:8000/api/items/
```

**Request Body:**
```json
{
  "biblio_id": 1,
  "item_code": "CS001-001",
  "call_number": "005.1 SMI",
  "coll_type_id": 1,
  "location_id": "001",
  "item_status_id": "001",
  "supplier_id": "SUP001",
  "order_date": "2024-01-01",
  "received_date": "2024-01-15",
  "price": 150000,
  "price_currency": "IDR"
}
```

### Loan an Item
```
Method: POST
URL: http://localhost:8000/api/items/{item_id}/loan/
```

**Request Body:**
```json
{
  "member_id": "MEM1234567890",
  "loan_date": "2024-09-16",
  "due_date": "2024-09-30"
}
```

### Return Loaned Item
```
Method: POST
URL: http://localhost:8000/api/loans/{loan_id}/return_item/
```

**Request Body:**
```json
{
  "return_date": "2024-09-20"
}
```

---

## 4. MASTER DATA ENDPOINTS

### Create Publisher
```
Method: POST
URL: http://localhost:8000/api/publishers/
```

**Request Body:**
```json
{
  "publisher_name": "Gramedia Pustaka Utama",
  "publisher_address": "Jl. Palmerah Barat 29-37, Jakarta",
  "publisher_phone": "021-53650110",
  "publisher_email": "contact@gramedia.com",
  "publisher_website": "https://www.gramedia.com"
}
```

### Create Author
```
Method: POST
URL: http://localhost:8000/api/authors/
```

**Request Body:**
```json
{
  "author_name": "Pramoedya Ananta Toer",
  "author_birth_date": "1925-02-06",
  "author_death_date": "2006-04-30",
  "author_description": "Indonesian author and writer",
  "author_photo": ""
}
```

### Create Topic/Subject
```
Method: POST
URL: http://localhost:8000/api/topics/
```

**Request Body:**
```json
{
  "topic": "Computer Programming",
  "topic_type": "subject",
  "classification": "005.1"
}
```

---

## 5. SYSTEM MANAGEMENT ENDPOINTS

### Create User (Admin)
```
Method: POST
URL: http://localhost:8000/auth/users/
```

**Request Body:**
```json
{
  "username": "admin",
  "realname": "Administrator",
  "passwd": "admin123",
  "email": "admin@library.com",
  "user_type": 0,
  "user_image": "",
  "social_media": "",
  "last_login_ip": "",
  "groups": "1",
  "forgot": "",
  "admin_template": ""
}
```

### Change User Password
```
Method: POST
URL: http://localhost:8000/auth/users/{user_id}/change_password/
```

**Request Body:**
```json
{
  "old_password": "oldpassword123",
  "new_password": "newpassword123"
}
```

---

## 6. CONTOH COLLECTION POSTMAN

### Environment Variables:
```
base_url: http://localhost:8000
auth_token: (akan diisi setelah login)
member_id: (akan diisi setelah create member)
```

### Authentication Flow:
1. **Register** → POST `/auth/register/` → Cek email untuk token
2. **Verify Email** → POST `/auth/verify-token/` → Aktifkan akun
3. **Login** → POST `/auth/login/` → Simpan token
4. **Set Authorization Header** → `Bearer {{auth_token}}`

### Library Operations Flow:
1. **Create Bibliography** → POST `/api/biblio/`
2. **Create Item** → POST `/api/items/`
3. **Loan Item** → POST `/api/items/{id}/loan/`
4. **Return Item** → POST `/api/loans/{id}/return_item/`

---

## 7. ERROR HANDLING EXAMPLES

### 400 Bad Request (Validation Error):
```json
{
  "error": "member_id is required"
}
```

### 400 Bad Request (Duplicate Registration):
```json
{
  "non_field_errors": [
    "NIK sudah terdaftar dalam sistem"
  ]
}
```

### 400 Bad Request (Email Already Registered):
```json
{
  "non_field_errors": [
    "Email sudah terdaftar dalam sistem"
  ]
}
```


### 400 Bad Request (Token Issues):
```json
{
  "error": "Token has expired"
}
```

### 400 Bad Request (Already Verified):
```json
{
  "error": "Account already verified and active"
}
```

### 401 Unauthorized:
```json
{
  "detail": "Authentication credentials were not provided."
}
```

### 404 Not Found:
```json
{
  "detail": "Not found."
}
```

---

## 8. TESTING TIPS

1. **Test Authentication First**: Pastikan login berhasil sebelum test endpoint lain
2. **Check Response Codes**:
   - 200/201: Success
   - 400: Bad Request (validation error)
   - 401: Unauthorized
   - 403: Forbidden
   - 404: Not Found
3. **Use Variables**: Simpan ID dari response untuk digunakan di request berikutnya
4. **Test CRUD Operations**: Create → Read → Update → Delete
5. **Validate Data Types**: Pastikan format date, number, dan string sesuai

---

## 9. POSTMAN COLLECTION EXPORT

Untuk memudahkan testing, Anda dapat mengimport collection berikut ke Postman:

```json
{
  "info": {
    "name": "Perpustakaan API",
    "description": "API Testing untuk Sistem Manajemen Perpustakaan",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "variable": [
    {
      "key": "base_url",
      "value": "http://localhost:8000"
    },
    {
      "key": "auth_token",
      "value": ""
    }
  ],
  "item": [
    {
      "name": "Authentication",
      "item": [
        {
          "name": "Register User",
          "request": {
            "method": "POST",
            "header": [
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"nama\": \"John Doe\",\n  \"nik\": \"1234567890123456\",\n  \"tempat_lahir\": \"Jakarta\",\n  \"tanggal_lahir\": \"1990-05-15\",\n  \"institusi\": \"Universitas Indonesia\",\n  \"tipe_keanggotaan\": \"Mahasiswa\",\n  \"jenis_kelamin\": \"L\",\n  \"alamat\": \"Jl. Sudirman No. 123, Jakarta\",\n  \"nomor_hp\": \"081234567890\",\n  \"email\": \"john.doe@example.com\",\n  \"password\": \"password123\",\n  \"konfirmasi_password\": \"password123\",\n  \"foto_diri\": \"\",\n  \"foto_ktp\": \"\"\n}"
            },
            "url": {
              "raw": "{{base_url}}/auth/register/",
              "host": ["{{base_url}}"],
              "path": ["auth", "register", ""]
            }
          }
        },
        {
          "name": "Login User",
          "request": {
            "method": "POST",
            "header": [
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"username\": \"1234567890123456\",\n  \"password\": \"password123\"\n}"
            },
            "url": {
              "raw": "{{base_url}}/auth/login/",
              "host": ["{{base_url}}"],
              "path": ["auth", "login", ""]
            }
          }
        }
      ]
    },
    {
      "name": "Library Management",
      "item": [
        {
          "name": "Create Bibliography",
          "request": {
            "method": "POST",
            "header": [
              {
                "key": "Content-Type",
                "value": "application/json"
              },
              {
                "key": "Authorization",
                "value": "Bearer {{auth_token}}"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"title\": \"Introduction to Computer Science\",\n  \"isbn_issn\": \"978-0123456789\",\n  \"publisher_id\": 1,\n  \"publish_year\": \"2023\",\n  \"collation\": \"450 pages\",\n  \"notes\": \"A comprehensive guide to computer science fundamentals\",\n  \"gmd_id\": 1,\n  \"language_id\": \"en\"\n}"
            },
            "url": {
              "raw": "{{base_url}}/api/biblio/",
              "host": ["{{base_url}}"],
              "path": ["api", "biblio", ""]
            }
          }
        }
      ]
    }
  ]
}
```

---

## 10. MENJALANKAN SERVER DJANGO

Sebelum testing dengan Postman, pastikan Django server sudah berjalan:

```bash
# Aktivasi virtual environment (jika ada)
source venv/bin/activate

# Jalankan migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Buat default member types (WAJIB untuk register)
python3 create_member_types.py

# Jalankan server
python3 manage.py runserver
```

Server akan berjalan di `http://localhost:8000`

### Member Types yang Tersedia:
- **Mahasiswa** (ID: 1) - 3 buku, 7 hari, denda Rp 500/hari
- **Dosen** (ID: 2) - 5 buku, 14 hari, denda Rp 1.000/hari
- **Staff** (ID: 3) - 4 buku, 10 hari, denda Rp 750/hari
- **Umum** (ID: 4) - 2 buku, 7 hari, denda Rp 1.000/hari

---

## 11. API DOCUMENTATION

Untuk dokumentasi API lengkap, kunjungi:
- Swagger UI: `http://localhost:8000/`
- OpenAPI Schema: `http://localhost:8000/api/schema/`

---

## 12. CATATAN PENTING

1. **Database**: Pastikan database sudah dikonfigurasi dengan benar
2. **Migrations**: Jalankan `python3 manage.py migrate` sebelum testing
3. **Authentication**: Beberapa endpoint memerlukan authentication token
4. **CORS**: Jika ada error CORS, pastikan Django CORS headers sudah dikonfigurasi
5. **File Upload**: Untuk endpoint yang menerima file, gunakan `form-data` instead of `raw JSON`
6. **Field Types**: Pastikan tipe data sesuai dengan model:
   - `user_type`: Integer (0=admin, 1=staff, 2=member)
   - `passwd`: String (akan di-hash secara otomatis)
   - `groups`: String (ID group dipisahkan koma)
   - Field dengan `blank=True, null=True` bersifat opsional
7. **Member Types untuk Register**: Pastikan jalankan `python3 create_member_types.py` terlebih dahulu
   - **Mahasiswa**: 3 buku, 7 hari peminjaman
   - **Dosen**: 5 buku, 14 hari peminjaman
   - **Staff**: 4 buku, 10 hari peminjaman
   - **Umum**: 2 buku, 7 hari peminjaman
8. **Register vs Users Endpoint**:
   - `/auth/register/`: Menggunakan RegisterSerializer untuk registrasi member (fields: nama, tempat_lahir, dll.)
   - `/auth/users/`: Menggunakan UserSerializer untuk CRUD user sistem (fields: username, realname, dll.)
9. **Field Types untuk Register**:
   - `foto_diri` & `foto_ktp`: CharField (bukan ImageField) - menerima string kosong atau path file
   - Field ini opsional dan bisa dikosongkan tanpa error

## 13. FIELD REFERENCE

### User Model Fields:
- `username`: String (50 chars, unique)
- `realname`: String (100 chars)
- `passwd`: String (64 chars, akan di-hash)
- `email`: String (200 chars, optional)
- `user_type`: Integer (0=admin, 1=staff, 2=member)
- `user_image`: String (250 chars, optional)
- `social_media`: Text (optional)
- `last_login`: DateTime (auto-generated)
- `last_login_ip`: String (15 chars, optional)
- `groups`: String (200 chars, optional)
- `forgot`: String (80 chars, optional)
- `admin_template`: Text (optional)

---

**Happy Testing! 🚀**