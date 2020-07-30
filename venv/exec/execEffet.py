from exec.execHistoire import *
from exec.execChoix import *

class ExecEffet(ExecNoeud):

    def __init__(self, effet):
        ExecNoeud.__init__(self, effet)
        self.m_Effet = effet

    def LancerNoeud(self):
        ExecNoeud.LancerNoeud(self)

        #affichage du texte
        print(self.m_Effet)

        if (len(self.m_Effet.m_Choix) > 1):  # il y a un choix qui se pose :
            index = 1
            for choix in self.m_Effet.ParcourirChoix():
                print("{} - {}".format(index, choix))
                index+=1
            indexChoisi = index
            choisi = False
            while(not choisi):
                indexChoisi = input("Que souhaitez vous faire ?")
                try:
                    indexChoisi = int(indexChoisi)
                except ValueError:
                    indexChoisi = -1
                choisi = indexChoisi > 0 and indexChoisi < index
                if not choisi:
                    print("Choisissez un numéro parmi les choix proposés.")

            execChoix = ExecChoix(self.m_Effet.m_Choix[indexChoisi-1])
            ExecHistoire.EXEC_HISTOIRE.m_ExecChoixActuel = execChoix

    def AMarqueUnePause(self):
        """

        :return: true si ce noeud à exécuter à forcément marqué une pause par exemple si il contiet un choix
        """
        return ExecNoeud.AMarqueUnePause(self) and len(self.m_Choix) > 0
