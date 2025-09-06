# Mengimpor fungsi konversi suhu dari modul utils.py
from utils import (konversi_suhu)

# Mencetak judul program
print("=== Konversi Suhu ===")

# Meminta input dari pengguna dan menampilkan hasil konversi
while True:    
    try:
        nilai = float(input("Masukkan nilai suhu: "))
        dari = input("Dari satuan (C/F/K): ").strip().upper()
        ke = input("Ke satuan (C/F/K): ").strip().upper()

        hasil = konversi_suhu(nilai, dari, ke)
        print(f"Hasil: {nilai:.2f}°{dari} = {hasil:.2f}°{ke}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
