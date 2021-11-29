angka = int(input("Masukkan angka: "))

for i in range(1, angka+1):
    if i % 2 == 0:
        print(f"{i} adalah bilangan genap")
    else:
        print(f"{i} adalah bilangan ganjil")