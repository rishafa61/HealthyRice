# Referensi API healthyriceAI

**Base URL (lokal):**

```text
http://127.0.0.1:8000/api/
```

Semua endpoint yang membutuhkan autentikasi harus menyertakan token akses pada header:

```http
Authorization: Bearer <access_token>
```

---

## Autentikasi

### Daftar Akun — `POST /auth/register/`

Digunakan untuk mendaftarkan akun baru. Endpoint ini terhubung dengan halaman **"Daftar Akun"** pada aplikasi.

**Request:**

```json
{
  "full_name": "Petani Test",
  "email": "petani@test.com",
  "password": "padihijau123",
  "confirm_password": "padihijau123"
}
```

**Response `201 Created`:**

```json
{
  "user": {
    "id": 1,
    "full_name": "Petani Test",
    "email": "petani@test.com",
    "date_joined": "..."
  },
  "access": "<jwt>",
  "refresh": "<jwt>"
}
```

Response akan berisi data pengguna serta **access token** dan **refresh token** yang digunakan untuk autentikasi.

---

### Login — `POST /auth/login/`

Digunakan untuk masuk ke akun yang sudah terdaftar. Endpoint ini terhubung dengan halaman **"Login"**.

**Request:**

```json
{
  "email": "petani@test.com",
  "password": "padihijau123"
}
```

**Response `200 OK`:**

```json
{
  "access": "<jwt>",
  "refresh": "<jwt>"
}
```

---

### Refresh Token — `POST /auth/refresh/`

Digunakan untuk mendapatkan **access token** baru ketika access token sebelumnya sudah kedaluwarsa.

**Request:**

```json
{
  "refresh": "<jwt>"
}
```

**Response `200 OK`:**

```json
{
  "access": "<jwt>"
}
```

---

### Data Pengguna Saat Ini — `GET /auth/me/`

**Membutuhkan autentikasi.**

Digunakan untuk mengambil informasi pengguna yang sedang login.

**Response `200 OK`:**

```json
{
  "id": 1,
  "full_name": "...",
  "email": "...",
  "date_joined": "..."
}
```

---

# Penyakit Padi

## Daftar Penyakit — `GET /diseases/`

Menampilkan daftar penyakit padi yang tersedia pada sistem. Endpoint ini digunakan pada halaman **"Penanganan Penyakit"**.

Endpoint ini **tidak membutuhkan autentikasi**.

**Response `200 OK`:**

```json
[
  {
    "id": 4,
    "slug": "blast",
    "name": "Blast",
    "short_description": "...",
    "risk_level": "high",
    "image": null
  }
]
```

---

## Detail Penyakit — `GET /diseases/{slug}/`

Menampilkan informasi lengkap mengenai suatu penyakit padi. Endpoint ini digunakan pada halaman **"Solusi Penanganan"**.

**Contoh:**

```http
GET /diseases/blast/
```

**Response `200 OK`:**

```json
{
  "id": 4,
  "slug": "blast",
  "name": "Blast",
  "short_description": "...",
  "symptoms": ["Lesi berbentuk belah ketupat dengan pusat abu-abu...", "..."],
  "treatment_steps": ["Aplikasikan fungisida...", "..."],
  "prevention_steps": ["Gunakan varietas tahan blast", "..."],
  "risk_level": "high",
  "image": null
}
```

Field berikut berbentuk **array**:

- `symptoms` — daftar gejala penyakit.
- `treatment_steps` — langkah-langkah penanganan penyakit.
- `prevention_steps` — langkah-langkah pencegahan penyakit.

Setiap item dalam array dapat langsung ditampilkan sebagai daftar menggunakan `.map()` pada React.

---

# Deteksi Penyakit

Semua endpoint pada bagian ini **membutuhkan autentikasi**.

Data deteksi secara otomatis dibatasi berdasarkan pengguna yang sedang login. Artinya, pengguna hanya dapat melihat dan mengelola **riwayat pemindaian miliknya sendiri**.

---

## Analisis Foto — `POST /detections/`

Digunakan untuk mengunggah foto daun padi dan melakukan deteksi penyakit. Endpoint ini terhubung dengan fitur **"Mulai Analisa"**.

Request harus menggunakan:

```http
Content-Type: multipart/form-data
```

### Field

| Field   | Tipe | Keterangan     |
| ------- | ---- | -------------- |
| `image` | File | Foto daun padi |

Format file yang didukung:

- JPG / JPEG
- PNG
- WebP

