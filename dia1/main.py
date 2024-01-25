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

## Desarrollado por: ANDRES DAVID PEREZ SANTIAGO - 1065593359