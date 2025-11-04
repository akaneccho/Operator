# Meminta inputan apakah pengguna adalah anggota
anggota = input("Apakah Anda anggota? (y/n): ").lower() == 'y'

# Meminta inputan total belanja pengguna
total_belanja = float(input("Masukkan total belanja Anda: "))

# Periksa apakah pengguna berhak mendapatkan diskon
dapat_diskon = anggota or total_belanja > 50000

# Tampilkan hasil
if dapat_diskon:
    print("Anda mendapatkan diskon!")
else:
    print("Anda tidak mendapatkan diskon.")
