import json
mijson = open('data.json')
variable = json.load(mijson)

comerciales_con_comision = []

for comercial in variable['ventas'],['comerciales']:
    comision = (comercial['comision'])
    if 0.05 <= comision <= 0.11:
        nombre_apellidos = (f"{comercial['nombre']} {comercial['apellido1']} {comercial.get('apellido2', '')}")
        comerciales_con_comision.append(nombre_apellidos)

print("Comerciales con comisión entre 0.05 y 0.11:")
for nombre_apellidos in comerciales_con_comision:
    print(nombre_apellidos)
