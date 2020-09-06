from exec.execNoeud import *
from exec.situation import *
from exec.execEffet import ExecEffet

class ExecEvt(ExecNoeud):

    def __init__(self, evt, execHistoire):
        ExecNoeud.__init__(self, evt, execHistoire)
        self.m_Evt = evt
        self.m_ExecEffetActuel = None

    def GetExecEffetActuel(self):
        situation = Situation()
        if self.m_ExecEffetActuel is None:
            # premier effet
            if (situation.GetEffetCourant() is None):
                assert len(self.m_Evt) > 0, "erreur dans GetExecEffetActuel : Il n'y a aucun effet dans l'événement '{}'!".format(self.m_Evt)
                situation.SetEffetCourant(self.m_Evt.m_Effets[0])
            effetCourant = situation.GetEffetCourant()
            self.m_ExecEffetActuel = ExecEffet(effetCourant, self.m_ExecHistoire)
        return self.m_ExecEffetActuel

    def EnregistrerVisite(self):
        id = "{}{}".format(Situation.PREFIXE_EVT_VISITE, self.m_Evt.m_Id )
        situation = Situation()
        situation.SetCarac(id, "1")

    def SetExecEffetActuel(self, execEffetActuel):
        self.m_ExecEffetActuel = execEffetActuel

    def LancerNoeud(self):
        print("Événement {}\n-----------------------".format(self.m_Evt.m_Id));
        ExecNoeud.LancerNoeud(self)

    def QuelquechoseAAfficher(self):
        return self.m_Evt.m_Texte != None and self.m_Evt.m_Texte != ""

    def __repr__(self):
        """Représentation d'un exec événement"""
        chaine = "ExecEvt : "
        chaine += self.m_Evt.m_Id
        chaine += "\n"
        if (self.m_NoeudAExecuter.m_Parcouru):
            chaine += "Déjà exécuté"
        else:
            chaine += "Pas encore exécuté"
        return chaine