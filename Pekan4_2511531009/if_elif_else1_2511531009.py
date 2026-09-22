umur_1009 = int(input("Input umur anda: "))
sim_1009 = input("apakah anda sudah punya SIM C? (y/n): ")[0]

if (umur_1009 >= 17) and sim_1009 == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")

elif umur_1009 >= 17 and sim_1009 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")
    
elif umur_1009 < 17 and sim_1009 == 'y':
    print("Anda belum cukup umur punya SIM")
    
else:
    print("Anda belum cukup umur dan tidak boleh bawa motor")
    
print("program selesai")