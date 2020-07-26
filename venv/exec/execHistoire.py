from abs.effet import *
from abs.evt import *
from abs.histoire import *

class ExecHistoire:

    def __init__(self):
        self._m_DernierEffetAffiche = Effet("effet_null")
        self._m_DernierEvtAffiche = Evt("evt_null")

    def LancerHistoire(self, histoire):
        self.m_Histoire = histoire
        # gérer persos et caracs ? Affichage graphique ?