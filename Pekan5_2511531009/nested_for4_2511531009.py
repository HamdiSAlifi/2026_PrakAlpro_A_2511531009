tinggi_1009 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_1009 % 2 != 0:
    print("Tinggi harus bilangan genap")
else:
    a_1009 = tinggi_1009
    c_1009 = a_1009
    lebar_1009 = (2 * tinggi_1009) - 2
    
    for i_1009 in range(1, tinggi_1009 + 1):
        b_1009 = c_1009 + 1
        
        for j_1009 in range(1, lebar_1009+1):
            
            if i_1009 == 1 or i_1009 == tinggi_1009:
                if j_1009 == 1 or j_1009 == lebar_1009:
                    print("#", end="")
                else:
                    print("=", end="")
            else: 
                if j_1009 == 1 or j_1009 == lebar_1009:
                    print("|", end="")
                else:
                    if j_1009 == c_1009:
                        print("<", end="")
                    elif j_1009 == b_1009:
                        print(">", end="")
                    elif j_1009 == (lebar_1009 - c_1009):
                        print("<", end="")
                    elif j_1009 == (lebar_1009 - c_1009 + 1):
                        print(">", end="")
                    elif j_1009 > b_1009 and j_1009 < (lebar_1009 - c_1009):
                        print(".", end="")
                    else:
                        print(" ", end="")
                        
        print()
            
        a_1009 -= 2
        
        if a_1009 <= 0:
            c_1009 = (-a_1009) + 2
        else:
            c_1009 = a_1009    
        
        