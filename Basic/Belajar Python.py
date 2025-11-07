# cara cek versi python
# python3 --version
 
#Hello world
print("Hello World")
 
#Belajar Tipe Data Numberik
panjang = 10
lebar = 8
 
luas_persegi_panjang = panjang * lebar
print(f"Luas Persegi Panjang: {luas_persegi_panjang}")
 
#Belajar tipe data string
 
nama_depan = "Abizar"
nama_belakang = "Al Ghifari"
pekerjaan = "Cloud Engineer"
 
nama_lengkap = nama_depan + " " + nama_belakang
print(f"Nama Saya adalah {nama_lengkap} dan pekerjaan saya adalah {pekerjaan}")
 
nama = 'Abizar"TM"'
print (nama)
 
 
# Belajar List, Tuple, Dictionary
# List adalah kumpulan data berurutan dan mutable (bisa diubah)
buah = ["Apel", "Jeruk", "Mangga"]
print(buah)
buah.append("Durian")
print(buah)
print(f"Buah ketiga: {buah[2]}")
 
#Tuple adalah kumpulan data berurutan dan immutable (tidak bisa diubah)
lokasi = (-6.22353453, 100.83733883)
print(f"lokasi berada di: {lokasi}")
print(f"latitude: {lokasi[0]}")
 
# Dictionary adalah kumpulan data tidak berurutan (sebelum Python 3.7) 
# datanya disimpan sebagai pasangan (key:value)
 
profil ={"nama": "Abe",
        "umur" : 18,
        "email":"abizar2110@gmail.com"
        }
print(f"Email {profil['nama']} adalah {profil['email']}")
 
 
# Fungsi logika if condition:
 
nilai = 75
 
if nilai >= 85:
    kategori = "A"
elif nilai >= 70:
    kategori = "B"
elif nilai >= 60:
    kategori = "C"
else:
    kategori = "D"
print (f"Ana mendapatkan nilai {nilai}, kategorinya: {kategori}")
 
# loop atau perulangan
#For digunakan ketika kita tau mau berapa kali proses tersebut diulang
buah = ["apel","jeruk","mangga"]
print("Daftar Buah")
 
for b in buah:
    print(f"- {b}")
print("============")
 
for i in range (5):
    print(i)
print("============")
 
nama = "Abe"
for huruf in nama:
    print(huruf)
#while digunakan ketika kita mau mengulang selama sebuah 
#kondisi itu masih benar
angka = 10
while angka > 0:
    print(f"Hitungan ke-{angka}")
    angka = angka - 1
print("Mulai!")
print("============")
 
for angka2 in range(1,11):
    print(f"Hitungan ke- {angka2}")
print("Mulai")
