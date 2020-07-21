from abs.effet import Effet
from abs.noeudNarration import NoeudNarration

class Evt(NoeudNarration):
    """sorte de chapitre groupant les effets"""

    compteurId = 0

    def __init__(self, id):
        NoeudNarration.__init__(self, id, "")
        self.m_Effets = list()

    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return "Evt {}".format(self.m_Id)

    def __getitem__(self, index):
        """Comme evt est essentiellement un conteneur d'effets ses fonctions d'accès sont surchargés par commodité"""
        return self.m_Evts[index]
    def __setitem__(self, index, effet):
        """Comme evt est essentiellement un conteneur d'effets ses fonctions d'accès sont surchargés par commodité"""
        self.m_Effets[index] = effet
    def __contains__(self, item):
        """Comme evt est essentiellement un conteneur d'effets ses fonctions d'accès sont surchargés par commodité"""
        return self.m_Effets.__contains__(item)
    def __len__(self):
        """Comme evt est essentiellement un conteneur d'effets ses fonctions d'accès sont surchargés par commodité"""
        return self.m_Effets.__len__()

    def ParcourirEffets(self):
        """pseudo itérateur des effets de l'événement"""
        for effet in self.m_Effets:
            yield effet

# stupides tests
print("------tests Evt")