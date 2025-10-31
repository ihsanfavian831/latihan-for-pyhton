print("masukan 5 angka")

angka = [3, 4, 2, 6, 5]
nomor_urut = 1

for i in angka:
    print(f"angka ke-{nomor_urut} : {i}")
    nomor_urut += 1

angka = [3, 4, 2, 6, 5]
total = 0

for i in angka:
    total += i

print(f"jumlah total= {total}")