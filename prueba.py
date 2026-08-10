import numpy as np
import matplotlib.pyplot as plt

print("Python está funcionando")
print("Versión de NumPy:", np.__version__)

tiempo = np.linspace(0, 1, 1000)

senal = np.sin(2 * np.pi * 5 * tiempo)

plt.plot(tiempo, senal)
plt.title("Prueba de señal senoidal")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()