def negate(num):
    return -num
def large_num(num):
    res = (num>10000)
    return res
b=int(input(""))
negate(b)
neg_b=negate(b)
print('b:',b,'neg_b:', neg_b)
big=large_num(b)
print('b is big:',big)


#1-Los valores que se guardan para que se impriman no estan entre parentesis
#2-" B "no estaba definida
#3-En la funcion large_num faltaba colocar un return para que no s devolviera que si num era mayor a 10000 seria true si no seria false