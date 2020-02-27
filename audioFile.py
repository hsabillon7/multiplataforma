# -*- coding: utf-8 -*-
# Programa: audioFile.py
# Objetivo: Accede a los archivos soportados y verifica que
#           el archivo actual se puede reproducir.
# Autor: Héctor Sabillón
# Fecha: 25/febrero/2020
from supportedExtensions import Mp3File, WavFile, OggFile


class AudioFile:
    """
    Verifica y reproduce un tipo de archivo.
    El archivo solamente se reproduce si existe un códec
    encargado de transformarlo.
    """

    def __init__(self, file_name):
        """
        Verifica el nombre del archivo en busca de su extensión y
        compara la misma contra todos los tipos de archivos soportados
        para obtener si es o no reproducible.
        """
        valid_format = Mp3File(file_name)

        if not file_name.endswith(valid_format.ext):
            valid_format = WavFile(file_name)
            if not file_name.endswith(valid_format.ext):
                valid_format = OggFile(file_name)
                if not file_name.endswith(valid_format.ext):
                    print("No se puede reproducir el archivo.")
                    print("Razón: ")
                    print("¡Extensión no soportada por el reproductor!")
                else:
                    valid_format.play()
            else:
                valid_format.play()
        else:
            print("Archivo MP3")
            valid_format.play()
