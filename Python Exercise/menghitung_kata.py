def hitung_kata(kalimat): # membuat fungsi hitung_kata dengan parameter kalimat
    total_kata = 1        # membuat variabel yg akan menampung total kata
    for i in kalimat:     # membuat perulangan di setiap kalimat
        if i == " ":       # jika setiap perulangan di kalimat terdapat ""
            total_kata += 1 # variabel total_kata akan menambah 1
    return total_kata       # mengembalikan nilai di total_kata

print(hitung_kata("hallo, its me")) # memanggil fungsi total_kata


