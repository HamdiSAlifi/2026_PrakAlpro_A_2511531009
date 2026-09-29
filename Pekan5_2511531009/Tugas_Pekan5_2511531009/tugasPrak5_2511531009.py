tinggi_1009 = int(input("Masukkan tinggi segitiga: "))

for i_1009 in range(1, tinggi_1009 + 1):
    print(" " * (tinggi_1009 - i_1009), end="")
    for j_1009 in range(i_1009):
        if j_1009 == i_1009 - 1:
            print("*", end="")
        else:
            print("* ", end="")
    print()
