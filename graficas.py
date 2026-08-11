from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def crear_grafica(parent):
    figura = Figure(
        figsize=(8, 4),
        dpi=100
    )

    eje = figura.add_subplot(111)

    eje.set_title("Señal en el dominio del tiempo")
    eje.set_xlabel("Tiempo (s)")
    eje.set_ylabel("Amplitud")
    eje.grid(True)

    canvas = FigureCanvasTkAgg(
        figura,
        master=parent
    )

    canvas.draw()

    return figura, eje, canvas


def actualizar_grafica(
    eje,
    canvas,
    tiempo,
    señal,
    tipo,
    frecuencia,
    amplitud,
    offset
):
    eje.clear()

    eje.plot(
        tiempo,
        señal
    )

    eje.set_title(
        f"{tipo} - {frecuencia:.0f} Hz"
    )

    eje.set_xlabel("Tiempo (s)")
    eje.set_ylabel("Amplitud")

    eje.grid(True)

    limite = max(
        1.2,
        abs(offset) + amplitud + 0.2
    )

    eje.set_ylim(
        -limite,
        limite
    )

    canvas.draw()