question = input("Apakah anda suka bubur ayam? (ya/ tidak)")

if question != "ya":
    print("cobain deh, gue ada saran bubur yg enak")
    coba = input("mau coba ngga? (mau/ ga)")
    if coba == "mau":
        print("oke nanti gue tlp ya")
    else:
        print("okee dehh")
elif "ya":
    ya = (input("diaduk/ engga?"))
    if ya == "diaduk":
        print("anda pemberani")
    else:
        print("anda suka keindahan")