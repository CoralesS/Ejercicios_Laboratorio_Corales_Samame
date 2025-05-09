import pandas as pd
# Ejercicio 4: GASTOS DE ALMUERZO SEMANAL  

# Lista de gastos de lunes a viernes
gastos = [4.0, 3.5, 5.0, 4.2, 3.8]
dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']

# Crear DataFrame con columnas Día y Gasto
df = pd.DataFrame({'Dia': dias, 'Gasto': gastos})

# Calcular gasto total y gasto medio
gasto_total = df['Gasto'].sum()
gasto_promedio = df['Gasto'].mean()

# Mostrar resultados generales
print("===== Gastos Semanales =====")
print(df)

print("\nGasto total de la semana: S/", gasto_total)
print("Gasto promedio diario: S/", round(gasto_promedio, 2))

# Identificar días con gasto mayor al promedio
dias_mayor_promedio = df[df['Gasto'] > gasto_promedio]

# Mostrar resultados del filtro
print("\nDias con gasto mayor al promedio:")
print(dias_mayor_promedio)

