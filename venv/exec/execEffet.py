from exec.execChoix import *
from abs.lancerDe import *

class ExecEffet(ExecNoeud):

    def __init__(self, effet, execHistoire):
        ExecNoeud.__init__(self, effet, execHistoire)
        self.m_Effet = effet

    def LancerNoeud(self):
        ExecNoeud.LancerNoeud(self)

        #affichage du texte
        print(self.m_Effet)

        if ( self.m_Effet.m_LancerDe != None):
            nbDes = self.m_Effet.m_LancerDe.m_NbDes
            arreterLancerDe = False
            while not arreterLancerDe:
                envoi = input(self.m_Effet.m_LancerDe.m_MessageLancerDe)
                arreterLancerDe = self.m_Effet.m_LancerDe.LancerDe(effetActuel= self.m_Effet, input=envoi)
                if not arreterLancerDe:
                    print("")

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
            indexChoisi = indexChoisi-1  # -1 car le premier choix affiché est '1'
            execChoix = ExecChoix(self.m_Effet.m_Choix[indexChoisi], self.m_ExecHistoire)
            self.m_ExecHistoire.m_ExecChoixActuel = execChoix

    def QuelquechoseAAfficher(self):
        return self.m_Effet.m_Texte != None and self.m_Effet.m_Texte != ""

    def AMarqueUnePause(self):
        """

        :return: true si ce noeud à exécuter à forcément marqué une pause par exemple si il contiet un choix
        """
        return ExecNoeud.AMarqueUnePause(self) or len(self.m_Effet.m_Choix) > 0

    def __repr__(self):
        """Représentation d'un exec effet"""
        chaine = "ExecEffet : "
        chaine += self.m_Effet.m_Id
        chaine += "\n"
        if (self.m_NoeudAExecuter.m_Execute):
            chaine += "Déjà exécuté"
        else:
            chaine += "Pas encore exécuté"
        return chaine