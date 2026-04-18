# VetConnect API: Sistem Manajemen Klinik Hewan Terpadu

VetConnect adalah proyek *RESTful API* tingkat lanjut yang dibangun menggunakan **FastAPI** dan **SQLAlchemy**. Sistem ini dirancang untuk mendigitalisasi operasional klinik hewan, mulai dari pendataan pasien hingga pencatatan riwayat rekam medis, dengan standar keamanan modern menggunakan **JSON Web Token (JWT)**.

##  Deskripsi Website & Sistem
VetConnect bertindak sebagai otak (*backend*) bagi aplikasi klinik hewan. Sistem ini mengelola tiga entitas utama yang saling berelasi:
1. **Admin (Users)**: Pengelola sistem yang memiliki hak akses penuh untuk melakukan modifikasi data setelah terautentikasi.
2. **Pasien (Pets)**: Data hewan peliharaan yang mencakup nama, spesies, ras, dan pemilik.
3. **Rekam Medis (Medical Records)**: Catatan histori kesehatan yang unik untuk setiap pasien, memastikan data diagnosa dan tindakan tertata dengan rapi.

##  Stack Teknologi
* **Backend**: FastAPI (Async support)
* **Database**: SQLite
* **ORM**: SQLAlchemy
* **Autentikasi**: JWT (JSON Web Tokens) & Passlib (Hashing Password)
* **Validasi**: Pydantic

##  Panduan Instalasi & Persiapan
Sebelum menjalankan, pastikan kamu telah menginstal Python di komputermu.

1. **Clone Repository**:
   ```bash
   git clone https://github.com/username-kamu/VetConnect.git
   cd VetConnect
   ```
2. **Buat Virtual Environment**:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   ```
3. **Instal Library**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Jalankan Aplikasi**:
   ```bash
   uvicorn main:app --reload
   ```

##  Panduan Penggunaan (API Flow)
Untuk menguji sistem, disarankan menggunakan **Postman** atau **Swagger UI** (akses `http://127.0.0.1:8000/docs`). Ikuti urutan ini:

### 1. Autentikasi
* **Registrasi**: `POST /register` untuk membuat akun admin.
* **Login**: `POST /login` untuk mendapatkan `access_token`. *Copy* token ini untuk digunakan di setiap *request* berikutnya.

### 2. Manajemen Pasien (Pets)
* **Tambah Pasien**: `POST /pets/` (Gunakan *Bearer Token* di tab Authorization).
* **Lihat Data**: `GET /pets/` untuk melihat daftar semua pasien yang terdaftar.

### 3. Manajemen Rekam Medis (Medical)
* **Tambah Catatan**: `POST /medical/{pet_id}`. Masukkan ID hewan peliharaan di bagian URL agar rekam medis terhubung ke hewan yang tepat.
* **Update/Hapus**: Gunakan `PUT` atau `DELETE` pada endpoint `/medical/{record_id}` untuk mengelola data riwayat kesehatan.

##  Mengapa Menggunakan VetConnect?
* **Modular**: Kode terbagi rapi berdasarkan fungsi (*routers*, *models*, *schemas*).
* **Secure**: Password tersimpan dalam bentuk *hashed* (tidak bisa dibaca secara langsung oleh siapapun).
* **Scalable**: Mudah dikembangkan untuk menambah fitur seperti penjadwalan dokter atau sistem pembayaran.


## Langkah Terakhir
Jangan lupa untuk melakukan langkah Git ini agar versi lengkap ini tersimpan di GitHub kamu:

```bash
git add README.md
git commit -m "docs: add comprehensive readme"
git push -u origin main
```
