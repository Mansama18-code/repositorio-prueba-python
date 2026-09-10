import pandas as pd
import numpy as np

# Semilla para reproducibilidad de las simulaciones con NumPy
np.random.seed(42)

# Carga de archivos CSV con rutas absolutas requeridas
df_sales = pd.read_csv('sales.csv')
df_inventories = pd.read_csv('inventories.csv')
df_satisfaction = pd.read_csv('satisfaction.csv')

# Limpieza de datos: eliminación de valores nulos
df_sales = df_sales.dropna()
df_inventories = df_inventories.dropna()
df_satisfaction = df_satisfaction.dropna()

# Verificación rápida de la estructura
print("Estructura de Ventas:", df_sales.shape)
print("Estructura de Inventarios:", df_inventories.shape)
print("Estructura de Satisfacción:", df_satisfaction.shape)


# Cálculo del ingreso total por transacción
df_sales['Total_Ventas'] = df_sales['Cantidad'] * df_sales['Precio_Unitario']

# Ventas totales por tienda
ventas_por_tienda = df_sales.groupby('Tienda')['Total_Ventas'].sum()
print("--- Ventas Totales por Tienda ---")
print(ventas_por_tienda)

# Ventas totales por producto
ventas_por_producto = df_sales.groupby('Producto')['Cantidad'].sum()

# Promedio de ventas por tienda y categoría (si existe la columna 'Categoria')
if 'Categoria' in df_sales.columns:
    ventas_categoria_tienda = df_sales.groupby(['Tienda', 'Categoria'])['Total_Ventas'].mean()
    print("\n--- Promedio de Ventas por Tienda y Categoría ---")
    print(ventas_categoria_tienda)

# Resumen estadístico
print("\n--- Resumen Estadístico de Ventas ---")
print(df_sales['Total_Ventas'].describe())

# Filtrar tiendas con baja satisfacción (< 60% o < 0.60 según el formato)
# Si los datos están de 0 a 100:
baja_satisfaccion = df_satisfaction[df_satisfaction['Puntaje_Satisfaccion'] < 60]

print("--- Tiendas con Baja Satisfacción del Cliente (<60%) ---")
print(baja_satisfaccion)

# 1. Conversión de columna Pandas a Array de NumPy
arr_ventas = df_sales['Total_Ventas'].to_numpy()

# 2. Estadísticas con NumPy
mediana_ventas = np.median(arr_ventas)
desviacion_std_ventas = np.std(arr_ventas)

print(f"Mediana de ventas (NumPy): {mediana_ventas:.2f}")
print(f"Desviación Estándar de ventas (NumPy): {desviacion_std_ventas:.2f}")

# 3. Simulación de proyecciones de ventas futuras
# Crecimiento estimado proyectado entre -5% y +15% para los próximos 30 días
simulaciones_crecimiento = np.random.uniform(low=-0.05, high=0.15, size=(30, len(arr_ventas)))
proyecciones = arr_ventas * (1 + simulaciones_crecimiento)

# Estadísticas sobre la proyección
promedio_proyectado = np.mean(proyecciones)
print(f"\nProyección Promedio de Ventas a 30 días: {promedio_proyectado:.2f}")

