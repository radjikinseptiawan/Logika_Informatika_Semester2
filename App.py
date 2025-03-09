print("="*64)
print("NIM : Radjikin Septiawan".center(64))
print(f'NIM : {312410071}'.center(64))
print("="*64)

# Fungsi untuk menghitung biaya pengiriman
def hitung_biaya_pengiriman(berat, jarak, express=False, member=False):
    biaya_dasar = 10000
    biaya_pembayaran = 0

    if berat > 5:
        biaya_pembayaran += 5000
    if jarak > 10:
        biaya_pembayaran += 8000
    if express == "express":
        biaya_pembayaran += 20000

    total_biaya = biaya_dasar + biaya_pembayaran

    if member == "ya":
        diskon = total_biaya * 0.1 
        total_biaya -= diskon  
    return int(total_biaya) 

# Input pengguna
try:
    berat_paket = int(input("Masukkan berat barang (kg): "))
    jarak_pengiriman = int(input("Masukkan jarak pengiriman (km): "))
    paket_layanan = input("Pilih Paket Layanan (Biasa/Express): ").strip().lower()
    status_member = input("Apakah Anda member? (Ya/Tidak): ").strip().lower()

    total_biaya = hitung_biaya_pengiriman(berat_paket, jarak_pengiriman, paket_layanan, status_member)

    print("="*62)
    print(f'Total Pembayaran Anda: Rp {total_biaya}')
    print("="*62)

except ValueError:
    print("Input tidak valid! Pastikan memasukkan angka untuk berat dan jarak.")
