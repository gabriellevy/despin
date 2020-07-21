from abs.noeudNarration import NoeudNarration

class Effet(NoeudNarration):
    """ élément de base pour raconter une histoire"""

    compteurId = 0

    def __init__(self, texte, id):
        NoeudNarration.__init__(self, id, texte)

    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return "Effet {}-{}".format(self.m_Id, self.m_Texte)



