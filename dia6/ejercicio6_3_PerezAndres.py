import math
print("Ingrese las posiciones de la Bola#1 y su radio:")
print("Ingre el valor de X")
bola1_X=int(input(""))
print("Ingre el valor de Y")
bola1_Y=int(input(""))
print("Ingre el valor del radio")
radio_1=int(input(""))

print("Ingrese las posiciones de la Bola#2 y su radio:")
print("Ingre el valor de X")
bola2_X=int(input(""))
print("Ingre el valor de Y")
bola2_Y=int(input(""))
print("Ingre el valor del radio")
radio_2=int(input(""))


distancia_centros = math.sqrt((bola2_X - bola1_X)**2 + (bola2_Y - bola1_Y)**2)
total_Radios= radio_1 + radio_2
colision=distancia_centros <= total_Radios

if colision:
    print("True")
else:
    print("false")
