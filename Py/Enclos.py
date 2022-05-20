from Animal import *
from Mamifere import *
from Oiseau import *
from Poisson import *

class Enclos:

    def __init__(self, p_numero_enclos = "", p_type_enclos = "", p_type_animal = ""):
        self.__Numero_enclos = p_numero_enclos
        self.Type_enclos = p_type_enclos
        self.Type_animal = p_type_animal

    def __str__(self):
        """
        Fonction magique __str__
        :return: Chaine à afficher
        """
        return " " * 60 + "\n" + "*" * 60 + "\n\n" +\
               "Numéro de l'enclos : " + str(self.__Numero_enclos) + "\n" +\
               "Type d'enclos : " + self.Type_enclos + "\n" +\
               "Type d'animal : " + self.Type_animal + "\n\n"+"*"*60


    def _get_numero_enclos(self):
        return self.__Numero_enclos

    def _set_numero_enclos(self, v):
        if v.isnumeric() and len(v) == 6:
            self.__Numero_enclos = v

    Numero = property(_get_numero_enclos, _set_numero_enclos)