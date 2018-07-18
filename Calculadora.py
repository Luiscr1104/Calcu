# -*- coding: utf-8 -*-

class calc:
    def suma(num1, num2):
        num1 + num2
    def resta(num1, num2):
        num1 - num2

def hexa_binario():
    Hexa = "AAABC"
    binario =""
    for char in Hexa:
        if char == "A":
            x = 1010
            binario =str(binario) + str(x)
        elif char == "B":
            x = 1011
            binario = str(binario) + str(x)
        elif char == "C":
            x = 1100
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
    print (binario)

def binario_a_decimal(x):
    n = len (x)
    valor = 0
    for xs in x:
        if xs == '1':
            valor = valor + 2**(n-1)
        n -=1
    print binario_a_decimal(x) 

def octal_to_decimal(number):
    i = 1
    decimal = 0
    while (number != 0):
        reminder = number % 8
        number /= 8
        decimal += reminder * i
        i *= 8
    return decimal

def hexadecimal_a_decimal(d):
    print int(d,16)