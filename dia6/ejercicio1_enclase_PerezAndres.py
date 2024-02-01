productos={"Papa":2800,
           "Banano":200,
           "Manzana":1500,
           "Yuca":1400,
           "Cebolla":200,
           "Tomate":300,
           "Limon":200
           }
print(productos)
print("Bienvenido usuario ingrese el producto que desea seleccionar")
producto_seleccionado=str(input(""))
print("Ingrese la cantidad de su producto seleccionado")
cantidad_del_producto=int(input(""))
if producto_seleccionado in productos:
    total= producto_seleccionado[productos]*cantidad_del_producto
    print("el total de su compra es:",total)
else:
    print("EL producto no se encuentra en la lista")





