# Setup Perpustakaan API

Panduan lengkap untuk setup dan menjalankan API Perpustakaan dengan Email Verification.

## 🚀 Quick Start

### 1. Setup Database
```bash
# Jalankan migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Buat default member types (WAJIB)
python3 create_member_types.py
```

### 2. Jalankan Server
```bash
python3 manage.py runserver
```

### 3. Test API dengan Postman
Import collection dari `POSTMAN_API_TESTING.md` dan mulai testing!

**Catatan Login**: Gunakan NIK yang diinput saat register sebagai username untuk login.

## 📋 Yang Sudah Dibuat

### ✅ Enhanced API Documentation
- Semua endpoint sudah memiliki deskripsi lengkap
- Request/response examples sudah tersedia
- Error handling sudah didokumentasikan

### ✅ Fixed Issues
- ✅ Register endpoint error (AssertionError) - **FIXED**
- ✅ Foto fields error (ImageField issue) - **FIXED**
- ✅ Member type validation error - **FIXED**

### ✅ Created Files
- `POSTMAN_API_TESTING.md` - Panduan testing lengkap
- `create_member_types.py` - Script untuk setup member types
- Enhanced semua views dengan dokumentasi lengkap

## 🎯 Available Endpoints

### Authentication
- `POST /auth/register/` - Registrasi member baru (mengirim email verifikasi)
- `POST /auth/verify-token/` - Verifikasi token email untuk aktivasi akun
- `POST /auth/login/` - Login user (hanya untuk akun yang sudah terverifikasi)

### User Management
- `GET /user/members/` - List semua member
- `POST /user/members/` - Buat member baru
- `POST /user/members/{id}/check_in/` - Check-in member

### Library Management
- `GET /api/biblio/` - List bibliography
- `POST /api/biblio/` - Buat bibliography baru
- `GET /api/items/` - List items
- `POST /api/items/` - Buat item baru
- `POST /api/items/{id}/loan/` - Pinjam item
- `POST /api/loans/{id}/return_item/` - Kembalikan item

### Master Data
- Publishers, Authors, Topics, Languages, Locations, etc.

## 🔧 Troubleshooting

### Error: "Tipe keanggotaan tidak valid"
**Solusi**: Jalankan `python3 create_member_types.py`

### Error: "The submitted data was not a file"
**Solusi**: Field foto sudah diperbaiki menjadi CharField, bisa kirim string kosong

### Error: AssertionError at /auth/register/
**Solusi**: Sudah diperbaiki dengan menambahkan return statement untuk validation error

## 📚 Member Types Available

| Tipe | Limit Buku | Periode (hari) | Denda/hari |
|------|------------|----------------|------------|
| Mahasiswa | 3 | 7 | Rp 500 |
| Dosen | 5 | 14 | Rp 1.000 |
| Staff | 4 | 10 | Rp 750 |
| Umum | 2 | 7 | Rp 1.000 |

## 📧 Email Verification Flow

### 1. Registrasi
- User mengisi data registrasi
- Sistem membuat Member record (status pending)
- Sistem mengirim email verifikasi dengan token

### 2. Verifikasi Email
- User menerima email dengan token/link verifikasi
- User mengklik link atau menggunakan token di aplikasi
- Sistem memverifikasi token dan membuat User record
- Member status berubah dari pending ke active

### 3. Login
- User dapat login dengan NIK + password
- Sistem memverifikasi credentials dari User table

## ⚙️ Konfigurasi Email

### 📊 **STATUS SAAT INI:**
**Console Backend** - Email ditampilkan di terminal Django (untuk development)

### 🔄 **Cara Mengganti ke Email Asli:**

#### **Untuk Mengirim Email ke Inbox User:**
1. Buka `backend/settings.py`
2. Comment out baris ini:
   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
   ```
3. Uncomment blok ini:
   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_USE_SSL = False
   EMAIL_HOST_USER = 'sajakcodingan@gmail.com'
   EMAIL_HOST_PASSWORD = 'hmkk cwdy wzgj seyv'
   DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
   EMAIL_TIMEOUT = 30
   ```
4. Restart Django server
5. Sekarang email akan dikirim ke inbox user sesungguhnya!

#### **Untuk Kembali ke Console (Development):**
1. Uncomment baris console backend
2. Comment out blok SMTP
3. Restart Django server

### 📧 **Perbedaan:**

| Mode | Tujuan Email | Keuntungan | Kekurangan |
|------|-------------|------------|------------|
| **Console** | Terminal Django | No setup, instant | Tidak ke inbox user |
| **SMTP** | Inbox Email User | Real experience | Perlu setup Gmail |

### 🎯 **Rekomendasi:**
- **Development**: Console Backend (mudah testing)
- **Production**: SMTP Backend (email ke user)

### 📧 Gmail App Password Setup:
1. Buka [Google Account Settings](https://myaccount.google.com/)
2. Security → 2-Step Verification → App passwords
3. Generate password untuk "Mail"
4. Ganti `EMAIL_HOST_PASSWORD` dengan password tersebut
5. **Catatan**: Password app berbeda dengan password akun Gmail biasa

### 🎯 Fitur Email:
- ✅ **Email Asli**: Dikirim ke inbox email user
- ✅ **Multiple Tokens**: Email yang sama bisa menerima token berkali-kali
- ✅ **Kode 6-Digit**: Mudah diingat dan diinput manual
- ✅ **Kode Unik**: Setiap registrasi dapat kode berbeda
- ✅ **Expiry 24 Jam**: Kode kadaluarsa dalam 24 jam

## 🚨 Error Handling

### Validation Errors:

**NIK Sudah Terdaftar:**
```json
{
  "non_field_errors": ["NIK sudah terdaftar dalam sistem"]
}
```
**Solusi:** Gunakan NIK yang berbeda atau login jika sudah terdaftar

**Email Sudah Terdaftar:**
```json
{
  "non_field_errors": ["Email sudah terdaftar dalam sistem"]
}
```
**Solusi:** Gunakan email yang berbeda

**Pending Verification:**
```json
{
  "non_field_errors": ["Email sudah terdaftar dan sedang menunggu verifikasi. Silakan cek email Anda untuk token verifikasi."]
}
```
**Solusi:** Cek email untuk token verifikasi yang sudah dikirim

**Token Expired:**
```json
{"error": "Token has expired"}
```
**Solusi:** Lakukan registrasi ulang untuk mendapatkan token baru

**Already Verified:**
```json
{"error": "Account already verified and active"}
```
**Solusi:** Langsung login dengan NIK dan password

## 🎉 Ready to Test!

API sudah siap untuk testing dengan Postman. Sistem email verification sudah fully implemented dan terintegrasi.

**Happy Testing! 🚀**