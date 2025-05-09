import pandas as pd
# Ejercicio 3: PRÉSTAMOS DE LIBROS EN LA BIBLIOTECA

# Crear el DataFrame con los datos de la tabla
datos = {
    'Estudiante': ['Rosa', 'David', 'Elena', 'Mario', 'Paula'],
    'Dias_prestamo': [7, 10, 5, 12, 3]
}
df = pd.DataFrame(datos)

# Mostrar el DataFrame
print("===== Tabla de Prestamos =====")
print(df)

# Calcular el promedio y el máximo de días de préstamo
promedio = df['Dias_prestamo'].mean()
maximo = df['Dias_prestamo'].max()

# Mostrar estadísticas
print("\n===== Estadisticas =====")
print(f"Promedio de dias de prestamo: {promedio:.2f}")
print(f"Maximo de dias de prestamo: {maximo}")

# Filtrar estudiantes que retuvieron el libro más de 8 días
filtro = df[df['Dias_prestamo'] > 8]

# Mostrar los resultados del filtro
print("\n===== Estudiantes con mes de 8 dias de prestamo =====")
print(filtro)

