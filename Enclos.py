from Animal import *
from Mamifere import *
from Oiseau import *
from Poisson import *

class Enclos:

    def __init__(self, p_contient_mamifere = "", p_contient_poisson = "", p_contient_oiseau = ""):
        self.contient_mamifere = p_contient_mamifere
        self.contient_poisson = p_contient_poisson
        self.contient_oiseau = p_contient_oiseau

    def __str__(self):
        """
        Fonction magique __str__
        :return: Chaine à afficher
        """
        return " " * 60 + "\n" + "*" * 60 + "\n\n" + "Le mamifère a été placé dans : " + self.contient_mamifere + "\n" +\
               "Le poisson a été placé dans : " + self.contient_poisson + "\n" +\
               "Le oiseau a été placé dans : " + self.contient_oiseau + "\n\n"+"*"*60