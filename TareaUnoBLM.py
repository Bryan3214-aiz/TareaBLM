#Programa realizado por Bryan Leiva.

arrayOne = []
arrayTwo = []

print("\n  Lista numero 1  \n")
for i in range(5):#Solicita 5 numeros que se almacenaran en "arrayOne"
    try:
        numbers = int(input("Ingrese un numero: "))
        arrayOne.append(numbers)
    except:#En caso de que se ingrese un valor incorrecto se muestra un mensaje de error y se ejecuta la excepción
        print("\nIngresaste un valor incorrecto, intentalo de nuevo.\n")
        numbers = int(input("Ingrese un numero: "))
        arrayOne.append(numbers)

print("\n  Lista numero 2  \n")
for i in range(5):#Solicita 5 numeros que se almacenaran en "arrayTwo"
    try:
        numbers = int(input("Ingrese un numero: "))
        arrayTwo.append(numbers)
    except:#En caso de que se ingrese un valor incorrecto se muestra un mensaje de error y se ejecuta la excepción
        print("\nIngresaste un valor incorrecto, intentalo de nuevo.\n")
        numbers = int(input("Ingrese un numero: "))
        arrayTwo.append(numbers)

arrayThree = arrayOne + arrayTwo
arrayThree.sort(reverse=True)

print("\n  LISTAS DE NUMEROS")
print(f"\nArreglo 1 = {arrayOne}\nArreglo 2 = {arrayTwo}\nArreglo 3 = {arrayThree}")
