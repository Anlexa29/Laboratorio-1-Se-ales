import numpy as np
import sounddevice as sd

frecuencia_muestreo = 44100
frecuencia = 440
duracion = 2

tiempo = np.arange(
    int(frecuencia_muestreo * duracion)
) / frecuencia_muestreo

senal = 0.3 * np.sin(
    2 * np.pi * frecuencia * tiempo
)

sd.play(
    senal,
    frecuencia_muestreo
)

sd.wait()