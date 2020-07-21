from abs.evt import Evt
from abs.effet import Effet

class Hist:
    """
    Cette classe est une pure structure de données. Elle fait le lien entre GenHistoire qui la créée et ExecHistoire qui l'exécute
    elle est donc tout aussi indépendante de la manière dont elle est générée ou exécutée
    """

    def __init__(self, titre):
        self.m_Titre = titre
        self.m_Evts = list();

    def __getattr__(self, nom):
        """Si Python ne trouve pas l'attribut nommé nom, il appelle
             cette méthode. On affiche une alerte"""
        print("Alerte ! Il n'y a pas d'attribut '{}' dans l'objet '{}' !".format(nom, self))

    def __getitem__(self, index):
        """Comme histoire est essentiellement un conteneur d'événements ses fonctions d'accès sont surchargés par commodité"""
        return self.m_Evts[index]
    def __setitem__(self, index, evt):
        """Comme histoire est essentiellement un conteneur d'événements ses fonctions d'accès sont surchargés par commodité"""
        self.m_Evts[index] = evt
    def __contains__(self, item):
        """Comme histoire est essentiellement un conteneur d'événements ses fonctions d'accès sont surchargés par commodité"""
        return self.m_Evts.__contains__(item)
    def __len__(self):
        """Comme histoire est essentiellement un conteneur d'événements ses fonctions d'accès sont surchargés par commodité"""
        return self.m_Evts.__len__()

    def ParcourirEvts(self):
        """pseudo itérateur des événements de l'histoire"""
        for evt in self.m_Evts:
            yield evt


# stupides tests
print("------tests HISTOIRE")