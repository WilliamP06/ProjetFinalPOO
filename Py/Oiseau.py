from Animal import *

class Oiseau(Animal):
    """
    Classe dérivée Mamifere de la classe parent Oiseau
    """
    def __init__(self, p_numero, p_poid = 0.0, p_taille = 0.0, p_longevite = 0, p_diet = "", p_couleur_plumes = "", p_couleur_bec = "",p_longueur_bec = 0.0, p_enclos = ""):
        """
        Contructeur de la classe Oiseau
        :param p_poid:
        :param p_taille:
        :param p_longevite:
        :param p_diet:
        """
        Animal.__init__(self, p_numero,p_poid, p_taille, p_longevite, p_diet, p_enclos)    # Appel du constructeur de la classe Animal
        self.Couleur_plumes = p_couleur_plumes      # Attribut de la classe Oiseau
        self.Couleur_bec = p_couleur_bec
        self.__Longueur_bec = p_longueur_bec

    def __str__(self):
        """
        Fonction magique __str__
        :return: La chaine qui permet de d'afficher les attributs de l'objet de la classe Oiseau instancié
        """
        return " " * 60 + "\n" + "*" * 60 + "\n\n" +\
                "Le numéro du oiseau est : " + str(self.Numero) +\
                "Poids du oiseau : " + str(self.Poid) + "\n" + \
                "Taille du oiseau : " + str(self.Taille) + "\n" + \
                "Espérence de vie du oiseau : " + str(self.Longevite) + "\n" + \
                "Diet du oiseau : " + self.Diet + "\n" + \
                "Couleur des plumes du oiseau : " + self.Couleur_plumes + "\n" + \
                "Couleur du bec du oiseau : " + self.Couleur_bec + "\n" + \
                "Longueur du bec du oiseau : " + str(self.Longueurbec) + "\n\n"+"*"*60

    def _get_longueur_bec(self):
        return self.__Longueur_bec

    def _set_longueur_bec(self, v):
        if self.__Longueur_bec <= 0.15 or self.__Longueur_bec >= 47 and v.isnumeric():
            self.__Longueur_bec = v

    Longueurbec = property(_get_longueur_bec, _set_longueur_bec)
