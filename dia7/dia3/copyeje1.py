def contador():
    cont=int(input("enter the quiantity: "))
    money=[10,5,1]
    monedas_usadas=[]
    for i in money:
        cantidad_de_monedas = cont // i
        cont = cont % i
        monedas_usadas.extend([i]*cantidad_de_monedas)
    total_monedas_usadas = len(monedas_usadas)
    print(total_monedas_usadas)
    print('+'.join(map(str,monedas_usadas)))
contador()