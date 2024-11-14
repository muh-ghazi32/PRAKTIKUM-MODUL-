angka1, angka2 = map(int, input("Input: ").split())

if angka1 < angka2:
    terkecil = angka1
    terbesar = angka2
elif angka1 > angka2:
    terkecil = angka2
    terbesar = angka1
else:
    terkecil = terbesar = angka1 

print(f"Output: {terkecil} {terbesar}")
