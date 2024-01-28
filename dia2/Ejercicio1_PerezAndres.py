def fibonacci(n):
    fibonacci_seq = [0, 1]
    while len(fibonacci_seq) < n:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    return fibonacci_seq

def main():
    print("La secuencia de Fibonacci es aquella en la cual se suma los dos numeros anteriores para obtener el siguiente, empezando desde 0 y 1.")

    while True:
        try:
            n = int(input("Ingrese el valor de 'n' para generar su secuencia de Fibonacci: "))
            
            if n < 0:
                print("Por favor, ingrese un valor no negativo.")
                continue

            result = fibonacci(n)
            print(f"Secuencia de Fibonacci hasta el termino {n}: {result}")

            continuar = input("¿Desea continuar? (si/no): ")
            if continuar != 'si':
                print("¡Hasta luego! Gracias por usar el generador de fibonacci.")
                break
        except ValueError:
            print("Por favor, ingrese un valor entero.")

if __name__ == "__main__":
    main()