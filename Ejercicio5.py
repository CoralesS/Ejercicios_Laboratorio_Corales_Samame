import numpy as np
# Ejercicio 5: RECARGA DE DATOS MÓVILES

# Datos de los paquetes
gb = np.array([1, 2, 5, 10])      
precios = np.array([5, 9, 20, 35])

# Calcular el costo por GB de cada paquete
costo_por_gb = precios / gb

# Encontrar el costo mínimo y el índice
minimo = costo_por_gb.min()
indice_min = costo_por_gb.argmin()

# Mostrar resultados
print("===== Costo por GB en cada paquete =====")
for i in range(len(gb)):
    print(f"Paquete de {gb[i]} GB: S/{precios[i]} --> S/{costo_por_gb[i]:.2f} por GB")

# Mostrar el paquete más económico
print(f"\nEl paquete mas economico por GB es el de {gb[indice_min]} GB (S/{precios[indice_min]}) con S/{minimo:.2f} por GB.")

