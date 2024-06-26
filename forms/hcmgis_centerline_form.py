# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hcmgis_centerline_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_hcmgis_centerline_form(object):
    def setupUi(self, hcmgis_centerline_form):
        hcmgis_centerline_form.setObjectName("hcmgis_centerline_form")
        hcmgis_centerline_form.setWindowModality(QtCore.Qt.ApplicationModal)
        hcmgis_centerline_form.setEnabled(True)
        hcmgis_centerline_form.resize(467, 394)
        hcmgis_centerline_form.setMouseTracking(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(hcmgis_centerline_form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox = QgsDoubleSpinBox(hcmgis_centerline_form)
        self.spinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBox.setDecimals(1)
        self.spinBox.setMinimum(0.1)
        self.spinBox.setMaximum(10.0)
        self.spinBox.setSingleStep(0.1)
        self.spinBox.setProperty("value", 0.5)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 3, 0, 1, 2)
        self.lblsurround = QtWidgets.QLabel(hcmgis_centerline_form)
        self.lblsurround.setObjectName("lblsurround")
        self.gridLayout.addWidget(self.lblsurround, 5, 0, 1, 2)
        self.output_file_name = QgsFileWidget(hcmgis_centerline_form)
        self.output_file_name.setObjectName("output_file_name")
        self.gridLayout.addWidget(self.output_file_name, 9, 0, 1, 2)
        self.LblInput = QtWidgets.QLabel(hcmgis_centerline_form)
        self.LblInput.setObjectName("LblInput")
        self.gridLayout.addWidget(self.LblInput, 0, 0, 1, 2)
        self.chksurround = QtWidgets.QCheckBox(hcmgis_centerline_form)
        self.chksurround.setChecked(False)
        self.chksurround.setObjectName("chksurround")
        self.gridLayout.addWidget(self.chksurround, 4, 0, 1, 2)
        self.status = QtWidgets.QProgressBar(hcmgis_centerline_form)
        self.status.setProperty("value", 24)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.status, 11, 0, 1, 2)
        self.CboInput = QgsMapLayerComboBox(hcmgis_centerline_form)
        self.CboInput.setProperty("showCrs", True)
        self.CboInput.setObjectName("CboInput")
        self.gridLayout.addWidget(self.CboInput, 1, 0, 1, 2)
        self.LblOutput = QtWidgets.QLabel(hcmgis_centerline_form)
        self.LblOutput.setObjectName("LblOutput")
        self.gridLayout.addWidget(self.LblOutput, 8, 0, 1, 2)
        self.label = QtWidgets.QLabel(hcmgis_centerline_form)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 7, 0, 1, 2)
        self.LblStatus = QtWidgets.QLabel(hcmgis_centerline_form)
        self.LblStatus.setText("")
        self.LblStatus.setObjectName("LblStatus")
        self.gridLayout.addWidget(self.LblStatus, 10, 0, 1, 2)
        self.LblInput_2 = QtWidgets.QLabel(hcmgis_centerline_form)
        self.LblInput_2.setObjectName("LblInput_2")
        self.gridLayout.addWidget(self.LblInput_2, 2, 0, 1, 2)
        self.distance = QgsDoubleSpinBox(hcmgis_centerline_form)
        self.distance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.distance.setDecimals(1)
        self.distance.setMinimum(0.1)
        self.distance.setSingleStep(0.1)
        self.distance.setProperty("value", 1.0)
        self.distance.setObjectName("distance")
        self.gridLayout.addWidget(self.distance, 6, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.BtnApplyClose = QtWidgets.QDialogButtonBox(hcmgis_centerline_form)
        self.BtnApplyClose.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Close)
        self.BtnApplyClose.setObjectName("BtnApplyClose")
        self.verticalLayout.addWidget(self.BtnApplyClose)

        self.retranslateUi(hcmgis_centerline_form)
        self.BtnApplyClose.accepted.connect(hcmgis_centerline_form.accept)
        self.BtnApplyClose.rejected.connect(hcmgis_centerline_form.reject)
        QtCore.QMetaObject.connectSlotsByName(hcmgis_centerline_form)

    def retranslateUi(self, hcmgis_centerline_form):
        _translate = QtCore.QCoreApplication.translate
        hcmgis_centerline_form.setWindowTitle(_translate("hcmgis_centerline_form", "Centerline in the gaps between polygons"))
        self.lblsurround.setText(_translate("hcmgis_centerline_form", "Distance to the bounding box of polygon (m)"))
        self.LblInput.setText(_translate("hcmgis_centerline_form", "Input Polygon (Ex: Block of Buildings)"))
        self.chksurround.setText(_translate("hcmgis_centerline_form", "Also create lines surrounding the polygon"))
        self.LblOutput.setText(_translate("hcmgis_centerline_form", "Output"))
        self.label.setText(_translate("hcmgis_centerline_form", "(Notice: Output should be refined after running)"))
        self.LblInput_2.setText(_translate("hcmgis_centerline_form", "Density (m)"))
from qgsdoublespinbox import QgsDoubleSpinBox
from qgsfilewidget import QgsFileWidget
from qgsmaplayercombobox import QgsMapLayerComboBox


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hcmgis_centerline_form = QtWidgets.QDialog()
    ui = Ui_hcmgis_centerline_form()
    ui.setupUi(hcmgis_centerline_form)
    hcmgis_centerline_form.show()
    sys.exit(app.exec_())
