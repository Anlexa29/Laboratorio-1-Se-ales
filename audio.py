import sounddevice as sd


def reproducir_señal(señal, frecuencia_muestreo):
    sd.stop()

    sd.play(
        señal,
        frecuencia_muestreo
    )


def detener_audio():
    sd.stop()