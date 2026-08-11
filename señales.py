import numpy as np


def generar_senoidal(t, frecuencia):
    return np.sin(2 * np.pi * frecuencia * t)


def generar_cuadrada(t, frecuencia):
    return np.where(
        np.sin(2 * np.pi * frecuencia * t) >= 0,
        1.0,
        -1.0
    )


def generar_triangular(t, frecuencia):
    return 2 * np.abs(
        2 * (frecuencia * t - np.floor(frecuencia * t + 0.5))
    ) - 1


def generar_diente_sierra(t, frecuencia):
    return 2 * (
        frecuencia * t - np.floor(frecuencia * t + 0.5)
    )


def generar_señal(tipo, t, frecuencia):
    if tipo == "Senoidal":
        return generar_senoidal(t, frecuencia)

    elif tipo == "Cuadrada":
        return generar_cuadrada(t, frecuencia)

    elif tipo == "Triangular":
        return generar_triangular(t, frecuencia)

    elif tipo == "Diente de sierra":
        return generar_diente_sierra(t, frecuencia)

    return generar_senoidal(t, frecuencia)