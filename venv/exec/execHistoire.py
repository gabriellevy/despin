from abs.effet import *
from abs.evt import *
from abs.histoire import *
from exec.execEvt import *
from exec.execEffet import *
from exec.situation import Situation

class ExecHistoire:

    def __init__(self):
        self.m_Situation = Situation()
        self.m_ExecEvtCourant = None
        self.m_ExecEffetCourant = None
        pass

    def LancerHistoire(self, histoire, premierEvtId = "", premierEffetId = ""):
        self.m_Histoire = histoire
        # gérer persos et caracs ? Affichage graphique ?

        #chargement de fichier

        #chargement éventuel d'evt et effet courants => APRES le chargement de fichier
        if ( premierEvtId != ""):
            evt = self.m_Histoire[premierEvtId]
            Situation.SetEvtCourant(evt)
            if (premierEffetId != ""):
                effet = evt[premierEffetId]
                Situation.SetEffetCourant(effet)

        self.LancerEvtEtOuEffetCourant()

    def LancerEvtEtOuEffetCourant(self):
        execEvtActuel = self.GetExecEvtActuel();
        exeEffetActuel = self.GetExecEffetActuel();
        assert (execEvtActuel is not None), "execEvtActuel actuel introuvable"
        assert (exeEffetActuel is not None), "effet_actuel actuel introuvable"

        execEvtActuel.LancerNoeud();

    def GetExecEvtActuel(self):
        if self.m_ExecEvtCourant is None:
            # premier lancement
            if (Situation.SITUATION.GetEvtCourant() is None):
                assert len(self.m_Histoire) > 0, "erreur dans GetExecEvtActuel : Il n'y a aucun événement dans l'histoire !"
                Situation.SITUATION.SetEvtCourant(self.m_Histoire.m_Evts[0])
            evtCourant = Situation.SITUATION.GetEvtCourant()
            self.m_ExecEvtCourant = ExecEvt(evtCourant)
        return self.m_ExecEvtCourant

    def GetExecEffetActuel(self):
        return self.GetExecEvtActuel().GetExecEffetActuel()
