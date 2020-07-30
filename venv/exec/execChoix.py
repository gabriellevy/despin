from exec.execNoeud import *
from abs.choix import *

class ExecChoix(ExecNoeud):

    def __init__(self, choix):
        ExecNoeud.__init__(self, choix)
        self.m_Choix = choix