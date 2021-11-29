angka = int(input("Masukkan angka? ")) # fungis input meminta angka

def faktor(angka):                     # membuat fungsi faktor dengan parameter angka
    tampung = []                       # membuat variabel tampung, yang akan mengisi nilai akhir
    for i in range(1, angka+1):        # membuat perulangan di range 1 sampai angka+1
        if angka % i == 0:             # jika hasil bagi antara angka dengan i(perulangan range) hasilnya 0
            tampung.append(i)          # maka variabel tampung akan diisi dengan nilai i tsb
    return tampung                     # mengembalikan nilai tampung

tampung = faktor(angka)                            # memanggil fungsi faktor yg dimasukkan ke dalam variabel tampung
print(f"Faktor dari {angka} adalah: {tampung}")    # print