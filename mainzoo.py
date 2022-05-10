####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Final (Zoo)
###  Nom: William Poiré
###  No étudiant: 2145322
###  No Groupe:
###  Description du fichier: Programme principal
####################################################################################

# Importer pour fonctions du terminal
import sys

# Importer pour UI - Dialogues
from PyQt5.QtGui import QStandardItemModel, QStandardItem

# importer les UI
from Animal import *
from Mamifere import *
from Oiseau import *
from Poisson import *
from Enclos import *
####################################################################################

# Déclarer une liste Animal, mamifères, oiseau, poisson et enclos
ls_Animal = []
ls_Mamifere = []
ls_Oiseau = []
ls_Poisson = []
ls_Enclos = []
####################################################################################

####################################################################################

# Main window
class MainWindow(QtWidgets.QMainWindow)