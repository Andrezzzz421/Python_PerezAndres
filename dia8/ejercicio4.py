import json

mijson = open('data.json')
variable = json.load(mijson)

pedidos_cumplen_criterios = []

for pedido in variable['ventas']['pedidos']:
    año_pedido = int(pedido['fecha'].split('-')[0])
    
    if año_pedido == 2017 and pedido['total'] > 500:
        pedidos_cumplen_criterios.append(pedido)

print(pedidos_cumplen_criterios)