print("==============================")
print("     2. OPERATOR BITWISE      ")
print("==============================")

# input angka
angka1_1009 = int(input("input angka 1: "))
angka2_1009 = int(input("input angka 2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =", angka1_1009, "| biner =", bin(angka1_1009))
print("angka1 =", angka2_1009, "| biner =", bin(angka2_1009))

# Bitwise AND
hasil_1009 = angka1_1009 & angka2_1009
print("\nBitwise AND (&)")
print(angka1_1009, "&", angka2_1009, "=", hasil_1009)
print("\nBiner hasil =", bin(hasil_1009))
print("\nBiner hasil (8 bit) =", format(hasil_1009, "08b"))

# Bitwise OR
hasil_1009 = angka1_1009 | angka2_1009
print("\nBitwise OR (|)")
print(angka1_1009, "|", angka2_1009, "=", hasil_1009)
print("\nBiner hasil =", bin(hasil_1009))
print("\nBiner hasil (8 bit) =", format(hasil_1009, "08b"))

# Bitwise XOR
hasil_1009 = angka1_1009 ^ angka2_1009
print("\nBitwise XOR (^)")
print(angka1_1009, "^", angka2_1009, "=", hasil_1009)
print("\nBiner hasil =", bin(hasil_1009))
print("\nBiner hasil (8 bit) =", format(hasil_1009, "08b"))

# Bitwise NOT
hasil_1009 = ~angka1_1009
print("\nBitwise NOT (~)")
print("~", angka1_1009, "=", hasil_1009)
print("\nBiner hasil =", bin(hasil_1009))
print("\nBiner hasil (8 bit) =", format(hasil_1009, "08b"))

 
# Left Shift
jumlah_geser_1009 = int(input("\nMasukkan jumlah pergeseran bit:"))

hasil_1009 = angka1_1009 << jumlah_geser_1009
print("\nBitwise Left Shift (<<)")
print(angka1_1009, "<<", jumlah_geser_1009, "=", hasil_1009)
print("\nBiner hasil =", bin(hasil_1009))
print("\nBiner hasil (8 bit) =", format(hasil_1009, "08b"))
 
# Left Shift
hasil_1009 = angka1_1009 >> jumlah_geser_1009
print("\nBitwise Right Shift (>>)")
print(angka1_1009, ">>", jumlah_geser_1009, "=", hasil_1009)
print("\nBiner hasil =", bin(hasil_1009))
print("\nBiner hasil (8 bit) =", format(hasil_1009, "08b"))
 