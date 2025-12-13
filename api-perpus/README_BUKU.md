# Panduan Menambahkan Buku ke Database Perpustakaan

## Struktur Database

Database menggunakan nama: `perpus`

Tabel utama:
- `biblio` - Menyimpan informasi katalog buku
- `item` - Menyimpan informasi fisik/item buku

## Cara Menambahkan Buku Baru

1. Edit file `sample_book.sql`
2. Ubah bagian berikut dengan data buku baru:

### Di bagian biblio:
- `title` - Judul buku
- `isbn_issn` - ISBN buku
- `publish_year` - Tahun terbit
- `call_number` - Nomor panggil
- `classification` - Klasifikasi
- `notes` - Catatan tentang buku

### Di bagian item:
- `item_code` - Kode item (harus unik, contoh: BK000002)
- `inventory_code` - Kode inventaris (harus unik, contoh: INV002)
- Pastikan `call_number` sama dengan yang di bagian biblio

## Contoh Format Item Code
- BK000001 (untuk buku pertama)
- BK000002 (untuk buku kedua)
- Dan seterusnya...

## Contoh Format Inventory Code
- INV001 (untuk inventaris pertama)
- INV002 (untuk inventaris kedua)
- Dan seterusnya...

## Cara Mengimport ke Database

Jalankan perintah berikut di terminal:

```bash
mysql -u perpus -pperpus123 -D perpus < sample_book.sql
```

## Verifikasi Data

Untuk mengecek apakah buku berhasil ditambahkan:

```bash
mysql -u perpus -pperpus123 -D perpus -e "SELECT biblio_id, title, isbn_issn FROM biblio ORDER BY biblio_id DESC LIMIT 5;"
```

## Catatan Penting

1. Setiap item_code harus unik
2. Setiap inventory_code harus unik
3. Nomor panggil harus konsisten antara biblio dan item
4. Jangan mengubah bagian yang menggunakan NOW(), CURDATE(), LAST_INSERT_ID()