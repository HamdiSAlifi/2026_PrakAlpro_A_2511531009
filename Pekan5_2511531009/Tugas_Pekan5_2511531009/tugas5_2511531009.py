print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
n_1009 = int(input("Masukkan ukuran skala jam pasir (N): "))

if n_1009 <= 0:
    print("Ukuran N harus bilangan bulat positif")
else:
    #  BINGKAI ATAS
    print("#", end="")
    for garis_1009 in range(4 * n_1009 + 5):
        print("=", end="")
    print("#")

    #  JAM PASIR ATAS (baris N - 1) 
    for baris_1009 in range(n_1009, 0, -1):
        print("|", end=" ")                                   # pagar kiri + 1 spasi padding
        for spasi_1009 in range(2 * (n_1009 - baris_1009)):   # spasi penyeimbang kiri
            print(" ", end="")
        for angka_1009 in range(baris_1009, 0, -1):           # deret mundur: baris .. 1
            print(angka_1009, end=" ")
        print("<*>", end="")                                  # poros kristal
        for angka_1009 in range(1, baris_1009 + 1):           # deret maju: 1 .. baris
            print(" ", end="")
            print(angka_1009, end="")
        for spasi_1009 in range(2 * (n_1009 - baris_1009)):   # spasi penyeimbang kanan
            print(" ", end="")
        print(" |", end="")                                   # 1 spasi padding + pagar kanan
        print()

    #  POROS TITIK PUSAT
    print("|", end="")
    for spasi_1009 in range(2 * n_1009 + 1):
        print(" ", end="")
    print("<*>", end="")
    for spasi_1009 in range(2 * n_1009 + 1):
        print(" ", end="")
    print("|")

    #  JAM PASIR BAWAH (baris 1 - N) 
    for baris_1009 in range(1, n_1009 + 1):
        print("|", end=" ")
        for spasi_1009 in range(2 * (n_1009 - baris_1009)):
            print(" ", end="")
        for angka_1009 in range(baris_1009, 0, -1):
            print(angka_1009, end=" ")
        print("<*>", end="")
        for angka_1009 in range(1, baris_1009 + 1):
            print(" ", end="")
            print(angka_1009, end="")
        for spasi_1009 in range(2 * (n_1009 - baris_1009)):
            print(" ", end="")
        print(" |", end="")
        print()

    #  BINGKAI BAWAH 
    print("#", end="")
    for garis_1009 in range(4 * n_1009 + 5):
        print("=", end="")
    print("#")
