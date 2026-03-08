import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Configuración
n_registros = 10000
seed = 42
np.random.seed(seed)
random.seed(seed)

# Listas para simular datos
clientes = [
    (101, "JUAN PEREZ", "CORDOBA"),
    (102, "  marta Sanchez  ", "ROSARIO"),
    (103, "Luis Garcia.", "CABA"),
    (104, "Ana Lopez", "Mendoza"),
    (105, "PEDRO GOMEZ", "CORDOBA"),
    (106, "Lucia Fernandez", "TUCUMAN")
]

productos = [
    ("Laptop Pro", "Electronica", 1200.50),
    ("Mouse Optico", "Accesorios", 25.00),
    ("Monitor 24'", "Electronica", 350.00),
    ("Teclado Mecanico", "Accesorios", 80.00),
    ("Cable HDMI", "Cables", 15.75),
    ("Silla Gamer", "Muebles", 250.00)
]

medios_pago = ["Tarjeta Credito", "Transferencia", "Efectivo", "Debito"]

data = []

for i in range(n_registros):
    # Seleccionar cliente y producto al azar
    c_id, c_nom, c_ciu = random.choice(clientes)
    p_nom, p_cat, p_pre = random.choice(productos)
    
    # Generar fecha con formatos inconsistentes
    base_date = datetime(2025, 1, 1)
    random_date = base_date + timedelta(days=random.randint(0, 365))
    
    if i % 10 == 0:
        fecha_str = random_date.strftime("%d/%m/%Y") # Formato latino
    else:
        fecha_str = random_date.strftime("%Y-%m-%d") # Formato ISO
        
    # Crear errores de nulos (5% de probabilidad)
    precio_final = f"$ {p_pre}" if random.random() > 0.05 else None
    cantidad = random.randint(1, 5) if random.random() > 0.02 else np.nan
    
    # Armar registro
    data.append({
        "id_venta": i + 1000,
        "fecha": fecha_str,
        "cliente_id": c_id,
        "nombre_cliente": c_nom,
        "ciudad": c_ciu,
        "producto": p_nom,
        "categoria": p_cat,
        "precio_unitario": precio_final,
        "cantidad": cantidad,
        "medio_pago": random.choice(medios_pago)
    })

# Convertir a DataFrame
df = pd.DataFrame(data)

# Añadir 200 duplicados exactos para limpieza
duplicados = df.sample(200)
df = pd.concat([df, duplicados], ignore_index=True)

# Guardar CSV
df.to_csv("ventas_raw.csv", index=False)

print(f"Dataset 'ventas_raw.csv' generado con {len(df)} registros.")
print("Errores inyectados: Fechas mixtas, nulos en precios/cantidad, duplicados y strings sucios.")
