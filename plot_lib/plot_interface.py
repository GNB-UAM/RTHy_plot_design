# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rth_plot/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 718)
        MainWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setStyleSheet("background-color:rgb(114, 159, 207)")
        self.centralWidget.setObjectName("centralWidget")
        self.frame_control = QtWidgets.QFrame(self.centralWidget)
        self.frame_control.setGeometry(QtCore.QRect(20, 20, 441, 681))
        self.frame_control.setStyleSheet("background:rgb(255, 255, 255)")
        self.frame_control.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_control.setObjectName("frame_control")
        self.pushButton_selectfile = QtWidgets.QPushButton(self.frame_control)
        self.pushButton_selectfile.setGeometry(QtCore.QRect(20, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        self.pushButton_selectfile.setFont(font)
        self.pushButton_selectfile.setStyleSheet("background:rgb(238, 238, 236)")
        self.pushButton_selectfile.setObjectName("pushButton_selectfile")
        self.frame_3 = QtWidgets.QFrame(self.frame_control)
        self.frame_3.setGeometry(QtCore.QRect(20, 290, 401, 121))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 16, 131, 101))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(11, 10, 11, 11)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.PlotAll = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        self.PlotAll.setFont(font)
        self.PlotAll.setStyleSheet("background:rgb(255, 255, 255)")
        self.PlotAll.setChecked(True)
        self.PlotAll.setObjectName("PlotAll")
        self.verticalLayout_3.addWidget(self.PlotAll)
        self.PlotSelect = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        self.PlotSelect.setFont(font)
        self.PlotSelect.setStyleSheet("background:rgb(255, 255, 255)")
        self.PlotSelect.setObjectName("PlotSelect")
        self.verticalLayout_3.addWidget(self.PlotSelect)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 10, 241, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_from = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_from.setEnabled(True)
        self.frame_from.setStyleSheet("background:rgb(255, 255, 255)")
        self.frame_from.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_from.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_from.setObjectName("frame_from")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.frame_from)
        self.textBrowser_4.setEnabled(False)
        self.textBrowser_4.setGeometry(QtCore.QRect(0, 10, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.spinBox_from_m = QtWidgets.QSpinBox(self.frame_from)
        self.spinBox_from_m.setEnabled(False)
        self.spinBox_from_m.setGeometry(QtCore.QRect(60, 10, 48, 24))
        self.spinBox_from_m.setMaximum(999)
        self.spinBox_from_m.setObjectName("spinBox_from_m")
        self.spinBox_from_s = QtWidgets.QSpinBox(self.frame_from)
        self.spinBox_from_s.setEnabled(False)
        self.spinBox_from_s.setGeometry(QtCore.QRect(150, 10, 48, 24))
        self.spinBox_from_s.setMaximum(999)
        self.spinBox_from_s.setSingleStep(5)
        self.spinBox_from_s.setProperty("value", 30)
        self.spinBox_from_s.setObjectName("spinBox_from_s")
        self.verticalLayout.addWidget(self.frame_from)
        self.frame_to = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_to.setStyleSheet("background:rgb(255, 255, 255)")
        self.frame_to.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_to.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_to.setObjectName("frame_to")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.frame_to)
        self.textBrowser_5.setEnabled(False)
        self.textBrowser_5.setGeometry(QtCore.QRect(0, 10, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.textBrowser_5.setFont(font)
        self.textBrowser_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.spinBox_to_m = QtWidgets.QSpinBox(self.frame_to)
        self.spinBox_to_m.setEnabled(False)
        self.spinBox_to_m.setGeometry(QtCore.QRect(60, 10, 48, 24))
        self.spinBox_to_m.setMaximum(999)
        self.spinBox_to_m.setProperty("value", 5)
        self.spinBox_to_m.setDisplayIntegerBase(10)
        self.spinBox_to_m.setObjectName("spinBox_to_m")
        self.spinBox_to_s = QtWidgets.QSpinBox(self.frame_to)
        self.spinBox_to_s.setEnabled(False)
        self.spinBox_to_s.setGeometry(QtCore.QRect(150, 10, 48, 24))
        self.spinBox_to_s.setMaximum(999)
        self.spinBox_to_s.setSingleStep(5)
        self.spinBox_to_s.setObjectName("spinBox_to_s")
        self.verticalLayout.addWidget(self.frame_to)
        self.frame_4 = QtWidgets.QFrame(self.frame_control)
        self.frame_4.setGeometry(QtCore.QRect(20, 430, 241, 51))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.JumpPointsValue = QtWidgets.QSpinBox(self.frame_4)
        self.JumpPointsValue.setGeometry(QtCore.QRect(160, 10, 51, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        self.JumpPointsValue.setFont(font)
        self.JumpPointsValue.setStyleSheet("background:rgb(255, 255, 255)")
        self.JumpPointsValue.setProperty("value", 2)
        self.JumpPointsValue.setObjectName("JumpPointsValue")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(20, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.frame_control)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 50, 121, 41))
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textEdit_experiment = QtWidgets.QTextEdit(self.frame_control)
        self.textEdit_experiment.setGeometry(QtCore.QRect(150, 90, 271, 71))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        self.textEdit_experiment.setFont(font)
        self.textEdit_experiment.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textEdit_experiment.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_experiment.setObjectName("textEdit_experiment")
        self.pushButton_selectlast = QtWidgets.QPushButton(self.frame_control)
        self.pushButton_selectlast.setGeometry(QtCore.QRect(20, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        self.pushButton_selectlast.setFont(font)
        self.pushButton_selectlast.setStyleSheet("background:rgb(238, 238, 236)")
        self.pushButton_selectlast.setObjectName("pushButton_selectlast")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.frame_control)
        self.textBrowser_7.setGeometry(QtCore.QRect(20, 250, 121, 31))
        self.textBrowser_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.frame_5 = QtWidgets.QFrame(self.frame_control)
        self.frame_5.setGeometry(QtCore.QRect(280, 430, 141, 51))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.latency_on = QtWidgets.QCheckBox(self.frame_5)
        self.latency_on.setGeometry(QtCore.QRect(20, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        self.latency_on.setFont(font)
        self.latency_on.setObjectName("latency_on")
        self.frame_6 = QtWidgets.QFrame(self.frame_control)
        self.frame_6.setGeometry(QtCore.QRect(20, 180, 251, 51))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frecuency = QtWidgets.QSpinBox(self.frame_6)
        self.frecuency.setGeometry(QtCore.QRect(160, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        self.frecuency.setFont(font)
        self.frecuency.setStyleSheet("background:rgb(255, 255, 255)")
        self.frecuency.setMaximum(99999)
        self.frecuency.setSingleStep(5000)
        self.frecuency.setProperty("value", 10000)
        self.frecuency.setObjectName("frecuency")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.frame_7 = QtWidgets.QFrame(self.frame_control)
        self.frame_7.setGeometry(QtCore.QRect(290, 180, 131, 51))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_time = QtWidgets.QLabel(self.frame_7)
        self.label_time.setGeometry(QtCore.QRect(10, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_time.setFont(font)
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")
        self.pushButton_plot = QtWidgets.QPushButton(self.frame_control)
        self.pushButton_plot.setGeometry(QtCore.QRect(140, 630, 151, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        self.pushButton_plot.setFont(font)
        self.pushButton_plot.setStyleSheet("background:rgb(238, 238, 236)")
        self.pushButton_plot.setObjectName("pushButton_plot")
        self.label_3 = QtWidgets.QLabel(self.frame_control)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.frame_4.raise_()
        self.textBrowser_3.raise_()
        self.textEdit_experiment.raise_()
        self.pushButton_selectlast.raise_()
        self.textBrowser_7.raise_()
        self.frame_3.raise_()
        self.pushButton_selectfile.raise_()
        self.frame_5.raise_()
        self.frame_6.raise_()
        self.frame_7.raise_()
        self.pushButton_plot.raise_()
        self.label_3.raise_()
        self.frame_log = QtWidgets.QFrame(self.centralWidget)
        self.frame_log.setGeometry(QtCore.QRect(480, 20, 621, 681))
        self.frame_log.setStyleSheet("background:rgb(255, 255, 255)")
        self.frame_log.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_log.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_log.setLineWidth(0)
        self.frame_log.setObjectName("frame_log")
        self.textEdit_log = QtWidgets.QTextEdit(self.frame_log)
        self.textEdit_log.setGeometry(QtCore.QRect(20, 60, 581, 551))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(13)
        self.textEdit_log.setFont(font)
        self.textEdit_log.setObjectName("textEdit_log")
        self.label_4 = QtWidgets.QLabel(self.frame_log)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 581, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_savelog = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_savelog.setGeometry(QtCore.QRect(920, 650, 131, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        self.pushButton_savelog.setFont(font)
        self.pushButton_savelog.setStyleSheet("background:rgb(238, 238, 236)")
        self.pushButton_savelog.setObjectName("pushButton_savelog")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.PlotSelect.clicked['bool'].connect(self.textBrowser_4.setEnabled)
        self.PlotSelect.clicked['bool'].connect(self.textBrowser_5.setEnabled)
        self.PlotSelect.clicked['bool'].connect(self.spinBox_from_m.setEnabled)
        self.PlotSelect.clicked['bool'].connect(self.spinBox_from_s.setEnabled)
        self.PlotSelect.clicked['bool'].connect(self.spinBox_to_m.setEnabled)
        self.PlotSelect.clicked['bool'].connect(self.spinBox_to_s.setEnabled)
        self.PlotAll.clicked['bool'].connect(self.textBrowser_4.setDisabled)
        self.PlotAll.clicked['bool'].connect(self.textBrowser_5.setDisabled)
        self.PlotAll.clicked['bool'].connect(self.spinBox_from_m.setDisabled)
        self.PlotAll.clicked['bool'].connect(self.spinBox_from_s.setDisabled)
        self.PlotAll.clicked['bool'].connect(self.spinBox_to_m.setDisabled)
        self.PlotAll.clicked['bool'].connect(self.spinBox_to_s.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RTHybrid Plot Tool"))
        self.pushButton_selectfile.setText(_translate("MainWindow", "Select file"))
        self.PlotAll.setText(_translate("MainWindow", "Plot all file"))
        self.PlotSelect.setText(_translate("MainWindow", "Select time"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Monospace\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:11pt;\">From:              m               s</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Monospace\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:11pt;\">To:                  m               s</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Downsampling:"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Experiment:</span></p></body></html>"))
        self.textEdit_experiment.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select file...</p></body></html>"))
        self.pushButton_selectlast.setText(_translate("MainWindow", "Last (beta)"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Options:</span></p></body></html>"))
        self.latency_on.setText(_translate("MainWindow", " Latencies"))
        self.label_2.setText(_translate("MainWindow", "Frecuency (Hz):"))
        self.label_time.setText(_translate("MainWindow", "Duration"))
        self.pushButton_plot.setText(_translate("MainWindow", "Plot"))
        self.label_3.setText(_translate("MainWindow", "PLOT"))
        self.label_4.setText(_translate("MainWindow", "LOG FILE"))
        self.pushButton_savelog.setText(_translate("MainWindow", "Save file"))

