a = 5
b = 3 

# a+=3 is same as a=a+3 

# before
print(a)
print("First modulus: ", a % b)

a += 4
# after
print(a)
print("Second modulus: ", a % b)

print(a**2)

# floor division vs division 
print("Floor division: ", 5 // b)
print("division: ", 5 / 3)

