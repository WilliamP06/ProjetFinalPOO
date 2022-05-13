# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets

# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la boite de dialogue
import interface_poisson

# Importer la classe Poisson
from Poisson import *

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
# Déclarer une liste Poisson
ls_Poisson = []

####################################################################################
class FenetrePoisson(QtWidgets.QDialog, interface_poisson.Ui_Dialog):
    def __init__(self, parent=None):
        super(FenetrePoisson, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Instancier un mamifère")
        # Camoufler les labels d'erreurs Poisson
        camoufler_label_poisson(self)

####################################################################################
    @pyqtSlot()
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
        poi.Type_eau = self.comboBox_type_eau()
        poi.Type_peau = self.comboBox_type_peau()
        poi.Type_queue = self.comboBox_type_queue()
        poi.Enclos = self.comboBox_enclos_poisson.currentText()
        # Ajouter l'objet instancié à la liste Mamifère
        ls_Poisson.append(poi)
        # Ajouter les informations du Poisson entré au textBrowser
        self.textBrowser_poisson.append(poi.__str__())

####################################################################################
    @pyqtSlot()
    def on_pushButton_quitter_poisson_clicked(self):
        self.close()
