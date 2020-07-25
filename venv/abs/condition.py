
class Condition:
    """
    Système de condition par comparaison d'une carac avec une valeur
    """

    def __init__(self, caracId, valeur):
        self._m_CaracId = caracId
        self._m_Valeur = valeur
        # TODO MATHIEU : Comparateur m_Comparateur = c_Aucun;

    def Tester(self):
        """
        renvoit true si la condition est vérifiée
        """
        return True

    def _get_m_CaracId(self):
        return  self._m_CaracId
    def _get_m_Valeur(self):
        return  self._m_Valeur

    # Les conditions sont (intégralement?) non mutables
    m_CaracId = property(_get_m_CaracId)
    m_Valeur = property(_get_m_Valeur)


# stupides tests
'''
print("------tests Condition")
condition = Condition("maCarac", 5)
print(condition.m_Valeur)
print(condition.Tester())
'''