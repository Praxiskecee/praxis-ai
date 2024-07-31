import os
os.system('cls')
os.system('color 3')

while True:

    choice = ["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian", "Pangkat"]

    print("Selamat datang di kalkulator")
    print("Pilih perhitungan")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Pangkat")

    choise = input("Ketik (1/2/3/4/5) untuk memilih : ")
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
        result = (int(number1) / int(number2)) 
        if int(number1) % int(number2)==0:
            print("Result :", int(result))
        else:
            print("Result :", result)

    if choise == "5":
        number1 = input("Masukan angka pertama : ")
        print(number1)
        number2 = input("Masukan angka kedua : ")
        print(number2) 
        result = int(number1) ** int(number2)
        print("Result :",result)



    ulang = input("Apakah anda ingin mengulang? (y/n): ")
    if ulang.lower() == 'n':
        print("Terimakasih telah menggunakan kalkulator")
        break
