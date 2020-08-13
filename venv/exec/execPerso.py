from exec.situation import Situation

class ExecPerso():
    """
    gestion du personnage en particulier son affichage
    les caracs du eprsos (toutes les caracs en fait) sont stockées dans Situation mais leur affichage ou non est déterminé ici
    à écrserer pour els affichages plus élaborés
    """

    def __init__(self, perso):
        self.m_Perso = perso

    def __repr__(self):
        """Affichage de base"""
        situation = Situation()
        chaine = "Caracs personnage : "
        chaine += "\n"
        for caracId in self.m_Perso.m_CaracsAffichees:
            chaine += "{} : {}\n".format(caracId, situation.m_Caracs[caracId])
        return chaine