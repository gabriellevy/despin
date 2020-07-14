class Noeud:
    """
    Structure de base du système destin.
    Contient essentiellement des valeurs d'affichage et est héritée par toute les briques principales de structure d'affichage/histoire
    """

    def __init__(self, id):
        """Constructeur"""
        self.m_Id = id
        # TODO MATHIEU : changeur de perso
        # TODO MATHIEU : modificateur de caracs (SetCarac)
        # TODO MATHIEU : conditions d'exécution (QList<std::shared_ptr<Condition>> m_Conditions;)


# stupid tests
bernard = Noeud("bernard")
print(bernard)
print(bernard.m_Id)