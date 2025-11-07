#Collection Data Types di Python ada 3
#1. List (daftar)
#2. Tuple
#3. Dictionary (kamus)

#=============================================================================

#List adalah kumpulan data berurutan dan mutable (bisa diubah)
myFruitList = ["apel", "pisang", "ceri"] #variabel
print(myFruitList)           # ['apel', 'pisang', 'ceri']
print(type(myFruitList))     # <class 'list'> untuk mengecek tipe data

#Bisa juga untuk menambahkan list berdasaran posisi (index)
#Index dimulai dari 0, bukan 1
print(myFruitList[0])        #apel
print(myFruitList[1])        #pisang
print(myFruitList[2])        #ceri

#Posisi urutan buah di dasarkan pada urutan buah yang di define di variabel myFruitList
#Jadi jika ingin ceri berada di posisi pertama, maka kita harus mengubah urutan di variabel myFruitList atau bisa juga dengan merubah urutan print seperti di bawah ini
print(myFruitList[2])        #ceri
print(myFruitList[1])        #pisang
print(myFruitList[0])        #apel

#Mengubah nilai dalam list
myFruitList[2] = "jeruk"     #Mengubah ceri jadi jeruk
print(myFruitList)           #Maka hasil outputnya seperti ini ['apel', 'pisang', 'jeruk']



#Operasi list lainnya
buah = ["apel", "jeruk", "mangga"]  #variabel

buah.append("Durian")       
print(buah)                  #Maka hasilnya ['Apel', 'Jeruk', 'Mangga', 'Durian']

#Menambah item di posisi tertentu
buah.insert(1, "Semangka")   #Mensisipkan di index 1
print(buah)                  #Hasilnya ['Apel', 'Semangka', 'Jeruk', 'Mangga', 'Durian']

# Menghapus item
buah.remove("jeruk")         #Hapus "Jeruk"
print(buah)                  #Hasilnya ['Apel', 'Semangka', 'Mangga', 'Durian']

# Menghitung jumlah item
print(len(buah))             #Hasilnya 4

#=============================================================================

#Tuple adalah kumpulan data berurutan dan immutable (tidak bisa diubah)
#Tuple mirip mirip seperti list, namun tidak bisa diubah dan menggunakan () bukan []

myFinalAnswerTuple = ("Apel", "Pisang", "Nanas")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

#Tuple berdasarkan posisi index
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

#Tuple tidak bisa diubah jika variabel sudah di define
#myFinalAnswerTuple[2] = "Jeruk"  #Maka akan error


#Kapan menggunakan tuple? tuple digunakan ketika data yang kita miliki bersifat tetap/konstan atau tidak berubah ubah/statik
#Misalnya  koordinat GPS, data warna RGB, data bulan dalam setahun, dsb
lokasi = (-6.22353453, 100.83733883, 50) #Urutan index didasarkan urutan angka pada variabel
print(f"lokasi berada di: {lokasi}")
print(f"latitude: {lokasi[0]}")
print(f"longitude: {lokasi[1]}")
print(f"altitude: {lokasi[2]} meters")

tanggal_lahir = (21, 10, 2000)
print(f"Tanggal lahir saya adalah: {tanggal_lahir[0]}-{tanggal_lahir[1]}-{tanggal_lahir[2]}")

warna_rgb = (255, 0, 0) 
print(f"Warna RGB untuk warna merah adalah: R={warna_rgb[0]}, G={warna_rgb[1]}, B={warna_rgb[2]}")
warna_rgb = (0, 255, 0)
print(f"Warna RGB untuk warna hijau adalah: R={warna_rgb[0]}, G={warna_rgb[1]}, B={warna_rgb[2]}")
warna_rgb = (0, 0, 255)
print(f"Warna RGB untuk warna biru adalah: R={warna_rgb[0]}, G={warna_rgb[1]}, B={warna_rgb[2]}")  

#=============================================================================

#Dictionary adalah kumpulan data tidak berurutan (sebelum Python 3.7)
#Namun, datanya disimpan sebagai pasangan (key:value)
#Dictionary menggunakan {} bukan []

myProfileDict = {
    "nama": "Sarah",
    "umur": 21,
    "email": "sarah.thereskova@gmail.com"
}

print(myProfileDict)
print(type(myProfileDict))

#Mengakses data dalam dictionary berdasarkan key
print(myProfileDict["nama"])
print(myProfileDict["umur"])
print(myProfileDict["email"])

#Agar output lebih rapih, kita bisa menggunakan f-string
print(f"Email {myProfileDict['nama']} adalah {myProfileDict['email']}")


#Operasi  Dictionary
profil = {"nama": "Sarah", "umur": 21}

# Menambah key baru
profil["kota"] = "Stuttgart"
print(profil)               #{'nama': 'Sarah', 'umur': 21, 'kota': 'Stuttgart'}

#Mengubah value
profil["umur"] = 22
print(profil)               #{'nama': 'Sarah', 'umur': 22}

#Menghapus keyvalue
del profil["kota"]
print(profil)               #{'nama': 'Sarah', 'umur': 22}

# Mendapatkan semua keys
print(profil.keys())        #dict_keys(['nama', 'umur'])

# Mendapatkan semua values
print(profil.values())      #dict_values(['Sarah', 22])

#=============================================================================

#Contoh Lengkap list, tuple, dan dictionary
#===== LIST =====
mahasiswa = ["Budi", "Abe", "Sarah"]
mahasiswa.append("Dina")
print(f"Total Mahasiswa: {len(mahasiswa)}")
print(f"Mahasiswa pertama: {mahasiswa[0]}")
print(f"Mahasiswa kedua: {mahasiswa[1]}")
print(f"Mahasiswa ketiga: {mahasiswa[2]}")
print(f"Mahasiswa keempat: {mahasiswa[3]}")

#===== TUPLE =====
tanggal_lahir = (21, 10, 2000)
print(f"Tahun Lahir: {tanggal_lahir[2]}")

#===== DICTIONARY =====
Biodata = {
    "nama": "Sarah",
    "umur": 21,
    "hobi": ["Tidur", "Membaca", "Coding"], #value bisa berupa list
    "alamat": {                             #value bisa berupa dictionary
        "jalan": "Adolf Street Num. 271",
        "kota": "Stuttgart",
        "negara": "Jerman"
    }
}

print(f"Nama: {Biodata['nama']}")
print(f"Hobi pertama: {Biodata['hobi'][0]}")
print(f"Kota: {Biodata['alamat']['kota']}")