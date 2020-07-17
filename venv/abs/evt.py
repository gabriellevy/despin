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

# stupid tests
truc = Evt()
print(truc.m_Id)
print(truc.m_Texte)

truc2 = Evt()
print(truc2.m_Id)