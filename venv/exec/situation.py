import pickle
import os
from abs.carac import Carac
from util.singleton import *
from enum import Enum

class PhaseHistoire(Enum):
    LANCE = -1 # le jeu a été lancé mais aucune partie n'est entamée
    GENERATION = 0
    EXECUTION = 1
    DEFAITE = 2 # la partie est perdue mais il peut encore y avoir des choses à afficher/exécuter
    VICTOIRE = 3 # la partie est gagnée mais il peut encore y avoir des choses à afficher/exécuter
    FIN = 4 # il n'y a plus rien à faire ou afficher, le jeu va être fermé

# passer cette classe en singleton serait peut-être une bonne idée...
class Situation(metaclass=Singleton):
    """
    Situation de jeu
    Etat d'une partie à un instant t avec toutes les informations nécessaires pour la sauvegarder et la recharger
    en particulier la liste intégrale des caractéristiques du perso (qui sont une sous catégorie de la situation de jeu)
    l'événement et l'effet courants font partie des caracs avec comme id "effetCourant" et "evtCOurant"
    """

    # Nom du fichier stockant la situation
    NOM_FICHIER = "D:/boulot/python/despin/Situation.despin"
    EVT_COURANT = "evtCourant"
    EFFET_COURANT = "effetCourant"

    def __init__(self):
        self.m_Caracs = dict() # self.m_Caracs[str idCarac] = Carac
        self.SetEvtCourant(None)
        self.SetEffetCourant(None)
        self.m_PhaseHistoire = PhaseHistoire.LANCE

    def SetEvtCourant(self, evt):
        self.m_Caracs[Situation.EVT_COURANT] = evt

    def SetEffetCourant(self, effet):
        self.m_Caracs[Situation.EFFET_COURANT] = effet

    def GetEvtCourant(self):
        return self.m_Caracs[Situation.EVT_COURANT]

    def GetEffetCourant(self):
        return self.m_Caracs[Situation.EFFET_COURANT]

    def Charger(self):
        """Charge une situation depuis un fichier vers cette classe.
        Dans tous les cas, on renvoie un dictionnaire,
        soit l'objet dépicklé,
        soit un dictionnaire vide.

        Pour l'instant utilise nom_fichier"""

        if os.path.exists(Situation.NOM_FICHIER):  # Le fichier existe
            # On le récupère
            fichier = open(Situation.NOM_FICHIER, "rb")
            mon_depickler = pickle.Unpickler(fichier)
            self.m_Caracs = mon_depickler.load()
            fichier.close()
        else:  # Le fichier n'existe pas
            self.m_Caracs = {}
        return self.m_Caracs

    def Sauver(self):
        """Cette fonction se charge d'enregistrer les caracs dans le fichier
        nom_fichier"""

        fichier = open(Situation.NOM_FICHIER, "wb")  # On écrase les anciens scores
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(self.m_Caracs)
        fichier.close()


    def __getattr__(self, nom):
        """Si Python ne trouve pas l'attribut nommé nom, il appelle
             cette méthode. On affiche une alerte"""
        print("Alerte ! Il n'y a pas d'attribut '{}' dans l'objet '{}' !".format(nom, self))

    def __getstate__(self):
        """
        Renvoie le dictionnaire d'attributs à sérialiser
        Sera utile quand l'objet situation ne devra aps être intégralement sauvegardé
        """
        dict_attr = dict(self.__dict__)
        # dict_attr["attribut_temporaire"] = 0
        return dict_attr

    def __setstate__(self, dict_attr):
        """
        Méthode appelée lors de la désérialisation de l'objet
        Sera utile quand l'objet situation ne devra aps être intégralement sauvegardé
        """
        # dict_attr["attribut_temporaire"] = 0
        self.__dict__ = dict_attr

    def AjouterCarac(self, carac):
        self.m_Caracs[carac.m_Id] = carac
        return carac

    def CreerCarac(self, idCarac, valCarac, valeurMin = "", valeurMax = ""):
        carac = Carac(idCarac, valCarac, valeurMin, valeurMax)
        return self.AjouterCarac(carac)

    def SetCarac(self, idCarac, valCarac, valeurMin = "", valeurMax = ""):
        # si la carac n'existe pas encore, la créer
        if not idCarac in self.m_Caracs:
            self.CreerCarac(idCarac, valCarac, valeurMin, valeurMax)

        carac = self.m_Caracs[idCarac]
        assert isinstance(carac, Carac)

        carac.m_Valeur = valCarac

    def AjouterACarac(self, idCarac, valCarac):
        finalVal = self.m_Caracs[idCarac].m_Valeur + valCarac
        self.SetCarac(idCarac, finalVal)

    def RetirerACarac(self, idCarac, valCarac):
        finalVal = self.m_Caracs[idCarac].m_Valeur - valCarac
        self.SetCarac(idCarac, finalVal)

'''
print("------tests Situation")
situation = Situation()
situation.Charger()
#caracNom = Carac("nom", "Mathieu Deharbe")
#situation.m_Caracs["nom"] = caracNom
#caracAge = Carac("age", 20)
situation.m_Caracs["ageMarjo"] = Carac("age", 33)
print("avant : {}".format(situation.m_Caracs))
situation.m_Caracs["age"] += 1
print("apres : {}".format(situation.m_Caracs))
print(situation.m_Caracs["ageMarjo"] == situation.m_Caracs["age"])
print(situation.m_Caracs["age"] == 31)
situation.Sauver()
'''