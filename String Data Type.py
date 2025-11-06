#Data String, simpelnya data string ini adalah kumpulan huruf yang diapit oleh tanda kutip satu ('...') atau tanda kutip dua ("...")
#untuk membuat data string kita bisa menggunakan tanda kutip satu atau dua, contoh:

myString = 'Ini String dengan tanda kutip satu'
print(myString)

myString2 = "Ini String dengan tanda kutip dua"
print(myString2)

#Tanda kutip satu atau dua ini memiliki fungsi yang sama, kita bisa menggunakan salah satu sesuai kebutuhan.

print(type(myString))  #menampilkan tipe data string
print(myString + "is of the data type" + str(type(myString)))  #menggabungkan dua string beserta menampilkan tipe datanya

#=============================================================================

#Menggabungkan String
#Kita bisa menggabungkan dua string atau lebih dengan menggunakan operator tambah (+)

#contoh 1
nama_depan = "Sarah"
nama_belakang = ' Thereskova' #berikan cela spasi untuk memisahkan nama depan dan belakang agar tidak nyambung
pekerjaan = "Model"
nama_lengkap = nama_depan + nama_belakang
print(nama_lengkap)
print(f"Nama lengkap: {nama_lengkap}, Pekerjaan: {pekerjaan}")

#contoh 2
salam = "Assalamu'alaikum"
nama = " Nama saya Sarah"
infomasi = " Saya seorang model"
perkenalan = salam + ',' + nama + '.' + infomasi + '.' #menggabungkan beberapa string dan diriingi dengan tanda baca agar keliatan rapi
print(perkenalan)

#=============================================================================

#Penggunaan input dengan String

#Input berguna untuk mengambil data dari user, data yang diambil dari user ini akan bertipe string 
#Ketika kita run program ini makan user akan diminta untuk menginput data, data yang diinput akan disimpan kedalam variabel

#contoh 1
user_input = input("Input nama Anda: ")
print(user_input)

#contoh 2
user_name_input = input("Input nama Anda: ")
user_job_input = input("Input pekerjaan Anda: ")
print(f"Nama Anda adalah {user_name_input}, Pekerjaan Anda adalah {user_job_input}")

#=============================================================================

#Penggunaan format output string
#Output string berfungsi untuk menyampaikan informasi kembali ke user dengan menggunakan print()

#contoh
nama_user = input("Masukkan nama Anda: ")
warna_favorit = input("Apa warna favorit Anda: ")
jenis_pakaian_favorit = input("Apa jenis pakaian favorit Anda: ")

print("{}, kamu suka {} {}!".format(nama, jenis_pakaian_favorit, warna_favorit)) #dalam mendefine format output harus berurutan dengan simbol ({}) pada command print


#Sebenernya ada cara yang lebih mudah yaitu menggunakan f-string dari pada pakai format 

#contoh
nama_user2 = input("Masukkan nama Anda: ")
warna_favorit2 = input("Apa warna favorit Anda: ")
jenis_pakaian_favorit2 = input("Apa jenis baju favorit Anda: ")    

print(f"{nama_user2}, kamu suka {jenis_pakaian_favorit2} {warna_favorit2}!") #jadi kamu tidak perlu berurutan dalam mendefine format output

#=============================================================================

#Ini jika semuanya digabungkan menjadi satu program sederhana:

#Input dari user
nama_depan = input("Nama depan: ")
nama_belakang = input("Nama belakang: ")
umur = input("Umur: ")
pekerjaan = input("Pekerjaan: ")
 
#Gabungkan string
nama_lengkap = nama_depan + " " + nama_belakang     #(" ") berfungsi untuk memberikan spasi antara nama depan dan belakang

#Output dengan f-string
print(f"\n=== PROFIL ===")      #fungsi /n untuk membuat baris baru
print(f"Nama: {nama_lengkap}")
print(f"Umur: {umur} tahun")
print(f"Pekerjaan: {pekerjaan}")
print(f"{nama_depan}, kamu adalah seorang {pekerjaan}!")