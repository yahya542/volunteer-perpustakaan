# Setup Pengembangan Perpustakaan Bersih

## Prasyarat

- Python 3.8+
- Node.js 14+
- npm 6+
- SQLite (sudah termasuk dengan Python)

## Instalasi

### 1. Setup API Backend (Django)

```bash
cd api-perpus

# Buat virtual environment
python3 -m venv venv

# Aktifkan virtual environment
# Linux/Mac:
source venv/bin/activate
# Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Jalankan migrasi database
python3 manage.py migrate

# Buat tipe keanggotaan default
python3 create_member_types.py

# Jalankan server pengembangan
python3 manage.py runserver
```

Server akan berjalan di `http://127.0.0.1:8000`

### 2. Setup Admin Web Interface (React/Vite)

```bash
cd admin-web

# Install dependencies
npm install

# Jalankan server pengembangan
npm run dev
```

Server akan berjalan di `http://localhost:5173`

## Struktur Direktori

```
perpustakaan-bersih/
├── api-perpus/           # API Backend (Django)
│   ├── api/              # Models, views, serializers untuk koleksi perpustakaan
│   ├── authentication/    # Autentikasi pengguna
│   ├── backend/          # Konfigurasi Django
│   ├── user/             # Manajemen pengguna
│   └── manage.py         # CLI Django
├── admin-web/            # Admin Dashboard (React/Vite)
│   ├── src/
│   │   ├── components/   # Komponen UI reusable
│   │   ├── pages/        # Halaman aplikasi
│   │   └── App.tsx       # Komponen utama
│   └── vite.config.ts    # Konfigurasi Vite
└── app/                  # Mobile App (React Native)
```

## Perintah Berguna

### API Backend

```bash
# Menjalankan server
python3 manage.py runserver

# Membuat migrasi baru
python3 manage.py makemigrations

# Menjalankan migrasi
python3 manage.py migrate

# Membuat superuser
python3 manage.py createsuperuser

# Shell Django interaktif
python3 manage.py shell
```

### Admin Web Interface

```bash
# Menjalankan server pengembangan
npm run dev

# Membuat build produksi
npm run build

# Menjalankan linter
npm run lint
```

## Konfigurasi Database

Secara default, proyek menggunakan SQLite dengan file `db.sqlite3`.

Untuk menggunakan database lain (MySQL, PostgreSQL), ubah konfigurasi di `api-perpus/backend/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # atau postgresql
        'NAME': 'nama_database',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',  # 5432 untuk PostgreSQL
    }
}
```

## Import Data Awal

Jika memiliki file SQL dump:

1. Untuk MySQL:
```bash
mysql -u username -p database_name < senayan.sql
```

2. Untuk PostgreSQL:
```bash
psql -U username -d database_name -f senayan.sql
```

## Menjalankan Kedua Sistem Secara Bersamaan

Untuk pengembangan, jalankan kedua sistem dalam terminal terpisah:

Terminal 1 (API):
```bash
cd api-perpus
python3 manage.py runserver
```

Terminal 2 (Admin Web):
```bash
cd admin-web
npm run dev
```

## Deployment

### API Backend

```bash
# Install dependencies produksi
pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic

# Gunakan server WSGI seperti Gunicorn
gunicorn backend.wsgi:application --bind 0.0.0.0:8000
```

### Admin Web Interface

```bash
# Build untuk produksi
npm run build

# File hasil build ada di dist/
# Deploy dist/ ke web server statis
```

## Troubleshooting

### Masalah Umum

1. **Port sudah digunakan**:
   - Ubah port: `python3 manage.py runserver 8001`

2. **Module not found**:
   - Pastikan virtual environment diaktifkan
   - Install ulang dependencies: `pip install -r requirements.txt`

3. **Permission denied**:
   - Gunakan virtual environment
   - Periksa permission file

4. **Database locked** (SQLite):
   - Tutup semua koneksi database
   - Restart server

### Debugging

1. **Cek log server**:
   - Lihat output terminal tempat server dijalankan

2. **Cek browser console**:
   - Buka Developer Tools > Console

3. **Test API langsung**:
   ```bash
   curl http://127.0.0.1:8000/api/biblio/
   ```

## Lisensi

Proyek ini dilisensikan di bawah MIT License.