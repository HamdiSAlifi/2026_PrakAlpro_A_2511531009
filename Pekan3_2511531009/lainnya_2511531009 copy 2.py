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

# +=
hasil_1009 = nilai_dicari_1009 not in data_1009
print("\nOperator Keanggotaan NOT IN")
print(f"{nilai_dicari_1009} in {data_1009} = ", hasil_1009)