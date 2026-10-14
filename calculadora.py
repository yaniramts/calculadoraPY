print("Introduce un número")
numero = int(input())

while True:

    print("Introduce la operación a realizar:")
    print("1, +")
    print("2, -")
    print("3, *")
    print("4, /")
    operacion = int(input())

    print("Introduce el segundo número")
    numero2 = int(input())

    if operacion == 1:
        resultado = numero + numero2
        expresion = "(" + str(numero) + " + " + str(numero2) + ")"

    elif operacion == 2:
        resultado = numero - numero2
        expresion = "(" + str(numero) + " - " + str(numero2) + ")"

    elif operacion == 3:
        resultado = numero * numero2
        expresion = "(" + str(numero) + " * " + str(numero2) + ")"

    elif operacion == 4:
        resultado = numero / numero2
        expresion = "(" + str(numero) + " / " + str(numero2) + ")"

    print("Resultado:", resultado)

    numero = resultado
