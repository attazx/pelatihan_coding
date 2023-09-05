print("Program Menghitung Volume Balok")

# Menerima input panjang, lebar dan tinggi balok
panjang = int(input("masukkan panjang balok :"))
lebar = int(input("masukkan lebar balok :"))
tinggi = int(input("masukkan tinggi balok :"))

# Menghitung Volume Balok 
volume_balok = panjang*lebar*tinggi

# Menampilkan Hasil
print("panjang balok adalah", panjang, "cm")
print("lebar balok adalah", lebar, "cm")
print("tinggi balok adalah", tinggi, "cm")
print("maka volume balok adalah", volume_balok, "cm2")