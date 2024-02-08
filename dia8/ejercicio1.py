import json

mijson = open('data.json')
variable = json.load(mijson)
mijson.close()

def fecha(pedido):
    return pedido['fecha']

pedidos = variable['ventas']['pedidos']
pedidos_ordenados = sorted(pedidos, key=fecha, reverse=True)
print(pedidos_ordenados)
