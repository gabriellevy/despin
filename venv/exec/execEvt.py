from exec.execNoeud import *
from exec.situation import *
from exec.execEffet import ExecEffet

class ExecEvt(ExecNoeud):

    def __init__(self, evt):
        self.m_Evt = evt
        self.m_ExecEffetCourant = None

    def GetExecEffetActuel(self):
        if self.m_ExecEffetCourant is None:
            # premier effet
            if (Situation.SITUATION.GetEffetCourant() is None):
                assert len(self.m_Evt) > 0, "erreur dans GetExecEffetActuel : Il n'y a aucun effet dans l'événement '{}'!".format(self.m_Evt)
                Situation.SITUATION.SetEffetCourant(self.m_Evt.m_Effets[0])
            effetCourant = Situation.SITUATION.GetEffetCourant()
            self.m_ExecEffetCourant = ExecEffet(effetCourant)
        return self.m_ExecEffetCourant

    def LancerNoeud(self):
        print("Événement {}\n-----------------------".format(self.m_Evt.m_Id));
        self.m_ExecEffetCourant.LancerNoeud()