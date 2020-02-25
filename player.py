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
        self.options = {"1": self.add_song,
                        "2": self.play_song,
                        "3": self.search_song,
                        "4": self.delete_song,
                        "5": self.close}

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

    def play_song(self):
        """
        Reproduce una canción si el formato es permitido.
        Los formatos permitidos se encuentran en ArchivosSoportados.
        """
        file_filter = input("Ingrese el nombre de la canci´ón a reproducir: ")
        if self.search_song(file_filter):
            pass

        self.press_enter()

    def search_song(self, file_filter="", delete=False):
        """ Busca una canción dentro de la lista de reproducción. """
        if file_filter == "":
            file_filter = input("Ingresa el término de búsqueda: ")

        for x in range(len(self.playlist)):
            if file_filter == self.playlist[x]:
                print("Canción {0} encontrada.".format(file_filter))
                # Operador ternario
                self.press_enter() if not delete else True

                return True

        print("Canción no existe dentro de la lista de reproducción.")
        self.press_enter()

        return False

    def delete_song(self):
        """ Elimina una canción de la lista de reproducción. """
        file_filter = input("Ingrese el nombre de la canción: ")
        if self.search_song(file_filter, True):
            try:
                self.playlist.remove(file_filter)
                print("¡La canción {0} ha sido removida de la lista!"
                      .format(file_filter))
                self.press_enter()
            except ValueError:
                print("¡La canción no se encuentra en tu lista de reproducción!")
                self.press_enter()

    def close(self):
        """ Cierra el reproductor musical. """
        print("Gracias por utilizar nuestro reproductor musical.")
        sys.exit(0)

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
                self.press_enter()


if __name__ == "__main__":
    player = Player()
    player.run()
