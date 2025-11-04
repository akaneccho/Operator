huruf = input("Masukkan kata: ")
count_a = 0

for h in huruf:
    if h == 'a':
        count_a += 1
    elif h == 'b':
        pass
    else:
        print(h)

print(f"Jumlah huruf 'a' dalam kata {huruf} adalah:", count_a)
