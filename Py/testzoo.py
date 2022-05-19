from Mamifere import *
from Poisson import *
from Oiseau import *
from Enclos import *

mamifere1 = Mamifere(1.2, 32, 104, "s", "f", "sdfsd", 24)
print(mamifere1)

poisson1 = Poisson(1.2, 32, 104, "s", "f", "sdfsd", 24)
print(poisson1)

oiseau1 = Oiseau(1.2, 32, 104, "s", "f", "sdfsd", 24)
print(oiseau1)

enclos1 = Enclos("dfs", "fdfsd", "sijudfdd")
print(enclos1)

##################
def _get_taille(self):
    return self.__Taille


def _set_taille(self, v):
    if self.__Taille <= 5.5 and self.__Taille >= 0.007 and v.isnumeric():
        self.__Taille = v


Taille = property(_get_taille, _set_taille)


def _get_longevite(self):
    return self.__Longevite


def _set_longevite(self, v):
    if self.__Longevite <= 255 and self.__Longevite >= 1 and v.isnumeric():
        self.__Longevite = v


Longevite = property(_get_longevite, _set_longevite)
##################
def _get_nb_doigts(self):
    return self.__Nb_Doigts


def _set_nb_doigts(self, v):
    if self.__Nb_Doigts >= 0 and self.__Nb_Doigts <= 28 and v.isnumeric():
        self.__Nb_Doigts = v


Nbdoigts = property(_get_nb_doigts, _set_nb_doigts)
#########
def _get_longueur_bec(self):
    return self.__Longueur_bec


def _set_longueur_bec(self, v):
    if self.__Longueur_bec <= 0.15 or self.__Longueur_bec >= 47 and v.isnumeric():
        self.__Longueur_bec = v


Longueurbec = property(_get_longueur_bec, _set_longueur_bec)