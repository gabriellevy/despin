from exec.execNoeud import *
from abs.choix import *

class ExecChoix(ExecNoeud):

    def __init__(self, choix, execHistoire):
        ExecNoeud.__init__(self, choix, execHistoire)
        self.m_Choix = choix

    def __repr__(self):
        """Représentation d'un exec choix"""
        chaine = "ExecChoix : "
        chaine += self.m_Choix.m_Id
        chaine += "\n"
        if (self.m_NoeudAExecuter.m_Execute):
            chaine += "Déjà exécuté"
        else:
            chaine += "Pas encore exécuté"
        return chaine