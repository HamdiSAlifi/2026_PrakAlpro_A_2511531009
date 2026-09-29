batas_1009 = int(input("Masukkan nilai batas: "))
for i_1009 in range(1, batas_1009 + 1):
    for j_1009 in range(1, (-1 * i_1009 + batas_1009) + 1):
        print(".", end="")
    print(i_1009)