# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets

# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Pour le boutton "Afficher"
from PyQt5.QtGui import QStandardItemModel

# Importer la boite de dialogue
import interface_enclos

# Importer la classe enclos
from Enclos import *

####################################################################################
# Déclarer une liste Enclos
ls_Enclos = []

####################################################################################
def valider_enclos_liste(p_numero):
    """
    Vérifie si l'enclos existe dans la liste des enclos
        :param p_numero: le numéro de l'enclos
        :return: True si l'enclos est dans la liste des enclos - sinon False
    """
    for enc in ls_Enclos:
        if enc.Numero == p_numero:
            return True
    return False

####################################################################################
def valider_enclos_liste(p_numero):
    """
    Vérifie si l'enclos existe dans la liste des enclos
        :param p_numero: le numéro enclos
        :return: True si l'enclos est dans la liste des enclos - sinon False
    """
    for enc in ls_Enclos:
        if enc.Numero == p_numero:
            return True
    return False

####################################################################################
def camoufler_label_enclos(objet):
    """
    Rendre les labels_erreur invisible
    :param objet:
    :return:
    """
    objet.label_erreur_numero_enclos.setVisible(False)

####################################################################################
class FenetreEnclos(QtWidgets.QDialog, interface_enclos.Ui_Dialog):
    def __init__(self, parent=None):
        super(FenetreEnclos, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Instancier un enclos")
        # Cacher les labels d'erreurs enclos
        camoufler_label_enclos(self)

####################################################################################
    @pyqtSlot()
    # Boutton ajouter
    def on_pushButton_ajouter_enclos_clicked(self):
        """
         Gestionnaire de l'événement click du bouton on_pushButton_ajouter_enclos_clicked
        :return:
        """
        # Instancier un objet Enclos
        enc = Enclos()
        # Entrée de donnée pour les attributs de l'objet Enclos
        enc.Numero = self.lineEdit_numero_enclos.text()
        enc.Type_enclos = self.comboBox_enclos_enclos.currentText()
        enc.Type_animal = self.comboBox_type_animal_enclos.currentText()
        # Booleen qui dit si le numéro du enclos existe ou non
        valider_enclos = valider_enclos_liste(enc.Numero)

        # Si le numéro de l'enclos est valide mais existe déja - On ne le met pas deux fois
        if valider_enclos is True:
            # Effacer le linEdit du numéro enclos et afficher le message d'erreur
            self.lineEdit_numero_enclos.clear()
            self.label_erreur_numero_enclos.setVisible(True)

        # Si le numéro de  l'enclos est invalide - Effacer le line edit + Afficher le message d'erreur
        if enc.Numero == 0:
            self.lineEdit_numero_enclos.clear()
            self.label_erreur_numero_enclos.setVisible(True)

        # Si les informations entrées sont valides et le enclos n'existe pas dans la liste
        if enc.Numero != 0 and valider_enclos is False:
            # Ajouter l'objet instancié à la liste enclos
            ls_Enclos.append(enc)
            # Ajouter les information du enclos entré au textBrowser
        self.textBrowser_enclos.append(enc.__str__())
        # Réinitialiser les LineEdits
        self.lineEdit_numero_enclos.clear()

####################################################################################
    @pyqtSlot()
    # Boutton Modifier
    def on_pushButton_modifier_enclos_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton modifier
        """
        # Cacher les labels d'erreur
        camoufler_label_enclos(self)
        # Instancier un objet enclos
        enc = Enclos()
        # Entrée de donnée pour les attributs de l'objet enclos
        enc.Numero = self.lineEdit_numero_enclos.text()
        enc.Type_enclos = self.comboBox_enclos_enclos.currentText()
        enc.Type_animal = self.comboBox_type_animal_enclos.currentText()

        # Booleen qui dit si le numéro du enclos existe ou non
        valider_enclos = valider_enclos_liste(enc.Numero)
        # Si le numéro du enclos est valide mais existe déja - On ne le met pas deux fois
        if valider_enclos is False and enc.Numero != 0:
            # Effacer le linEdit du numéro enclos et afficher le message d'erreur
            self.lineEdit_numero_enclos.clear()
            self.label_erreur_numero_enclos.setVisible(True)

        # Si le numéro du enclos est invalide - Effacer le line edit + Afficher le message d'erreur
        if enc.Numero == 0:
            self.lineEdit_numero_enclos.clear()
            self.label_erreur_numero_enclos.setVisible(True)

        # Si les informations sont valides et le enclos n'existe pas dans la liste de enclos
        if enc.Numero != 0 and valider_enclos is True:
            for enc in ls_Enclos:
                # Chercher dans la liste des enclos un enclos qui a le même numéro
                if enc.Numero == self.lineEdit_numero_enclos.text():
                    # Apporter les modifications aux attributs concernés
                    enc.Type_enclos = self.comboBox_enclos_enclos.currentText()
                    enc.Type_animal = self.comboBox_type_animal_enclos.currentText()
                    # Effacer le textBrowser
                    self.textBrowser_enclos.clear()
                    # Après modifications - Réafficher tout les enclos de la liste dans le textBrowser
                    for enc in ls_Enclos:
                        self.textBrowser_enclos.append(enc.__str__())
                    # Réinitialiser les lineEdits du enclos
                    self.lineEdit_numero_enclos.clear()

####################################################################################
    @pyqtSlot()
    # Boutton Supprimer
    def on_pushButton_supprimer_enclos_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Supprimer
        """
        # Cacher les labels d'erreur
        camoufler_label_enclos(self)
        # Instancier un objet enclos
        enc = Enclos()
        # Entrée de donnée pour les attributs de l'objet enclos
        enc.Numero = self.lineEdit_numero_enclos.text()
        enc.Type_enclos = self.comboBox_enclos_enclos.currentText()
        enc.Type_animal = self.comboBox_type_animal_enclos.currentText()

        # Booleen qui dit si le numéro du enclos existe ou non
        valider_enclos = valider_enclos_liste(enc.Numero)
        if enc.Numero != 0 and valider_enclos is True:
            decouvre = False
            for enc in ls_Enclos:
                # Chercher dans la lise pour un enclos avec les mêmes informations
                if enc.Numero == self.lineEdit_numero_enclos.text() and enc.Type_enclos == self.comboBox_enclos_enclos.currentText()\
                    and enc.Type_animal == self.comboBox_type_animal_enclos.currentText():
                    # Supprimer l'enclos de la liste
                    decouvre = True
                    ls_Enclos.remove(enc)
                    break
            # Si le enclos n'existe pas dans la liste - Afficher un message d'erreur (le même que celui pour erreur normale)
            if not decouvre:
                self.label_erreur_numero_enclos.setVisible(True)
            else:
                # Réafficher dans le textBroser la nouvelle lise qui ne contient pas l'étudient supprimé
                self.textBrowser_enclos.clear()
                for enc in ls_Enclos:
                    self.textBrowser_enclos.append(enc.__str__())
                # Réinitialiser le lineEdit numéro
                self.lineEdit_numero_enclos.clear()
        # Si le numéro du enclos = valid MAIS existe déja - On ne peux pas l'ajouter
        if valider_enclos is False and enc.Numero != "":
            # Effacer le lineEdit du numéro + afficher le message d'erreur
            self.lineEdit_numero_enclos.clear()
            self.label_erreur_numero_enclos.setVisible(True)
        # Si le numéro d'étudiant est invalide, effacer le lineEdit du numéro étudiant  et afficher un message d'erreur
        if enc.Numero == "":
            self.lineEdit_numero_enclos.clear()
            self.label_erreur_numero_enclos.setVisible(True)

####################################################################################
    @pyqtSlot()
    # Boutton Afficher
    def on_pushButton_afficher_enclos_clicked(self):
        boite = FenetreEnclos()
        model = QStandardItemModel()
        boite.textBrowser_enclos.append(model)
        for enc in ls_Enclos:
            item = QStandardItemModel(enc.Numero + " * " + enc.Type_enclos + " * " + enc.Type_animal)
            model.appendRow(item)

####################################################################################

    @pyqtSlot()
    # Boutton Quitter
    def on_pushButton_quitter_enclos_clicked(self):
        self.close()