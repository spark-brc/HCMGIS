# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hcmgis_opendata_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_hcmgis_opendata_form(object):
    def setupUi(self, hcmgis_opendata_form):
        hcmgis_opendata_form.setObjectName("hcmgis_opendata_form")
        hcmgis_opendata_form.setWindowModality(QtCore.Qt.ApplicationModal)
        hcmgis_opendata_form.setEnabled(True)
        hcmgis_opendata_form.resize(593, 619)
        hcmgis_opendata_form.setMouseTracking(False)
        self.gridLayout_2 = QtWidgets.QGridLayout(hcmgis_opendata_form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.BtnApplyClose = QtWidgets.QDialogButtonBox(hcmgis_opendata_form)
        self.BtnApplyClose.setOrientation(QtCore.Qt.Horizontal)
        self.BtnApplyClose.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Close)
        self.BtnApplyClose.setObjectName("BtnApplyClose")
        self.gridLayout_2.addWidget(self.BtnApplyClose, 10, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ChkSaveShapefile = QtWidgets.QCheckBox(hcmgis_opendata_form)
        self.ChkSaveShapefile.setObjectName("ChkSaveShapefile")
        self.gridLayout.addWidget(self.ChkSaveShapefile, 18, 0, 1, 2)
        self.TxtTitle = QtWidgets.QPlainTextEdit(hcmgis_opendata_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TxtTitle.sizePolicy().hasHeightForWidth())
        self.TxtTitle.setSizePolicy(sizePolicy)
        self.TxtTitle.setMaximumSize(QtCore.QSize(16777215, 80))
        self.TxtTitle.setReadOnly(True)
        self.TxtTitle.setObjectName("TxtTitle")
        self.gridLayout.addWidget(self.TxtTitle, 15, 0, 1, 1)
        self.LblTitle = QtWidgets.QLabel(hcmgis_opendata_form)
        self.LblTitle.setObjectName("LblTitle")
        self.gridLayout.addWidget(self.LblTitle, 14, 0, 1, 1)
        self.label = QtWidgets.QLabel(hcmgis_opendata_form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 13, 0, 1, 1)
        self.BtnOutputFolder = QtWidgets.QPushButton(hcmgis_opendata_form)
        self.BtnOutputFolder.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnOutputFolder.sizePolicy().hasHeightForWidth())
        self.BtnOutputFolder.setSizePolicy(sizePolicy)
        self.BtnOutputFolder.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.BtnOutputFolder.setFont(font)
        self.BtnOutputFolder.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BtnOutputFolder.setObjectName("BtnOutputFolder")
        self.gridLayout.addWidget(self.BtnOutputFolder, 19, 2, 1, 1)
        self.LinOutputFolder = QtWidgets.QLineEdit(hcmgis_opendata_form)
        self.LinOutputFolder.setEnabled(False)
        self.LinOutputFolder.setMouseTracking(True)
        self.LinOutputFolder.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.LinOutputFolder.setAcceptDrops(False)
        self.LinOutputFolder.setText("")
        self.LinOutputFolder.setReadOnly(True)
        self.LinOutputFolder.setObjectName("LinOutputFolder")
        self.gridLayout.addWidget(self.LinOutputFolder, 19, 0, 1, 2)
        self.cboServerName = QtWidgets.QComboBox(hcmgis_opendata_form)
        self.cboServerName.setObjectName("cboServerName")
        self.gridLayout.addWidget(self.cboServerName, 13, 1, 1, 2)
        self.TxtAbstract = QtWidgets.QPlainTextEdit(hcmgis_opendata_form)
        self.TxtAbstract.setMaximumSize(QtCore.QSize(16777215, 80))
        self.TxtAbstract.setReadOnly(True)
        self.TxtAbstract.setObjectName("TxtAbstract")
        self.gridLayout.addWidget(self.TxtAbstract, 15, 1, 1, 2)
        self.TblWFSLayers = QtWidgets.QTableWidget(hcmgis_opendata_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TblWFSLayers.sizePolicy().hasHeightForWidth())
        self.TblWFSLayers.setSizePolicy(sizePolicy)
        self.TblWFSLayers.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TblWFSLayers.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.TblWFSLayers.setObjectName("TblWFSLayers")
        self.TblWFSLayers.setColumnCount(2)
        self.TblWFSLayers.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TblWFSLayers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TblWFSLayers.setHorizontalHeaderItem(1, item)
        self.TblWFSLayers.horizontalHeader().setCascadingSectionResizes(False)
        self.TblWFSLayers.horizontalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.TblWFSLayers, 17, 0, 1, 3)
        self.CboFormat = QtWidgets.QComboBox(hcmgis_opendata_form)
        self.CboFormat.setEnabled(False)
        self.CboFormat.setMaximumSize(QtCore.QSize(100, 16777215))
        self.CboFormat.setObjectName("CboFormat")
        self.CboFormat.addItem("")
        self.CboFormat.addItem("")
        self.CboFormat.addItem("")
        self.CboFormat.addItem("")
        self.CboFormat.addItem("")
        self.CboFormat.addItem("")
        self.CboFormat.addItem("")
        self.CboFormat.addItem("")
        self.gridLayout.addWidget(self.CboFormat, 20, 2, 1, 1)
        self.LblFormat = QtWidgets.QLabel(hcmgis_opendata_form)
        self.LblFormat.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LblFormat.setObjectName("LblFormat")
        self.gridLayout.addWidget(self.LblFormat, 20, 0, 1, 2)
        self.lblAbstract = QtWidgets.QLabel(hcmgis_opendata_form)
        self.lblAbstract.setObjectName("lblAbstract")
        self.gridLayout.addWidget(self.lblAbstract, 14, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(hcmgis_opendata_form)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 16, 0, 1, 3)
        self.status = QtWidgets.QProgressBar(hcmgis_opendata_form)
        self.status.setProperty("value", 24)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.status, 22, 0, 1, 3)
        self.LblSattus = QtWidgets.QLabel(hcmgis_opendata_form)
        self.LblSattus.setText("")
        self.LblSattus.setObjectName("LblSattus")
        self.gridLayout.addWidget(self.LblSattus, 21, 0, 1, 3)
        self.LblServerType = QtWidgets.QLabel(hcmgis_opendata_form)
        self.LblServerType.setObjectName("LblServerType")
        self.gridLayout.addWidget(self.LblServerType, 0, 0, 1, 1)
        self.cboServerType = QtWidgets.QComboBox(hcmgis_opendata_form)
        self.cboServerType.setObjectName("cboServerType")
        self.gridLayout.addWidget(self.cboServerType, 0, 1, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 9, 0, 1, 2)

        self.retranslateUi(hcmgis_opendata_form)
        self.BtnApplyClose.accepted.connect(hcmgis_opendata_form.accept)
        self.BtnApplyClose.rejected.connect(hcmgis_opendata_form.reject)
        QtCore.QMetaObject.connectSlotsByName(hcmgis_opendata_form)

    def retranslateUi(self, hcmgis_opendata_form):
        _translate = QtCore.QCoreApplication.translate
        hcmgis_opendata_form.setWindowTitle(_translate("hcmgis_opendata_form", "HCMGIS OpenData"))
        self.ChkSaveShapefile.setText(_translate("hcmgis_opendata_form", "Save layers to disk"))
        self.LblTitle.setText(_translate("hcmgis_opendata_form", "Title"))
        self.label.setText(_translate("hcmgis_opendata_form", "Server Name"))
        self.BtnOutputFolder.setText(_translate("hcmgis_opendata_form", "Browse..."))
        self.TblWFSLayers.setSortingEnabled(True)
        item = self.TblWFSLayers.horizontalHeaderItem(0)
        item.setText(_translate("hcmgis_opendata_form", "Name"))
        item = self.TblWFSLayers.horizontalHeaderItem(1)
        item.setText(_translate("hcmgis_opendata_form", "Title"))
        self.CboFormat.setItemText(0, _translate("hcmgis_opendata_form", "SHAPE-ZIP"))
        self.CboFormat.setItemText(1, _translate("hcmgis_opendata_form", "JSON"))
        self.CboFormat.setItemText(2, _translate("hcmgis_opendata_form", "KML"))
        self.CboFormat.setItemText(3, _translate("hcmgis_opendata_form", "CSV"))
        self.CboFormat.setItemText(4, _translate("hcmgis_opendata_form", "XLSX"))
        self.CboFormat.setItemText(5, _translate("hcmgis_opendata_form", "XLS"))
        self.CboFormat.setItemText(6, _translate("hcmgis_opendata_form", "GML3"))
        self.CboFormat.setItemText(7, _translate("hcmgis_opendata_form", "GML2"))
        self.LblFormat.setText(_translate("hcmgis_opendata_form", "Format"))
        self.lblAbstract.setText(_translate("hcmgis_opendata_form", "Abstract"))
        self.label_4.setText(_translate("hcmgis_opendata_form", "WFS layers"))
        self.LblServerType.setText(_translate("hcmgis_opendata_form", "Server Type"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hcmgis_opendata_form = QtWidgets.QDialog()
    ui = Ui_hcmgis_opendata_form()
    ui.setupUi(hcmgis_opendata_form)
    hcmgis_opendata_form.show()
    sys.exit(app.exec_())

