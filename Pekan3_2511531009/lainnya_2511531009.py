print("==============================")
print("   1. OPERATOR KEANGGOTAAN    ")
print("==============================")

# input data
input_data_1009 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# input mmenjadi list integer
data_1009 = [int(angka.strip()) for angka in input_data_1009.split(",")]

nilai_dicari_1009 = int(input("masukkan angka yang ingin dicari: "))

# in
hasil_1009 = nilai_dicari_1009 in data_1009
print("\nOperator Keanggotaan IN")
print(f"{nilai_dicari_1009} in {data_1009} = ", hasil_1009)

# operator not in
hasil_1009 = nilai_dicari_1009 not in data_1009
print("\nOperator Keanggotaan NOT IN")
print(f"{nilai_dicari_1009} in {data_1009} = ", hasil_1009)

print("\n=====================================")
print("         2. OPERATOR IDENTITAS       ")
print("=====================================")

# objek1 menggunakan list dari input pengguna
objek1_1009 =data_1009

# objek2 merujuk pada objek yang sama dengan objek1
objek2_1009 = objek1_1009

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_1009 = data_1009.copy()

print("objek1 =", objek1_1009)
print("objek2 =", objek2_1009)
print("objek3 =", objek3_1009)

# Operator is
hasil_1009 = objek1_1009 is objek2_1009
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil_1009)

# Operator is not
hasil_1009 = objek1_1009 is not objek3_1009
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil_1009)

# membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 == objek3 =", objek1_1009 == objek3_1009)
print("objek1 == objek3 =", objek1_1009 is objek3_1009)
