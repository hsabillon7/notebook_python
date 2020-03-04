# -*- coding: utf8 -*-
from nota import Note


class Notebook:
    """
    Representa una colección de notas que pueden ser
    etiquetadas, modificadas y buscadas.
    """

    def __init__(self):
        """ Inicializa una libreta vacía """
        self.notes = list()

    def new_note(self, memo, tags=""):
        """ Crea una nueva nota y la agrega a la libreta """
        self.notes.append(Note(memo, tags))

    def _search_note(self, note_id):
        """
        Busca una nota con el id enviado.
        Esta función es privada (empieza con _).
        https://docs.python.org/2/tutorial/classes.html
        """
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note

        return None

    def modify_note(self, note_id, memo):
        """
        Encuentra la nota con el valor del id y modifica
        el contenido de la misma.
        """
        note = self._search_note(note_id)

        if note:
            note.memo = memo
            return True
        else:
            print("No existe una nota con el id: {0}"
                  .format(note_id))
            return False

    def modify_tags_note(self, note_id, tags):
        """
        Encuentra la nota con el valor del id y modifica
        las etiquetas de la misma.
        """
        note = self._search_note(note_id)

        if note:
            note.tags = tags
            return True
        else:
            print("No existe una nota con el id: {0}"
                  .format(note_id))
            return False

    def search(self, filter):
        """
        Busca todas las notas que satisfacen el filtro enviado.
        """
        return [note for note in self.notes if note.search(filter)]
