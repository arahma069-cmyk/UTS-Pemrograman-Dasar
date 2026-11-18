from mahasiswa.data import (
    load_students, search_student, filter_students, calculate_summary,
    add_student, delete_student
)
from mahasiswa.file_handler import load_csv, save_json, save_csv
from mahasiswa.utils import print_students, get_valid_score

DATA_FILE = "data/mahasiswa.csv"
OUTPUT_JSON = "output/hasil_analisis.json"
OUTPUT_CSV = "output/hasil_analisis.csv"


def show_menu():
    print("\n=== SISTEM PENGELOLAAN DATA MAHASISWA ===")
    print("1. Tampilkan semua mahasiswa")
    print("2. Cari mahasiswa berdasarkan NIM")
    print("3. Filter mahasiswa berdasarkan nilai minimum")
    print("4. Tampilkan rekapitulasi nilai")
    print("5. Tambah mahasiswa")
    print("6. Hapus mahasiswa")
    print("7. Simpan hasil ke JSON dan CSV")
    print("0. Keluar")


def main():
    students = load_csv(DATA_FILE)
    print(f"Data awal berhasil dimuat: {len(students)} mahasiswa.")

    while True:
        show_menu()
        choice = input("Pilih menu: ").strip()

        if choice == "1":
            print_students(students)

        elif choice == "2":
            nim = input("Masukkan NIM: ").strip()
            result = search_student(students, nim)
            if result:
                print_students([result])
            else:
                print("Mahasiswa dengan NIM tersebut tidak ditemukan.")

        elif choice == "3":
            try:
                minimum = get_valid_score("Masukkan nilai minimum (0-100): ")
                result = filter_students(students, minimum)
                print_students(result)
                print(f"Jumlah mahasiswa yang memenuhi: {len(result)}")
            except ValueError as error:
                print(f"Input tidak valid: {error}")

        elif choice == "4":
            summary = calculate_summary(students)
            print("\n=== REKAPITULASI ===")
            print(f"Jumlah mahasiswa : {summary['jumlah']}")
            print(f"Rata-rata nilai  : {summary['rata_rata']}")
            print(f"Nilai tertinggi  : {summary['tertinggi']}")
            print(f"Nilai terendah   : {summary['terendah']}")
            print(f"Jumlah NIM unik  : {summary['nim_unik']}")

        elif choice == "5":
            nim = input("NIM: ").strip()
            nama = input("Nama: ").strip()
            try:
                nilai = get_valid_score("Nilai (0-100): ")
                if add_student(students, nim, nama, nilai):
                    print("Data mahasiswa berhasil ditambahkan.")
                else:
                    print("Gagal: NIM sudah terdaftar atau data tidak lengkap.")
            except ValueError as error:
                print(f"Input tidak valid: {error}")

        elif choice == "6":
            nim = input("Masukkan NIM yang akan dihapus: ").strip()
            if delete_student(students, nim):
                print("Data berhasil dihapus.")
            else:
                print("Data tidak ditemukan.")

        elif choice == "7":
            try:
                summary = calculate_summary(students)
                save_json(OUTPUT_JSON, {"mahasiswa": students, "rekapitulasi": summary})
                save_csv(OUTPUT_CSV, students)
                print(f"Hasil tersimpan di {OUTPUT_JSON} dan {OUTPUT_CSV}.")
            except OSError as error:
                print(f"Gagal menyimpan file: {error}")

        elif choice == "0":
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak tersedia. Masukkan angka 0 sampai 7.")


if __name__ == "__main__":
    main()
