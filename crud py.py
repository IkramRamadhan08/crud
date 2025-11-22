import os
from tabulate import tabulate

# Dictionary data mahasiswa
data = {}

def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def tambah_data():
    clear()
    print("=== Tambah Data Mahasiswa ===")
    nama = input("Nama mahasiswa : ")
    tugas = float(input("Nilai Tugas  : "))
    uts = float(input("Nilai UTS    : "))
    uas = float(input("Nilai UAS    : "))

    akhir = hitung_nilai_akhir(tugas, uts, uas)
    data[nama] = {
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": akhir
    }
    print("\nData berhasil ditambah!")
    input("Tekan Enter untuk kembali...")

def tampilkan_data():
    clear()
    print("=== Daftar Nilai Mahasiswa ===")

    if not data:
        print("Belum ada data.")
    else:
        table = []
        for nama, nilai in data.items():
            table.append([nama, nilai["tugas"], nilai["uts"], nilai["uas"], f"{nilai['akhir']:.2f}"])
        print(tabulate(table, headers=["Nama", "Tugas", "UTS", "UAS", "Akhir"], tablefmt="grid"))

    input("\nTekan Enter untuk kembali...")

def ubah_data():
    clear()
    print("=== Ubah Data Mahasiswa ===")
    nama = input("Masukkan nama mahasiswa: ")

    if nama in data:
        print("\nData lama:")
        print(f"Tugas: {data[nama]['tugas']}")
        print(f"UTS  : {data[nama]['uts']}")
        print(f"UAS  : {data[nama]['uas']}")
        print()

        tugas = float(input("Nilai Tugas baru: "))
        uts = float(input("Nilai UTS baru  : "))
        uas = float(input("Nilai UAS baru  : "))

        akhir = hitung_nilai_akhir(tugas, uts, uas)
        data[nama] = {
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "akhir": akhir
        }
        print("\nData berhasil diubah!")
    else:
        print("Nama tidak ditemukan!")

    input("Tekan Enter untuk kembali...")

def hapus_data():
    clear()
    print("=== Hapus Data Mahasiswa ===")
    nama = input("Nama mahasiswa yang akan dihapus: ")

    if nama in data:
        del data[nama]
        print("Data berhasil dihapus!")
    else:
        print("Nama tidak ditemukan!")

    input("Tekan Enter untuk kembali...")

def cari_data():
    clear()
    print("=== Cari Data Mahasiswa ===")
    nama = input("Masukkan nama mahasiswa: ")

    if nama in data:
        n = data[nama]
        print("\nData ditemukan:")
        print(f"Nama  : {nama}")
        print(f"Tugas : {n['tugas']}")
        print(f"UTS   : {n['uts']}")
        print(f"UAS   : {n['uas']}")
        print(f"Akhir : {n['akhir']:.2f}")
    else:
        print("Nama tidak ditemukan!")

    input("Tekan Enter untuk kembali...")

# ================================================================
# Menu Utama
# ================================================================
while True:
    clear()
    print("=== PROGRAM CRUD NILAI MAHASISWA ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("0. Keluar")
    pilihan = input("\nPilih menu: ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        ubah_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "5":
        cari_data()
    elif pilihan == "0":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter...")
