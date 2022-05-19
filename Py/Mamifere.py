from Animal import *

class Mamifere(Animal):
    """
    Classe dérivée Mamifere de la classe parent Animal
    """
    def __init__(self, p_numero = 0, p_poid = 0, p_taille = 0.0, p_longevite = 0, p_diet = "",p_couleur_fourrure = "", p_type_patte = "", nb_doigts = 0, p_enclos = ""):
        """
        Contructeur de la classe Mamifere
        :param p_couleur_fourrure:
        :param p_type_patte:
        :param nb_doigts:
        """
        Animal.__init__(self, p_numero, p_poid, p_taille, p_longevite, p_diet, p_enclos)    # Appel du constructeur de la classe Animal
        self.Couleur_fourrure = p_couleur_fourrure      # Attribut de la classe Mamifere
        self.Type_patte = p_type_patte
        self.__Nb_Doigts = nb_doigts

    def __str__(self):
        """
        Fonction magique __str__
        :return: La chaine qui permet de d'afficher les attributs de l'objet de la classe Mamifere instancié
        """
        return " " * 60 + "\n" + "*" * 60 + "\n\n" +\
               "Numéro du mamifère : " + str(self.Numero) + "\n" +\
               "Poids du mamifère : " + str(self.Poid) + "\n" +\
               "Taille du mamifère : " + str(self.Taille) + "\n" +\
               "Espérence de vie du mamifère : " + str(self.Longevite) + "\n" +\
               "Diet du mamifère : " + self.Diet + "\n" +\
               "Couleur de la fourrure du mamifère : " + self.Couleur_fourrure + "\n" +\
               "Type de patte du mamifère : " + self.Type_patte + "\n" +\
               "Nombre de doigts du mamifère : " + str(self.Nbdoigts) + "\n\n"+"*"*60

    def _get_nb_doigts(self):
        return self.__Nb_Doigts

    def _set_nb_doigts(self, v):
        if v.isnumeric():
            if (int(v) <= 28) and (int(v) >= 0):
                self.__Nb_Doigts = int(v)

    Nbdoigts = property(_get_nb_doigts, _set_nb_doigts)
