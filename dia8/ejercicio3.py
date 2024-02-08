import json

mijson = open('data.json')
variable = json.load(mijson)

clientes_sin_repetir = set()
for pedido in variable['ventas']['pedidos']:
    clientes_sin_repetir.add(pedido['id_cliente'])

print(clientes_sin_repetir)