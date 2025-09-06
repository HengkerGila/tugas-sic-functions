# Fungsi konversi suhu
def konversi_suhu(nilai, dari, ke):
    """Mengonversi suhu dari satu satuan ke satuan lain.

    Args:
        nilai (float): Nilai suhu yang akan dikonversi.
        dari (str): Satuan asal ('C', 'F', 'K').
        ke (str): Satuan tujuan ('C', 'F', 'K').

    Returns:
        float: Nilai suhu setelah konversi.
    """
    if dari == ke:
        return nilai
    
    # Validasi input
    if nilai < 0 and dari == 'K':
        raise ValueError("Suhu dalam Kelvin tidak boleh negatif.")

    # Konversi ke Celsius terlebih dahulu
    if dari == 'C':
        celsius = nilai
    elif dari == 'F':
        celsius = (nilai - 32) * 5.0/9.0
    elif dari == 'K':
        celsius = nilai - 273.15
    else:
        raise ValueError("Satuan asal tidak valid. Gunakan 'C', 'F', atau 'K'.")

    # Konversi dari Celsius ke satuan tujuan
    if ke == 'C':
        return celsius
    elif ke == 'F':
        return celsius * 9.0/5.0 + 32
    elif ke == 'K':
        return celsius + 273.15
    else:
        raise ValueError("Satuan tujuan tidak valid. Gunakan 'C', 'F', atau 'K'.")
