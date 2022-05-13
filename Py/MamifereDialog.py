# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets

# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la boite de dialogue
import interface_mamifere

# Importer la classe Mamifere
from Mamifere import *

####################################################################################
def camoufler_label_mamifere(objet):
    """
    Rendre les labels_erreur invisible
    :param objet:
    :return:
    """
    objet.label_erreur_numero_mamifere.setVisible(False)
    objet.label_erreur_poids_mamifere.setVisible(False)
    objet.label_erreur_taille_mamifere.setVisible(False)
    objet.label_erreur_longevite_mamifere.setVisible(False)

####################################################################################
# Déclarer une liste Mamifère
ls_Mamifere = []

####################################################################################
class FenetreMamifere(QtWidgets.QDialog, interface_mamifere.Ui_Dialog):
    def __init__(self, parent=None):
        super(FenetreMamifere, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Instancier un mamifère")
        # Cacher les labels d'erreurs mamifere
        camoufler_label_mamifere(self)

####################################################################################
    @pyqtSlot()
    # Boutton Ajouter
    def on_pushButton_ajouter_mamifere_clicked(self):
        """
        Gestionnaire de l'événement click du bouton on_pushButton_ajouter_mamifere_clicked
        :return:
        """
        # instancier un objet mamifère
        mam = Mamifere()
        # Entrée de donnée pour les attributs de l'objet Mamifère
        mam.Numero = self.lineEdit_numero_mamifere.text()
        mam.Poid = self.lineEdit_poids_mamifere.text()
        mam.Taille = self.lineEdit_taille_mamifere.text()
        mam.Longevite = self.lineEdit_longevite_mamifere.text()
        mam.Diet = self.comboBox_diet_mamifere.currentText()
        mam.Couleur_fourrure = self.comboBox_couleur_fourrure.currentText()
        mam.Type_patte = self.comboBox_type_patte.currentText()
        mam.Nbdoigts = self.lineEdit_nbdoigts_mamifere
        mam.Enclos = self.comboBox_type_enclos_mamifere.currentText()
        # Ajouter l'objet instancié à la liste Mamifère
        ls_Mamifere.append(mam)
        # Ajouter les information du mamifère entré au textBrowser
        self.textBrowser_mamifere.append(mam.__str__())

####################################################################################
    @pyqtSlot()
    def on_pushButton_quitter_mamifere_clicked(self):
        self.close()
