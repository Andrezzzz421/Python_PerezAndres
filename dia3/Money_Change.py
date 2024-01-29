cont = int(input("Enter the quantity: "))
money = [10, 5, 1] 
for i in money:
    cantidad_de_monedas = cont // i
    cont = cont % i
    print(f"You need {cantidad_de_monedas} coins of {i}.")