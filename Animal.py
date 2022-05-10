class Animal:
    """
    Classe parent Animal
    """
    def __init__(self, p_poid = 0.0, p_taille = 0.0, p_longevite = 0, p_diet = ""):
        """
        Constructeur de la classe parent Animal
        :param p_poid:
        :param p_taille:
        :param p_protection:
        """
        self.__Poid = p_poid
        self.__Taille = p_taille
        self.__Longevite = p_longevite
        self.Diet = p_diet

    def _get_poid(self):
        return self.__Poid

    def _set_poid(self, v):
        if self.__Poid <= 13228 or self.__Poid >= 0.00220462 and v.isnumeric():
            self.__Poid = v

    Poid = property(_get_poid, _set_poid)


    def _get_taille(self):
        return self.__Taille

    def _set_taille(self, v):
        if self.__Taille <= 5.5 or self.__Taille >= 0.0077 and v.isnumeric():
            self.__Taille = v

    Taille = property(_get_taille, _set_taille)


    def _get_longevite(self):
        return self.__Longevite

    def _set_longevite(self, v):
        if self.__Longevite <= 255 or self.__Longevite >= 1 and v.isnumeric():
            self.__Longevite = v

    Longevite = property(_get_longevite, _set_longevite)
