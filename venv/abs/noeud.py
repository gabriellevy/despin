from condition import Condition

class Noeud:
    """
    Structure de base du système destin.
    Contient essentiellement des valeurs d'affichage et est héritée par toute les briques principales de structure d'affichage/histoire
    """

    def __init__(self, id):
        """Constructeur"""
        self._m_Id = id
        # TODO MATHIEU : changeur de perso
        # TODO MATHIEU : modificateur de caracs (SetCarac)
        self.m_Conditions = list()

    def _get_m_Id(self):
        return self._m_Id

    # L'identifiant ne peut jamais être modifié après création
    m_Id = property(_get_m_Id)
