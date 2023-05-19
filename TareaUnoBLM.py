#Programa realizado por Bryan Leiva.

arrayOne = []
arrayTwo = []

print("\n---Lista numero 1---\n")
for i in range(5):
    numbers = int(input("Ingrese un numero: "))
    arrayOne.append(numbers)
    print(arrayOne)
print("\n---Lista numero 2---\n")
for x in range(5):
    numbers = int(input("Ingrese un numero: "))
    arrayTwo.append(numbers)
    print(arrayTwo)

arrayThree = arrayOne + arrayTwo
arrayThree.sort(reverse=True)

print(f"\nLista ordenada: {arrayThree}")

