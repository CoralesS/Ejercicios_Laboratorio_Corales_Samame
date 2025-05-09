import numpy as np
# Ejercicio 1: FOTOCOPIAS PARA APUNTES

# Definimos el presupuesto disponible 
presupuesto = 8.0

# Array con los precios por página de cada copistería
precios = np.array([0.10, 0.12, 1.75, 0.08])

# Calculamos cuántas copias se pueden hacer en cada copistería
copias_array = np.floor(presupuesto / precios)  

# Obtenemos el valor máximo de copias que se pueden hacer y el índice de la copistería correspondiente
max_copias = int(copias_array.max())           
indice_max = int(copias_array.argmax())       

# Asignamos nombres de las copisterías 
nombres = ['A', 'B', 'C', 'D']

# Mostramos los resultados de cada copistería
print("===== Resultados Ejercicio Fotocopias =====")
for i, nombre in enumerate(nombres):
    print(f"Copisteria {nombre}: precio S/{precios[i]:.2f} ----> puede copiar {int(copias_array[i])} paginas")

# Mostramos cuál es la mejor opción
print(f"\nCon S/{presupuesto:.2f} obtienes la mayor cantidad de copias ({max_copias}) en la copisteria {nombres[indice_max]}.")
