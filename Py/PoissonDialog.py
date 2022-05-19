# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets

# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la boite de dialogue
import interface_poisson

# Importer la classe Poisson
from Poisson import *


####################################################################################
# Déclarer une liste Poisson
ls_Poisson = []

####################################################################################
def valider_poisson_liste(p_numero):
    """
    Vérifie si le poisson existe dans la liste des poisson
        :param p_numero: le numéro poisson
        :return: True si le poisson est dans la liste des poisson - sinon False
    """
    for poi in ls_Poisson:
        if poi.Numero == p_numero:
            return True
    return False

####################################################################################
def camoufler_label_poisson(objet):
    """
    Rendre les labels_erreur invisible
    :param objet:
    :return:
    """
    objet.label_erreur_numero_poisson.setVisible(False)
    objet.label_erreur_poids_poisson.setVisible(False)
    objet.label_erreur_taille_poisson.setVisible(False)
    objet.label_erreur_longevite_poisson.setVisible(False)

####################################################################################
class FenetrePoisson(QtWidgets.QDialog, interface_poisson.Ui_Dialog):
    def __init__(self, parent=None):
        super(FenetrePoisson, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Instancier un poisson")
        # Camoufler les labels d'erreurs Poisson
        camoufler_label_poisson(self)

####################################################################################
    @pyqtSlot()
    # Boutton ajouter
    def on_pushButton_ajouter_poisson_clicked(self):
        """
         Gestionnaire de l'événement click du bouton on_pushButton_ajouter_poisson_clicked
        :return:
        """
        # Instancier un objet Poisson
        poi = Poisson()
        # Entrée de donnée pour les attributs de l'objet Poisson
        poi.Numero = self.lineEdit_numero_poisson.text()
        poi.Poid = self.lineEdit_poids_poisson.text()
        poi.Taille = self.lineEdit_taille_poisson.text()
        poi.Longevite = self.lineEdit_longevite_poisson.text()
        poi.Diet = self.comboBox_diet_poisson.currentText()
        poi.Type_eau = self.comboBox_type_eau.currentText()
        poi.Type_peau = self.comboBox_type_peau.currentText()
        poi.Type_queue = self.comboBox_type_queue.currentText()
        poi.Enclos = self.comboBox_enclos_poisson.currentText()
        # Booleen qui dit si le numéro du poisson existe ou non
        valider_poisson = valider_poisson_liste(poi.Numero)

        # Si le numéro du poisson est valide mais existe déja - On ne le met pas deux fois
        if valider_poisson is True:
            # Effacer le linEdit du numéro poisson et afficher le message d'erreur
            self.lineEdit_numero_poisson.clear()
            self.label_erreur_numero_poisson.setVisible(True)

        # Si le numéro du poisson est invalide - Effacer le line edit + Afficher le message d'erreur
        if poi.Numero == 0:
            self.lineEdit_numero_poisson.clear()
            self.label_erreur_numero_poisson.setVisible(True)

        # Si le poid du poisson est invalide - Effacer le line edit + Afficher le message d'erreur
        if poi.Poid == 0:
            self.lineEdit_poids_poisson.clear()
            self.label_erreur_poids_poisson.setVisible(True)

        # Si la taille du poisson est invalide - Effacer le line edit + Afficher le message d'erreur
        if poi.Taille == 0:
            self.lineEdit_taille_poisson.clear()
            self.label_erreur_taille_poisson.setVisible(True)

        # Si la longévité du poisson est invalide - Effacer le line edit + Afficher le message d'erreur
        if poi.Longevite == 0:
            self.lineEdit_longevite_poisson.clear()
            self.label_erreur_longevite_poisson.setVisible(True)

        # Si les informations entrées sont valides et le poisson n'existe pas dans la liste
        if poi.Numero != 0 and poi.Poid != 0 and poi.Taille != 0 and poi.Longevite != 0 and valider_poisson is False:
            # Ajouter l'objet instancié à la liste poisson
            ls_Poisson.append(poi)
            # Ajouter les information du poisson entré au textBrowser
        self.textBrowser_poisson.append(poi.__str__())
        # Réinitialiser les LineEdits
        self.lineEdit_numero_poisson.clear()
        self.lineEdit_poids_poisson.clear()
        self.lineEdit_taille_poisson.clear()
        self.lineEdit_longevite_poisson.clear()
        # Ajouter l'objet instancié à la liste poisson
        ls_Poisson.append(poi)
        # Ajouter les informations du Poisson entré au textBrowser
        self.textBrowser_poisson.append(poi.__str__())

####################################################################################
    @pyqtSlot()
    # Bouton Modifier
    def on_pushButton_modifier_poisson_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton modifier
        """
        # Cacher les labels d'erreur
        camoufler_label_poisson(self)
        # Instancier un objet poisson
        poi = Poisson()
        # Entrée de donnée pour les attributs de l'objet Poisson
        poi.Numero = self.lineEdit_numero_poisson.text()
        poi.Poid = self.lineEdit_poids_poisson.text()
        poi.Taille = self.lineEdit_taille_poisson.text()
        poi.Longevite = self.lineEdit_longevite_poisson.text()
        poi.Enclos = self.comboBox_enclos_poisson.currentText()
        # Booleen qui dit si le numéro du poisson existe ou non
        valider_poisson = valider_poisson_liste(poi.Numero)
        # Si le numéro du poisson est valide mais existe déja - On ne le met pas deux fois
        if valider_poisson is False and poi.Numero != 0:
            # Effacer le linEdit du numéro poisson et afficher le message d'erreur
            self.lineEdit_numero_poisson.clear()
            self.label_erreur_numero_poisson.setVisible(True)

        # Si le numéro du poisson est invalide - Effacer le line edit + Afficher le message d'erreur
        if poi.Numero == 0:
            self.lineEdit_numero_poisson.clear()
            self.label_erreur_numero_poisson.setVisible(True)

        # Si le poid du poisson est invalide - Effacer le line edit + Afficher le message d'erreur
        if poi.Poid == 0.0:
            self.lineEdit_poids_poisson.clear()
            self.label_erreur_poids_poisson.setVisible(True)

        # Si la taille du poisson est invalide - Effacer le line edit + Afficher le message d'erreur
        if poi.Taille == 0.0:
            self.lineEdit_taille_poisson.clear()
            self.label_erreur_taille_poisson.setVisible(True)

        # Si la longévité du poisson est invalide - Effacer le line edit + Afficher le message d'erreur
        if poi.Longevite == 0.0:
            self.lineEdit_longevite_poisson.clear()
            self.label_erreur_longevite_poisson.setVisible(True)

        # Si les informations sont valides et le poisson n'existe pas dans la liste de poissons
        if poi.Numero != 0 and poi.Poid != 0 and poi.Taille != 0 and poi.Longevite != 0 and valider_poisson is True:
            for poi in ls_Poisson:
                # Chercher dans la liste des poisson un poisson qui a le même numéro
                if poi.Numero == self.lineEdit_numero_poisson.text():
                    # Apporter les modifications aux attributs concernés
                    poi.Poid == self.lineEdit_poids_poisson.text()
                    poi.Taille == self.lineEdit_taille_poisson.text()
                    poi.Longevite == self.lineEdit_longevite_poisson.text()
                    poi.Diet == self.comboBox_diet_poisson.currentText()
                    poi.Enclos == self.comboBox_enclos_poisson.currentText()
                    # Effacer le textBrowser
                    self.textBrowser_poisson.clear()
                    # Après modifications - Réafficher tout les poissons de la liste dans le textBrowser
                    for poi in ls_Poisson:
                        self.textBrowser_poisson.append(poi.__str__())
                    # Réinitialiser les lineEdits du poisson
                    self.lineEdit_numero_poisson.clear()
                    self.lineEdit_poids_poisson.clear()
                    self.lineEdit_taille_poisson.clear()
                    self.lineEdit_longevite_poisson.clear()

####################################################################################
    @pyqtSlot()
    # Bouton Supprimer
    def on_pushButton_supprimer_poisson_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Supprimer
        """
        # Cacher les labels d'erreur
        camoufler_label_poisson(self)
        # Instancier un objet poisson
        poi = Poisson()
        # Entrée de donnée pour les attributs de l'objet Poisson
        poi.Numero = self.lineEdit_numero_poisson.text()
        poi.Poid = self.lineEdit_poids_poisson.text()
        poi.Taille = self.lineEdit_taille_poisson.text()
        poi.Longevite = self.lineEdit_longevite_poisson.text()
        poi.Diet = self.comboBox_diet_poisson.currentText()
        poi.Enclos = self.comboBox_enclos_poisson.currentText()
        # Booleen qui dit si le numéro du poisson existe ou non
        valider_poisson = valider_poisson_liste(poi.Numero)
        if poi.Numero != 0 and poi.Poid != 0 and poi.Taille != 0 and poi.Longevite != 0 and valider_poisson is True:
            decouvre = False
            for poi in ls_Poisson:
                # Chercher dans la lise pour un poisson avec les mêmes informations
                if poi.Numero == self.lineEdit_numero_poisson.text() and poi.Poid == self.lineEdit_poids_poisson.text() \
                        and poi.Taille == self.lineEdit_taille_poisson.text() and poi.Longevite == self.lineEdit_longevite_poisson.text() \
                        and poi.Diet == self.comboBox_diet_poisson.currentText() and poi.Type_eau == self.comboBox_type_eau.currentText() \
                        and poi.Type_peau == self.comboBox_type_peau.currentText() and poi.Type_queue == self.comboBox_type_queue.currentText() \
                        and poi.Enclos == self.comboBox_enclos_poisson.currentText():
                    # Supprimer le poisson de la liste
                    decouvre = True
                    ls_Poisson.remove(poi)
                    break
            # Si le poisson n'existe pas dans la liste - Afficher un message d'erreur (le même que celui pour erreur normale)
            if not decouvre:
                self.label_erreur_numero_poisson.setVisible(True)
            else:
                # Réafficher dans le textBroser la nouvelle lise qui ne contient pas l'étudient supprimé
                self.textBrowser_poisson.clear()
                for poi in ls_Poisson:
                    self.textBrowser_poisson.append(poi.__str__())
                # Réinitialiser le lineEdit numéro
                self.lineEdit_numero_poisson.clear()
        # Si le numéro du poisson = valid MAIS existe déja - On ne peux pas l'ajouter
        if valider_poisson is False and poi.Numero != "":
            # Effacer le lineEdit du numéro + afficher le message d'erreur
            self.lineEdit_numero_poisson.clear()
            self.label_erreur_numero_poisson.setVisible(True)
        # Si le numéro d'étudiant est invalide, effacer le lineEdit du numéro étudiant  et afficher un message d'erreur
        if poi.Numero == "":
            self.lineEdit_numero_poisson.clear()
            self.label_erreur_numero_poisson.setVisible(True)

####################################################################################
    @pyqtSlot()
    def on_pushButton_quitter_poisson_clicked(self):
        self.close()
