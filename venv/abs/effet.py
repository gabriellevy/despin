from noeudNarration import NoeudNarration

class Effet(NoeudNarration):
    """ élément de base pour raconter une histoire"""

    def __init__(self, id, texte):
        NoeudNarration.__init__(self, id, texte)

