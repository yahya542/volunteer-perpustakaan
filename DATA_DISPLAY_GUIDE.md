# Panduan Menampilkan Data Perpustakaan

## Struktur Proyek

Proyek ini terdiri dari tiga komponen utama:
1. **API Backend** (Django) - `/api-perpus`
2. **Admin Web Interface** (React/Vite) - `/admin-web`
3. **Mobile App** (React Native) - `/app`

## Menampilkan Data di Admin Web Interface

### 1. Komponen yang Sudah Diperbarui

#### Books Management (`/admin-web/src/pages/Books.tsx`)
- Menampilkan daftar buku dalam bentuk tabel
- Menggunakan data dummy untuk demonstrasi
- Siap terhubung ke API ketika tersedia

#### Users Management (`/admin-web/src/pages/Users.tsx`)
- Menampilkan daftar pengguna perpustakaan
- Menampilkan informasi lengkap termasuk nama lengkap dan email

#### Dashboard (`/admin-web/src/pages/Dashboard.tsx`)
- Menampilkan statistik perpustakaan
- Menampilkan aktivitas terbaru

### 2. Cara Menghubungkan dengan API Backend

#### Langkah-langkah:
1. Pastikan API backend berjalan di `http://localhost:8000`
2. Di setiap komponen, ganti bagian fetch data dummy dengan fetch ke API sebenarnya:

```typescript
// Contoh penggunaan API sebenarnya
const fetchBooks = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/biblio/');
    if (!response.ok) {
      throw new Error('Failed to fetch books');
    }
    const data = await response.json();
    setBooks(data);
    setLoading(false);
  } catch (err) {
    setError('Failed to load books');
    setLoading(false);
  }
};
```

### 3. Endpoint API yang Tersedia

#### Bibliografi (Buku)
- `GET /api/biblio/` - Mendapatkan semua data buku
- `GET /api/biblio/{id}/` - Mendapatkan detail buku tertentu

#### Pengguna
- `GET /user/members/` - Mendapatkan semua data member

#### Peminjaman
- `GET /api/loans/` - Mendapatkan semua data peminjaman
- `GET /api/loan-history/` - Mendapatkan riwayat peminjaman

#### Master Data
- `GET /api/publishers/` - Penerbit
- `GET /api/authors/` - Penulis
- `GET /api/topics/` - Topik

### 4. Menjalankan Sistem

#### Menjalankan API Backend:
```bash
cd api-perpus
python3 manage.py runserver
```

#### Menjalankan Admin Web Interface:
```bash
cd admin-web
npm run dev
```

Akses admin interface di `http://localhost:5173`

## Struktur Data Utama

### Bibliografi (Buku)
- `biblio_id`: ID unik buku
- `title`: Judul buku
- `publish_year`: Tahun terbit
- `isbn_issn`: ISBN/ISSN
- `publisher_id`: ID penerbit
- `gmd_id`: ID tipe materi

### Pengguna
- `id`: ID unik pengguna
- `username`: Nama pengguna
- `email`: Alamat email
- `first_name`: Nama depan
- `last_name`: Nama belakang

## Catatan Penting

1. Untuk saat ini, sistem menggunakan data dummy untuk demonstrasi
2. Ketika API backend berjalan, sistem akan secara otomatis terhubung
3. Pastikan kedua sistem (API dan Admin Web) berjalan bersamaan
4. Port default API: 8000
5. Port default Admin Web: 5173

## Troubleshooting

### Jika data tidak muncul:
1. Pastikan API backend berjalan
2. Periksa koneksi jaringan
3. Verifikasi endpoint API
4. Cek console browser untuk error

### Jika terjadi error CORS:
1. Tambahkan konfigurasi CORS di `api-perpus/backend/settings.py`:
```python
INSTALLED_APPS = [
    # ... aplikasi lain
    'corsheaders',
]

MIDDLEWARE = [
    # ... middleware lain
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173"
]
```