import numpy as np
# Ejercicio 2: VIAJES AL CAMPUS 

# Dinero disponible para transporte en la semana
presupuesto = 15.0

# Precios por viaje para cada medio de transporte (bus, combi, tren)
precios = np.array([2.50, 3.00, 1.80])

# Calculamos cuántos viajes puede hacer con cada medio de transporte 
viajes_array = np.floor(presupuesto / precios)

# Encontramos la mayor cantidad de viajes y el medio de transporte correspondiente
max_viajes = int(viajes_array.max())
indice_max = int(viajes_array.argmax())

# Nombres de los medios de transporte
medios = ['Bus', 'Combi', 'Tren']

# Mostramos los resultados
print("===== Resultados Ejercicio Viajes al Campus =====")
for i, medio in enumerate(medios):
    print(f"{medio}: precio S/{precios[i]:.2f} ----> puede realizar {int(viajes_array[i])} viajes")

# Mostramos la mejor opción
print(f"\nCon S/{presupuesto:.2f}, el medio que permite mas viajes ({max_viajes}) es el {medios[indice_max]}.")
