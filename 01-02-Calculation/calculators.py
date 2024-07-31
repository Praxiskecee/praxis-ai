choice = ["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"]

print("Selamat datang di kalkulator")
print("Pilih perhitungan")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

choise = input("Ketik (1/2/3/4) untuk memilih : ")
print("Anda memilih : ", choice[int(choise) -1 ]) 

if choise == "1":
    number1 = input("Masukan angka pertama : ")
    print(number1)
    number2 = input("Masukan angka kedua : ")
    print(number2) 
    result = int(number1) + int(number2)
    print("Result :",result)

if choise == "2":
    number1 = input("Masukan angka pertama : ")
    print(number1)
    number2 = input("Masukan angka kedua : ")
    print(number2) 
    result = int(number1) - int(number2)
    print("Result :",result)

if choise == "3":
    number1 = input("Masukan angka pertama : ")
    print(number1)
    number2 = input("Masukan angka kedua : ")
    print(number2) 
    result = int(number1) * int(number2)
    print("Result :",result)

if choise == "4":
    number1 = input("Masukan angka pertama : ")
    print(number1)
    number2 = input("Masukan angka kedua : ")
    print(number2) 
    result = int(number1) / int(number2)
    print("Result :",result)

