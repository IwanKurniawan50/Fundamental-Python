def hitung_huruf(kalimat):
    total_huruf = 0
    for i in kalimat:
        if i == "a":
            total_huruf += 1
    return total_huruf

print(hitung_huruf("everything can be fun yayaya"))