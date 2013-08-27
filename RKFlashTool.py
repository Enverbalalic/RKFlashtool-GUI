#!/usr/bin/env python3

import subprocess
import sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):

        def Flash_Backup(self):
            FlashBackupDetector = Form.sender()

            if(FlashBackupDetector.objectName() == "FlashButton"):
                if(self.LoaderCheckBox.checkState() == 2):
                    process = subprocess.Popen("sudo ./RKFlashTool w "+ self.LoaderOffset.text() + " " + self.LoaderPartitionSize.text() + " <" + self.LoaderLocationDisplay.text(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    out, err = process.communicate()
                    self.LogText.append(out.decode("ascii"))
                    self.LogText.append(err.decode("ascii"))

                if(self.ParameterCheckBox.checkState() == 2):
                    process = subprocess.Popen("sudo ./RKFlashTool w "+ self.ParameterOffset.text() + " " + self.ParameterPartitionSize.text() + " <" + self.ParameterLocationDisplay.text(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    out, err = process.communicate()
                    self.LogText.append(out.decode("ascii"))
                    self.LogText.append(err.decode("ascii"))

                if(self.MiscCheckBox.checkState() == 2):
                    process = subprocess.Popen("sudo ./RKFlashTool w "+ self.MiscOffset.text() + " " + self.MiscPartitionSize.text() + " <" + self.MiscLocationDisplay.text(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    out, err = process.communicate()
                    self.LogText.append(out.decode("ascii"))
                    self.LogText.append(err.decode("ascii"))

                if(self.KernelCheckBox.checkState() == 2):
                    process = subprocess.Popen("sudo ./RKFlashTool w "+ self.KernelOffset.text() + " " + self.KernelPartitionSize.text() + " <" + self.MiscLocationDisplay.text(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    out, err = process.communicate()
                    self.LogText.append(out.decode("ascii"))
                    self.LogText.append(err.decode("ascii"))

                if(self.RamdiskCheckBox.checkState() == 2):
                    process = subprocess.Popen("sudo ./RKFlashTool w "+ self.RamdiskOffset.text() + " " + self.RamdiskPartitionSize.text() + " <" + self.RamdiskLocationDisplay.text(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    out, err = process.communicate()
                    self.LogText.append(out.decode("ascii"))
                    self.LogText.append(err.decode("ascii"))

                if(self.RecoveryCheckBox.checkState() == 2):
                    process = subprocess.Popen("sudo ./RKFlashTool w "+ self.RecoveryOffset.text() + " " + self.RecoveryPartitionSize.text() + " <" + self.RecoveryLocationDisplay.text(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    out, err = process.communicate()
                    self.LogText.append(out.decode("ascii"))
                    self.LogText.append(err.decode("ascii"))

                if(self.SystemCheckBox.checkState() == 2):
                    process = subprocess.Popen("sudo ./RKFlashTool w "+ self.SystemOffset.text() + " " + self.SystemPartitionSize.text() + " <" + self.SystemLocationDisplay.text(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    out, err = process.communicate()
                    self.LogText.append(out.decode("ascii"))
                    self.LogText.append(err.decode("ascii"))

            if(FlashBackupDetector.objectName() == "BackupButton"):
                if(self.LoaderCheckBox.checkState() == 2):
                    process = subprocess.Popen("sudo ./RKFlashTool r "+ self.LoaderOffset.text() + " " + self.LoaderPartitionSize.text() + " > " + "loaderBackup.img", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    out, err = process.communicate()
                    self.LogText.append(out.decode("ascii"))
                    self.LogText.append(err.decode("ascii"))

                if(self.ParameterCheckBox.checkState() == 2):
                    process = subprocess.Popen("sudo ./RKFlashTool r "+ self.ParameterOffset.text() + " " + self.ParameterPartitionSize.text() + " > " + "parameterBackup.img", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    out, err = process.communicate()
                    self.LogText.append(out.decode("ascii"))
                    self.LogText.append(err.decode("ascii"))
                
                elif(self.MiscCheckBox.checkState() == 2):
                    process = subprocess.Popen("sudo ./RKFlashTool r "+ self.MiscOffset.text() + " " + self.MiscPartitionSize.text() + " > " + "miscBackup.img", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    out, err = process.communicate()
                    self.LogText.append(out.decode("ascii"))
                    self.LogText.append(err.decode("ascii"))

                if(self.KernelCheckBox.checkState() == 2):
                    process = subprocess.Popen("sudo ./RKFlashTool r "+ self.KernelOffset.text() + " " + self.KernelPartitionSize.text() + " > " + "kernelBackup.img", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    out, err = process.communicate()
                    self.LogText.append(out.decode("ascii"))
                    self.LogText.append(err.decode("ascii"))

                if(self.RamdiskCheckBox.checkState() == 2):
                    process = subprocess.Popen("sudo ./RKFlashTool r "+ self.RamdiskOffset.text() + " " + self.RamdiskPartitionSize.text() + " > " + "ramdiskBackup.img", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    out, err = process.communicate()
                    self.LogText.append(out.decode("ascii"))
                    self.LogText.append(err.decode("ascii"))

                if(self.RecoveryCheckBox.checkState() == 2):
                    process = subprocess.Popen("sudo ./RKFlashTool r "+ self.RecoveryOffset.text() + " " + self.RecoveryPartitionSize.text() + " > " + "recoveryBackup.img", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    out, err = process.communicate()
                    self.LogText.append(out.decode("ascii"))
                    self.LogText.append(err.decode("ascii"))

                if(self.SystemCheckBox.checkState() == 2):
                    process = subprocess.Popen("sudo ./RKFlashTool r "+ self.SystemOffset.text() + " " + self.SystemPartitionSize.text() + " > " + "systemBackup.img", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    out, err = process.communicate()
                    self.LogText.append(out.decode("ascii"))
                    self.LogText.append(err.decode("ascii"))

            if(FlashBackupDetector.objectName() == "ClearButton"):
                self.LogText.setText("")

        def callFlashBackup():
            Flash_Backup(self)

        def getImageLocation(self):
            buttonSignalDetector = Form.sender()
            
            if(buttonSignalDetector.objectName() == "MiscImageBrowse"):
                MiscFilePath = QtGui.QFileDialog.getOpenFileName(Form, "Select misc image", "/home")
                self.MiscLocationDisplay.setText(MiscFilePath)

            elif(buttonSignalDetector.objectName() == "KernelImageBrowse"):
                KernelFilePath = QtGui.QFileDialog.getOpenFileName(Form, "Select kernel image", "/home")
                self.KernelLocationDisplay.setText(KernelFilePath)

            elif(buttonSignalDetector.objectName() == "RamdiskImageBrowse"):
                RamdiskFilePath = QtGui.QFileDialog.getOpenFileName(Form, "Select ramdisk image", "/home")
                self.RamdiskLocationDisplay.setText(RamdiskFilePath)

            elif(buttonSignalDetector.objectName() == "RecoveryImageBrowse"):
                RecoveryFilePath = QtGui.QFileDialog.getOpenFileName(Form, "Select recovery image", "/home")
                self.RecoveryLocationDisplay.setText(RecoveryFilePath)

            elif(buttonSignalDetector.objectName() == "SystemImageBrowse"):
                SystemFilePath = QtGui.QFileDialog.getOpenFileName(Form, "Select system image", "/home")
                self.SystemLocationDisplay.setText(SystemFilePath)

            elif(buttonSignalDetector.objectName() == "ParameterImageBrowse"):
                ParameterFilePath = QtGui.QFileDialog.getOpenFileName(Form, "Select parameter image", "/home")
                self.ParameterLocationDisplay.setText(ParameterFilePath)

            elif(buttonSignalDetector.objectName() == "LoaderImageBrowse"):
                LoaderFilePath = QtGui.QFileDialog.getOpenFileName(Form, "Select loader image", "/home")
                self.LoaderLocationDisplay.setText(LoaderFilePath)

        def callGetImageLocation():
            getImageLocation(self)

        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(842, 660)
        Form.setMinimumSize(QtCore.QSize(842, 660))
        Form.setMaximumSize(QtCore.QSize(842, 660))
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))

        self.MiscCheckBox = QtGui.QCheckBox(Form)
        self.MiscCheckBox.setGeometry(QtCore.QRect(10, 70, 91, 21))
        self.MiscCheckBox.setChecked(True)
        self.MiscCheckBox.setObjectName(_fromUtf8("MiscCheckBox"))

        self.KernelCheckBox = QtGui.QCheckBox(Form)
        self.KernelCheckBox.setGeometry(QtCore.QRect(10, 100, 91, 21))
        self.KernelCheckBox.setChecked(True)
        self.KernelCheckBox.setObjectName(_fromUtf8("KernelCheckBox"))

        self.RecoveryCheckBox = QtGui.QCheckBox(Form)
        self.RecoveryCheckBox.setGeometry(QtCore.QRect(10, 160, 91, 21))
        self.RecoveryCheckBox.setChecked(True)
        self.RecoveryCheckBox.setObjectName(_fromUtf8("RecoveryCheckBox"))

        self.SystemCheckBox = QtGui.QCheckBox(Form)
        self.SystemCheckBox.setGeometry(QtCore.QRect(10, 190, 91, 21))
        self.SystemCheckBox.setChecked(True)
        self.SystemCheckBox.setObjectName(_fromUtf8("SystemCheckBox"))

        self.RamdiskCheckBox = QtGui.QCheckBox(Form)
        self.RamdiskCheckBox.setGeometry(QtCore.QRect(10, 130, 91, 21))
        self.RamdiskCheckBox.setChecked(True)
        self.RamdiskCheckBox.setObjectName(_fromUtf8("RamdiskCheckBox"))

        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 70, 51, 21))
        self.label.setObjectName(_fromUtf8("label"))

        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 100, 51, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 130, 51, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(110, 160, 51, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(110, 190, 51, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.MiscOffset = QtGui.QLineEdit(Form)
        self.MiscOffset.setGeometry(QtCore.QRect(160, 70, 113, 25))
        self.MiscOffset.setObjectName(_fromUtf8("MiscOffset"))

        self.KernelOffset = QtGui.QLineEdit(Form)
        self.KernelOffset.setGeometry(QtCore.QRect(160, 100, 113, 25))
        self.KernelOffset.setObjectName(_fromUtf8("KernelOffset"))

        self.RamdiskOffset = QtGui.QLineEdit(Form)
        self.RamdiskOffset.setGeometry(QtCore.QRect(160, 130, 113, 25))
        self.RamdiskOffset.setObjectName(_fromUtf8("RamdiskOffset"))

        self.RecoveryOffset = QtGui.QLineEdit(Form)
        self.RecoveryOffset.setGeometry(QtCore.QRect(160, 160, 113, 25))
        self.RecoveryOffset.setObjectName(_fromUtf8("RecoveryOffset"))

        self.SystemOffset = QtGui.QLineEdit(Form)
        self.SystemOffset.setGeometry(QtCore.QRect(160, 190, 113, 25))
        self.SystemOffset.setObjectName(_fromUtf8("SystemOffset"))

        self.MiscLocationDisplay = QtGui.QLineEdit(Form)
        self.MiscLocationDisplay.setGeometry(QtCore.QRect(430, 70, 351, 25))
        self.MiscLocationDisplay.setObjectName(_fromUtf8("MiscLocationDisplay"))

        self.KernelLocationDisplay = QtGui.QLineEdit(Form)
        self.KernelLocationDisplay.setGeometry(QtCore.QRect(430, 100, 351, 25))
        self.KernelLocationDisplay.setObjectName(_fromUtf8("KernelLocationDisplay"))

        self.RamdiskLocationDisplay = QtGui.QLineEdit(Form)
        self.RamdiskLocationDisplay.setGeometry(QtCore.QRect(430, 130, 351, 25))
        self.RamdiskLocationDisplay.setObjectName(_fromUtf8("RamdiskLocationDisplay"))

        self.RecoveryLocationDisplay = QtGui.QLineEdit(Form)
        self.RecoveryLocationDisplay.setGeometry(QtCore.QRect(430, 160, 351, 25))
        self.RecoveryLocationDisplay.setObjectName(_fromUtf8("RecoveryLocationDisplay"))

        self.SystemLocationDisplay = QtGui.QLineEdit(Form)
        self.SystemLocationDisplay.setGeometry(QtCore.QRect(430, 190, 351, 25))
        self.SystemLocationDisplay.setObjectName(_fromUtf8("SystemLocationDisplay"))

        self.MiscImageBrowse = QtGui.QPushButton(Form)
        self.MiscImageBrowse.setGeometry(QtCore.QRect(790, 70, 41, 21))
        self.MiscImageBrowse.setObjectName(_fromUtf8("MiscImageBrowse"))
        self.MiscImageBrowse.clicked.connect(callGetImageLocation)

        self.KernelImageBrowse = QtGui.QPushButton(Form)
        self.KernelImageBrowse.setGeometry(QtCore.QRect(790, 100, 41, 21))
        self.KernelImageBrowse.setObjectName(_fromUtf8("KernelImageBrowse"))
        self.KernelImageBrowse.clicked.connect(callGetImageLocation)

        self.RamdiskImageBrowse = QtGui.QPushButton(Form)
        self.RamdiskImageBrowse.setGeometry(QtCore.QRect(790, 130, 41, 21))
        self.RamdiskImageBrowse.setObjectName(_fromUtf8("RamdiskImageBrowse"))
        self.RamdiskImageBrowse.clicked.connect(callGetImageLocation)

        self.RecoveryImageBrowse = QtGui.QPushButton(Form)
        self.RecoveryImageBrowse.setGeometry(QtCore.QRect(790, 160, 41, 21))
        self.RecoveryImageBrowse.setObjectName(_fromUtf8("RecoveryImageBrowse"))
        self.RecoveryImageBrowse.clicked.connect(callGetImageLocation)

        self.SystemImageBrowse = QtGui.QPushButton(Form)
        self.SystemImageBrowse.setGeometry(QtCore.QRect(790, 190, 41, 21))
        self.SystemImageBrowse.setObjectName(_fromUtf8("SystemImageBrowse"))
        self.SystemImageBrowse.clicked.connect(callGetImageLocation)
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(16)

        self.BackupButton = QtGui.QPushButton(Form)
        self.BackupButton.setGeometry(QtCore.QRect(220, 220, 201, 51))
        self.BackupButton.setFont(font)
        self.BackupButton.setObjectName(_fromUtf8("BackupButton"))
        self.BackupButton.clicked.connect(callFlashBackup)

        self.ClearButton = QtGui.QPushButton(Form)
        self.ClearButton.setGeometry(QtCore.QRect(640, 220, 191, 51))
        self.ClearButton.setFont(font)
        self.ClearButton.setObjectName(_fromUtf8("ClearButton"))
        self.ClearButton.clicked.connect(callFlashBackup)

        self.FlashButton = QtGui.QPushButton(Form)
        self.FlashButton.setGeometry(QtCore.QRect(10, 220, 201, 51))
        self.FlashButton.setFont(font)
        self.FlashButton.setObjectName(_fromUtf8("FlashButton"))
        self.FlashButton.clicked.connect(callFlashBackup)

        self.LogText = QtGui.QTextEdit(Form)
        self.LogText.setGeometry(QtCore.QRect(10, 280, 821, 371))
        self.LogText.setReadOnly(True)
        self.LogText.setObjectName(_fromUtf8("LogText"))

        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(320, 10, 191, 31))
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.MiscPartitionSize = QtGui.QLineEdit(Form)
        self.MiscPartitionSize.setGeometry(QtCore.QRect(320, 70, 101, 25))
        self.MiscPartitionSize.setObjectName(_fromUtf8("MiscPartitionSize"))

        self.KernelPartitionSize = QtGui.QLineEdit(Form)
        self.KernelPartitionSize.setGeometry(QtCore.QRect(320, 100, 101, 25))
        self.KernelPartitionSize.setObjectName(_fromUtf8("KernelPartitionSize"))

        self.RamdiskPartitionSize = QtGui.QLineEdit(Form)
        self.RamdiskPartitionSize.setGeometry(QtCore.QRect(320, 130, 101, 25))
        self.RamdiskPartitionSize.setObjectName(_fromUtf8("RamdiskPartitionSize"))

        self.RecoveryPartitionSize = QtGui.QLineEdit(Form)
        self.RecoveryPartitionSize.setGeometry(QtCore.QRect(320, 160, 101, 25))
        self.RecoveryPartitionSize.setObjectName(_fromUtf8("RecoveryPartitionSize"))

        self.SystemPartitionSize = QtGui.QLineEdit(Form)
        self.SystemPartitionSize.setGeometry(QtCore.QRect(320, 190, 101, 25))
        self.SystemPartitionSize.setObjectName(_fromUtf8("SystemPartitionSize"))

        self.EraseButton = QtGui.QPushButton(Form)
        self.EraseButton.setGeometry(QtCore.QRect(430, 220, 201, 51))
        self.EraseButton.setFont(font)
        self.EraseButton.setObjectName(_fromUtf8("EraseButton"))

        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(280, 70, 41, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(280, 100, 41, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(280, 130, 41, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(280, 160, 41, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))

        self.label_11 = QtGui.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(280, 190, 41, 21))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(110, 40, 51, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.ParameterLocationDisplay = QtGui.QLineEdit(Form)
        self.ParameterLocationDisplay.setGeometry(QtCore.QRect(430, 40, 351, 25))
        self.ParameterLocationDisplay.setObjectName(_fromUtf8("ParameterLocationDisplay"))

        self.ParameterImageBrowse = QtGui.QPushButton(Form)
        self.ParameterImageBrowse.setGeometry(QtCore.QRect(790, 40, 41, 21))
        self.ParameterImageBrowse.setObjectName(_fromUtf8("ParameterImageBrowse"))
        self.ParameterImageBrowse.clicked.connect(callGetImageLocation)

        self.ParameterOffset = QtGui.QLineEdit(Form)
        self.ParameterOffset.setGeometry(QtCore.QRect(160, 40, 113, 25))
        self.ParameterOffset.setObjectName(_fromUtf8("ParameterOffset"))

        self.ParameterPartitionSize = QtGui.QLineEdit(Form)
        self.ParameterPartitionSize.setGeometry(QtCore.QRect(320, 40, 101, 25))
        self.ParameterPartitionSize.setObjectName(_fromUtf8("ParameterPartitionSize"))

        self.ParameterCheckBox = QtGui.QCheckBox(Form)
        self.ParameterCheckBox.setGeometry(QtCore.QRect(10, 40, 91, 21))
        self.ParameterCheckBox.setChecked(True)
        self.ParameterCheckBox.setObjectName(_fromUtf8("ParameterCheckBox"))

        self.label_12 = QtGui.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(280, 40, 41, 21))
        self.label_12.setObjectName(_fromUtf8("label_12"))

        self.LoaderOffset = QtGui.QLineEdit(Form)
        self.LoaderOffset.setGeometry(QtCore.QRect(160, 10, 113, 25))
        self.LoaderOffset.setText(_fromUtf8(""))
        self.LoaderOffset.setObjectName(_fromUtf8("LoaderOffset"))

        self.LoaderCheckBox = QtGui.QCheckBox(Form)
        self.LoaderCheckBox.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.LoaderCheckBox.setChecked(False)
        self.LoaderCheckBox.setObjectName(_fromUtf8("LoaderCheckBox"))

        self.label_13 = QtGui.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(280, 10, 41, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))

        self.LoaderLocationDisplay = QtGui.QLineEdit(Form)
        self.LoaderLocationDisplay.setGeometry(QtCore.QRect(430, 10, 351, 25))
        self.LoaderLocationDisplay.setObjectName(_fromUtf8("LoaderLocationDisplay"))

        self.LoaderPartitionSize = QtGui.QLineEdit(Form)
        self.LoaderPartitionSize.setGeometry(QtCore.QRect(320, 10, 101, 25))
        self.LoaderPartitionSize.setText(_fromUtf8(""))
        self.LoaderPartitionSize.setObjectName(_fromUtf8("LoaderPartitionSize"))

        self.label_14 = QtGui.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(110, 10, 51, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))

        self.LoaderImageBrowse = QtGui.QPushButton(Form)
        self.LoaderImageBrowse.setGeometry(QtCore.QRect(790, 10, 41, 21))
        self.LoaderImageBrowse.setObjectName(_fromUtf8("LoaderImageBrowse"))
        self.LoaderImageBrowse.clicked.connect(callGetImageLocation)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "RKFlashTool", None))
        self.MiscCheckBox.setText(_translate("Form", "Misc", None))
        self.KernelCheckBox.setText(_translate("Form", "Kernel", None))
        self.RecoveryCheckBox.setText(_translate("Form", "Recovery", None))
        self.SystemCheckBox.setText(_translate("Form", "System", None))
        self.RamdiskCheckBox.setText(_translate("Form", "Ramdisk", None))
        self.LoaderCheckBox.setText(_translate("Form", "Loader", None))
        self.ParameterCheckBox.setText(_translate("Form", "Parameter", None))

        self.label.setText(_translate("Form", "Offset:", None))
        self.label_2.setText(_translate("Form", "Offset:", None))
        self.label_3.setText(_translate("Form", "Offset:", None))
        self.label_4.setText(_translate("Form", "Offset:", None))
        self.label_5.setText(_translate("Form", "Offset:", None))
        self.label_6.setText(_translate("Form", "Offset:", None))
        self.label_14.setText(_translate("Form", "Offset:", None))

        self.MiscOffset.setText(_translate("Form", "0x2000", None))
        self.KernelOffset.setText(_translate("Form", "0x4000", None))
        self.RamdiskOffset.setText(_translate("Form", "0x8000", None))
        self.RecoveryOffset.setText(_translate("Form", "0x10000", None))
        self.SystemOffset.setText(_translate("Form", "0x61A000", None))

        self.MiscImageBrowse.setText(_translate("Form", "...", None))
        self.KernelImageBrowse.setText(_translate("Form", "...", None))
        self.RamdiskImageBrowse.setText(_translate("Form", "...", None))
        self.RecoveryImageBrowse.setText(_translate("Form", "...", None))
        self.SystemImageBrowse.setText(_translate("Form", "...", None))
        self.ParameterImageBrowse.setText(_translate("Form", "...", None))
        self.LoaderImageBrowse.setText(_translate("Form", "...", None))

        self.BackupButton.setText(_translate("Form", "BACKUP", None))
        self.ClearButton.setText(_translate("Form", "CLEAR", None))
        self.FlashButton.setText(_translate("Form", "FLASH", None))
        self.EraseButton.setText(_translate("Form", " ", None))

        self.MiscPartitionSize.setText(_translate("Form", "0x2000", None))
        self.KernelPartitionSize.setText(_translate("Form", "0x4000", None))
        self.RamdiskPartitionSize.setText(_translate("Form", "0x8000", None))
        self.RecoveryPartitionSize.setText(_translate("Form", "0x8000", None))
        self.SystemPartitionSize.setText(_translate("Form", "0x200000", None))
        self.ParameterOffset.setText(_translate("Form", "0x0000", None))
        self.ParameterPartitionSize.setText(_translate("Form", "0x2000", None))

        self.label_7.setText(_translate("Form", "Size:", None))
        self.label_8.setText(_translate("Form", "Size:", None))
        self.label_9.setText(_translate("Form", "Size:", None))
        self.label_10.setText(_translate("Form", "Size:", None))
        self.label_11.setText(_translate("Form", "Size:", None))
        self.label_12.setText(_translate("Form", "Size:", None))
        self.label_13.setText(_translate("Form", "Size:", None))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

