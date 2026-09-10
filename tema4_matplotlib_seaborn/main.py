import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Configuración del estilo general de Seaborn
sns.set_theme(style="whitegrid")

# ==========================================
# 1. PASO 1 Y 2: Carga, exploración y preparación de datos
# ==========================================

# Cargar el dataset (ajusta la ruta según tu entorno)
df = pd.read_csv("tema4_matplotlib_seaborn/superstore_dataset2012.csv", encoding="latin-1")

# Limpieza y preparación inicial de variables
# Limpieza de nombres de columnas (eliminar espacios en blanco)
df.columns = df.columns.str.strip()

# Conversión de variables de fecha a datetime
# Conversión de variables de fecha indicando dayfirst=True
if "Order Date" in df.columns:
    df["Order Date"] = pd.to_datetime(
        df["Order Date"], dayfirst=True, errors="coerce"
    )

if "Ship Date" in df.columns:
    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"], dayfirst=True, errors="coerce"
    )

# Tratamiento de nulos en variables numéricas clave
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce").fillna(0)
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce").fillna(0)
df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce").fillna(0)
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce").fillna(0)

# ==========================================
# 2. VISUALIZACIONES INDIVIDUALES
# ==========================================

# --- Requisito: Univariante Matplotlib ---
plt.figure(figsize=(8, 5))
plt.hist(df["Sales"], bins=50, color="teal", edgecolor="black", alpha=0.7)
plt.title(
    "Distribución de Ventas (Matplotlib)", fontsize=14, fontweight="bold"
)
plt.xlabel("Monto de Ventas ($)", fontsize=11)
plt.ylabel("Frecuencia", fontsize=11)
plt.yscale("log")  # Escala logarítmica debido al sesgo de las ventas
plt.tight_layout()
plt.show()
# Conclusión: Las ventas presentan un fuerte sesgo a la izquierda; la inmensa mayoría de las
# transacciones son de bajo valor, con unas pocas transacciones excepcionalmente altas.

# --- Requisito: Univariante Seaborn ---
plt.figure(figsize=(9, 5))
sns.boxplot(
    data=df,
    x="Category",
    y="Profit",
    hue="Category",
    palette="Set2",
    legend=False,
)
plt.title(
    "Distribución de Beneficios por Categoría (Seaborn)",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Categoría de Producto", fontsize=11)
plt.ylabel("Beneficio ($)", fontsize=11)
plt.ylim(-1000, 1000)  # Limitar para visualizar mejor la mediana y RIO
plt.tight_layout()
plt.show()
# Conclusión: Tecnología presenta la mediana de beneficio más alta, mientras que
# Mobiliario (Furniture) muestra mayor dispersión y pérdidas significativas en ciertos artículos.

# --- Requisito: Bivariante Matplotlib ---
plt.figure(figsize=(9, 5))
plt.scatter(
    df["Sales"], df["Profit"], color="darkorchid", alpha=0.5, edgecolors="none"
)
plt.title(
    "Relación entre Ventas y Beneficios (Matplotlib)",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Ventas ($)", fontsize=11)
plt.ylabel("Beneficio ($)", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
# Conclusión: Un mayor volumen de ventas no garantiza mayor beneficio; existen ventas elevadas
# que generan pérdidas sustanciales, probablemente debido a descuentos excesivos.

# --- Requisito: Bivariante Seaborn ---
plt.figure(figsize=(9, 5))
sns.regplot(
    data=df,
    x="Discount",
    y="Profit",
    scatter_kws={"alpha": 0.3, "color": "darkorange"},
    line_kws={"color": "red", "linewidth": 2},
)
plt.title(
    "Impacto del Descuento en los Beneficios (Seaborn)",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Tasa de Descuento", fontsize=11)
plt.ylabel("Beneficio ($)", fontsize=11)
plt.tight_layout()
plt.show()
# Conclusión: La línea de regresión confirma una tendencia negativa clara: a mayor nivel de descuento,
# los beneficios decrecen significativamente, convirtiéndose en pérdidas sistemáticas a partir de ciertos umbrales.

# --- Requisito: Multivariante Seaborn (Heatmap de Correlación) ---
plt.figure(figsize=(8, 6))
cols_num = ["Sales", "Profit", "Discount", "Quantity"]
matriz_corr = df[cols_num].corr()

sns.heatmap(
    matriz_corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5,
    square=True,
)
plt.title(
    "Matriz de Correlación de Variables Numéricas",
    fontsize=14,
    fontweight="bold",
)
plt.tight_layout()
plt.show()
# Conclusión: Ventas y Beneficios tienen una correlación positiva moderada. El Descuento presenta
# una correlación negativa con los Beneficios, identificándolo como un factor crítico de pérdida.

# ==========================================
# 3. FIGURA INTEGRADA CON SUBPLOTS Y GUARDADO DE IMAGEN
# ==========================================

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle(
    "Análisis Integral de Ventas Minoristas (Superstore Dataset)",
    fontsize=18,
    fontweight="bold",
    y=0.98,
)

# Subplot 1: Histograma de Ventas (Matplotlib)
axes[0, 0].hist(df["Sales"], bins=40, color="skyblue", edgecolor="navy")
axes[0, 0].set_title(
    "1. Distribución de Ventas (Escala Log)", fontweight="bold"
)
axes[0, 0].set_xlabel("Ventas ($)")
axes[0, 0].set_ylabel("Frecuencia")
axes[0, 0].set_yscale("log")

# Subplot 2: Violinplot de Beneficios por Segmento (Seaborn)
sns.violinplot(
    data=df,
    x="Segment",
    y="Profit",
    hue="Segment",
    palette="Pastel1",
    ax=axes[0, 1],
    legend=False,
)
axes[0, 1].set_title(
    "2. Distribución de Beneficio por Segmento", fontweight="bold"
)
axes[0, 1].set_xlabel("Segmento de Cliente")
axes[0, 1].set_ylabel("Beneficio ($)")
axes[0, 1].set_ylim(-500, 500)

# Subplot 3: Dispersión Ventas vs Beneficios (Matplotlib)
axes[1, 0].scatter(
    df["Sales"], df["Profit"], alpha=0.4, c=df["Discount"], cmap="viridis"
)
axes[1, 0].set_title("3. Ventas vs Beneficios (Color=Descuento)", fontweight="bold")
axes[1, 0].set_xlabel("Ventas ($)")
axes[1, 0].set_ylabel("Beneficio ($)")
axes[1, 0].grid(True, linestyle=":")

# Subplot 4: Heatmap de Correlación (Seaborn)
sns.heatmap(
    matriz_corr,
    annot=True,
    cmap="Blues",
    fmt=".2f",
    ax=axes[1, 1],
    cbar=False,
)
axes[1, 1].set_title("4. Matriz de Correlación", fontweight="bold")

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Guardar la figura integrada en un archivo de imagen
output_filename = "analisis_superstore_subfigures.png"
plt.savefig(output_filename, dpi=300, bbox_inches="tight")
plt.show()

print(f"El panel de gráficos se ha guardado correctamente como: {output_filename}")