import json

mijson = open('data.json')
variable = json.load(mijson)

def fecha(pedido):
    return pedido['fecha']

pedidos = variable['ventas']['pedidos']
pedidos_ordenados = sorted(pedidos, key=fecha, reverse=True)
for i in pedidos_ordenados:
    print(i)