**Ukuran maksimum:** 10 MB.

### Response `201 Created`

```json
{
  "id": 1,
  "image": "http://.../media/detections/user_1/leaf.jpg",
  "disease": {
    "id": 2,
    "slug": "tungro",
    "name": "Tungro",
    "short_description": "...",
    "risk_level": "medium",
    "image": null
  },
  "confidence": 99.71,
  "inference_time_ms": 722,
  "created_at": "2026-09-06T20:07:15Z"
}
```

Hasil deteksi berisi:

- `id` — ID hasil deteksi.
- `image` — URL foto yang telah diunggah.
- `disease` — informasi penyakit yang terdeteksi.
- `confidence` — tingkat keyakinan model dalam persen.
- `inference_time_ms` — waktu yang dibutuhkan model untuk melakukan inferensi dalam milidetik.
- `created_at` — waktu ketika deteksi dibuat.

### Response `400 Bad Request`

Jika file tidak memenuhi validasi, API akan mengembalikan pesan error.

**Contoh:**

```json
{
  "error": "Unsupported file type: .gif"
}
```

Frontend dapat menggunakan response ini untuk menampilkan pesan **"Format file tidak didukung"** kepada pengguna.

---

## Riwayat Deteksi — `GET /detections/`

Digunakan untuk mengambil seluruh riwayat deteksi milik pengguna yang sedang login. Endpoint ini terhubung dengan halaman **"Riwayat Deteksi"**.

### Filter Berdasarkan Penyakit

Riwayat dapat difilter berdasarkan jenis penyakit menggunakan query parameter:

```http
GET /detections/?disease=tungro
```

**Response `200 OK`:**

```json
[
  {
    "id": 1,
    "image": "...",
    "disease": {
      "...": "..."
    },
    "confidence": 99.71,
    "created_at": "..."
  }
]
```

---

## Detail Hasil Deteksi — `GET /detections/{id}/`

Digunakan untuk mengambil detail satu hasil deteksi berdasarkan ID.

Endpoint ini dapat digunakan ketika pengguna membuka kembali hasil pemindaian sebelumnya dari halaman **"Riwayat Deteksi"**.

**Contoh:**

```http
GET /detections/1/
```

Endpoint membutuhkan autentikasi dan hanya dapat mengakses hasil deteksi milik pengguna yang sedang login.

---

## Hapus Riwayat Deteksi — `DELETE /detections/{id}/`

Digunakan untuk menghapus satu hasil deteksi dari riwayat pengguna. Endpoint ini terhubung dengan tombol **"Hapus"**.

**Contoh:**

```http
DELETE /detections/1/
```

**Response `204 No Content`:**

Jika penghapusan berhasil, API tidak mengembalikan body response.

---

# Format Error

## Error Validasi

Error validasi dari Django REST Framework dikembalikan dengan status **`400 Bad Request`**.

Error biasanya dikelompokkan berdasarkan field yang mengalami masalah.

**Contoh:**

```json
{
  "confirm_password": ["Passwords do not match."]
}
```

Frontend akan membaca nama field tersebut untuk menentukan pesan error yang harus ditampilkan.

---

## Error Autentikasi

Jika access token tidak tersedia, sudah kedaluwarsa, atau tidak valid, API akan mengembalikan status **`401 Unauthorized`**.

**Contoh:**

```json
{
  "detail": "Given token not valid for any token type",
  "code": "token_not_valid"
}
```

Frontend akan menangani response `401` dengan meminta pengguna melakukan login kembali atau menggunakan refresh token untuk mendapatkan access token baru.

---

# Ringkasan Endpoint

| Fitur           | Method   | Endpoint            | Auth |
| --------------- | -------- | ------------------- | ---- |
| Daftar akun     | `POST`   | `/auth/register/`   | x    |
| Login           | `POST`   | `/auth/login/`      | x    |
| Refresh token   | `POST`   | `/auth/refresh/`    | x    |
| Data pengguna   | `GET`    | `/auth/me/`         | v    |
| Daftar penyakit | `GET`    | `/diseases/`        | x    |
| Detail penyakit | `GET`    | `/diseases/{slug}/` | x    |
| Analisis foto   | `POST`   | `/detections/`      | v    |
| Riwayat deteksi | `GET`    | `/detections/`      | v    |
| Detail deteksi  | `GET`    | `/detections/{id}/` | v    |
| Hapus deteksi   | `DELETE` | `/detections/{id}/` | v    |
