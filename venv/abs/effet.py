from noeudNarration import NoeudNarration

class Effet(NoeudNarration):
    """ élément de base pour raconter une histoire"""

    compteurId = 0

    def __init__(self, texte, id = ""):
        if ( id == ""):
            id = "effet_id_{0}".format(Effet.compteurId)
            Effet.compteurId += 1

        NoeudNarration.__init__(self, id, texte)

    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return "Effet {}-{}".format(self.m_Id, self.m_Texte)



