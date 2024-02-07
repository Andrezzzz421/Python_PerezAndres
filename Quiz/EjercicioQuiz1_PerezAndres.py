##Escribe un programa en python (EjercicioQuiz1_ApellidoNombre.py) que lea las tres notas obtenidas por 5 estudiantes y calcule la nota final de cada uno, 
##sabiendo que las cada nota tiene el siguiente valor: n1 (30%), n2 (30%), n3 (40%). Se debe crear una función calcular_definitiva que reciba como parámetros 
##las 3 notas del estudiante y retorne su nota definitiva. En esa misma función debe indicar que si la nota obtenida es menor a 2,0 deberá indicarle al 
##estudiante que no puede habilitar, si la nota obtenida es menor a 3 deberá indicar que reprobó, si la nota es mayor o igual a 3 deberá indicar que aprobó y si es mayor a 4,5 
##extenderá un mensaje de felicitación al estudiante.
##En ese mismo programa uno de los valores retornados por la función deberán ser agregados a una lista y posteriormente en esa lista encontrar la mejor nota (sin usar la función MAX de Python) y mostrarlo en pantalla.

def calcular_definitiva(n1, n2, n3):
    definitiva = (n1 * 0.3) + (n2 * 0.3) + (n3 * 0.4)
    
    if definitiva < 2.0:
        return definitiva, "No puede habilitar"
    elif definitiva < 3.0:
        return definitiva, "Reprobó"
    elif definitiva >= 3.0 and definitiva <= 4.5:
        return definitiva, "Aprobó"
    else:
        return definitiva, "¡Felicitaciones!"

definitivas = []

print("Ingrese la cantidad de estudiantes a los cuales les ingresará sus 3 notas:")
cantidad_estudiantes = int(input())

for estudiante in range(1, cantidad_estudiantes + 1):
    print(f"Ingrese la primera nota del estudiante #{estudiante}:")
    n1 = float(input())
    print(f"Ingrese la segunda nota del estudiante #{estudiante}:")
    n2 = float(input())
    print(f"Ingrese la tercera nota del estudiante #{estudiante}:")
    n3 = float(input()) 

    nota_final, mensaje = calcular_definitiva(n1, n2, n3)

    print(f"Nota final del estudiante #{estudiante}: {nota_final} - {mensaje}")

    definitivas.append(nota_final)

mejor_nota = definitivas[0]
for nota in definitivas:
    if nota > mejor_nota:
        mejor_nota = nota

print(f"\nLa mejor nota obtenida es: {mejor_nota}")