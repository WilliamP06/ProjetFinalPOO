# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enclos.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(491, 421)
        self.comboBox_enclos_enclos = QtWidgets.QComboBox(Dialog)
        self.comboBox_enclos_enclos.setGeometry(QtCore.QRect(270, 90, 211, 41))
        self.comboBox_enclos_enclos.setObjectName("comboBox_enclos_enclos")
        self.comboBox_enclos_enclos.addItem("")
        self.comboBox_enclos_enclos.addItem("")
        self.comboBox_enclos_enclos.addItem("")
        self.comboBox_enclos_enclos.addItem("")
        self.comboBox_enclos_enclos.addItem("")
        self.comboBox_enclos_enclos.addItem("")
        self.comboBox_enclos_enclos.addItem("")
        self.comboBox_enclos_enclos.addItem("")
        self.comboBox_enclos_enclos.addItem("")
        self.comboBox_enclos_enclos.addItem("")
        self.comboBox_enclos_enclos.addItem("")
        self.comboBox_enclos_enclos.addItem("")
        self.label_numero_enclos = QtWidgets.QLabel(Dialog)
        self.label_numero_enclos.setGeometry(QtCore.QRect(10, 60, 211, 21))
        self.label_numero_enclos.setObjectName("label_numero_enclos")
        self.label_enclos_enclos_2 = QtWidgets.QLabel(Dialog)
        self.label_enclos_enclos_2.setGeometry(QtCore.QRect(10, 10, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_enclos_enclos_2.setFont(font)
        self.label_enclos_enclos_2.setObjectName("label_enclos_enclos_2")
        self.label_erreur_numero_enclos = QtWidgets.QLabel(Dialog)
        self.label_erreur_numero_enclos.setGeometry(QtCore.QRect(10, 70, 221, 21))
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
        self.label_erreur_numero_enclos.setPalette(palette)
        self.label_erreur_numero_enclos.setAutoFillBackground(False)
        self.label_erreur_numero_enclos.setObjectName("label_erreur_numero_enclos")
        self.lineEdit_numero_enclos = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_numero_enclos.setGeometry(QtCore.QRect(10, 90, 211, 41))
        self.lineEdit_numero_enclos.setObjectName("lineEdit_numero_enclos")
        self.label_enclos_enclos = QtWidgets.QLabel(Dialog)
        self.label_enclos_enclos.setGeometry(QtCore.QRect(270, 60, 211, 21))
        self.label_enclos_enclos.setObjectName("label_enclos_enclos")
        self.textBrowser_enclos = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_enclos.setGeometry(QtCore.QRect(10, 219, 471, 192))
        self.textBrowser_enclos.setObjectName("textBrowser_enclos")
        self.pushButton_quitter_enclos = QtWidgets.QPushButton(Dialog)
        self.pushButton_quitter_enclos.setGeometry(QtCore.QRect(400, 200, 81, 20))
        self.pushButton_quitter_enclos.setObjectName("pushButton_quitter_enclos")
        self.pushButton_supprimer_enclos = QtWidgets.QPushButton(Dialog)
        self.pushButton_supprimer_enclos.setGeometry(QtCore.QRect(250, 140, 111, 51))
        self.pushButton_supprimer_enclos.setObjectName("pushButton_supprimer_enclos")
        self.pushButton_modifier_enclos = QtWidgets.QPushButton(Dialog)
        self.pushButton_modifier_enclos.setGeometry(QtCore.QRect(130, 140, 111, 51))
        self.pushButton_modifier_enclos.setObjectName("pushButton_modifier_enclos")
        self.pushButton_ajouter_enclos = QtWidgets.QPushButton(Dialog)
        self.pushButton_ajouter_enclos.setGeometry(QtCore.QRect(10, 140, 111, 51))
        self.pushButton_ajouter_enclos.setObjectName("pushButton_ajouter_enclos")
        self.pushButton_afficher_enclos = QtWidgets.QPushButton(Dialog)
        self.pushButton_afficher_enclos.setGeometry(QtCore.QRect(370, 140, 111, 51))
        self.pushButton_afficher_enclos.setObjectName("pushButton_afficher_enclos")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox_enclos_enclos.setItemText(0, _translate("Dialog", "Petit enclos"))
        self.comboBox_enclos_enclos.setItemText(1, _translate("Dialog", "Moyen enclos"))
        self.comboBox_enclos_enclos.setItemText(2, _translate("Dialog", "Grand enclos"))
        self.comboBox_enclos_enclos.setItemText(3, _translate("Dialog", "Très grand enclos"))
        self.comboBox_enclos_enclos.setItemText(4, _translate("Dialog", "Petite cage"))
        self.comboBox_enclos_enclos.setItemText(5, _translate("Dialog", "Moyenne cage"))
        self.comboBox_enclos_enclos.setItemText(6, _translate("Dialog", "Grande cage"))
        self.comboBox_enclos_enclos.setItemText(7, _translate("Dialog", "Très grande cage"))
        self.comboBox_enclos_enclos.setItemText(8, _translate("Dialog", "Petit aquarium"))
        self.comboBox_enclos_enclos.setItemText(9, _translate("Dialog", "Moyen aquarium"))
        self.comboBox_enclos_enclos.setItemText(10, _translate("Dialog", "Grand aquarium"))
        self.comboBox_enclos_enclos.setItemText(11, _translate("Dialog", "Très grand aquarium"))
        self.label_numero_enclos.setText(_translate("Dialog", "Numéro de l\'enclos"))
        self.label_enclos_enclos_2.setText(_translate("Dialog", "Enclos"))
        self.label_erreur_numero_enclos.setText(_translate("Dialog", "Erreur! Ce numéro est invalide ou déja pris."))
        self.label_enclos_enclos.setText(_translate("Dialog", "Type d\'enclos"))
        self.pushButton_quitter_enclos.setText(_translate("Dialog", "Quitter"))
        self.pushButton_supprimer_enclos.setText(_translate("Dialog", "Supprimer"))
        self.pushButton_modifier_enclos.setText(_translate("Dialog", "Modifier"))
        self.pushButton_ajouter_enclos.setText(_translate("Dialog", "Ajouter"))
        self.pushButton_afficher_enclos.setText(_translate("Dialog", "Afficher"))