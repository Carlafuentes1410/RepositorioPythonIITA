#Ejercicio1
def num_primo (num):
    if num <=1:
        return False
    if num <=3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i+2) == 0:
            return False
        i += 6 
    return True

def primos_hasta_n (n):
    if n < 2:
        print ("No hay numeros primos en el rango especificado.")
        return
    print ("Numeros primos entre 1 y", n, ":")
    for numero in range (2, n + 1):
        if num_primo (numero):
            print(numero, end=" ")
n = int(input("Ingrese un numero n: "))
primos_hasta_n(n)

#Ejercicio2
def armar_sandwich ():
    condimentos = []
    while True:
        condimento = input("Ingrese un condimento para el sandwich o salir para terminar: ")
        if condimento.lower() == 'salir':
            break
        condimentos.append (condimento)
        print (f"{condimento} ah sido agregado al sandwich.")
        if condimentos:
            print ("\nEl sandwich tiene los siguientes condimentos: ")
            for condimento in condimentos:
                print(condimento)
    else:
        print("\nNo se agregaron condimentos al sandwich.")
armar_sandwich()

#Ejercicio3A
def hacer_remera(tamaño, mensaje):
    print(f"Se ha creado una remera de tamaño {tamaño} con el siguiente mensaje impreso: {mensaje}")
hacer_remera("XL", "Hola mundo!")
hacer_remera(tamaño="S", mensaje="Bienvenido a Python.")

#Ejercicio3B
def hacer_remera(tamaño='L', mensaje = 'Me gusta Python'):
    print(f"Se creó una remera tamaño {tamaño}, con el mensaje: {mensaje}")
hacer_remera()

