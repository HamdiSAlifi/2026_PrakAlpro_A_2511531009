# Program: Sistem Simulasi Transaksi Toko (NIM: 2511531009)

# 1. Input Data Pelanggan & Transaksi
print("=== SISTEM TRANSAKSI TOKO ===\n")

nama_1009 = input("Masukkan Nama Pelanggan : ")
status_input_1009 = input("Masukkan Status Pelanggan (member/nonmember) : ")
total_belanja_1009 = float(input("Masukkan Total Belanja : "))
jumlah_barang_1009 = int(input("Masukkan Jumlah Barang : "))
kode_promo_input_1009 = input("Masukkan Kode Promo : ")

# Break line setelah input terakhir
print()

# Normalisasi teks input
status_1009 = status_input_1009.strip().lower()
kode_promo_1009 = kode_promo_input_1009.strip().upper()

# Daftar promo resmi
promo_tersedia_1009 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]


# 2. Operator Keanggotaan (Membership)
is_promo_valid_1009 = kode_promo_1009 in promo_tersedia_1009
is_promo_invalid_1009 = kode_promo_1009 not in promo_tersedia_1009


# 3. Operator Perbandingan (Comparison)
syarat_belanja_1009 = total_belanja_1009 >= 200000
syarat_barang_1009 = jumlah_barang_1009 >= 3
is_member_1009 = status_1009 == "member"


# 4. Operator Logika (Logical)
dapat_diskon_1009 = is_member_1009 and syarat_belanja_1009
dapat_promo_1009 = (syarat_barang_1009 and is_promo_valid_1009) or dapat_diskon_1009
is_nonmember_1009 = not is_member_1009


# 5. Operator Aritmatika & Penugasan (Assignment)
persen_diskon_1009 = 0.10 if dapat_diskon_1009 else 0.0
besarnya_diskon_1009 = total_belanja_1009 * persen_diskon_1009

total_pembayaran_1009 = total_belanja_1009 - besarnya_diskon_1009

# Augmented assignment (-=) potongan tambahan promo HEMAT10
if is_promo_valid_1009 and kode_promo_1009 == "HEMAT10":
    potongan_promo_1009 = 10000.0
    total_pembayaran_1009 -= potongan_promo_1009
else:
    potongan_promo_1009 = 0.0

rata_rata_harga_1009 = total_pembayaran_1009 / jumlah_barang_1009 if jumlah_barang_1009 > 0 else 0.0
sisa_pembagian_1009 = int(total_pembayaran_1009) % jumlah_barang_1009 if jumlah_barang_1009 > 0 else 0


# 6. Operator Identitas (Identity)
objek_a_1009 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]
objek_b_1009 = promo_tersedia_1009          # Alias (referensi memori sama)
objek_c_1009 = promo_tersedia_1009.copy()   # Duplikat (referensi memori berbeda)

identitas_alias_1009 = objek_b_1009 is promo_tersedia_1009
identitas_copy_1009 = objek_c_1009 is not promo_tersedia_1009
nilai_sama_1009 = objek_c_1009 == promo_tersedia_1009


# 7. Operator Bitwise
# Representasi biner kondisi transaksi
bit_member_1009 = 0b0001 if is_member_1009 else 0b0000
bit_belanja_1009 = 0b0010 if syarat_belanja_1009 else 0b0000
bit_barang_1009 = 0b0100 if syarat_barang_1009 else 0b0000
bit_promo_1009 = 0b1000 if is_promo_valid_1009 else 0b0000

# Bitwise OR (|), AND (&), XOR (^), dan Shift (<< / >>)
kode_status_1009 = bit_member_1009 | bit_belanja_1009 | bit_barang_1009 | bit_promo_1009

cek_member_1009 = kode_status_1009 & 0b0001
cek_promo_1009 = kode_status_1009 & 0b1000

kode_referensi_1009 = 0b1011
beda_status_1009 = kode_status_1009 ^ kode_referensi_1009

shift_left_1009 = kode_status_1009 << 1
shift_right_1009 = kode_status_1009 >> 1


# 8. Output Ringkasan Hasil Program
print("=== DATA TRANSAKSI ===")
print(f"Nama Pelanggan        : {nama_1009}")
print(f"Status Pelanggan      : {status_1009}")
print(f"Total Belanja         : Rp{total_belanja_1009:.0f}")
print(f"Jumlah Barang         : {jumlah_barang_1009}")
print(f"Kode Promo            : {kode_promo_1009}")

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000        : {syarat_belanja_1009}")
print(f"Jumlah Barang >= 3         : {syarat_barang_1009}")
print(f"Status Member              : {is_member_1009}")
print(f"Kode Promo Tersedia        : {is_promo_valid_1009}")
print(f"Mendapatkan Diskon         : {dapat_diskon_1009}")
print(f"Mendapatkan Promo          : {dapat_promo_1009}")

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                     : Rp{besarnya_diskon_1009:.0f}")
print(f"Total Pembayaran           : Rp{total_pembayaran_1009:.0f}")
print(f"Rata-rata Harga Barang     : Rp{rata_rata_harga_1009:.2f}")
print(f"Sisa Bagi Pembayaran % Qty : {sisa_pembagian_1009}")

print("\n=== HAK AKSES PELANGGAN ===")
print(f"Kode Hak Akses             : {format(kode_status_1009, '04b')}")
print(f"Member Access              : {is_member_1009}")
print(f"Promo Access               : {is_promo_valid_1009}")
print(f"Free Shipping Access       : {is_promo_valid_1009 and kode_promo_1009 == 'GRATISONGKIR'}")

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print("0001 | 0010 | 0100 | 1000")
print(f"Kode Biner    : {format(kode_status_1009, '04b')}")
print(f"Kode Desimal  : {kode_status_1009}")

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{format(kode_status_1009, '04b')} & 0001")
print(f"Hasil Biner   : {format(cek_member_1009, '04b')}")
print(f"Hasil Desimal : {cek_member_1009}")

print("\nCek Promo")
print(f"{format(kode_status_1009, '04b')} & 1000")
print(f"Hasil Biner   : {format(cek_promo_1009, '04b')}")
print(f"Hasil Desimal : {cek_promo_1009}")

print("\n=== Perbandingan Status ===")
print(f"Kode Transaksi : {format(kode_status_1009, '04b')}")
print(f"Kode Referensi : {format(kode_referensi_1009, '04b')}")
print(f"{format(kode_status_1009, '04b')} ^ {format(kode_referensi_1009, '04b')}")
print(f"Hasil Biner   : {format(beda_status_1009, '04b')}")
print(f"Hasil Desimal : {beda_status_1009}")

print("\n=== Shift ===")
print(f"{format(kode_status_1009, '04b')} << 1")
print(f"Hasil Biner   : {format(shift_left_1009, '05b')}")
print(f"Hasil Desimal : {shift_left_1009}")

print("\n=== SELESAI ===")