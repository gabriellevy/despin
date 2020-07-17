from evt import Evt

class Hist:
    """
    Cette classe est une pure structure de données. Elle fait le lien entre GenHistoire qui la créée et ExecHistoire qui l'exécute
    elle est donc tout aussi indépendante de la manière dont elle est générée ou exécutée
    """

    def __init__(self):
        self.m_Evts = list();