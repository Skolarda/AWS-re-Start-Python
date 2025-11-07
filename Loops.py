#Loop atau pengulangan

#Loop while membuat bagian kode berulang sampai kondisi tertentu terpenuhi
import random #untuk mengimpor modul random

print("Welcome to guess the Number!")
print("The rules are simple. Iwill think of a number, and you will try to guess it.")

number = random.randint(1, 10) #menghasilkan angka acak antara 1 dan 10
isGuessRight = False           

while isGuessRight != True:
    guess = input("Guess a number betwween 1 and 10: ")
    if int(guess) == number:
        isGuessRight = True
        print("You guessed {}.That is correct! You Win!".format(guess))
    else:
        print("You guessed {}. That is incorrect. Try again!".format(guess))
print("Thanks for playing!")

#while digunakan ketika kita mau mengulang selama sebuah kondisi itu masih benar
angka = 10
while angka > 0:
    print(f"Hitungan ke-{angka}")
    angka = angka - 1
print("Mulai!")
print("============")
 
for angka2 in range(1,11):
    print(f"Hitungan ke- {angka2}")
print("Mulai")

#contoh while loop login system
password = "9112001"
attempts = 0
max_attempts = 3   

while attempts < max_attempts:
    user_input = input("Enter your password: ")
    if user_input == password:
        print("Access Granted. Welcome!")
        break #Keluar dari loop jika password benar
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        else:
            print("Account locked due to too many failed attempts.")

#==============================================================================

#For loop digunakan ketika kita tahu mau berapa kali proses tersebut diulang
for i in range (5):
    print(i)

#contoh for loop - tabel perkalian
angka = int(input("Masukkan Angka:"))

print(f"\nTabel Perkalian {angka}:")
for i in range(1, 11):
    hasil = angka * i
    print(f"{angka} x {i} = {hasil}")

#contoh loop untuk list
buah = ["apel","jeruk","mangga"]
print("Daftar Buah")
for item in buah:
    print(f"- {item}")