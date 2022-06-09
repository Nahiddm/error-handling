print("Operasi Pembagian")
angka1 = int(input("Masukkan angka1 : "))
angka2 = int(input("Masukkan angka2 : "))
try:
    count = angka1 / angka2
    print("hasil pembagian : ",count)
except:
    print("Anda tidak dapat membagi bilangan dengan angka 0")       