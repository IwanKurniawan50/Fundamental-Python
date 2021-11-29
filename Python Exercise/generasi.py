nama = input("Masukkan nama anda : ")
tahun = int(input("Tahun berapa anda lahir? "))

if tahun >= 1994 and tahun <= 1964:
    print(nama, "anda adalah Generasi boomer")
elif tahun >= 1965 and tahun <= 1979:
    print(nama, "anda adalah Generasi X")
elif tahun >= 1980 and tahun <= 1994:
    print(nama, "anda adalah Generasi Y (Millenials)")
elif tahun >= 1995 and tahun >= 2015:
    print(nama, "anda adalah Generasi Z")
else:
    print("error")
