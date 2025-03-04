print("="*64)
print("NIM : Radjikin Septiawan".center(64))
print(f'NIM : {312410071}'.center(64))
print("="*64)


# Inisialisasi Input pengguna
berat_paket = int(input("Masukkan berat barang(kg): "))
jarak_pengiriman = int(input("Masukkan jarak pengiriman(km): "))
paket_layanan = input("Pilih Paket Layanan (Express/Member) : ")
biaya_dasar = 10000

# Merubah ukuran paket menjadi standart internasional
berat_paket_gram = berat_paket * 1000
jarak_pengiriman_meter = jarak_pengiriman * 1000

# Melakukan conditional processing pada paket
total_pembayaran = biaya_dasar
if berat_paket_gram > 5000:
    total_pembayaran += biaya_dasar + 5000

if jarak_pengiriman_meter > 10000:
    total_pembayaran += biaya_dasar + 8000

if paket_layanan.lower() == 'express':
    total_pembayaran += biaya_dasar + 20000

if paket_layanan.lower() == 'member':
    total_pembayaran += biaya_dasar * 10/100

# Menghasilkan output pengguna
print("="*62)
print('Total Pembayaran anda : ',total_pembayaran)
print("="*62)
