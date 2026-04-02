 #teknik casting /////////////////////////////////
def latihan_castig ():
    nama = str(input("masukan angka = "))
    angka = 120
    nama = int(nama)
    print(nama + angka)


#test beli barang ////////////////////
def latihan_kasir ():
    harga = 10000
    bayar = int(input("uang kamu : "))
    proses = bayar >= harga 
    print(f"apakah bisa di beli? {proses}")
    

#latihan//////////////////////////
def data_diri():
    nama = str(input("masukan nama kamu :"))
    lahir = int(input("masukan tahun lahir mu,(cth:2006) : "))
    tinggi = float(input("masukan tinggi badan kamu : "))
    umur = 2026 - lahir 
    bisa_daftar = umur >= 17
    print(f"nama kamu {nama}, umur kamu {umur}, tinggi kamu {tinggi}, status daftar : {bisa_daftar}")













def toko() : 
    jumlah = input("susu harganya 8000, kamu mau beli berapa ? : ")
    uang = int(input("uang kamu berapa: "))
    jumlah = int(jumlah)
    hitung = jumlah * 8000
    hasil = uang >= hitung
    print(f"kamu membeli susu sebanyak {jumlah}, uang kamu {uang},pas di hitung semuanya jadi {hitung},apakah kamu bisa beli ? : {hasil}")
toko()