## ----------------------------
## ---- Ejercicio 1 ----
## ----------------------------

# Impresion en consola
print("Hola Mundo") 

# ---- Datos primitivos ----
#1. String
texto = "Campus"
print(texto)
print(type(texto))
#2. Int
numeroentero = 1
print(numeroentero)
#3. Float
numerodecimal = 2.7
print(numerodecimal)
#4. Double
numerodecimallargo = 3.14167582737283
print(numerodecimallargo)
#5. Boolean
boolean = True
print(boolean)
# ---- Entradas por parte del usuario ----
entradaUsuario = input("Ingresa tu nombre: ")
print ("Tu nombre es: ",entradaUsuario)
# ---- Entradas por parte del usuario con definicion de tipo dato primitivo----
entradaUsuarioNumero = input("Ingresa tu edad: ")
numeroFinal = int(entradaUsuarioNumero)
print ("Tu edad es: ",numeroFinal)
# ---- Ciclos ----
# ---- For(para) ----
for i in range (5,10,2):#for contador in range(desde,hasta,pasos):
    print(i)
# ---- While ----
booleanito = True
while booleanito == True:#while condicion_a_cumplir :
    print("Sigo vivo")
    booleanito = False
    # ---- Condicionales ----
    Texto1="campus"
    if texto=="Campus":
        print("Soy campus")
    else:
        print("No soy campus")
 # ---- Funciones ----
  # ---- Funciones sin y sin ----
    def saludo():
      print("Hola,como estas")
   
    saludo()
# ---- Funciones sin y con ----
    def mt():
      numero1=20
      numero2=15
      return numero1*numero2
   
    total=mt()
    print("el resultado es:",total)
# ---- Funciones con y con ----
    def restar(numero1,numero2):
        return numero1-numero2
    total=restar(20,10)
    print("el total de la resta es:",total)

# ---- Funciones con y sin ----
    def restar2(numero1,numero2):
        print("Total:",numero1-numero2)

    restar2(60,31)

# ---- Arreglos ----
from array import array
numeros = array("i",[5,6,7,8])

print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])

## Desarrollado por: ANDRES DAVID PEREZ SANTIAGO - 1065593359