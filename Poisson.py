from Animal import *

class Poisson(Animal):
    """
    Classe dérivée Mamifere de la classe parent Poisson
    """
    def __init__(self, p_poid = 0.0, p_taille = 0.0, p_longevite = 0, p_diet = "", p_type_eau = "", p_type_peau = "",p_type_queue = ""):
        """
        Contructeur de la classe Poisson
        :param p_poid:
        :param p_taille:
        :param p_longevite:
        :param p_diet:
        :param p_type_eau:
        :param p_type_peau:
        :param p_type_queue:
        """
        Animal.__init__(self, p_poid, p_taille, p_longevite, p_diet)    # Appel du constructeur de la classe Animal
        self.Type_eau = p_type_eau     # Attribut de la classe Poisson
        self.Type_peau = p_type_peau
        self.Type_queue = p_type_queue

    def __str__(self):
        """
        Fonction magique __str__
        :return: La chaine qui permet de d'afficher les attributs de l'objet de la classe Poisson instancié
        """
        return " " * 60 + "\n" + "*" * 60 + "\n\n" + "Poids du poisson : " + str(self.Poid) + "\n" + \
                "Taille du poisson : " + str(self.Taille) + "\n" + \
                "Espérence de vie du poisson : " + str(self.Longevite) + "\n" + \
                "Diet du poisson : " + self.Diet + "\n" + \
                "Type d'eau du poisson : " + self.Type_eau + "\n" + \
                "Type de peau du poisson : " + self.Type_peau + "\n" + \
                "Type de queue du poisson : " + str(self.Type_queue) + "\n\n"+"*"*60