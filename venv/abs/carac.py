

class Carac:
    """
    caractéristique de base avec un identifiant et une valeur qui peut être un nombre ou une string
    pour les caracs plus spécifiques, les faire hériter de cette classe
    """

    def __init__(self, id, valeur):
        self.m_Id = id
        self.m_Valeur = valeur

    def __add__(self, other):
        """Ajoute des nombre uniquement"""
        self.m_Valeur += other
        return self

    def __radd__(self, objet_a_ajouter):
        """Au cas où la carac et l'objet à ajouter son inversés"""
        return self + objet_a_ajouter

    def __mul__(self, other):
        """Multiplie des nombre uniquement"""
        self.m_Valeur *= other
        return self

    def __truediv__(self, other):
        """Divise des nombre uniquement"""
        self.m_Valeur /= other
        return self

    def __floordiv__(self, other):
        """Divise des nombre uniquement"""
        self.m_Valeur //= other
        return self

    def __mod__(self, other):
        """Modulo des nombre uniquement"""
        self.m_Valeur = self.m_Valeur % other
        return self

    def __pow__(self, autre):
        """Puissance des nombre uniquement"""
        self.m_Valeur = self.m_Valeur ** autre
        return self

    def __ne__(self, autre):
        if isinstance(autre, Carac):
            return self.m_Valeur != autre.m_Valeur
        return self.m_Valeur != autre

    def __gt__(self, autre):
        if isinstance(autre, Carac):
            return self.m_Valeur > autre.m_Valeur
        return self.m_Valeur > autre

    def __ge__(self, autre):
        if isinstance(autre, Carac):
            return self.m_Valeur >= autre.m_Valeur
        return self.m_Valeur >= autre

    def __lt__(self, autre):
        if isinstance(autre, Carac):
            return self.m_Valeur < autre.m_Valeur
        return self.m_Valeur < autre

    def __le__(self, autre):
        if isinstance(autre, Carac):
            return self.m_Valeur <= autre.m_Valeur
        return self.m_Valeur <= autre

    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return "Carac '{}', Valeur '{}'".format(self.m_Id, self.m_Valeur)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        return "{} : {}".format(self.m_Id, self.m_Valeur)