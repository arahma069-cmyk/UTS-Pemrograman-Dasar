"""Fungsi untuk membaca dan menyimpan file CSV serta JSON."""
import csv
import json
import os


def load_csv(path):
    """Membaca CSV dan mengembalikan data mahasiswa yang sudah divalidasi."""
    from mahasiswa.data import load_students

    try:
        with open(path, "r", newline="", encoding="utf-8") as file:
            rows = list(csv.DictReader(file))
        return load_students(rows)

    except FileNotFoundError:
        print(f"File {path} tidak ditemukan. Program menggunakan data kosong.")
        return []

    except (csv.Error, UnicodeDecodeError) as error:
        print(f"File CSV tidak dapat dibaca: {error}")
        return []


def save_json(path, data):
    """Menyimpan hasil analisis ke file JSON."""
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def save_csv(path, students):
    """Menyimpan daftar mahasiswa ke file CSV."""
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["nim", "nama", "nilai"]
        )
        writer.writeheader()
        writer.writerows(students)
