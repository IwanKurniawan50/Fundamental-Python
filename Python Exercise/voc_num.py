# Vocal to Number

def ubah(teks):
    convert = {"a":4, "i":1, "e":3, "o":0}
    huruf = list(convert.keys())
    final = []
    x = teks.split()
    for a in range(len(x)):
        for b in x[a]:
            if not b in huruf:
                final.append(b)
            else:
                angka = str(convert[b])
                final.append(angka)
    final = "".join(final)
    print(final)
    
kata = "kemerdekaan"
ubah(kata)

## CONVERT
convert = {"a":4, "i":1, "e":3, "o":0}
huruf = list(convert.keys())
print(huruf)