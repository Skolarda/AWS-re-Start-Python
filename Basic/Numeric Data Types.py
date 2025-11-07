#Membuat Variabel
myValue = 10
print(myValue)
print(type(myValue))

#Fungsi dari "type()" adalah untuk mengetahui tipe data dari sebuah variabel, apakah itu string, integer, float, dll.
#Mendefine variabel itu bebas dengan apa saja, asalkan tidak diawali dengan angka dan tidak menggunakan spasi.
Nama = "Abe"
print(Nama)
print(type(Nama))

Makanan_Favorit = "Sate Padang"
print(Makanan_Favorit)  
print(type(Makanan_Favorit)) 

#=============================================================================

#Untuk meggabungkan angka dan teks kita bisa menggunakan str()

#Mengubah angka menjadi string
myUmur = 18
print("Umur saya " + str(myUmur) + " tahun")

Harga = 25000
print("Harga sate padang adalah Rp " + str(Harga))

#Mengubah type data ke string
myValue2 = 10
print(str(myValue2) + " is of the data type " + str(type(myValue2)))

#Berbagai Tipe data
angka = 100         #integer (Bilangan bulat)
desimal = 3.14      #float (Bilangan desimal)
benar = True        #boolean (Nilai benar/salah), bisa juga didefiniskan sebagai true=1 dan false=0
kompleks = 2 + 3j   #complex (Bilangan kompleks), umumnya untuk matematika tingkat lanjut

print("angka " + str(angka))        # Angka: 100
print("desimal " + str(desimal))    # Desimal: 3.14
print("benar " + str(benar))        # Benar: True
print("kompleks " + str(kompleks))  # Kompleks: (2+3j)

#Konversi antar tipe data

#integer ke float
a = 10
b = float(a)
print(b)              #output: 10.0

#float ke integer (menghilangkan desimal)
c = 3.14
d = int(c)
print(d)              #output: 3

#integer ke boolean
print(bool(1))        #output: True
print(bool(0))        #output: False
print(bool(100))      #output: True (semua angka selain 0 = True)

#boolean ke integer
print(int(True))      #output: 1
print(int(False))     #output: 0

#=============================================================================

#Alternatif tanpa str() - bisa menggunakan f-string (formatted string literals) dan jadi lebih modern

#variabel
Nama = "Abe"
Umur = 18

#Cara lama dengan str()
print("Nama saya " + Nama + ", umur saya " + str(Umur) + " tahun.")

#Cara Modern dengan f-string ({Variabel})
print(f"Nama saya {Nama}, umur saya {Umur} tahun.")     #Jadi tidak perlu lagi menggunakan (+) dan str() karena sudah digantikan oleh f-string ({Variabel})

#=============================================================================

#Kombinasi f-string dengan operasi matematika

#contoh 1
panjang = 10
lebar = 8
 
luas_persegi_panjang = panjang * lebar
print(f"Luas Persegi Panjang: {luas_persegi_panjang}") 

#contoh 2
modal = 10000
harga_jual= 15000

keuntungan = harga_jual - modal
 
print(f"Omset penjualan Rp.{keuntungan},-")