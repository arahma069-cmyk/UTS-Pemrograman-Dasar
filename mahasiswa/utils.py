"""Fungsi bantuan untuk tampilan dan validasi input."""


def print_students(students):
    """Menampilkan daftar mahasiswa dalam bentuk tabel sederhana."""
    if not students:
        print("Belum ada data mahasiswa.")
        return

    print("\nNIM\t\tNama\t\tNilai")
    print("-" * 45)

    for student in students:
        print(
            f"{student['nim']}\t"
            f"{student['nama']}\t\t"
            f"{student['nilai']}"
        )


def get_valid_score(prompt):
    """Meminta nilai numerik dari 0 sampai 100."""
    raw = input(prompt).strip()

    try:
        score = float(raw)
    except ValueError:
        raise ValueError("nilai harus berupa angka.")

    if not 0 <= score <= 100:
        raise ValueError("nilai harus berada pada rentang 0 sampai 100.")

    return score
