for i in range(5): 
    print(f"detik ke - {i}")

is_paid = False
percobaan = 1

while not is_paid : 
    print(f"mengecek status pembayaran ke- {percobaan}...")
    if percobaan == 3:
        is_paid = True
    percobaan += 1
print(f"pembayaran berhasil")