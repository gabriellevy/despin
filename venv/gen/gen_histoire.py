from abs.histoire import Hist
from abs.evt import *
from abs.effet import *
from abs.choix import *
from abs.perso import *
from abs.setCarac import *
from abs.condition import *

class GenHist:
    """
    Class servant à générer toute l'histoire d'un jeu destin.
    Une fois cette exécution terminée elle renvoie un objet ExecHistoire à exécuter et n'est plus utilisée.
    Elle peut alors être supprimée

    à surclasser quand on crée une histoire ?
    """

    def __init__(self, titre):
        self._m_Histoire = Hist(titre) # histoire générée
        self._m_DernierEvtGenere = None
        self._m_DernierEffetGenere = None

    def GenererHistoire(self):
        """
        génère toute l'histoire  (donc tous les événements et effets)
        IMPERATIVEMENT surclasser cette fonction dans les créations d'histoires
        """
        situation = Situation()
        situation.m_PhaseHistoire = PhaseHistoire.GENERATION
        return self._m_Histoire

    def GenererCaracs(self):
        """
        génère toutes les caracs qui peuvent être visualisées par le joueur
        (d'autres caracs peuvent être générées et invisibles n'importe quand dans l'aventure)
        surclasser cette fonction dans les créations d'histoires
        """
        perso = Perso()
        self._m_Histoire.m_Perso = perso
        return perso

    def GenererPersos(self):
        """
        génère tous les persos qui peuvent être joués par le joueur
        surclasser cette fonction dans les créations d'histoires
        """
        pass

    def AjouterEvt(self, id = ""):
        if ( id == ""):
            id = "evt_id_{0}".format(Evt.compteurId)
            Evt.compteurId += 1
        #tester qu'un événement ayant cet id n'existe pas déjà
        for evt in self._m_Histoire.ParcourirEvts():
            if evt.m_Id == id:
                raise ValueError("Id déjà existant dans l'histoire pour cet evt : {}".format(id))
        evtFinal = Evt(id)
        self._m_DernierEvtGenere = evtFinal
        self._m_Histoire[id] = evtFinal
        return evtFinal

    def AjouterEffetGoToEffet(self, texte = "", id = "", evt = "", goToEffetId = "", titre=""):
        effet = self.AjouterEffet( texte, id, evt, titre)
        effet.m_GoToEffetId = goToEffetId

    def AjouterEffetDefaite(self, texte = "", id = "", evt = "", titre=""):
        effet = self.AjouterEffet( texte, id, evt, titre)
        effet.m_ChangementPhaseHistoire = PhaseHistoire.DEFAITE

    def AjouterEffetFin(self, texte = "", id = "", evt = "", titre=""):
        effet = self.AjouterEffet( texte, id, evt, titre)
        effet.m_ChangementPhaseHistoire = PhaseHistoire.FIN

    def AjouterEffetGoToSiDejaVisite(self, goToEffetId, id):
        effet = self.AjouterEffet( goToEffetId = goToEffetId, id = id)
        idCarac = "{}{}".format(Situation.PREFIXE_EFFET_VISITE, id)
        effet.AjouterCondition(idCarac, "1", Comparateur.EGAL)

    def AjouterEffet(self, texte = "", id = "", evt = "", goToEffetId="", titre=""):
        if evt == "":
            evt = self._m_DernierEvtGenere

        if (  isinstance(evt, Evt)) != True:
            raise TypeError( \
                "Impossible d'ajouter un effet à un objet qui n'est pas un événement mais un : '{0}'".format( \
                    type(evt)))

        if ( id == ""):
            id = "effet_id_{0}".format(Effet.compteurId)
            Effet.compteurId += 1

        #tester qu'un effet ayant cet id n'existe pas déjà
        for effet in evt.ParcourirEffets():
            if effet.m_Id == id:
                raise ValueError("Id déjà existant dans l'événement pour cet effet : {}".format(id))
        effetFinal = Effet(evt, texte, id, titre)
        if goToEffetId != "":
            effetFinal.m_GoToEffetId = goToEffetId
        self._m_DernierEffetGenere = effetFinal

        evt[id] = effetFinal
        return effetFinal

    def AjouterChoix(self, texte = "", id = "", effet = ""):
        if effet == "":
            effet = self._m_DernierEffetGenere

        if ( isinstance(effet, Effet)) != True:
            raise TypeError( \
                "Impossible d'ajouter un choix à un objet qui n'est pas un effet mais un : '{0}'".format( \
                    type(effet)))

        if ( id == ""):
            id = "choix_id_{0}".format(Choix.compteurId)
            Choix.compteurId += 1

        #tester qu'un choix ayant cet id n'existe pas déjà
        for choix in effet.ParcourirChoix():
            if choix.m_Id == id:
                raise ValueError("Id déjà existant dans l'effet pour ce choix : {}".format(id))
        choixFinal = Choix(effet, texte, id)

        effet[id] = choixFinal
        return choixFinal

    def AjouterModificateurCarac(self, setCarac, effet = ""):
        if effet == "":
            effet = self._m_DernierEffetGenere

        if ( isinstance(effet, Effet)) != True:
            raise TypeError( \
                "Impossible d'ajouter un set carac à un objet qui n'est pas un effet mais un : '{0}'".format( \
                    type(effet)))

        effet.m_SetsCaracs.append(setCarac)
        return setCarac

    def AjouterRetireurCarac(self, caracId, valeur, effet = ""):
        setCarac = SetCarac(caracId, ModifCaracType.RETIRE, valeur)
        return self.AjouterModificateurCarac(setCarac, effet)

    def AjouterAjouteurCarac(self, caracId, valeur, effet = ""):
        setCarac = SetCarac(caracId, ModifCaracType.AJOUTE, valeur)
        return self.AjouterModificateurCarac(setCarac, effet)

    def AjouterSetteurCarac(self, caracId, valeur, effet = ""):
        setCarac = SetCarac(caracId, ModifCaracType.SET, valeur)
        return self.AjouterModificateurCarac(setCarac, effet)

    def AjouterSetteurCaracTrue(self, caracId, effet = ""):
        return self.AjouterSetteurCarac(caracId, "1", effet)

    def AjouterSetteurCaracFalse(self, caracId, effet = ""):
        return self.AjouterSetteurCarac(caracId, "", effet)

    def AjouterChoixGoToEffet(self, texte = "", id = "", evt = "", goToEffetId = ""):
        choixFinal = self.AjouterChoix( texte, id, evt)
        choixFinal.m_GoToEffetId = goToEffetId

# stupides tests
'''
print("------tests GenHist")
truc = GenHist("Rick et morty ! ")
evt1 = truc.AjouterEvt("id1");
evt2 = truc.AjouterEvt("id2");
effet1 = truc.AjouterEffet("Il se passe des choses dans cet effet d'histoire ! ", evt = evt2)
effet2 = truc.AjouterEffet("Mais vraiment plein de trucs ", evt = evt2)
print(truc._m_Histoire)
print(truc._m_Histoire.__contains__(evt1))
'''