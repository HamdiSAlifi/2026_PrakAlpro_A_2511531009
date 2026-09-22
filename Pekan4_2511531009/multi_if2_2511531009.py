total_belanja_1009 = float(input("Masukkan total belanja (Rp): "))

input_member_1009 = input("Apakah Anda member? (y/n): ").strip().lower()
is_member_1009 = input_member_1009 in ['y', "ya"]

input_promo_1009 = input("Apakah kode promo valid? (y/n): ").strip().lower()
kode_promo_valid_1009 = input_promo_1009 in ["y", "ya"]

total_diskon_persen_1009 = 0

if total_belanja_1009 > 100000:
    total_diskon_persen_1009 += 10

if is_member_1009:
    total_diskon_persen_1009 += 5
    
if kode_promo_valid_1009:
    total_diskon_persen_1009 += 15
    
nominal_diskon_1009 = total_belanja_1009 * (total_diskon_persen_1009 / 100)
total_bayar_1009 = total_belanja_1009 - nominal_diskon_1009

print("\n--- [ RINCIAN PEMBAYARAN ] ---")
print(f"Total Diskon : {total_diskon_persen_1009}% (Rp{nominal_diskon_1009:,.0f})")
print(f"Total Bayar  : Rp{total_bayar_1009:,.0f}")

print(f"Total diskon yang anda dapatkan: Rp{total_diskon_persen_1009}%")