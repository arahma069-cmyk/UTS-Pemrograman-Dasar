# Sistem Pengelolaan Data Mahasiswa

## 1. Deskripsi Program

Sistem Pengelolaan Data Mahasiswa merupakan aplikasi berbasis Python yang digunakan untuk mengelola dan menganalisis data mahasiswa. Program ini berjalan melalui Command Line Interface (CLI).

Program ini membantu pengguna dalam melihat, mencari, menambahkan, menghapus, dan menganalisis data mahasiswa berdasarkan nilai.

## 2. Tujuan Program

Program ini dibuat untuk mempermudah pengelolaan data mahasiswa serta menerapkan konsep dasar pemrograman Python, seperti list, dictionary, set, function, module, package, dan pengolahan file CSV serta JSON.

## 3. Fitur Program

1. Menampilkan seluruh data mahasiswa.
2. Mencari mahasiswa berdasarkan NIM.
3. Menambahkan data mahasiswa baru.
4. Menghapus data mahasiswa.
5. Menyaring mahasiswa berdasarkan nilai minimum.
6. Menghitung jumlah mahasiswa, nilai rata-rata, nilai tertinggi, dan nilai terendah.
7. Menyimpan hasil analisis ke dalam file CSV dan JSON.

## 4. Struktur Folder

```text
UTS-Pemrograman-Dasar/
│
├── main.py
├── README.md
│
├── data/
│   └── mahasiswa.csv
│
├── mahasiswa/
│   ├── __init__.py
│   ├── data.py
│   ├── file_handler.py
│   └── utils.py
│
└── output/
    ├── hasil_analisis.csv
    └── hasil_analisis.json
```

## 5. Format Data Input

Data mahasiswa disimpan dalam file `data/mahasiswa.csv` dengan format:

| NIM | Nama | Nilai |
|---|---|---:|
| 23001 | Andi | 85 |
| 23002 | Budi | 72 |
| 23003 | Citra | 90 |
| 23004 | Dinda | 78 |
| 23005 | Eko | 65 |

Program juga melakukan validasi untuk mengabaikan data yang tidak lengkap, nilai di luar rentang 0–100, dan NIM yang duplikat.

## 6. Cara Menjalankan Program

1. Pastikan Python sudah terinstal.
2. Buka folder project melalui Visual Studio Code atau terminal.
3. Jalankan perintah berikut:

