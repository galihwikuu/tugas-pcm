# Website PCM

Website Pimpinan Cabang Muhammadiyah (PCM) merupakan aplikasi berbasis web yang dikembangkan menggunakan Django untuk menyajikan informasi organisasi, berita, agenda kegiatan, pimpinan, ranting, dan amal usaha.

## Teknologi yang Digunakan

- **Python** — bahasa pemrograman utama.
- **Django** — framework backend.
- **uv** — pengelola environment dan dependency Python.
- **SQLite** — database lokal, jika menggunakan konfigurasi bawaan project.
- **Bootstrap 5** — framework antarmuka.
- **HTML, CSS, dan JavaScript** — pengembangan tampilan website.

## Persyaratan

Pastikan perangkat sudah memiliki:

- Git
- Python dengan versi yang sesuai dengan project
- uv
- Koneksi internet untuk mengunduh dependency

## 1. Clone Repository

Clone repository project ke komputer lokal:

```bash
git clone https://github.com/galihwikuu/tugas-pcm.git
```

Masuk ke direktori project:

```bash
cd tugas-pcm
```

## 2. Install Dependency

Jalankan perintah berikut:

```bash
uv sync
```

Perintah tersebut akan menyiapkan virtual environment dan memasang dependency berdasarkan konfigurasi project, seperti `pyproject.toml` dan `uv.lock` jika tersedia.

## 3. Jalankan Migrasi Database

Buat atau sesuaikan struktur database dengan model Django:

```bash
uv run python manage.py migrate
```

## 4. Memuat Data Awal (Seed)

Project menyediakan fixture data awal pada:

```text
pcm/fixtures/data_awal.json
```

Untuk memasukkan data awal ke database lokal, jalankan:

```bash
uv run python manage.py loaddata data_awal
```

Perintah tersebut akan memuat data dari fixture `data_awal.json` ke database yang digunakan oleh Django.

**Catatan:** sebaiknya gunakan database lokal yang masih kosong saat melakukan seed pertama kali. Jika database sudah berisi data, perhatikan kemungkinan konflik primary key atau data yang sudah ada.

## 5. Menyiapkan File Media

Foto yang digunakan oleh berita, agenda, profil organisasi, pimpinan, dan amal usaha disimpan di direktori `media/`.

Pastikan direktori media beserta file di dalamnya tersedia setelah repository di-clone, dengan struktur yang sesuai dengan referensi gambar pada fixture.

Contoh struktur project:

```text
tugas-pcm/
├── manage.py
├── pyproject.toml
├── uv.lock
├── pcm/
│   ├── fixtures/
│   │   └── data_awal.json
│   └── migrations/
├── media/
│   ├── berita/
│   ├── agenda/
│   ├── profil/
│   ├── pimpinan/
│   └── amal_usaha/
├── templates/
└── static/
```

Struktur direktori dapat berbeda mengikuti perkembangan project.

## 6. Menjalankan Server Lokal

Jalankan server development Django:

```bash
uv run python manage.py runserver
```

Buka browser dan akses:

```text
http://127.0.0.1:8000/
```

Untuk menghentikan server, tekan `Ctrl + C` pada terminal.

## 7. Membuat Akun Administrator

Jika perlu mengelola data melalui Django Admin, buat akun administrator dengan perintah:

```bash
uv run python manage.py createsuperuser
```

Ikuti instruksi untuk mengisi username, email, dan password.

Setelah server berjalan, akses:

```text
http://127.0.0.1:8000/admin/
```

Gunakan akun administrator yang telah dibuat untuk masuk.

## Perintah yang Sering Digunakan

| Kebutuhan | Perintah |
|---|---|
| Install dependency | `uv sync` |
| Migrasi database | `uv run python manage.py migrate` |
| Memuat data awal | `uv run python manage.py loaddata data_awal` |
| Menjalankan server | `uv run python manage.py runserver` |
| Membuat admin | `uv run python manage.py createsuperuser` |
| Memeriksa konfigurasi | `uv run python manage.py check` |
| Membuat migration | `uv run python manage.py makemigrations` |

## Catatan Pengembangan

- Jangan mengunggah password, secret key, atau informasi sensitif ke repository.
- Pastikan dependency dan konfigurasi project sudah sesuai sebelum menjalankan aplikasi.
- File fixture digunakan untuk menyediakan data awal, sedangkan direktori media menyimpan file gambar yang dirujuk oleh data tersebut.
- Jika terdapat perubahan pada model Django, buat dan jalankan migration sebelum menggunakan perubahan tersebut.
- Data pada setiap database lokal dapat berbeda sesuai perubahan yang dilakukan selama pengembangan.

---

**PCM Website** — Sistem informasi berbasis web untuk mendukung penyajian informasi dan kegiatan organisasi secara digital.