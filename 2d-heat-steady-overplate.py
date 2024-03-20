import numpy as np
import matplotlib.pyplot as plt

Lx, Ly = 1.0, 1.0 # Lengths
Nx, Ny = 50, 50 # Grid points (x & y)
dx, dy = Lx / (Nx - 1), Ly / (Ny - 1) # Grid spacing (x & y)

# Boundary
T_top, T_bottom, T_left, T_right= 100.0, 50.0, 100.0, 50.0

T_initial = np.zeros((Ny, Nx)) # arbitiary Ti


T_initial[0, :] = T_top
T_initial[-1, :] = T_bottom
T_initial[:, 0] = T_left
T_initial[:, -1] = T_right

# Using FDM
T = np.copy(T_initial)
maxi = 9000
tolerance = 1e-6

for itr in range(maxi):
    T_new = np.copy(T)
    for i in range(1, Ny-1):
        for j in range(1, Nx-1):
            T_new[i, j] = 0.25 * (T[i+1, j] + T[i-1, j] + T[i, j+1] + T[i, j-1])
    if np.max(np.abs(T_new - T)) < tolerance:
        break
    T = np.copy(T_new)

print("Converged in", itr+1, "iterations")

X, Y = np.meshgrid(np.linspace(0, Lx, Nx), np.linspace(0, Ly, Ny))

plt.figure(figsize=(8, 6))
plt.contourf(X, Y, T, cmap='hot')
plt.colorbar(label='Temperature °C)')
plt.title(f'Distribution Gradient ({itr+1} iterations)')
plt.xlabel('X - axis')
plt.ylabel('Y - axis')
plt.grid(True)

def return_node_temperatures(vertices):
    for vertex in vertices:
        plt.plot(vertex[0], vertex[1], 'ro')    
    vertex_temperatures = []
    for vertex in vertices:
        i_vertex = int(vertex[1] / Ly * (Ny - 1))
        j_vertex = int(vertex[0] / Lx * (Nx - 1))
        temperature = T[i_vertex, j_vertex]
        vertex_temperatures.append(temperature)
        textindic = plt.text(vertex[0], vertex[1], f'{temperature:.2f}', fontsize=10, color='black', ha='center', va='center')
        textindic.set_bbox(dict(facecolor='white', alpha=0.5, edgecolor='white', boxstyle='round'))

# 0.5x0.5 central node inscription
return_node_temperatures([(0.25, 0.25), (0.25, 0.75), (0.75, 0.75), (0.75, 0.25)])
return_node_temperatures([(0.3, 0.3), (0.3, 0.7), (0.7, 0.7), (0.7, 0.3)])

plt.show()
