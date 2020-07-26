from exec.execNoeud import *

class ExecEffet(ExecNoeud):

    def __init__(self, effet):
        self.m_Effet = effet
        pass

    def LancerNoeud(self):
        print(self.m_Effet);
