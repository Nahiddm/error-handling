try:
    bilangan1 = int(input("Masukkan Bilangan 1: "))
    bilangan2 = int(input("Masukkan Bilangan 2: "))
    bagi = bilangan1/bilangan2
except ZeroDivisionError:
    print("Program tidak dapat membagi oprasi pembagian dengan nol")
except ValueError:
    print("tipe data tidak sesuai!")
else:
    print("Total Hasil pembagian: ",bagi)

