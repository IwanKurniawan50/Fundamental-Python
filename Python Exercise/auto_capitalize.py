def auto_cap(kalimat):          # buat fungsi dengan parameter kalimat
    wadah = []                  # buat variabel berisi list untuk menampung hasil akhir
    pecah = kalimat.split()     # memecah kalimat lalu dimasukkan ke dalam variabel
    for i in pecah:             # perulangan setiap kalimat di variabel pecah (isi sudah di pecah per kata) 
        wadah.append(i.capitalize()) # wadah ditambah kata yg sudah di capitalize di pecah  
    wadah = " ".join(wadah)     # join -> list menjadi string
    return wadah                # mengembalikan nilai wadah

print(auto_cap("mantap say"))

### SPLIT ###
# Hasil split akan menjadi list
barcelona = "messi. puyol. xavi"

print(barcelona.split(". "))

### JOIN ###
# Mengubah list -> string
game = ["ctr", "bike", "mountain"]

nah = " ".join(game)
print(nah)
            