print("#--------------------------#")
print("#--| calculadora basica |--#")
print("#--------------------------#")
print("#--| 1) suma            |--#")
print("#--| 2) resta           |--#")
print("#--| 3) multiplicacion  |--#")
print("#--| 4) division        |--#")
print("#--------------------------#")
opcion = input("seleccione una opcion: ")
num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))
def mostrar_resultado(resultado):
    if resultado.is_integer():
        print("resultado:", int(resultado))
    else:
        print("resultado:", resultado)
if opcion == "1":
    mostrar_resultado(num1 + num2)
elif opcion == "2":
    mostrar_resultado(num1 - num2)
elif opcion == "3":
    mostrar_resultado(num1 * num2)
elif opcion == "4":
    if num2 != 0:
        mostrar_resultado(num1 / num2)
    else:
        print("error: no se puede dividir entre cero")
else:
    print("opcion no valida")
