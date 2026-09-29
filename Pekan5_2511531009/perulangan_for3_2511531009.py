ulang_1009 = int(input("Masukkan jumlah perulangan: "))

jumlah_1009 = 0

for i_1009 in range(1, ulang_1009 + 1):
    print(i_1009, end=" ")
    jumlah_1009 = (jumlah_1009 + i_1009)
    
    if i_1009 < ulang_1009:
        print(" + ", end="")
    else:
        print(" = ", jumlah_1009, end="")
        
print()
print(f"Jumlah: {jumlah_1009}")