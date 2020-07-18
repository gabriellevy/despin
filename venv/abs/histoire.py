from evt import Evt
from effet import Effet

class Hist:
    """
    Cette classe est une pure structure de données. Elle fait le lien entre GenHistoire qui la créée et ExecHistoire qui l'exécute
    elle est donc tout aussi indépendante de la manière dont elle est générée ou exécutée
    """

    def __init__(self):
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

# stupides tests
print("------tests HISTOIRE")
truc = Hist()
evt1 = Evt();
evt2 = Evt();
truc.m_Evts.append( evt1 )
truc.m_Evts.append( evt2 )
effet1 = Effet("Il se passe des choses dans cet effet d'histoire ! ")
evt1.m_Effets.append(effet1)
print(truc[0].m_Effets[0])
print(truc.__contains__(evt1))