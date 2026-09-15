angka1_1009 = int(input("input angka 1: "))
angka2_1009 = int(input("input angka 2: "))

print("\nNiali angka 1 =", angka1_1009)
print("Nilai angka 2 =", angka2_1009)

# =
hasil_1009 = angka1_1009
print("\nAssigmnent Biasa")
print("Hasil =", hasil_1009)

# +=
hasil_1009 = angka1_1009
hasil_1009 += angka2_1009
print("\nAssigmnent Penambahan")
print("Hasil =", hasil_1009)

# -=
hasil_1009 = angka1_1009
hasil_1009 -= angka2_1009
print("\nAssigmnent Pengurangan")
print("Hasil =", hasil_1009)

# *=
hasil_1009 = angka1_1009
hasil_1009 *= angka2_1009
print("\nAssigmnent Perkalian")
print("Hasil =", hasil_1009)

# /=
if angka2_1009 != 0:
    hasil_1009 = angka1_1009
    hasil_1009 /= angka2_1009
    print("\nAssigmnent Pembagian")
    print("Hasil =", hasil_1009)
    
    hasil_1009 = angka1_1009
    hasil_1009 //= angka2_1009
    print("\nAssigmnent Pembagian Bulat")
    print("Hasil =", hasil_1009)

    hasil_1009 = angka1_1009
    hasil_1009 %= angka2_1009
    print("\nAssigmnent Sisa Bagi")
    print("Hasil =", hasil_1009)
else:
    print("\nPembagian tidak dapat dilakukan")
    print("Angka tidak boleh bernilai nol")
    