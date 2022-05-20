# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets

# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Pour le boutton "Afficher"
from PyQt5.QtGui import QStandardItemModel

# Importer la boite de dialogue
import interface_mamifere

# Importer la classe Mamifere
from Mamifere import *

####################################################################################
# Déclarer une liste Mamifère
ls_Mamifere = []

####################################################################################
def valider_mamifere_liste(p_numero):
    """
    Vérifie si le mamifère existe dans la liste des mamifères
        :param p_numero: le numéro mamifère
        :return: True si le mamifère est dans la liste des mamifères - sinon False
    """
    for mam in ls_Mamifere:
        if mam.Numero == p_numero:
            return True
    return False

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
    objet.label_erreur_nbdoigts_mamifere.setVisible(False)

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
        #TODO self.lineEdit_poids_mamifere.text()

        # Cacher les labels d'erreur mamifère
        camoufler_label_mamifere(self)
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
        mam.Nbdoigts = self.lineEdit_nbdoigts_mamifere.text()
        mam.Enclos = self.comboBox_type_enclos_mamifere.currentText()
        # Booleen qui dit si le numéro du mamifère existe ou non
        valider_mamifere = valider_mamifere_liste(mam.Numero)

        # Si le numéro du mamifère est valide mais existe déja - On ne le met pas deux fois
        if valider_mamifere is True:
            # Effacer le linEdit du numéro mamifère et afficher le message d'erreur
            self.lineEdit_numero_mamifere.clear()
            self.label_erreur_numero_mamifere.setVisible(True)

        # Si le numéro du mamifère est invalide - Effacer le line edit + Afficher le message d'erreur
        if mam.Numero == 0:
            self.lineEdit_numero_mamifere.clear()
            self.label_erreur_numero_mamifere.setVisible(True)

        # Si le poid du mamifère est invalide - Effacer le line edit + Afficher le message d'erreur
        if mam.Poid == 0:
            self.lineEdit_poids_mamifere.clear()
            self.label_erreur_poids_mamifere.setVisible(True)

        # Si la taille du mamifère est invalide - Effacer le line edit + Afficher le message d'erreur
        if mam.Taille == 0:
            self.lineEdit_taille_mamifere.clear()
            self.label_erreur_taille_mamifere.setVisible(True)

        # Si la longévité du mamifère est invalide - Effacer le line edit + Afficher le message d'erreur
        if mam.Longevite == 0:
            self.lineEdit_longevite_mamifere.clear()
            self.label_erreur_longevite_mamifere.setVisible(True)

        # Si le nombre de doigts du mamifère est invalide - Effacer le line edit + Afficher le message d'erreur
        if mam.Nbdoigts == 0:
            self.lineEdit_nbdoigts_mamifere.clear()
            self.label_erreur_nbdoigts_mamifere.setVisible(True)

        # Si les informations entrées sont valides et le mamifère n'existe pas dans la liste
        if mam.Numero != 0 and mam.Poid != 0 and mam.Taille != 0 and mam.Longevite != 0 and mam.Nbdoigts != 0 and valider_mamifere is False:
            # Ajouter l'objet instancié à la liste Mamifère
            ls_Mamifere.append(mam)
            # Ajouter les information du mamifère entré au textBrowser
        self.textBrowser_mamifere.append(mam.__str__())
        # Réinitialiser les LineEdits
        self.lineEdit_numero_mamifere.clear()
        self.lineEdit_poids_mamifere.clear()
        self.lineEdit_taille_mamifere.clear()
        self.lineEdit_longevite_mamifere.clear()
        self.lineEdit_nbdoigts_mamifere.clear()

