nilai1_1009 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
nilai2_1009 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true" == "true"

print("\nA1 =", nilai1_1009)
print("A2 =", nilai2_1009)

# and
hasil_1009 = nilai1_1009 and nilai2_1009
print("\nKonjungsi (AND)")
print(f"{nilai1_1009} AND {nilai2_1009} = ", hasil_1009)

# or
hasil_1009 = nilai1_1009 or nilai2_1009
print("\nDisjungsi (OR)")
print(f"{nilai1_1009} OR {nilai2_1009} = ", hasil_1009)

# NOT
hasil_1009 = not nilai1_1009
print("\nNegasi A1 (NOT)")
print(f"NOT {nilai1_1009} = ", hasil_1009)

hasil_1009 = not nilai2_1009
print("\nNegasi A2 (NOT)")
print(f"NOT {nilai2_1009} = ", hasil_1009)

# xor
hasil_1009 = nilai1_1009 != nilai2_1009
print("\nDisjungsi Ekslusif (XOR)")
print(f"{nilai1_1009} XOR {nilai2_1009} = ", hasil_1009)

