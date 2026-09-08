is_lulus_1009 = True
is_cumlaude_1009 = True

nilai_1009 = 85
batas_lulus_1009 = 75

status_kelulusan_1009 = nilai_1009 >= batas_lulus_1009

print("=== CHECK STASTUS KELULUSAN ===")
print("Nilai        : ", nilai_1009)
print("Apakah Lulus : ", status_kelulusan_1009)
if is_lulus_1009 and is_cumlaude_1009:
    print("Selamat anda lulus dengan predikat Cum Laude")