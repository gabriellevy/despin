from evt import Evt

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