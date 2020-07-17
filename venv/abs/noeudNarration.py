from noeud import Noeud

class NoeudNarration(Noeud):
    """
    Noeud contenant des membres de déroulement d'histoires en plus de la logique de noeud comme :
     - du texte
     - des images
     ...
     """

    def __init__(self, id, texte):
        """Constructeur de neoud narratif : à priori ne devrait pas être appelé directement, c'est une classe plus ou moins abstraite"""
        Noeud.__init__(self, id)
        self.m_Texte = texte

    def AQuelqueChoseAAfficher(self):
        return self.m_Texte != ""

