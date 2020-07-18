import pickle
import os

class Situation:
    """
    Situation de jeu
    Etat d'une partie à un instant t avec toutes les informations nécessaires pour la sauvegarder et la recharger
    en particulier la liste intégrale des caractéristiques du perso (qui sont une sous catégorie de la situation de jeu)
    """

    # Nom du fichier stockant la situation
    nom_fichier = "D:/boulot/python/despin/Situation.despin"

    def __init__(self):
        self.m_Caracs = dict()

    def Charger(self):
        """Charge une situation depuis un fichier vers cette classe.
        Dans tous les cas, on renvoie un dictionnaire,
        soit l'objet dépicklé,
        soit un dictionnaire vide.

        Pour l'instant utilise nom_fichier"""

        if os.path.exists(Situation.nom_fichier):  # Le fichier existe
            # On le récupère
            fichier = open(Situation.nom_fichier, "rb")
            mon_depickler = pickle.Unpickler(fichier)
            self.m_Caracs = mon_depickler.load()
            fichier.close()
        else:  # Le fichier n'existe pas
            self.m_Caracs = {}
        return self.m_Caracs

    def Sauver(self):
        """Cette fonction se charge d'enregistrer les caracs dans le fichier
        nom_fichier"""

        fichier = open(Situation.nom_fichier, "wb")  # On écrase les anciens scores
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(self.m_Caracs)
        fichier.close()

    def __getattr__(self, nom):
        """Si Python ne trouve pas l'attribut nommé nom, il appelle
             cette méthode. On affiche une alerte"""
        print("Alerte ! Il n'y a pas d'attribut '{}' dans l'objet '{}' !".format(nom, self))

situation = Situation()
situation.Charger()
print(situation)
print(situation.m_Caracs)
situation.m_Caracs["nom"] = "Mathieu Deharbe"
print(situation.m_Caracs)
situation.Sauver()