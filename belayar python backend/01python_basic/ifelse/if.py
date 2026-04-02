def ganjil_genap() :
    angka = int(input("masukan angka : "))

    if angka % 2 == 0 :
        print(f"ini adalah angka genap : {angka}")
    else : print(f"ini adalah angka ganjil {angka}")

def profile_game() :
    nama = input("masukan nama kamu : ")
    level = int(input("masukan level kamu : "))
    hp = float(input("masukan hp kamu : "))
    status = str(input("apakah kamu sedang online? masukan (y/n) : "))

    print(f"nama kamu adalah : {nama}")
    print(f"level kamu adalah : {level}")
    print(f"hp kamu sekarang : {hp}")
    print("-----------------------")

    if status == "y" :
        print("kamu sedang online")
    else : 
        print("kamu sedang offline")

def cek_xp () :
    xp_sekarang = int(input("masukan xp kamu sekarang : "))
    xp_butuh = int(input("masukan xp yang di butuhkan : "))
    
    level_up = xp_sekarang >= xp_butuh
    print(f"apakah kamu bisa naik level sekarang?, status = {level_up}")
cek_xp()