import random

def juego_alzar():
    numero_aleatorio = random.randint(1, 100)
    print("Bienvenido querido usuario al juego del alzar, Usted tendra que adivinar el numero secreto que esta entre el 1 y el 100")
    print("¡Cabe recalcar que solamente tiene 10 intentos mucha suerte usuario!")
    intentos=0
    while intentos<10:
        try:
            numero_usuario = int(input("Ingrese un numero: "))
            if numero_usuario == numero_aleatorio:
                print(f"FELICIDADES,Has acertado el numero {numero_aleatorio}")
                break
            elif numero_usuario < numero_aleatorio:
                print("El numero ingresado es menor que el numero escojido al azar")
            elif numero_usuario > numero_aleatorio:
                print("El numero ingresado es mayor que el numero escojido al azar")
            intentos+=1
        except ValueError:
            print("Por favor, ingrese un valor entero.")
    if intentos == 10:
        print(f"Lo siento pero se le acabarons sus intentos. el numero secreto era {numero_aleatorio}")

juego_alzar()
    
