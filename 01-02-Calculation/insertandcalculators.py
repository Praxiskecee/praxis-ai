choice = ["Penjumlahan", "Pengurangan", "pembagian", "Perkalian"]

print("Selamat datang di kalkulator")
print("Pilih perhitungan")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

choise = input("Ketik (1/2/3/4) untuk memilih : ")
print("Anda memilih : ", choice[int(choise) -1 ]) 

number1 = input("Masukan angka pertama : ")
print(number1)

number2 = input("Masukan angka kedua : ")
print(number2) 

result = ('result :', int(number1) + int(number2))
print(result)

# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return "Cannot divide by zero!"
#     return x / y

# print("Pilih Perhitungan:")
# print("1. Pertambahan")
# print("2. Pengurangan")
# print("3. Perkalian")
# print("4. Pembagian")

# choice = input("Ketik (1/2/3/4) untuk memilih: ")

# if choice in ('1', '2', '3', '4'):
#     num1 = int(input("Masukan angka pertama: "))
#     num2 = int(input("Masukan angka kedua: "))

#     if choice == '1':
#         print(f"Jawaban: {add(num1, num2)}")
#     elif choice == '2':
#         print(f"Jawaban: {subtract(num1, num2)}")
#     elif choice == '3':
#         print(f"Jawaban: {multiply(num1, num2)}")
#     elif choice == '4':
#         print(f"Jawaban: {divide(num1, num2)}")
# else:
#     print("Invalid input")
