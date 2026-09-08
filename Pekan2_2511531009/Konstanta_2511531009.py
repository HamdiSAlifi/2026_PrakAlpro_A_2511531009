from typing import final
PI_xc: final = 3.14

print("pi: %f" % (PI_xc))
jari_xc = float(input("masukkan nilai jari-jari : "))
luas_xc = PI_xc * jari_xc * jari_xc

print("Luas lingkaran dengan jari jari %f adalah %f" % (jari_xc, luas_xc))