class Animal:
    """
    Classe parent Animal
    """
    def __init__(self, p_numero = 0, p_poid = 0, p_taille = 0.0, p_longevite = 0, p_diet = "", p_enclos = ""):
        """
        Constructeur de la classe parent Animal
        :param p_numero
        :param p_poid:
        :param p_taille:
        :param p_longevite:
        :param p_diet
        """
        self.__Numero = p_numero
        self.__Poid = p_poid
        self.__Taille = p_taille
        self.__Longevite = p_longevite
        self.Diet = p_diet
        self.Enclos = p_enclos



    def _get_numero(self):
        return self.__Numero

    def _set_numero(self, v):
        if v.isnumeric() and len(v) == 6:
            self.__Numero = v

    Numero = property(_get_numero, _set_numero)


    def _get_poid(self):
        return self.__Poid

    def _set_poid(self, v):
        if v.isnumeric():
            if (int(v) <= 6000120) and (int(v) >= 2):
                self.__Poid = int(v)

    Poid = property(_get_poid, _set_poid)


    def _get_taille(self):
        return self.__Taille

    def _set_taille(self, v):
        if v.isnumeric():
            if (int(v) <= 550) and (int(v) >= 3):
                self.__Taille = int(v)

    Taille = property(_get_taille, _set_taille)


    def _get_longevite(self):
        return self.__Longevite

    def _set_longevite(self, v):
        if v.isnumeric():
            if (int(v) <= 255) and (int(v) >= 1):
                self.__Longevite = int(v)

    Longevite = property(_get_longevite, _set_longevite)
