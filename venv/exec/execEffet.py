from exec.execNoeud import *
from abs.choix import *

class ExecEffet(ExecNoeud):

    def __init__(self, effet):
        self.m_Effet = effet
        pass

    def LancerNoeud(self):
        print(self.m_Effet)
        index = 1
        for choix in self.m_Effet.ParcourirChoix():
            print("{} - {}".format(index, choix))
            index+=1
