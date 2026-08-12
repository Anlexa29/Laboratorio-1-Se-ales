import tkinter as tk
from tkinter import ttk

import numpy as np

from señales import generar_señal
from graficas import crear_grafica, actualizar_grafica
from audio import reproducir_señal, detener_audio


class Aplicacion:
    def __init__(self, root):
        self.root = root

        self.root.title(
            "Generador de Señales Digitales"
        )

        self.root.geometry(
            "1000x750"
        )

        self.tipo_señal = tk.StringVar(
            value="Senoidal"
        )

        self.frecuencia = tk.DoubleVar(
            value=440
        )

        self.amplitud = tk.DoubleVar(
            value=100
        )

        self.offset = tk.DoubleVar(
            value=0
        )

        self.frecuencia_muestreo = tk.IntVar(
            value=40000
        )

        self.crear_controles()

        self.figura, self.eje, self.canvas = crear_grafica(
            self.frame_grafica
        )

        self.canvas.get_tk_widget().pack(
            fill=tk.BOTH,
            expand=True
        )

        self.actualizar()

    def crear_controles(self):

        frame_controles = ttk.Frame(
            self.root,
            padding=10
        )

        frame_controles.pack(
            fill=tk.X
        )

        
        # TIPO DE SEÑAL

        ttk.Label(
            frame_controles,
            text="Señal:"
        ).grid(
            row=0,
            column=0,
            sticky="w"
        )

        combo_señal = ttk.Combobox(
            frame_controles,
            textvariable=self.tipo_señal,
            values=[
                "Senoidal",
                "Cuadrada",
                "Triangular",
                "Diente de sierra"
            ],
            state="readonly",
            width=20
        )

        combo_señal.grid(
            row=0,
            column=1,
            padx=10
        )

        combo_señal.bind(
            "<<ComboboxSelected>>",
            lambda event: self.actualizar()
        )

        # FRECUENCIA

        ttk.Label(
            frame_controles,
            text="Frecuencia:"
        ).grid(
            row=1,
            column=0,
            sticky="w"
        )

        self.etiqueta_frecuencia = ttk.Label(
            frame_controles,
            text="440 Hz"
        )

        self.etiqueta_frecuencia.grid(
            row=1,
            column=2,
            padx=10
        )

        escala_frecuencia = ttk.Scale(
            frame_controles,
            from_=100,
            to=2000,
            variable=self.frecuencia,
            command=lambda value: self.actualizar()
        )

        escala_frecuencia.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=10
        )


        # AMPLITUD


        ttk.Label(
            frame_controles,
            text="Amplitud:"
        ).grid(
            row=2,
            column=0,
            sticky="w"
        )

        self.etiqueta_amplitud = ttk.Label(
            frame_controles,
            text="100 %"
        )

        self.etiqueta_amplitud.grid(
            row=2,
            column=2,
            padx=10
        )

        escala_amplitud = ttk.Scale(
            frame_controles,
            from_=0,
            to=100,
            variable=self.amplitud,
            command=lambda value: self.actualizar()
        )

        escala_amplitud.grid(
            row=2,
            column=1,
            sticky="ew",
            padx=10
        )


        # OFFSET


        ttk.Label(
            frame_controles,
            text="Offset:"
        ).grid(
            row=3,
            column=0,
            sticky="w"
        )

        self.etiqueta_offset = ttk.Label(
            frame_controles,
            text="0.00"
        )

        self.etiqueta_offset.grid(
            row=3,
            column=2,
            padx=10
        )

        escala_offset = ttk.Scale(
            frame_controles,
            from_=-1,
            to=1,
            variable=self.offset,
            command=lambda value: self.actualizar()
        )

        escala_offset.grid(
            row=3,
            column=1,
            sticky="ew",
            padx=10
        )


        # FRECUENCIA DE MUESTREO


        ttk.Label(
            frame_controles,
            text="Frecuencia de muestreo:"
        ).grid(
            row=4,
            column=0,
            sticky="w"
        )

        combo_muestreo = ttk.Combobox(
            frame_controles,
            textvariable=self.frecuencia_muestreo,
            values=[
                1000,
                8000,
                22000,
                40000
            ],
            state="readonly",
            width=20
        )

        combo_muestreo.grid(
            row=4,
            column=1,
            padx=10
        )

        combo_muestreo.bind(
            "<<ComboboxSelected>>",
            lambda event: self.actualizar()
        )

   
        # BOTONES
   

        frame_botones = ttk.Frame(
            frame_controles
        )

        frame_botones.grid(
            row=5,
            column=0,
            columnspan=3,
            pady=15
        )

        ttk.Button(
            frame_botones,
            text="▶ Reproducir",
            command=self.reproducir
        ).pack(
            side=tk.LEFT,
            padx=5
        )

        ttk.Button(
            frame_botones,
            text="■ Detener",
            command=detener_audio
        ).pack(
            side=tk.LEFT,
            padx=5
        )

        frame_controles.columnconfigure(
            1,
            weight=1
        )


        # GRÁFICA


        self.frame_grafica = ttk.Frame(
            self.root,
            padding=10
        )

        self.frame_grafica.pack(
            fill=tk.BOTH,
            expand=True
        )

    def obtener_parametros(self):

        frecuencia = self.frecuencia.get()

        amplitud = self.amplitud.get() / 100

        offset = self.offset.get()

        frecuencia_muestreo = self.frecuencia_muestreo.get()

        return (
            frecuencia,
            amplitud,
            offset,
            frecuencia_muestreo
        )

    def generar_datos(self):

        (
            frecuencia,
            amplitud,
            offset,
            frecuencia_muestreo
        ) = self.obtener_parametros()

        duracion = 0.02

        tiempo = np.arange(
            0,
            duracion,
            1 / frecuencia_muestreo
        )

        señal_base = generar_señal(
            self.tipo_señal.get(),
            tiempo,
            frecuencia
        )

        señal = (
            amplitud * señal_base
            + offset
        )

        return (
            tiempo,
            señal
        )

    def actualizar(self):

        tiempo, señal = self.generar_datos()

        (
            frecuencia,
            amplitud,
            offset,
            frecuencia_muestreo
        ) = self.obtener_parametros()

        self.etiqueta_frecuencia.config(
            text=f"{frecuencia:.0f} Hz"
        )

        self.etiqueta_amplitud.config(
            text=f"{amplitud * 100:.0f} %"
        )

        self.etiqueta_offset.config(
            text=f"{offset:.2f}"
        )

        actualizar_grafica(
            self.eje,
            self.canvas,
            tiempo,
            señal,
            self.tipo_señal.get(),
            frecuencia,
            amplitud,
            offset
        )

    def reproducir(self):

        (
            frecuencia,
            amplitud,
            offset,
            frecuencia_muestreo
        ) = self.obtener_parametros()

        duracion = 2

        tiempo = np.arange(
            0,
            duracion,
            1 / frecuencia_muestreo
        )

        señal_base = generar_señal(
            self.tipo_señal.get(),
            tiempo,
            frecuencia
        )

        señal = (
            amplitud * señal_base
            + offset
        )

        # Evita valores fuera del rango
        # permitido por el audio digital.
        señal = np.clip(
            señal,
            -1,
            1
        )

        reproducir_señal(
            señal.astype(np.float32),
            frecuencia_muestreo
        )