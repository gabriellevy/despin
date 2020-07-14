class Condition:
    """
    Système de condition par comparaison d'une carac avec une valeur
    """

    def __init__(self, caracId, valeur):
        self.m_CaracId = caracId
        self.m_Valeur = valeur
        # TODO MATHIEU : Comparateur m_Comparateur = c_Aucun;

    def Tester(self):
        """
        renvoit true si la condition est vérifiée
        """
        return True

condition = Condition("maCarac", 5)
print(condition.m_Valeur)
print(condition.Tester())