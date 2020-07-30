# from abs.effet import *
# from abs.evt import *
# from abs.histoire import *
from exec.execEvt import *
# import exec.execEffet
from exec.situation import *

class ExecHistoire:

    EXEC_HISTOIRE = None

    def __init__(self):
        self.m_Situation = Situation()
        ExecHistoire.EXEC_HISTOIRE = self
        self.m_ExecEvtCourant = None
        self.m_ExecEffetCourant = None
        self.m_ExecChoixActuel = None
        pass

    def LancerHistoire(self, histoire, premierEvtId = "", premierEffetId = ""):
        self.m_Histoire = histoire
        # gérer persos et caracs ? Affichage graphique ?

        #chargement de fichier

        #chargement éventuel d'evt et effet courants => APRES le chargement de fichier
        if ( premierEvtId != ""):
            evt = self.m_Histoire[premierEvtId]
            Situation.SITUATION.SetEvtCourant(evt)
            if (premierEffetId != ""):
                effet = evt[premierEffetId]
                Situation.SITUATION.SetEffetCourant(effet)

        self.LancerEvtEtOuEffetCourant()

    def LancerEvtEtOuEffetCourant(self):
        quelqueChoseAffiche = False
        execNoeudActuel = self.GetExecEvtActuel()
        if execNoeudActuel.m_NoeudAExecuter.m_Execute:
            execNoeudActuel = self.GetExecEffetActuel()
        if execNoeudActuel.m_NoeudAExecuter.m_Execute:
            execNoeudActuel = self.GetExecChoixActuel()

        assert (not execNoeudActuel.m_NoeudAExecuter.m_Execute), "execNoeudActuel actuel déjà exécuté : \n{}".format(execNoeudActuel)
        assert (execNoeudActuel is not None), "execNoeudActuel actuel introuvable"

        if not execNoeudActuel.m_NoeudAExecuter.m_Execute:
            execNoeudActuel.LancerNoeud()
            execNoeudActuel.m_NoeudAExecuter.m_Execute = True
            quelqueChoseAffiche = True # bof en fait faire une fonction qui vérifie qu'il y a bien quelque chsoe à afficher

        # on considère que l'exécution d'un noeud qui contient du texte sera toujours bloquée par une validation (entrée?)
        if not quelqueChoseAffiche:
            valider = input("Rien à afficher. Validez pour continuer")

        transitionOk = False
        if execNoeudActuel.AMarqueUnePause():
            transitionOk = execNoeudActuel.AppliquerGoTo()
        '''
        # transition vers noeud courant suivant automatiquement (sans go to):
        if not transitionOk:
            if isinstance(execNoeudActuel, ExecEvt):
        '''

        self.LancerEvtEtOuEffetCourant()

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

    def GetExecChoixActuel(self):
        return self.m_ExecChoixActuel

    def GetEvtActuel(self):
        return self.GetExecEvtActuel().m_Evt
