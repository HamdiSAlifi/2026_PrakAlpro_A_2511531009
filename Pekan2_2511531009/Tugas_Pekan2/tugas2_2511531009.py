from typing import Final

# 1. Deklarasi Konstanta Batas Kelulusan
BATAS_LULUS_1009: Final[float] = 75.0

# 2. Input Data Pelanggan / Praktikan
print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_1009 = input("Masukkan Nama Mahasiswa : ")
jenis_kelamin_1009 = input("Masukkan Jenis Kelamin (L/P): ")
umur_1009 = int(input("Masukkan Umur : "))
skor_tes_1009 = float(input("Masukkan Skor Tes Awal : "))

# Alamat multiline (String tiga tanda petik)
alamat_1009 = """Jl. Kampus Unand,
Kecamatan Pauh,
Kota Padang"""

# Variabel Kompleks sebagai Token Identifikasi
token_1009: complex = 100 + 3j

# 3. Evaluasi Status Kelulusan (Boolean)
is_lulus_1009: bool = skor_tes_1009 >= BATAS_LULUS_1009


# 4. Menampilkan Data & Tipe Data (type())
print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print(f"Nama Mahasiswa : {nama_1009} | Tipe: {type(nama_1009)}")
print(f"Jenis Kelamin  : {jenis_kelamin_1009} | Tipe: {type(jenis_kelamin_1009)}")
print(f"Alamat Domisili:\n{alamat_1009} | Tipe: {type(alamat_1009)}")
print(f"Umur           : {umur_1009} tahun | Tipe: {type(umur_1009)}")
print(f"Skor Tes Awal  : {skor_tes_1009} | Tipe: {type(skor_tes_1009)}")
print(f"ID Token Sinyal: {token_1009} | Tipe: {type(token_1009)}")

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print(f"Batas Minimum Nilai: {BATAS_LULUS_1009}")
print(f"Apakah Dinyatakan Lulus?: {is_lulus_1009} | Tipe: {type(is_lulus_1009)}")