class SautVersNoeud:
    """
    Classe gérant le passage du noeud courant vers le noeud suivant et les différents modes liés :
    - go to un effet
    - go to un evt (premier effet ou effet précisé)
    - sélectionneur de noeud selon une liste de possibilités et de probas associés
    """

    def __init__(self):
        self.m_GoToEffetId = "go to effet id"
        self.m_GoToEvtId = "go to evt id"
        # TODO MATHIEU : sélectionneur de do to selon proba (SelectionneurDeNoeud)