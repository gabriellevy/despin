from exec.situation import *
from exec.execHistoire import *

class ExecNoeud:

    def __init__(self, noeudAExecuter, execHistoire):
        self.m_NoeudAExecuter = noeudAExecuter
        self.m_ExecHistoire = execHistoire

    # def ExecuterActionsNoeud(self, noeudAExecuter):
        """
        exécute tout ce qui est défini dans ce noeud (changements de caracs, etc...
        :param noeudAExecuter:
        """
        # self.m_NoeudAExecuter = noeudAExecuter

    def LancerNoeud(self):
        self.m_NoeudAExecuter.m_Execute = True

        for changeCarac in self.m_NoeudAExecuter.m_SetsCaracs:
            changeCarac.Appliquer()

        if self.m_NoeudAExecuter.m_ChangementPhaseHistoire != None:
            situation = Situation()
            situation.m_PhaseHistoire = self.m_NoeudAExecuter.m_ChangementPhaseHistoire

    def QuelquechoseAAfficher(self):
        """
        :return: True si l'execNoeud doit faire une pause pour afficher quelque chose
        """
        return False

    def AMarqueUnePause(self):
        """

        :return: true si ce noeud à exécuter à forcément marqué une pause par exemple si c'est un effet qui contient un choix
        """
        return False

    def AppliquerGoTo(self):
        """
        cherche si le noeud courant contient un saut vers un autre effet ou evt et l'applique
        :return: true si il y a un go to qui a été appliqué
        """
        if ( self.m_NoeudAExecuter.m_GoToEffetId != None):
            self.m_ExecHistoire.GoToEffetId(self.m_NoeudAExecuter.m_GoToEffetId)
            return True

        return False