####################################################################################
    @pyqtSlot()
    # Bouton Modifier
    def on_pushButton_modifier_mamifere_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton modifier
        """
        # Cacher les labels d'erreur
        camoufler_label_mamifere(self)
        # Instancier un objet Mamifère
        mam = Mamifere()
        # Entrée de donnée pour les attributs de l'objet Mamifère
        mam.Numero = self.lineEdit_numero_mamifere.text()
        mam.Poid = self.lineEdit_poids_mamifere.text()
        mam.Taille = self.lineEdit_taille_mamifere.text()
        mam.Longevite = self.lineEdit_longevite_mamifere.text()
        mam.Diet = self.comboBox_diet_mamifere.currentText()
        mam.Couleur_fourrure = self.comboBox_couleur_fourrure.currentText()
        mam.Type_patte = self.comboBox_type_patte.currentText()
        mam.Nbdoigts = self.lineEdit_nbdoigts_mamifere.text()
        mam.Enclos = self.comboBox_type_enclos_mamifere.currentText()
        # Booleen qui dit si le numéro du mamifère existe ou non
        valider_mamifere = valider_mamifere_liste(mam.Numero)
        # Si le numéro du mamifère est valide mais existe déja - On ne le met pas deux fois
        if valider_mamifere is False and mam.Numero != 0:
            # Effacer le linEdit du numéro mamifère et afficher le message d'erreur
            self.lineEdit_numero_mamifere.clear()
            self.label_erreur_numero_mamifere.setVisible(True)

        # Si le numéro du mamifère est invalide - Effacer le line edit + Afficher le message d'erreur
        if mam.Numero == 0:
            self.lineEdit_numero_mamifere.clear()
            self.label_erreur_numero_mamifere.setVisible(True)

        # Si le poid du mamifère est invalide - Effacer le line edit + Afficher le message d'erreur
        if mam.Poid == 0.0:
            self.lineEdit_poids_mamifere.clear()
            self.label_erreur_poids_mamifere.setVisible(True)

        # Si la taille du mamifère est invalide - Effacer le line edit + Afficher le message d'erreur
        if mam.Taille == 0.0:
            self.lineEdit_taille_mamifere.clear()
            self.label_erreur_taille_mamifere.setVisible(True)

        # Si la longévité du mamifère est invalide - Effacer le line edit + Afficher le message d'erreur
        if mam.Longevite == 0.0:
            self.lineEdit_longevite_mamifere.clear()
            self.label_erreur_longevite_mamifere.setVisible(True)

        # Si le nombre de doigts du mamifère est invalide - Effacer le line edit + Afficher le message d'erreur
        if mam.Nbdoigts == 0:
            self.lineEdit_nbdoigts_mamifere.clear()
            self.label_erreur_nbdoigts_mamifere.setVisible(True)

        # Si les informations sont valides et le mamifère n'existe pas dans la liste de mamifères
        if mam.Numero != 0 and mam.Poid != 0 and mam.Taille != 0 and mam.Longevite != 0 and mam.Nbdoigts != 0 and valider_mamifere is True:
            for mam in ls_Mamifere:
                # Chercher dans la liste des mamifères un mamifère qui a le même numéro
                if mam.Numero == self.lineEdit_numero_mamifere.text():
                    # Apporter les modifications aux attributs concernés
                    mam.Poid == self.lineEdit_poids_mamifere.text()
                    mam.Taille == self.lineEdit_taille_mamifere.text()
                    mam.Longevite == self.lineEdit_longevite_mamifere.text()
                    mam.Diet == self.comboBox_diet_mamifere.currentText()
                    mam.Couleur_fourrure == self.comboBox_couleur_fourrure.currentText()
                    mam.Type_patte == self.comboBox_type_patte.currentText()
                    mam.Nbdoigts == self.lineEdit_nbdoigts_mamifere.text()
                    mam.Enclos == self.comboBox_type_enclos_mamifere.currentText()
                    # Effacer le textBrowser
                    self.textBrowser_mamifere.clear()
                    # Après modifications - Réafficher tout les mamifères de la liste dans le textBrowser
                    for mam in ls_Mamifere:
                        self.textBrowser_mamifere.append(mam.__str__())
                    # Réinitialiser les lineEdits du mamifère
                    self.lineEdit_numero_mamifere.clear()
                    self.lineEdit_poids_mamifere.clear()
                    self.lineEdit_taille_mamifere.clear()
                    self.lineEdit_longevite_mamifere.clear()
                    self.lineEdit_nbdoigts_mamifere.clear()

####################################################################################
    @pyqtSlot()
    # Bouton Supprimer
    def on_pushButton_supprimer_mamifere_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Supprimer
        """
        # Cacher les labels d'erreur
        camoufler_label_mamifere(self)
        # Instancier un objet Mamifère
        mam = Mamifere()
        # Entrée de donnée pour les attributs de l'objet Mamifère
        mam.Numero = self.lineEdit_numero_mamifere.text()
        mam.Poid = self.lineEdit_poids_mamifere.text()
        mam.Taille = self.lineEdit_taille_mamifere.text()
        mam.Longevite = self.lineEdit_longevite_mamifere.text()
        mam.Diet = self.comboBox_diet_mamifere.currentText()
        mam.Couleur_fourrure = self.comboBox_couleur_fourrure.currentText()
        mam.Type_patte = self.comboBox_type_patte.currentText()
        mam.Nbdoigts = self.lineEdit_nbdoigts_mamifere.text()
        mam.Enclos = self.comboBox_type_enclos_mamifere.currentText()
        # Booleen qui dit si le numéro du mamifère existe ou non
        valider_mamifere = valider_mamifere_liste(mam.Numero)
        if mam.Numero != 0 and mam.Poid != 0 and mam.Taille != 0 and mam.Longevite != 0 and mam.Nbdoigts != 0 and valider_mamifere is True:
            decouvre = False
            for mam in ls_Mamifere:
                # Chercher dans la lise pour un Mamifère avec les mêmes informations
                if mam.Numero == self.lineEdit_numero_mamifere.text() and mam.Poid == self.lineEdit_poids_mamifere.text()\
                    and mam.Taille == self.lineEdit_taille_mamifere.text() and mam.Longevite == self.lineEdit_longevite_mamifere.text()\
                    and mam.Diet == self.comboBox_diet_mamifere.currentText() and mam.Couleur_fourrure == self.comboBox_couleur_fourrure.currentText()\
                    and mam.Type_patte == self.comboBox_type_patte.currentText() and mam.Nbdoigts == self.lineEdit_nbdoigts_mamifere.text()\
                    and mam.Enclos == self.comboBox_type_enclos_mamifere.currentText():
                    # Supprimer le mamifère de la liste
                    decouvre = True
                    ls_Mamifere.remove(mam)
                    break
            # Si le mamifère n'existe pas dans la liste - Afficher un message d'erreur (le même que celui pour erreur normale)
            if not decouvre:
                self.label_erreur_numero_mamifere.setVisible(True)
            else:
                # Réafficher dans le textBroser la nouvelle lise qui ne contient pas l'étudient supprimé
                self.textBrowser_mamifere.clear()
                for mam in ls_Mamifere:
                    self.textBrowser_mamifere.append(mam.__str__())
                # Réinitialiser le lineEdit numéro
                self.lineEdit_numero_mamifere.clear()
        # Si le numéro du mamifère = valid MAIS existe déja - On ne peux pas l'ajouter
        if valider_mamifere is False and mam.Numero != "":
            # Effacer le lineEdit du numéro + afficher le message d'erreur
            self.lineEdit_numero_mamifere.clear()
            self.label_erreur_numero_mamifere.setVisible(True)
        # Si le numéro d'étudiant est invalide, effacer le lineEdit du numéro étudiant  et afficher un message d'erreur
        if mam.Numero == "":
            self.lineEdit_numero_mamifere.clear()
            self.label_erreur_numero_mamifere.setVisible(True)

####################################################################################
    @pyqtSlot()
    # Boutton Afficher
    def on_pushButton_afficher_mamifere_clicked(self):
        boite = FenetreMamifere()
        model = QStandardItemModel()
        boite.textBrowser_mamifere.append(model)
        for mam in ls_Mamifere:
            item = QStandardItemModel(mam.Numero + " * " + mam.Poid + " * " + mam.Taille + " * " + mam.Longevite + " * " + mam.Diet + " * " + mam.Enclos + " * " + mam.Couleur_fourrure + " * " + mam.Type_patte + " * " + mam.Nbdoigts)
            model.appendRow(item)

####################################################################################
    @pyqtSlot()
    # Boutton Quitter
    def on_pushButton_quitter_mamifere_clicked(self):
        self.close()
