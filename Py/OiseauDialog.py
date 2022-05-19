# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets

# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la boite de dialogue
import interface_oiseau

# Importer la classe Oiseau
from Oiseau import *

####################################################################################
# Déclarer une liste Oiseau
ls_Oiseau = []

####################################################################################
def valider_oiseau_liste(p_numero):
    """
    Vérifie si le oiseau existe dans la liste des oiseau
        :param p_numero: le numéro oiseau
        :return: True si le oiseau est dans la liste des oiseau - sinon False
    """
    for ois in ls_Oiseau:
        if ois.Numero == p_numero:
            return True
    return False

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
    objet.label_erreur_longueurbec_oiseau.setVisible(False)

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
        # Cacher les labels d'erreur du Oiseau
        camoufler_label_oiseau(self)
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
        # Booleen qui dit si le numéro du Oiseau existe ou non
        valider_oiseau = valider_oiseau_liste(ois.Numero)

        # Si le numéro du Oiseau est valide mais existe déja - On ne le met pas deux fois
        if valider_oiseau is True:
            # Effacer le linEdit du numéro Oiseau et afficher le message d'erreur
            self.lineEdit_numero_oiseau.clear()
            self.label_erreur_numero_oiseau.setVisible(True)

        # Si le numéro du Oiseau est invalide - Effacer le line edit + Afficher le message d'erreur
        if ois.Numero == 0:
            self.lineEdit_numero_oiseau.clear()
            self.label_erreur_numero_oiseau.setVisible(True)

        # Si le poid du Oiseau est invalide - Effacer le line edit + Afficher le message d'erreur
        if ois.Poid == 0:
            self.lineEdit_poids_oiseau.clear()
            self.label_erreur_poids_oiseau.setVisible(True)

        # Si la taille du Oiseau est invalide - Effacer le line edit + Afficher le message d'erreur
        if ois.Taille == 0:
            self.lineEdit_taille_oiseau.clear()
            self.label_erreur_taille_oiseau.setVisible(True)

        # Si la longévité du Oiseau est invalide - Effacer le line edit + Afficher le message d'erreur
        if ois.Longevite == 0:
            self.lineEdit_longevite_oiseau.clear()
            self.label_erreur_longevite_oiseau.setVisible(True)
        # # Si la longueur du bec du oiseau est invalide - Effacer le line edit + Afficher le message d'erreur
        if ois.Longueurbec == 0:
            self.lineEdit_longueur_bec_oiseau.clear()
            self.label_erreur_longueurbec_oiseau.setVisible(True)

        # Si les informations entrées sont valides et le oiseau n'existe pas dans la liste
        if ois.Numero != 0 and ois.Poid != 0 and ois.Taille != 0 and ois.Longevite != 0 and ois.Longueurbec !=0 and valider_oiseau is False:
        # Ajouter l'objet instancié à la liste Oiseau
            ls_Oiseau.append(ois)
        # Ajouter les informations du oiseau entré au textBrowser
        self.textBrowser_oiseau.append(ois.__str__())
        # Réinitialiser les LineEdits
        self.lineEdit_numero_oiseau.clear()
        self.lineEdit_poids_oiseau.clear()
        self.lineEdit_taille_oiseau.clear()
        self.lineEdit_longevite_oiseau.clear()
        self.lineEdit_longueur_bec_oiseau.clear()

