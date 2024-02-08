import json

with open("data.json", "r") as f:
    data = json.load(f)
    comerciales = data["ventas"]["comerciales"]

max_comision = 0

for comercial in comerciales:
    comision = comerciales["comision"]
    if comision > max_comision:
        max_comision = comision

print(f"El valor máximo de la comisión es {max_comision}")