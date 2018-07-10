Hexa= "ABC432"
binario=""
for char in Hexa:
    if char == "A":
        x = 1010
        binario =str(binario) + str(x)
    elif char == "B":
        x = 1011
        binario = str(binario) + str(x)
    elif char == "C":
        x= 1100
        binario = str(binario) + str(x)
    elif char == "D":
        x = 1101
        binario = str(binario) + str(x)
    elif char == "E":
        x = 1110
        binario = str(binario) + str(x)
    elif char == "F":
        x = 1111
        binario = str(binario) + str(x)
    elif char == "0":
        x = str("0000")
        binario = str(binario) + str(x)
    elif char == "1":
        x = str("0001")
        binario = str(binario) + str(x)
    elif char == "2":
        x = str("0010")
        binario = str(binario) + x
    elif char == "3":
        x = 0011
        binario = str(binario) + str(x)
    elif char == "4":
        x = 0100
        binario = str(binario) + str(x)
print("Su numero convertido a Binario es: ")
print(binario)

