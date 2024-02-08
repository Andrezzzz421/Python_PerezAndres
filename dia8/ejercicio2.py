import json

mijson = open('data.json')
variable = json.load(mijson)

def val_mayor(pedido):
    return pedido['total']
pedidos = variable['ventas']['pedidos']
pedidos_ordenados = sorted(pedidos, key=val_mayor , reverse=True)

print(pedidos_ordenados[0],pedidos_ordenados[1])
