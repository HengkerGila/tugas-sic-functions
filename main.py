# Mengimpor fungsi konversi suhu dari modul utils.py
from utils import (konversi_suhu)

# Mencetak judul program
print("Program Konversi Suhu")
print("======================")

# Meminta input dari pengguna dan menampilkan hasil konversi
while True:    
    try:
        nilai = float(input("Masukkan nilai suhu: "))
        dari = input("Masukkan satuan asal (C, F, K): ").strip().upper()
        ke = input("Masukkan satuan tujuan (C, F, K): ").strip().upper()

        hasil = konversi_suhu(nilai, dari, ke)
        print(f"Hasil konversi: {hasil:.2f} {ke}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