####################################################################################
    @pyqtSlot()
    # Bouton Modifier
    def on_pushButton_modifier_oiseau_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton modifier
        """
        # Cacher les labels d'erreur
        camoufler_label_oiseau(self)
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
        # Booleen qui dit si le numéro du Oiseau existe ou non
        valider_oiseau = valider_oiseau_liste(ois.Numero)
        # Si le numéro du Oiseau est valide mais existe déja - On ne le met pas deux fois
        if valider_oiseau is False and ois.Numero != 0:
            # Effacer le linEdit du numéro Oiseau et afficher le message d'erreur
            self.lineEdit_numero_oiseau.clear()
            self.label_erreur_numero_oiseau.setVisible(True)

        # Si le numéro du Oiseau est invalide - Effacer le line edit + Afficher le message d'erreur
        if ois.Numero == 0:
            self.lineEdit_numero_oiseau.clear()
            self.label_erreur_numero_oiseau.setVisible(True)

        # Si le poid du Oiseau est invalide - Effacer le line edit + Afficher le message d'erreur
        if ois.Poid == 0:
            self.lineEdit_poids_oiseau.clear()
            self.label_erreur_poids_oiseau.setVisible(True)

        # Si la taille du Oiseau est invalide - Effacer le line edit + Afficher le message d'erreur
        if ois.Taille == 0:
            self.lineEdit_taille_oiseau.clear()
            self.label_erreur_taille_oiseau.setVisible(True)

        # Si la longévité du Oiseau est invalide - Effacer le line edit + Afficher le message d'erreur
        if ois.Longevite == 0:
            self.lineEdit_longevite_oiseau.clear()
            self.label_erreur_longevite_oiseau.setVisible(True)

        # Si le nombre de doigts du Oiseau est invalide - Effacer le line edit + Afficher le message d'erreur
        if ois.Longueurbec == 0:
            self.lineEdit_longueur_bec_oiseau.clear()
            self.label_erreur_longueurbec_oiseau.setVisible(True)

        # Si les informations sont valides et le Oiseau n'existe pas dans la liste de Oiseau
        if ois.Numero != 0 and ois.Poid != 0 and ois.Taille != 0 and ois.Longevite != 0 and ois.Longueurbec != 0 and valider_oiseau is True:
            for ois in ls_Oiseau:
                # Chercher dans la liste des Oiseau un Oiseau qui a le même numéro
                if ois.Numero == self.lineEdit_numero_oiseau.text():
                    # Apporter les modifications aux attributs concernés
                    ois.Numero = self.lineEdit_numero_oiseau.text()
                    ois.Poid = self.lineEdit_poids_oiseau.text()
                    ois.Taille = self.lineEdit_taille_oiseau.text()
                    ois.Longevite = self.lineEdit_longevite_oiseau.text()
                    ois.Diet = self.comboBox_diet_oiseau.currentText()
                    ois.Couleur_plumes = self.comboBox_couleur_plumes.currentText()
                    ois.Couleur_bec = self.comboBox_couleur_bec.currentText()
                    ois.Longueurbec = self.lineEdit_longueur_bec_oiseau.text()
                    ois.Enclos = self.comboBox_enclos_oiseau.currentText()
                    # Effacer le textBrowser
                    self.textBrowser_oiseau.clear()
                    # Après modifications - Réafficher tout les Oiseau de la liste dans le textBrowser
                    for ois in ls_Oiseau:
                        self.textBrowser_oiseau.append(ois.__str__())
                        # Réinitialiser les LineEdits
                    self.lineEdit_numero_oiseau.clear()
                    self.lineEdit_poids_oiseau.clear()
                    self.lineEdit_taille_oiseau.clear()
                    self.lineEdit_longevite_oiseau.clear()
                    self.lineEdit_longueur_bec_oiseau.clear()

####################################################################################
    @pyqtSlot()
    # Bouton Supprimer
    def on_pushButton_supprimer_oiseau_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton modifier
        """
        # Cacher les labels d'erreur
        camoufler_label_oiseau(self)
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
        # Booleen qui dit si le numéro du Oiseau existe ou non
        valider_oiseau = valider_oiseau_liste(ois.Numero)
        if ois.Numero != 0 and ois.Poid != 0 and ois.Taille != 0 and ois.Longevite != 0 and ois.Nbdoigts != 0 and valider_oiseau is True:
            decouvre = False
            for ois in ls_Oiseau:
                # Chercher dans la lise pour un Oiseau avec les mêmes informations
                if ois.Numero == self.lineEdit_numero_oiseau.text() and ois.Poid == self.lineEdit_poids_oiseau.text() \
                        and ois.Taille == self.lineEdit_taille_oiseau.text() and ois.Longevite == self.lineEdit_longevite_oiseau.text() \
                        and ois.Diet == self.comboBox_diet_oiseau.currentText() and ois.Couleur_plumes == self.comboBox_couleur_plumes.currentText() \
                        and ois.Couleur_bec == self.comboBox_couleur_bec.currentText() and ois.Longueurbec == self.lineEdit_longueur_bec_oiseau.text() \
                        and ois.Enclos == self.comboBox_enclos_oiseau.currentText():
                    # Supprimer le Oiseau de la liste
                    decouvre = True
                    ls_Oiseau.remove(ois)
                    break
            # Si le Oiseau n'existe pas dans la liste - Afficher un message d'erreur (le même que celui pour erreur normale)
            if not decouvre:
                self.label_erreur_numero_oiseau.setVisible(True)
            else:
                # Réafficher dans le textBroser la nouvelle lise qui ne contient pas l'étudient supprimé
                self.textBrowser_oiseau.clear()
                for ois in ls_Oiseau:
                    self.textBrowser_oiseau.append(ois.__str__())
                # Réinitialiser le lineEdit numéro
                self.lineEdit_numero_oiseau.clear()
        # Si le numéro du Oiseau = valid MAIS existe déja - On ne peux pas l'ajouter
        if valider_oiseau is False and ois.Numero != "":
            # Effacer le lineEdit du numéro + afficher le message d'erreur
            self.lineEdit_numero_oiseau.clear()
            self.label_erreur_numero_oiseau.setVisible(True)
        # Si le numéro d'étudiant est invalide, effacer le lineEdit du numéro étudiant  et afficher un message d'erreur
        if ois.Numero == "":
            self.lineEdit_numero_oiseau.clear()
            self.label_erreur_numero_oiseau.setVisible(True)

####################################################################################
# TODO Bouton Afficher
####################################################################################
    @pyqtSlot()
    def on_pushButton_quitter_oiseau_clicked(self):
        self.close()
