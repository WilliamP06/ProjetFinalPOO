# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets

# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la boite de dialogue
import interface_oiseau

# Importer la classe Oiseau
from Oiseau import *

####################################################################################
def camoufler_label_oiseau(objet):
    """
    Rendre les labels_erreur invisible
    :param objet:
    :return:
    """
    objet.label_erreur_numero_oiseau.setVisible(False)
    objet.label_erreur_poids_oiseau.setVisible(False)
    objet.label_erreur_taille_oiseau.setVisible(False)
    objet.label_erreur_longevite_oiseau.setVisible(False)

####################################################################################
# Déclarer une liste Oiseau
ls_Oiseau = []

####################################################################################
class FenetreOiseau(QtWidgets.QDialog, interface_oiseau.Ui_Dialog):
    def __init__(self, parent=None):
        super(FenetreOiseau, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Instancier un oiseau")
        # Camoufler les labels d'erreurs oiseau
        camoufler_label_oiseau(self)

####################################################################################
    @pyqtSlot()
    # Bouton ajouter
    def on_pushButton_ajouter_oiseau_clicked(self):
        """
        Gestionnaire de l'événement click du bouton on_pushButton_ajouter_oiseau_clicked
        :return:
        """
        # Instancier un objet Oiseau
        ois = Oiseau()
        # Entrée de donnée pour les attributs de l'objet Oiseau
        ois.Numero = self.lineEdit_numero_oiseau.text()
        ois.Poid = self.lineEdit_poids_oiseau.text()
        ois.Taille = self.lineEdit_taille_oiseau.text()
        ois.Longevite = self.lineEdit_longevite_oiseau.text()
        ois.Diet = self.comboBox_diet_oiseau.currentText()
        ois.Couleur_plumes = self.comboBox_couleur_plumes.currentText()
        ois.Couleur_bec = self.comboBox_couleur_bec.currentText()
        ois.Longueurbec = self.lineEdit_longueur_bec_oiseau.text()
        ois.Enclos = self.comboBox_enclos_oiseau.currentText()
        # Ajouter l'objet instancié à la liste Oiseau
        ls_Oiseau.append(ois)
        # Ajouter les informations du oiseau entré au textBrowser
        self.textBrowser_oiseau.append(ois.__str__())

####################################################################################
    @pyqtSlot()
    def on_pushButton_quitter_oiseau_clicked(self):
        self.close()
