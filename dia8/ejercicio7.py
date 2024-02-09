import json

mijson = open('data.json')
variable = json.load(mijson)
def orden(cliente):
    return (cliente['apellido1'], cliente['nombre'])

clientes_sevilla = []
for i in variable['ventas']['clientes']:
    if i['ciudad'] == 'Sevilla':
        clientes_sevilla.append(i)
clientes_sevilla_ordenados = sorted(clientes_sevilla, key=orden)

for cliente in clientes_sevilla_ordenados:
    apellido2 = cliente.get('apellido2', '') 
    print("ID: {}, Nombre: {} {}, Apellido: {}".format(cliente['id'], cliente['nombre'], cliente['apellido1'], apellido2))