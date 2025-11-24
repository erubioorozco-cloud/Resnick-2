import numpy as np
import matplotlib.pyplot as plt

# --- DATOS ---
v0 = 50 
angulo = 45
theta = np.radians(angulo)

# --- ESCENARIO 1: TIERRA (g = 9.81) ---
g_tierra = 9.81
t_total_tierra = 2 * v0 * np.sin(theta) / g_tierra
t1 = np.linspace(0, t_total_tierra, 100)

x_tierra = v0 * np.cos(theta) * t1
y_tierra = v0 * np.sin(theta) * t1 - 0.5 * g_tierra * t1**2

# --- ESCENARIO 2: LUNA (g = 1.62) ---
g_luna = 1.62
t_total_luna = 2 * v0 * np.sin(theta) / g_luna
t2 = np.linspace(0, t_total_luna, 100)

x_luna = v0 * np.cos(theta) * t2
y_luna = v0 * np.sin(theta) * t2 - 0.5 * g_luna * t2**2

# --- GRÁFICA COMPARATIVA ---
plt.figure(figsize=(10, 6))

# Dibujamos las dos líneas
plt.plot(x_tierra, y_tierra, color='blue', label='En la Tierra', linewidth=2)
plt.plot(x_luna, y_luna, color='gray', linestyle='--', label='En la Luna', linewidth=2)

plt.title(f"Comparación: Tierra vs Luna (v0={v0} m/s)")
plt.xlabel("Distancia (m)")
plt.ylabel("Altura (m)")
plt.axhline(0, color='black')
plt.grid(True)
plt.legend() # Muestra las etiquetas
plt.show()