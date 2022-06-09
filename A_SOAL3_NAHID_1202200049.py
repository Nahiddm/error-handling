list= ["lala","dede","lulu","doni"] 
def indeks():
    index=int(input("Masukkan index: "))
    try:
        print("Data index ke -", index, "adalah", list[index])
    except IndexError:
        print("Indexnya tidak ada")
indeks()