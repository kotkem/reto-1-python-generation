productos = [
    {"id": 1, "nombre": "Laptop Pro 14", "categoria": "Computo", "precio": 25000, "descuento": 0.10, "stock": 5},
    {"id": 2, "nombre": "Mouse Gamer X", "categoria": "Accesorios", "precio": 1200, "descuento": 0.15, "stock": 20},
    {"id": 3, "nombre": "Teclado Mecánico K1", "categoria": "Accesorios", "precio": 2200, "descuento": 0.05, "stock": 10},
    {"id": 4, "nombre": "Monitor 27'' 4K", "categoria": "Computo", "precio": 8000, "descuento": 0.20, "stock": 7},
    {"id": 5, "nombre": "Audífonos Bluetooth Z", "categoria": "Audio", "precio": 1500, "descuento": 0.0, "stock": 15},
]

ventas = [
    {"venta_id": 101, "producto_id": 1, "cantidad": 1, "cliente": "Ana"},
    {"venta_id": 102, "producto_id": 2, "cantidad": 2, "cliente": "Luis"},
    {"venta_id": 103, "producto_id": 4, "cantidad": 1, "cliente": "Sofía"},
    {"venta_id": 104, "producto_id": 2, "cantidad": 1, "cliente": "Carlos"},
    {"venta_id": 105, "producto_id": 5, "cantidad": 3, "cliente": "Ana"},
]

tienda_info = ("TechieStore", "Santiago", 2025)

print(f"Bienvenido a {tienda_info[0]} en {tienda_info[1]} ({tienda_info[2]})")

print(f"Total de productos: {len(productos)}")

#Laptop

p0_precio = productos[0] ["precio"]
p0_desc = productos[0]["descuento"]
p0_final = p0_precio - (p0_precio * p0_desc) 
print(f"{productos[0] ["nombre"]} -> ${p0_final}")

#Mause

p1_precio = productos[1]["precio"]
p1_desc = productos[1]["descuento"]
p1_final = p1_precio - (p1_precio * p1_desc)
print(f"{productos[1]["nombre"]} -> ${p1_final}")

# Teclado

p2_precio = productos[2]["precio"]
p2_desc = productos[2]["descuento"]
p2_final = p2_precio - (p2_precio * p2_desc)
print(f"{productos[2]["nombre"]} -> $ {p2_final}")

# Monitor 

p3_precio = productos[3]["precio"]
p3_desc = productos[3]["descuento"]
p3_final = p3_precio - (p3_precio * p3_desc)
print(f"{productos[3]["nombre"]} ->${p3_final}")

# Audifonos
p4_precio = productos[4]["precio"]
p4_desc = productos[4]["descuento"]
p4_final = p4_precio - (p4_precio * p4_desc)
print(f"{productos[4]["nombre"]} ->  ${p4_final}")


v0 = ventas[0]
v0_total = p0_final * v0["cantidad"]
print(f"Venta {v0['venta_id']}: {v0['cliente']} compró {v0['cantidad']} {productos[0]['nombre']} y pagó {v0_total}")

v1 = ventas[1]
v1_total = p1_final * v1["cantidad"]
print(f"Venta {v1['venta_id']}: {v1['cliente']} compró {v1['cantidad']} {productos[1]['nombre']} y pagó {v1_total}")

v2 = ventas[1]
v2_total = p2_final * v2["cantidad"]
print(f"Venta {v2['venta_id']}: {v2['cliente']} compró {v2['cantidad']} {productos[3]['nombre']} y pagó {v2_total}")

v3 = ventas[3]
v3_total = p1_final * v3["cantidad"]
print(f"Venta {v3['venta_id']}: {v3['cliente']} compró {v3['cantidad']} {productos[1]['nombre']} y pagó {v3_total}")

v4 = ventas[4]
v4_total = p4_final * v4["cantidad"]
print(f"Venta {v4['venta_id']}: {v4['cliente']} compró {v4['cantidad']} {productos[4]['nombre']} y pagó {v4_total}")

ingreso_total = v0_total + v1_total + v2_total + v3_total + v4_total
print(f"Ingreso total: {ingreso_total}")