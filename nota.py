# -*- coding: utf-8 -*-
import datetime

# Almacena el último id de la nota
last_id = 0


class Note:
    """
    Representa una nota en una libreta.
    Permite almacenar una nota, colocarle etiquetas, buscar
    una nota. 
    """

    def __init__(self, memo, tags=""):
        """
        Inicializa una nota con el valor de memo y las etiquetas
        enviadas por el usuario(separadas por espacio). Automáticamente
        inserta la fecha de creación y un id único.
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def search(self, filter):
        """
        Determina si la nota actual está contenida en el valor
        del filtro (distingue mayúsculas de minúsculas). 
        Retorna True si es igual o False en caso contrario.
        """
        return filter in self.memo or filter in self.tags
