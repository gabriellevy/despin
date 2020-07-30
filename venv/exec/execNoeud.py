from exec.situation import *
from exec.execHistoire import *

class ExecNoeud:

    def __init__(self, noeudAExecuter):
        self.m_NoeudAExecuter = noeudAExecuter

    def ExecuterActionsNoeud(self, noeudAExecuter):
        """
        exécute tout ce qui est défini dans ce noeud (changements de caracs, go to un autre effet etc...
        :param noeudAExecuter:
        """
        self.m_NoeudAExecuter = noeudAExecuter

    def LancerNoeud(self):

        self.m_NoeudAExecuter.m_Execute = True

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
            effetToGoTo = ExecHistoire.EXEC_HISTOIRE.GetEvtActuel()[self.m_NoeudAExecuter.m_GoToEffetId]
            Situation.SITUATION.SetEffetCourant(effetToGoTo)