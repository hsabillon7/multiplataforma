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
    ext = ".mp3"

    def play(self):
        """ Reproduce el archivo de audio. """
        print("Reproducir {0} con el códec MP3".format(self.filename))


class WavFile:
    """
    Clase que se encarga de manejar los archivos de audio
    con formato WAV (.wav).
    """
    ext = ".wav"

    def play(self):
        """ Reproduce el archivo de audio. """
        print("Reproducir {0} con el códec WAV".format(self.filename))


class OggFile:
    """
    Clase que se encarga de manejar los archivos de audio
    con formato OGG (.ogg).
    """
    ext = ".ogg"

    def play(self):
        """ Reproduce el archivo de audio. """
        print("Reproducir {0} con el códec OGG".format(self.filename))
