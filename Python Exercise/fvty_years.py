usia = int(input("How old r u? "))
tahun = int(input("What years is it now? "))
future = int(input("Future years? "))


def fvty(usia):
    nom = future - usia
    show = tahun + nom
    return show

show = fvty(usia)
print(f"u'll be {future} years at {show}")