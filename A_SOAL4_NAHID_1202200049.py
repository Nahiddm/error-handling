try:
    nama=input("Masukkan nama Gen (minimal 5 huruf) : ")
    assert len(nama)>=5
    jumlah=int(input("Masukkan Jumlah anggotan gen (tidak boleh 0): "))
    assert jumlah > 0
except AssertionError:
    print("Isi sesuai ketentuan yang diberikan")
finally:
    print("Percobaan selesai")