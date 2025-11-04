# Meminta inputan umur dari pengguna
umur = int(input("Masukkan umur Anda: "))

# Periksa apakah umur cukup untuk mengendarai mobil
cukup_umur = umur >= 17

# Tampilkan hasil
if cukup_umur:
    print("Selamat Anda sudah cukup umur untuk mengendarai mobil.")
else:
    print("Maaf Anda belum cukup umur untuk mengendarai mobil.")
