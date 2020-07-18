from effet import Effet
from noeudNarration import NoeudNarration

class Evt(NoeudNarration):
    """sorte de chapitre groupant les effets"""

    compteurId = 0

    def __init__(self, id = ""):
        if ( id == ""):
            id = "evt_id_{0}".format(Evt.compteurId)
            Evt.compteurId += 1

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

# stupides tests
print("------tests Evt")
truc = Evt()
print(truc.m_Id)
print(truc.m_Texte)
effet1 = Effet("Il se passe des choses dans cet effet ! ")
truc.m_Effets.append(effet1)
print(truc.m_Effets[0])

truc2 = Evt()
print(truc2.m_Id)
print(truc2.existePas)