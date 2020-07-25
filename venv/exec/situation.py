import pickle
import os
from abs.carac import Carac


class Situation:
    """
    Situation de jeu
    Etat d'une partie à un instant t avec toutes les informations nécessaires pour la sauvegarder et la recharger
    en particulier la liste intégrale des caractéristiques du perso (qui sont une sous catégorie de la situation de jeu)
    """

    # Nom du fichier stockant la situation
    NOM_FICHIER = "D:/boulot/python/despin/Situation.despin"

    def __init__(self):
        # m_Caracs devra être un dico avec comme identifiant une string carac_id et comme donnée une Carac
        self.m_Caracs = dict()
        # données décrivant la situation actulle du joueur dans le jeu
        self.m_EvtCourant = ""
        self.m_EffetCourant = ""

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