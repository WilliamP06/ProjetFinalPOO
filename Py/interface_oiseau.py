# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oiseau.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(491, 717)
        self.label_poids_oiseau = QtWidgets.QLabel(Dialog)
        self.label_poids_oiseau.setGeometry(QtCore.QRect(10, 140, 211, 21))
        self.label_poids_oiseau.setObjectName("label_poids_oiseau")
        self.label_taille_oiseau = QtWidgets.QLabel(Dialog)
        self.label_taille_oiseau.setGeometry(QtCore.QRect(10, 220, 211, 21))
        self.label_taille_oiseau.setObjectName("label_taille_oiseau")
        self.label_longevite_oiseau = QtWidgets.QLabel(Dialog)
        self.label_longevite_oiseau.setGeometry(QtCore.QRect(10, 300, 211, 21))
        self.label_longevite_oiseau.setObjectName("label_longevite_oiseau")
        self.label_diet_oiseau = QtWidgets.QLabel(Dialog)
        self.label_diet_oiseau.setGeometry(QtCore.QRect(270, 60, 211, 21))
        self.label_diet_oiseau.setObjectName("label_diet_oiseau")
        self.label_numero_oiseau = QtWidgets.QLabel(Dialog)
        self.label_numero_oiseau.setGeometry(QtCore.QRect(10, 60, 211, 21))
        self.label_numero_oiseau.setObjectName("label_numero_oiseau")
        self.label_longueur_bec = QtWidgets.QLabel(Dialog)
        self.label_longueur_bec.setGeometry(QtCore.QRect(270, 300, 211, 21))
        self.label_longueur_bec.setObjectName("label_longueur_bec")
        self.label_couleur_plumes = QtWidgets.QLabel(Dialog)
        self.label_couleur_plumes.setGeometry(QtCore.QRect(270, 140, 211, 21))
        self.label_couleur_plumes.setObjectName("label_couleur_plumes")
        self.label_couleur_bec = QtWidgets.QLabel(Dialog)
        self.label_couleur_bec.setGeometry(QtCore.QRect(270, 220, 211, 21))
        self.label_couleur_bec.setObjectName("label_couleur_bec")
        self.lineEdit_taille_oiseau = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_taille_oiseau.setGeometry(QtCore.QRect(10, 250, 211, 41))
        self.lineEdit_taille_oiseau.setObjectName("lineEdit_taille_oiseau")
        self.comboBox_enclos_oiseau = QtWidgets.QComboBox(Dialog)
        self.comboBox_enclos_oiseau.setGeometry(QtCore.QRect(270, 410, 211, 41))
        self.comboBox_enclos_oiseau.setObjectName("comboBox_enclos_oiseau")
        self.lineEdit_poids_oiseau = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_poids_oiseau.setGeometry(QtCore.QRect(10, 170, 211, 41))
        self.lineEdit_poids_oiseau.setObjectName("lineEdit_poids_oiseau")
        self.lineEdit_longevite_oiseau = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_longevite_oiseau.setGeometry(QtCore.QRect(10, 330, 211, 41))
        self.lineEdit_longevite_oiseau.setObjectName("lineEdit_longevite_oiseau")
        self.comboBox_couleur_plumes = QtWidgets.QComboBox(Dialog)
        self.comboBox_couleur_plumes.setGeometry(QtCore.QRect(270, 170, 211, 41))
        self.comboBox_couleur_plumes.setObjectName("comboBox_couleur_plumes")
        self.comboBox_couleur_bec = QtWidgets.QComboBox(Dialog)
        self.comboBox_couleur_bec.setGeometry(QtCore.QRect(270, 250, 211, 41))
        self.comboBox_couleur_bec.setObjectName("comboBox_couleur_bec")
        self.pushButton_modifier_oiseau = QtWidgets.QPushButton(Dialog)
        self.pushButton_modifier_oiseau.setGeometry(QtCore.QRect(130, 380, 111, 51))
        self.pushButton_modifier_oiseau.setObjectName("pushButton_modifier_oiseau")
        self.pushButton_supprimer_oiseau = QtWidgets.QPushButton(Dialog)
        self.pushButton_supprimer_oiseau.setGeometry(QtCore.QRect(10, 440, 111, 51))
        self.pushButton_supprimer_oiseau.setObjectName("pushButton_supprimer_oiseau")
        self.comboBox_diet_oiseau = QtWidgets.QComboBox(Dialog)
        self.comboBox_diet_oiseau.setGeometry(QtCore.QRect(270, 90, 211, 41))
        self.comboBox_diet_oiseau.setObjectName("comboBox_diet_oiseau")
        self.pushButton_quitter_oiseau = QtWidgets.QPushButton(Dialog)
        self.pushButton_quitter_oiseau.setGeometry(QtCore.QRect(400, 481, 81, 20))
        self.pushButton_quitter_oiseau.setObjectName("pushButton_quitter_oiseau")
        self.lineEdit_numero_oiseau = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_numero_oiseau.setGeometry(QtCore.QRect(10, 90, 211, 41))
        self.lineEdit_numero_oiseau.setObjectName("lineEdit_numero_oiseau")
        self.pushButton_ajouter_oiseau = QtWidgets.QPushButton(Dialog)
        self.pushButton_ajouter_oiseau.setGeometry(QtCore.QRect(10, 380, 111, 51))
        self.pushButton_ajouter_oiseau.setObjectName("pushButton_ajouter_oiseau")
        self.label_enclos_oiseau = QtWidgets.QLabel(Dialog)
        self.label_enclos_oiseau.setGeometry(QtCore.QRect(270, 380, 211, 21))
        self.label_enclos_oiseau.setObjectName("label_enclos_oiseau")
        self.label_oiseau = QtWidgets.QLabel(Dialog)
        self.label_oiseau.setGeometry(QtCore.QRect(10, 10, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_oiseau.setFont(font)
        self.label_oiseau.setObjectName("label_oiseau")
        self.label_erreur_numero_oiseau = QtWidgets.QLabel(Dialog)
        self.label_erreur_numero_oiseau.setGeometry(QtCore.QRect(10, 70, 221, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_erreur_numero_oiseau.setPalette(palette)
        self.label_erreur_numero_oiseau.setAutoFillBackground(False)
        self.label_erreur_numero_oiseau.setObjectName("label_erreur_numero_oiseau")
        self.label_erreur_longevite_oiseau = QtWidgets.QLabel(Dialog)
        self.label_erreur_longevite_oiseau.setGeometry(QtCore.QRect(10, 310, 211, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_erreur_longevite_oiseau.setPalette(palette)
        self.label_erreur_longevite_oiseau.setAutoFillBackground(False)
        self.label_erreur_longevite_oiseau.setObjectName("label_erreur_longevite_oiseau")
        self.label_erreur_poids_oiseau = QtWidgets.QLabel(Dialog)
        self.label_erreur_poids_oiseau.setGeometry(QtCore.QRect(10, 150, 211, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_erreur_poids_oiseau.setPalette(palette)
        self.label_erreur_poids_oiseau.setAutoFillBackground(False)
        self.label_erreur_poids_oiseau.setObjectName("label_erreur_poids_oiseau")
        self.label_erreur_taille_oiseau = QtWidgets.QLabel(Dialog)
        self.label_erreur_taille_oiseau.setGeometry(QtCore.QRect(10, 230, 211, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_erreur_taille_oiseau.setPalette(palette)
        self.label_erreur_taille_oiseau.setAutoFillBackground(False)
        self.label_erreur_taille_oiseau.setObjectName("label_erreur_taille_oiseau")
        self.pushButton_afficher_oiseau = QtWidgets.QPushButton(Dialog)
        self.pushButton_afficher_oiseau.setGeometry(QtCore.QRect(130, 440, 111, 51))
        self.pushButton_afficher_oiseau.setObjectName("pushButton_afficher_oiseau")
        self.textBrowser_oiseau = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_oiseau.setGeometry(QtCore.QRect(10, 500, 471, 192))
        self.textBrowser_oiseau.setObjectName("textBrowser_oiseau")
        self.lineEdit_longueur_bec_oiseau = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_longueur_bec_oiseau.setGeometry(QtCore.QRect(270, 330, 211, 41))
        self.lineEdit_longueur_bec_oiseau.setObjectName("lineEdit_longueur_bec_oiseau")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_poids_oiseau.setText(_translate("Dialog", "Poids (lbs)"))
        self.label_taille_oiseau.setText(_translate("Dialog", "Taille (m)"))
        self.label_longevite_oiseau.setText(_translate("Dialog", "Espérence de vie (années)"))
        self.label_diet_oiseau.setText(_translate("Dialog", "Diet"))
        self.label_numero_oiseau.setText(_translate("Dialog", "Numéro du oiseau"))
        self.label_longueur_bec.setText(_translate("Dialog", "Longueur du bec (cm)"))
        self.label_couleur_plumes.setText(_translate("Dialog", "Couleur des plumes"))
        self.label_couleur_bec.setText(_translate("Dialog", "Couleur du bec"))
        self.pushButton_modifier_oiseau.setText(_translate("Dialog", "Modifier"))
        self.pushButton_supprimer_oiseau.setText(_translate("Dialog", "Supprimer"))
        self.pushButton_quitter_oiseau.setText(_translate("Dialog", "Quitter"))
        self.pushButton_ajouter_oiseau.setText(_translate("Dialog", "Ajouter"))
        self.label_enclos_oiseau.setText(_translate("Dialog", "Type d\'enclos"))
        self.label_oiseau.setText(_translate("Dialog", "Oiseau"))
        self.label_erreur_numero_oiseau.setText(_translate("Dialog", "Erreur! Ce numéro est invalide ou déja pris."))
        self.label_erreur_longevite_oiseau.setText(_translate("Dialog", "Erreur! cette longévité n\'est pas valide"))
        self.label_erreur_poids_oiseau.setText(_translate("Dialog", "Erreur! ce poid n\'est pas valide"))
        self.label_erreur_taille_oiseau.setText(_translate("Dialog", "Erreur! cette taille n\'est pas valide"))
        self.pushButton_afficher_oiseau.setText(_translate("Dialog", "Afficher"))