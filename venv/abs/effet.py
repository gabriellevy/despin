from abs.noeudNarration import NoeudNarration
from abs.evt import *

class Effet(NoeudNarration):
    """ élément de base pour raconter une histoire"""

    compteurId = 0

    def __init__(self, evt, texte, id):
        if (isinstance(evt, Evt)) != True:
            raise TypeError( \
                "Impossible de créer un effet avec comme 'evt' un objet qui n'est pas un événement mais un : '{0}'".format( \
                    type(evt)))
        self.m_Evt = evt
        NoeudNarration.__init__(self, id, texte)

    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return "Effet {}-{}".format(self.m_Id, self.m_Texte)



