# Meminta input harga barang dari pengguna
harga_barang1 = float(input("Masukkan harga barang 1: "))
harga_barang2 = float(input("Masukkan harga barang 2: "))
harga_barang3 = float(input("Masukkan harga barang 3: "))

# Pajak 10%
pajak = 0.1

# Hitung total harga tanpa pajak
total_harga = harga_barang1 + harga_barang2 + harga_barang3

# Hitung pajak
total_pajak = total_harga * pajak

# Hitung total harga setelah pajak
total_setelah_pajak = total_harga + total_pajak

# Tampilkan hasil
print("*** Hasil Perhitungan ***")
print("Total harga sebelum pajak:", total_harga)
print("Total pajak:", total_pajak)
print("Total harga setelah pajak:", total_setelah_pajak)
