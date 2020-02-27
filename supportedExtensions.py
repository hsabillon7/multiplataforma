# -*- coding: utf-8 -*-
# Programa: supportedExtensions.py
# Objetivo: Define los tipos de archivos soportados por
#           el reproductor.
# Autor: Héctor Sabillón
# Fecha: 25/febrero/2020


class Mp3File:
    """
    Clase que se encarga de manejar los archivos de audio
    con formato MP3 (.mp3).
    """

    def __init__(self, filename):
        """ Inicializa los valores de la clase MP3. """
        self.ext = ".mp3"
        self.filename = filename

    def play(self):
        """ Reproduce el archivo de audio. """
        print("Reproducir {0} con el códec MP3".format(self.filename))


class WavFile:
    """
    Clase que se encarga de manejar los archivos de audio
    con formato WAV (.wav).
    """

    def __init__(self, filename):
        """ Inicializa los valores de la clase WAV. """
        self.ext = ".wav"
        self.filename = filename

    def play(self):
        """ Reproduce el archivo de audio. """
        print("Reproducir {0} con el códec WAV".format(self.filename))


class OggFile:
    """
    Clase que se encarga de manejar los archivos de audio
    con formato OGG (.ogg).
    """

    def __init__(self, filename):
        """ Inicializa los valores de la clase OGG. """
        self.ext = ".ogg"
        self.filename = filename

    def play(self):
        """ Reproduce el archivo de audio. """
        print("Reproducir {0} con el códec OGG".format(self.filename))
