angka1_1009 = int(input("input angka 1: "))
angka2_1009 = int(input("input angka 2: "))

# +
hasiladd_1009 = angka1_1009 + angka2_1009
print("\nOperator Penjumlahan")
print("Hasil: ", hasiladd_1009)

# -
hasilmin_1009 = angka1_1009 - angka2_1009
print("\nOperator Pengurangan")
print("Hasil: ", hasilmin_1009)

# *
hasiltimes_1009 = angka1_1009 * angka2_1009
print("\nOperator Perkalian")
print("Hasil: ", hasiltimes_1009)

# /
if angka2_1009 != 0:
    hasildiv_1009 = angka1_1009 / angka2_1009
    print("\nOperator Pembagian")
    print("Hasil: ", hasildiv_1009)

    hasildivv_1009 = angka1_1009 // angka2_1009 # Round floor
    print("\nOperator Pembagian Bulat")
    print("Hasil: ", hasildivv_1009)

    hasilmod_1009 = angka1_1009 % angka2_1009
    print("\nOperator Sisa Bagi")
    print("Hasil: ", hasilmod_1009)
else:
    print("Angka Tidak Boleh Bernilai Nol")
    


# Pangkat
hasilpow_1009 = angka1_1009 ** angka2_1009
print("\nOperator Pangkat")
print("Hasil: ", hasilpow_1009)