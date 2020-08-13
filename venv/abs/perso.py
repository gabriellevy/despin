from exec.situation import Situation

class Perso():
    """
    caractéristiques fixes du personnage indépendante du déroulement de l'aventure
    (pour l'instant juste liste des caracs qu'il affiche, les autres sont cachées)
    """

    def __init__(self):
        self.m_CaracsAffichees = list()

    def AjouterCarac(self, idCarac, valCarac):
        self.m_CaracsAffichees.append(idCarac)
        situation = Situation()
        situation.SetCarac(idCarac, valCarac)
