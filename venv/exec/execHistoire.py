# from abs.effet import *
# from abs.evt import *
# from abs.histoire import *
from exec.execEvt import *
# import exec.execEffet
from exec.situation import *
from util.singleton import *
from exec.execPerso import *

class ExecHistoire(metaclass=Singleton):

    def __init__(self):
        self.m_Situation = Situation()
        self.m_ExecEvtCourant = None
        self.m_ExecChoixActuel = None
        self.m_ExecPerso = None

    def LancerHistoire(self, histoire, premierEvtId = "", premierEffetId = ""):
        self.m_Histoire = histoire
        situation = Situation()
        # gérer persos et caracs ? Affichage graphique ?
        self.m_ExecPerso = ExecPerso(histoire.m_Perso)

        #chargement de fichier

        #chargement éventuel d'evt et effet courants => APRES le chargement de fichier
        if ( premierEvtId != ""):
            evt = self.m_Histoire[premierEvtId]
            situation.SetEvtCourant(evt)
            if (premierEffetId != ""):
                effet = evt[premierEffetId]
                situation.SetEffetCourant(effet)

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
            quelqueChoseAffiche = execNoeudActuel.QuelquechoseAAfficher()
            print(self.m_ExecPerso) # affichage des caracs actuelles du personnage (mise à jour)

        transitionOk = False

        # on considère que l'exécution d'un noeud qui contient du texte sera toujours bloquée par une validation (entrée?)
        # pas besoin si il a déjà marqué une pause pour un choix par exemple
        if not execNoeudActuel.AMarqueUnePause():
            if quelqueChoseAffiche:
                valider = input("Validez pour continuer")

        transitionOk = execNoeudActuel.AppliquerGoTo()
        '''
        # transition vers noeud courant suivant automatiquement (sans go to):
        if not transitionOk:
            if isinstance(execNoeudActuel, ExecEvt):
        '''

        self.LancerEvtEtOuEffetCourant()

    def GetExecEvtActuel(self):
        situation = Situation()
        if self.m_ExecEvtCourant is None:
            # premier lancement
            if (situation.GetEvtCourant() is None):
                assert len(self.m_Histoire) > 0, "erreur dans GetExecEvtActuel : Il n'y a aucun événement dans l'histoire !"
                situation.SetEvtCourant(self.m_Histoire.m_Evts[0])
            evtCourant = situation.GetEvtCourant()
            self.m_ExecEvtCourant = ExecEvt(evtCourant, self)
        return self.m_ExecEvtCourant

    def GetExecEffetActuel(self):
        return self.GetExecEvtActuel().GetExecEffetActuel()

    def SetExecEffetActuel(self, execEffetActuel):
        self.GetExecEvtActuel().SetExecEffetActuel(execEffetActuel)

    def GetExecChoixActuel(self):
        return self.m_ExecChoixActuel

    def GetEvtActuel(self):
        return self.GetExecEvtActuel().m_Evt

    def GoToEffetId(self, effetId):
        situation = Situation()
        effetToGoTo = self.GetEvtActuel()[effetId]
        situation.SetEffetCourant(effetToGoTo)
        self.SetExecEffetActuel(ExecEffet(effetToGoTo, self))