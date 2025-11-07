#Conditionals memungkinkan program mengambil keputusan berdasarkan kondisi tertentu
#if, elif, dan else akan menjadi componen utama dalam struktur kondisional di Python

#if else statement
userReply = input("Apakah kamu suka ngoding? (ya/tidak): ")
if userReply == "ya":                                                     
    print("Bagus! Terus semangat belajar ngoding!")
else:                                                                       
    print("Tidak apa-apa, mungkin kamu akan suka ngoding suatu hari nanti.")

# if elif else statement
userInput = input("Apakah kamu mau membeli perangko, amplop, atau membuat salinan? (perangko/amplop/salinan): ")

if userInput == "perangko":
    print("Kami punya banyak desain perangko untuk dipilih")
elif userInput == "amplop":
    print("Kami memiliki berbagai ukuran amplop")
elif userInput == "salinan":
    copies = input("berapa banyak salinan yang kamu butuhkan? (Masukkan jumlah) : ")
    print("Ini dia salinan kamu sebanyak {} salinan".format(copies))
else:
    print("Maaf, kami tidak menyediakan layanan tersebut.")

#Urutan kondisi dalam if elif else statement akan dieksekusi dari atas ke bawah


#Contoh program menggunakan conditionals

#Cek umur
umur = int(input("Masukkan umur kamu: "))
if umur < 13:
    print("Kamu anak-anak.")
elif umur < 18:
    print("Kamu remaja.")
elif umur < 60:
    print("Kamu dewasa.")
else:
    print("Kamu lansia.")

#Sistem penilaian sederhana
nilai = int(input("Masukkan nilai ujian kamu (0-100): "))
if nilai >= 90:
    print("Nilai kamu: A")
elif nilai >= 80:
    print("Nilai kamu: B")
elif nilai >= 70:
    print("Nilai kamu: C")
elif nilai >= 60:
    print("Nilai kamu: D")
else:
    print("Nilai kamu: F - Tidak lulus")