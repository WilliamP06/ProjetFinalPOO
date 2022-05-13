####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Final (Zoo)
###  Nom: William Poiré
###  No étudiant: 2145322
###  No Groupe:
###  Description du fichier: Programme principal
####################################################################################

# Importer les dialog
import MamifereDialog
import OiseauDialog
import PoissonDialog

# Importer pour fonctions du terminal
import sys

# Importer pour UI - Dialogues
from PyQt5.QtGui import QStandardItemModel, QStandardItem

# Importation du fichier du ui converti en py
import interface_zoomain
import interface_mamifere
import interface_oiseau
import interface_poisson

# Importation des librairies nécessaies à QtDesigner
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

# importer les classes
from Animal import *
from Mamifere import *
from Oiseau import *
from Poisson import *
from Enclos import *
from MamifereDialog import FenetreMamifere
from OiseauDialog import FenetreOiseau
from PoissonDialog import FenetrePoisson
####################################################################################

# Déclarer une liste Animal, mamifères, oiseau, poisson et enclos
ls_Animal = []
ls_Mamifere = []
ls_Oiseau = []
ls_Poisson = []
ls_Enclos = []
####################################################################################

####################################################################################
####################################################################################

class mainwindow(QtWidgets.QMainWindow, interface_zoomain.Ui_MainWindow):
    """
    Nom de la classe: mainwindow
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe mainwindow
        :param parent: QtWidwidgets & QMainWindow
        """
        # Appel du constructeur de la classe parent
        super(mainwindow, self).__init__(parent)
        self.setupUi(self) # Initialiser l'interface graphique
        self.setWindowTitle("Fenêtre principale") # Apparait sur a barre de titre de la fenêtre
####################################################################################
    # Utiliser le décorateur pour empêcher que le code du gestionnaire d'événement du bouton ne s'éxecute deux fois
    @pyqtSlot()
    def on_pushButton_mamifere_clicked(self):
    # Bouton Mamifère
        """
        Gestionnaire de l'événement click du bouton on_pushButton_mamifere_clicked
        :return:
        """

        # Instancier une boite de dialogue FenetreMamifere
        dialog = FenetreMamifere()

        # Afficher la boite de dialogue
        dialog.show()
        reponse = dialog.exec_()


####################################################################################
    # Utiliser le décorateur pour empêcher que le code du gestionnaire d'événement du bouton ne s'éxecute deux fois
    @pyqtSlot()
    def on_pushButton_oiseau_clicked(self):
    # Boutton Oiseau
        """
        Gestionnaire de l'événement click du bouton on_pushButton_oiseau_clicked
        :return:
        """

        # Instancier une boite de dialogue FenetreOiseau
        dialog = FenetreOiseau()

        # Afficher la boite de dialogue
        dialog.show()
        reponse = dialog.exec_()

####################################################################################
    # Utiliser le décorateur pour empêcher que le code du gestionnaire d'événement du bouton ne s'éxecute deux fois
    @pyqtSlot()
    def on_pushButton_poisson_clicked(self):
    # Boutton Poisson
        """
        Gestionnaire de l'événement click du bouton on_pushButton_poisson_clicked
        :return:
        """

        # Instancier une boite de dialogue FenetrePoisson
        dialog = FenetrePoisson()

        # Afficher la boite de dialogue
        dialog.show()
        reponse = dialog.exec_()

####################################################################################
    @pyqtSlot()
    def on_pushButton_quitter_clicked(self):
        self.close()

####################################################################################
# Creer ce qui va lancer la fenetre principale
def main():
    # Instancier une application et une fenêtre principale
    app = QtWidgets.QApplication(sys.argv)
    form = mainwindow()
    # Afficher la fenêtre principale
    form.show()
    # Lancer l'application
    app.exec()

if __name__ == "__main__":
    main()
