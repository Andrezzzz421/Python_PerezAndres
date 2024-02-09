import json
mijson = open('data.json')
variable = json.load(mijson)

nombres_filtrados = []

for cliente in variable['ventas']['clientes']:
    nombre = cliente['nombre']
    if nombre.startswith('A') and nombre.endswith('n'):
        nombres_filtrados.append(nombre)

for cliente in variable['ventas']['clientes']:
    nombre = cliente['nombre']
    if nombre.startswith('P'):
        nombres_filtrados.append(nombre)

nombres_ordenados = sorted(nombres_filtrados)

for nombre in nombres_ordenados:
    print(nombre)