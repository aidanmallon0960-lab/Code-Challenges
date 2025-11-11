I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

temp = 0
print("(if the roman numeral is invalid it will give you a wrong answer)")
num = input("Enter a roman numeral: ")
total = 0

for char in num:
    if char == "I":
        temp = char
        total += I
    elif char == "V":
        if temp == "I":
            total +=3
        else:
            total += V
    elif char == "X":
        if temp == "I":
            total += 8
        else:
            total += X
        temp = char
    elif char == "L":
        if temp == "X":
            total += 30
        else:
            total += L
    elif char == "C":
        if temp == "X":
            total += 80
        else:
            total += C
        temp = char
    elif char == "D":
        if temp == "C":
            total += 400
        else:
            total += D
    elif char == "M":
        if temp == "C":
            total += 800
        else:
            total += M

print(total)