from abs.histoire import Hist
from abs.evt import Evt
from abs.effet import Effet

class GenHist:
    """
    Class servant à générer toute l'histoire d'un jeu destin.
    Une fois cette exécution terminée elle renvoie un objet ExecHistoire à exécuter et n'est plus utilisée.
    Elle peut alors être supprimée

    à surclasser quand on crée une histoire ?
    """

    def __init__(self, titre):
        self._m_Histoire = Hist(titre) # histoire générée

    def GenererCaracs(self):
        """
        génère toutes les caracs qui peuvent être visualisées par le joueur
        (d'autres caracs peuvent être générées et invisibles n'importe quand dans l'aventure)
        surclasser cette fonction dans les créations d'histoires
        """
        pass

    def GenererPersos(self):
        """
        génère tous les persos qui peuvent être joués par le joueur
        surclasser cette fonction dans les créations d'histoires
        """
        pass

    def GenererHistoire(self):
        """
        génère toute l'histoire (donc tous les événements et effets)
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
        self._m_Histoire.m_Evts.append(evtFinal)
        return evtFinal

    def AjouterEffet(self, texte = "", id = "", evt = ""):
        if (isinstance(evt, Evt)) != True:
            raise TypeError( \
                "Impossible d'ajouter un effet à un objet qui n'est pas un événement mais un : '{0}'".format( \
                    type(evt)))

        if ( id == ""):
            id = "effet_id_{0}".format(Effet.compteurId)
            Effet.compteurId += 1

        if evt == "":
            evt = self._m_DernierEvtGenere

        #tester qu'un effet ayant cet id n'existe pas déjà
        for effet in evt.ParcourirEffets():
            if effet.m_Id == id:
                raise ValueError("Id déjà existant dans l'événement pour cet effet : {}".format(id))
        effetFinal = Effet(texte, id)

        evt.m_Effets.append(effetFinal)
        return effetFinal

# stupides tests
print("------tests GenHist")
truc = GenHist("Rick et morty ! ")
evt1 = truc.AjouterEvt("id1");
evt2 = truc.AjouterEvt("id2");
effet1 = truc.AjouterEffet("Il se passe des choses dans cet effet d'histoire ! ", "effet1", evt2)
effet2 = truc.AjouterEffet("Mais vraiment plein de trucs ", "effet2", evt2)
print(truc._m_Histoire[0])
print(truc._m_Histoire[1])
print(truc._m_Histoire[1].m_Effets[0])
print(truc._m_Histoire[1].m_Effets[1])
print(truc._m_Histoire.__contains__(evt1))