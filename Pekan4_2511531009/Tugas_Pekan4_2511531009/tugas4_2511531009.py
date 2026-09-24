# Program: Sistem Loket Terpadu Alpro Adventure Park
# NIM    : 2511531009

# BAGIAN 1: Input Data Pengunjung
print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

nama_1009         = input("Masukkan Nama Pengunjung        : ")
umur_1009         = int(input("Input umur anda                 : "))
# Hanya ambil karakter pertama agar input 'ya' atau 'tidak' tetap terbaca konsisten
sim_1009          = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()[0]

print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

paket_1009        = int(input("Masukkan nomor paket (1-5)      : "))
jumlah_tiket_1009 = int(input("Masukkan jumlah tiket           : "))
input_member_1009 = input("Apakah Anda member? (y/t)       : ").strip().lower()
input_promo_1009  = input("Apakah kode promo valid? (y/t)  : ").strip().lower()

# Percabangan 1: if tunggal - validasi kelogisan jumlah tiket
if jumlah_tiket_1009 <= 0:
    print("\nPeringatan: Kuota tiket tidak valid! Jumlah tiket harus lebih dari 0.")

# Inisialisasi variabel wahana sebelum diisi oleh match-case
nama_wahana_1009  = ""
harga_satuan_1009 = 0
paket_valid_1009  = True

# Percabangan 2: match-case - pemilihan wahana dan harga satuan
match paket_1009:
    case 1:
        nama_wahana_1009  = "Wahana Safari Rimba"
        harga_satuan_1009 = 50000
    case 2:
        nama_wahana_1009  = "Wahana Arung Jeram"
        harga_satuan_1009 = 75000
    case 3:
        nama_wahana_1009  = "Wahana Motor ATV Ekstrim"
        harga_satuan_1009 = 120000
    case 4:
        nama_wahana_1009  = "Wahana Roller Coaster Kilat"
        harga_satuan_1009 = 100000
    case 5:
        nama_wahana_1009  = "Wahana All-Access VIP"
        harga_satuan_1009 = 220000
    case _:
        # Input di luar 1-5 tidak valid, eksekusi transaksi dihentikan
        print("\nPaket wahana tidak valid!")
        paket_valid_1009 = False

if paket_valid_1009 and jumlah_tiket_1009 > 0:

    print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

    # Percabangan 3: if-elif-else - validasi izin kendali wahana
    # Paket 3 memerlukan pengecekan SIM C karena melibatkan kendaraan bermotor
    if paket_1009 == 3:

        if umur_1009 >= 17 and sim_1009 == 'y':
            status_akses_1009 = "Anda sudah dewasa dan boleh mengendarai ATV sendiri."

        elif umur_1009 >= 17 and sim_1009 != 'y':
            status_akses_1009 = "Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur)."

        elif umur_1009 < 17 and sim_1009 == 'y':
            status_akses_1009 = "Identitas tidak valid: Belum cukup umur memiliki SIM."

        else:
            status_akses_1009 = "Anda belum cukup umur dan tidak boleh bawa motor ATV."

    else:
        # Untuk paket selain ATV, syarat minimum hanya usia 10 tahun
        if umur_1009 >= 10:
            status_akses_1009 = "Usia Anda memenuhi syarat untuk wahana ini."
        else:
            status_akses_1009 = "Maaf, usia Anda belum memenuhi syarat minimum (10 tahun) untuk wahana ini."

    print(f"Status Akses: {status_akses_1009}")

    # Hitung subtotal sebelum diskon diterapkan
    subtotal_1009             = harga_satuan_1009 * jumlah_tiket_1009
    total_diskon_persen_1009  = 0

    # Percabangan 4: Multi-if terpisah - akumulasi diskon bertingkat
    # Setiap blok dievaluasi sendiri sehingga diskon dapat menumpuk
    if subtotal_1009 >= 200000:
        total_diskon_persen_1009 += 10

    if input_member_1009 in ['y', 'ya']:
        total_diskon_persen_1009 += 5

    if input_promo_1009 in ['y', 'ya']:
        total_diskon_persen_1009 += 15

    if jumlah_tiket_1009 >= 5:
        total_diskon_persen_1009 += 5

    nominal_diskon_1009 = subtotal_1009 * (total_diskon_persen_1009 / 100)
    total_bayar_1009    = subtotal_1009 - nominal_diskon_1009

    # Percabangan 5: if-else - audit total bayar dan catatan layanan 
    if total_bayar_1009 > 300000:
        catatan_layanan_1009 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
    else:
        catatan_layanan_1009 = "Terima kasih telah berkunjung."

    print("\n--- Rincian Pembayaran ---")
    print(f"Wahana           : {nama_wahana_1009}")
    print(f"Nama Pengunjung  : {nama_1009}")
    print(f"Subtotal Belanja : Rp {subtotal_1009:,.0f}")
    print(f"Total Diskon     : {total_diskon_persen_1009}% (Rp {nominal_diskon_1009:,.0f})")
    print(f"Total Bayar      : Rp {total_bayar_1009:,.0f}")
    print(f"Catatan Layanan  : {catatan_layanan_1009}")

print("\nProgram Selesai")