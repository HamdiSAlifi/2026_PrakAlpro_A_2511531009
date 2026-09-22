umur_1009 = int(input("Input umur anda: "))
sim_1009 = input("apakah anda sudah punya SIM C? (y/n): ")

if (umur_1009 >= 17) and sim_1009 == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")
    
if (umur_1009 >= 17) and sim_1009 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")
    
if (umur_1009 < 17) and sim_1009 == 'y':
    print("Anda belum cukup umur punya SIM")
    
if (umur_1009 < 17) and sim_1009 != 'y':
    print("Anda belum cukup umur bawa motor")