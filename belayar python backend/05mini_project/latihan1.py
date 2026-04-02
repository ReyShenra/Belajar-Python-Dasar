def tugas1 ():
    angka_pertama = int(input("masukan angka pertama : "))
    angka_kedua = int(input("masukan angka kedua :" ))

    penjumlahan = angka_pertama + angka_kedua
    pengurangan = angka_pertama - angka_kedua
    pembagian = angka_pertama / angka_kedua
    perkalian = angka_pertama * angka_kedua

    print(f"{penjumlahan}")
    print(f"{pengurangan}")
    print(f"{pembagian}")
    print(f"{perkalian}")

def tugas2 (): 
    angka_satu = int(input("masukan angka pertama: "))
    angka_dua = int(input("masukan angka kedua: "))

    print(f"hasil pembagian tanpa koma : {angka_satu // angka_dua}")
    print(f"hasil pembagian sisa bagi : {angka_satu % angka_dua}")
tugas2()