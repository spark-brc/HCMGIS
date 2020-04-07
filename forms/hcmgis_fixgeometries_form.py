# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hcmgis_fixgeometries_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_hcmgis_fixgeometries_form(object):
    def setupUi(self, hcmgis_fixgeometries_form):
        hcmgis_fixgeometries_form.setObjectName("hcmgis_fixgeometries_form")
        hcmgis_fixgeometries_form.setWindowModality(QtCore.Qt.ApplicationModal)
        hcmgis_fixgeometries_form.setEnabled(True)
        hcmgis_fixgeometries_form.resize(341, 162)
        hcmgis_fixgeometries_form.setMouseTracking(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(hcmgis_fixgeometries_form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LblInput = QtWidgets.QLabel(hcmgis_fixgeometries_form)
        self.LblInput.setObjectName("LblInput")
        self.verticalLayout.addWidget(self.LblInput)
        self.CboInput = QgsMapLayerComboBox(hcmgis_fixgeometries_form)
        self.CboInput.setObjectName("CboInput")
        self.verticalLayout.addWidget(self.CboInput)
        self.LblOutput_3 = QtWidgets.QLabel(hcmgis_fixgeometries_form)
        self.LblOutput_3.setObjectName("LblOutput_3")
        self.verticalLayout.addWidget(self.LblOutput_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.LinOutput = QtWidgets.QLineEdit(hcmgis_fixgeometries_form)
        self.LinOutput.setEnabled(True)
        self.LinOutput.setMouseTracking(True)
        self.LinOutput.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.LinOutput.setAcceptDrops(False)
        self.LinOutput.setText("")
        self.LinOutput.setReadOnly(False)
        self.LinOutput.setObjectName("LinOutput")
        self.gridLayout.addWidget(self.LinOutput, 0, 0, 1, 1)
        self.BtnOutput = QtWidgets.QPushButton(hcmgis_fixgeometries_form)
        self.BtnOutput.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.BtnOutput.setFont(font)
        self.BtnOutput.setObjectName("BtnOutput")
        self.gridLayout.addWidget(self.BtnOutput, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.BtnOKCancel = QtWidgets.QDialogButtonBox(hcmgis_fixgeometries_form)
        self.BtnOKCancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.BtnOKCancel.setObjectName("BtnOKCancel")
        self.verticalLayout.addWidget(self.BtnOKCancel)

        self.retranslateUi(hcmgis_fixgeometries_form)
        self.BtnOKCancel.accepted.connect(hcmgis_fixgeometries_form.accept)
        self.BtnOKCancel.rejected.connect(hcmgis_fixgeometries_form.reject)
        QtCore.QMetaObject.connectSlotsByName(hcmgis_fixgeometries_form)

    def retranslateUi(self, hcmgis_fixgeometries_form):
        _translate = QtCore.QCoreApplication.translate
        hcmgis_fixgeometries_form.setWindowTitle(_translate("hcmgis_fixgeometries_form", "Fix Geometries"))
        self.LblInput.setText(_translate("hcmgis_fixgeometries_form", "Input Layer"))
        self.LblOutput_3.setText(_translate("hcmgis_fixgeometries_form", "Output Shapefile"))
        self.BtnOutput.setText(_translate("hcmgis_fixgeometries_form", "Browse..."))

from qgsmaplayercombobox import QgsMapLayerComboBox

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hcmgis_fixgeometries_form = QtWidgets.QDialog()
    ui = Ui_hcmgis_fixgeometries_form()
    ui.setupUi(hcmgis_fixgeometries_form)
    hcmgis_fixgeometries_form.show()
    sys.exit(app.exec_())

