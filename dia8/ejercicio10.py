import json
mijson = open('data.json')
variable = json.load(mijson)    
nombres_comerciales_ruiz = set()  # Utilizamos un conjunto para eliminar duplicados

for comercial in variable['ventas']['comerciales']:
    apellido = comercial['apellido1']
    if apellido == 'Ruiz':
        nombres_comerciales_ruiz.add(comercial['nombre'])

nombres_comerciales_ruiz_ordenados = sorted(list(nombres_comerciales_ruiz))

for nombre in nombres_comerciales_ruiz_ordenados:
    print(nombre)