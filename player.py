# -*- coding: utf-8 -*-
# Programa: player.py
# Objetivo: Clase que simula el comportamiento de un
#           reproductor de música orientado a objetos.
# Autor: Héctor Sabillón
# Fecha: 10/febrero/2020
import sys
import os
import platform


class Player:
    """
    Se encargar de las funcionalidades del reproductor de
    audio. Reproduce, pausa y detiene la reproducción
    de archivos de audio.
    """

    def __init__(self):
        """ Inicializa una lista de reproducción """
        self.playlist = list()
        # Diccionarios
        # Objetos que almacenan información en pares (clave y valor)
        self.options = {"1": self.add_song}
        #                 "2": self.play,
        #                 "3": self.search_song,
        #                 "4": self.delete_song,
        #                 "5": self.close}

    def menu(self):
        """ Despliega el menú principal. """
        self.clear_screen()
        print("""
                Reproductor musical
                
                1. Agregar canción a la lista de reproducción
                2. Reproducir
                3. Buscar una canción en la lista de reproducción
                4. Eliminar una canción en la lista de reproducción
                5.Salir
                """)

    def press_enter(self):
        """ Realiza una pausa y solicita presionar una tecla """
        input("\nPresiona Enter para continuar")

    def clear_screen(self):
        """
        Verifica mediante la librería platform el sistema operativo
        del usuario y limpia la pantalla dependiendo del SO utilizado.
        """
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Darwin" or platform.system() == "Linux":
            os.system("clear")
        else:
            print("Plataforma no soportada")

    def add_song(self):
        """ Agrega una nueva canción a la lista de reproducción. """
        print("\n======= Agregar nuevas canciones al reproductor =======")
        print(" Las canciones deben seguir el siguiente formato: ")
        print(" nombrecancion + . + extensión (ejemplo: \"canción.mp3\")")
        print("---------------------------------------------------------")
        self.playlist.append(
            input("Ingrese el nombre de la canción: "))
        self.press_enter()

    def run(self):
        """ Despliega el menú principal y procesa las opciones. """
        while True:
            self.menu()
            choice = input("Ingrese una opción: ")
            action = self.options.get(choice)
            if action:
                action()
            else:
                print("¡{0} no es una opción vålida!".format(choice))


if __name__ == "__main__":
    player = Player()
    player.run()
