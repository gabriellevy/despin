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
        situation.m_PhaseHistoire = PhaseHistoire.EXECUTION
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
        if execNoeudActuel.m_NoeudAExecuter.m_Parcouru:
            execNoeudActuel = self.GetExecEffetActuel()
        if execNoeudActuel.m_NoeudAExecuter.m_Parcouru:
            execNoeudActuel = self.GetExecChoixActuel()

        assert (not execNoeudActuel.m_NoeudAExecuter.m_Parcouru), "execNoeudActuel actuel déjà exécuté : \n{}".format(execNoeudActuel)
        assert (execNoeudActuel is not None), "execNoeudActuel actuel introuvable"

        situation = Situation()
        if not execNoeudActuel.m_NoeudAExecuter.m_Parcouru:
            # même si on est passé on affiche des choses seulement si la condition est validée :
            if execNoeudActuel.TesterCondition():
                execNoeudActuel.LancerNoeud()
                quelqueChoseAffiche = execNoeudActuel.QuelquechoseAAfficher()
                execNoeudActuel.EnregistrerVisite()
                print(self.m_ExecPerso) # affichage des caracs actuelles du personnage (mises à jour)

            # on enregistre qu'on est passé par ce noeud :
            execNoeudActuel.m_NoeudAExecuter.m_Parcouru = True

        transitionOk = False

        if ( situation.m_PhaseHistoire != PhaseHistoire.EXECUTION):
            # cette partie n'est plus en cours d'exécution
            if ( situation.m_PhaseHistoire == PhaseHistoire.DEFAITE):
                self.Defaite(situation)
            elif ( situation.m_PhaseHistoire == PhaseHistoire.VICTOIRE):
                self.Victoire(situation)
            elif ( situation.m_PhaseHistoire == PhaseHistoire.FIN):
                exit()
            return

        # on considère que l'exécution d'un noeud qui contient du texte sera toujours bloquée par une validation (entrée?)
        # pas besoin si il a déjà marqué une pause pour un choix par exemple
        if not execNoeudActuel.AMarqueUnePause():
            if quelqueChoseAffiche:
                valider = input("Validez pour continuer")

        transitionOk = execNoeudActuel.AppliquerGoTo()

        # transition vers noeud courant suivant automatiquement (sans go to):
        if not transitionOk:
            if isinstance(execNoeudActuel, ExecEffet):
                # récupérer l'effet suivant c'est à dire l'effet suivant de l'évt de l'effet actuel :
                effetSuivant = self.GetEvtActuel().EffetSuivant(execNoeudActuel.m_Effet.m_Id)
                assert effetSuivant != None, "TODO : passer à événement suivant ?"
                self.GoToEffetId(effetSuivant.m_Id)


        self.LancerEvtEtOuEffetCourant()

    def Defaite(self, situation):
        print(self.m_Histoire.m_MessageDefaite)
        situation.m_PhaseHistoire = PhaseHistoire.FIN

    def Victoire(self, situation):
        print(self.m_Histoire.m_MessageVictoire)
        situation.m_PhaseHistoire = PhaseHistoire.FIN

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