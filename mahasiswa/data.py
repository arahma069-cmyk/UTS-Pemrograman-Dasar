"""Fungsi untuk manipulasi dan analisis data mahasiswa."""


def load_students(rows):
    """Mengubah baris data menjadi list dictionary yang tervalidasi."""
    students = []
    seen_nim = set()

    for row in rows:
        nim = str(row.get("nim", "")).strip()
        nama = str(row.get("nama", "")).strip()

        try:
            nilai = float(row.get("nilai", ""))
        except (TypeError, ValueError):
            continue

        if nim and nama and 0 <= nilai <= 100 and nim not in seen_nim:
            students.append({
                "nim": nim,
                "nama": nama,
                "nilai": nilai
            })
            seen_nim.add(nim)

    return students


def search_student(students, nim):
    """Mencari mahasiswa berdasarkan NIM."""
    return next(
        (student for student in students if student["nim"] == nim),
        None
    )


def filter_students(students, minimum):
    """Menyaring mahasiswa berdasarkan nilai minimum."""
    return [
        student for student in students
        if student["nilai"] >= minimum
    ]


def calculate_summary(students):
    """Menghitung rekapitulasi nilai mahasiswa."""
    if not students:
        return {
            "jumlah": 0,
            "rata_rata": 0,
            "tertinggi": 0,
            "terendah": 0,
            "nim_unik": 0
        }

    scores = [student["nilai"] for student in students]
    unique_nim = {student["nim"] for student in students}

    return {
        "jumlah": len(students),
        "rata_rata": round(sum(scores) / len(scores), 2),
        "tertinggi": max(scores),
        "terendah": min(scores),
        "nim_unik": len(unique_nim)
    }


def add_student(students, nim, nama, nilai):
    """Menambahkan mahasiswa jika data valid dan NIM belum ada."""
    if not nim or not nama or not 0 <= nilai <= 100:
        return False

    if any(student["nim"] == nim for student in students):
        return False

    students.append({
        "nim": nim,
        "nama": nama,
        "nilai": float(nilai)
    })
    return True


def delete_student(students, nim):
    """Menghapus mahasiswa berdasarkan NIM."""
    for index, student in enumerate(students):
        if student["nim"] == nim:
            del students[index]
            return True

    return False
