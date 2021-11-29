massa = int(input("berapa massa tubuh anda?(kg) : "))
tinggi = int(input("berapa tinggi badan anda?(cm):  "))

IMT = massa / (tinggi/100)**2
print(IMT)
if IMT < 18.5:
    print("kurang")
elif IMT >= 18.5 and IMT <= 24.9:
    print("ideal")
elif IMT >= 25 and IMT <= 29.9:
    print("berlebih")
elif IMT >= 30 and IMT <= 39.9:
    print("sangat berlebih")
elif IMT > 39.9:
    print("obesitas")
else:
    print("error")
 