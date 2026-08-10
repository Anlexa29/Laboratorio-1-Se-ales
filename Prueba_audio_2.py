import numpy as np
import sounddevice as sd

# Parámetros
frecuencia_muestreo = 44100
frecuencia = 440
duracion = 2
amplitud = 0.3

# Crear vector de tiempo
cantidad_muestras = int(
    frecuencia_muestreo * duracion
)

tiempo = np.arange(
    cantidad_muestras
) / frecuencia_muestreo

# Generar señal senoidal
senal = amplitud * np.sin(
    2 * np.pi * frecuencia * tiempo
)

print("Reproduciendo señal...")
print(f"Frecuencia: {frecuencia} Hz")
print(f"Muestreo: {frecuencia_muestreo} Hz")
print(f"Amplitud: {amplitud}")

# Reproducir
sd.play(
    senal,
    frecuencia_muestreo
)

# Esperar hasta que termine
sd.wait()

print("Reproducción terminada.")