# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\python\pyqt\hallsensortest.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 478)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_speedadd = QtWidgets.QPushButton(self.centralwidget)
        self.bt_speedadd.setGeometry(QtCore.QRect(20, 330, 145, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.bt_speedadd.setFont(font)
        self.bt_speedadd.setObjectName("bt_speedadd")
        self.bt_speedsub = QtWidgets.QPushButton(self.centralwidget)
        self.bt_speedsub.setGeometry(QtCore.QRect(220, 330, 145, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.bt_speedsub.setFont(font)
        self.bt_speedsub.setObjectName("bt_speedsub")
        self.bt_shutdown = QtWidgets.QPushButton(self.centralwidget)
        self.bt_shutdown.setGeometry(QtCore.QRect(420, 330, 145, 80))
        self.bt_shutdown.setObjectName("bt_shutdown")
        self.ln_speed = QtWidgets.QLCDNumber(self.centralwidget)
        self.ln_speed.setGeometry(QtCore.QRect(90, 100, 211, 121))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ln_speed.sizePolicy().hasHeightForWidth())
        self.ln_speed.setSizePolicy(sizePolicy)
        self.ln_speed.setAutoFillBackground(False)
        self.ln_speed.setFrameShape(QtWidgets.QFrame.Box)
        self.ln_speed.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ln_speed.setLineWidth(1)
        self.ln_speed.setSmallDecimalPoint(False)
        self.ln_speed.setDigitCount(3)
        self.ln_speed.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.ln_speed.setProperty("value", 0.0)
        self.ln_speed.setProperty("intValue", 0)
        self.ln_speed.setObjectName("ln_speed")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 420, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 31, 121))
        font = QtGui.QFont()
        font.setFamily("04b_21")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 800, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 300, 800, 20))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setLineWidth(2)
        self.line_2.setMidLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.ln_speed_1250 = QtWidgets.QLCDNumber(self.centralwidget)
        self.ln_speed_1250.setGeometry(QtCore.QRect(580, 100, 121, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ln_speed_1250.sizePolicy().hasHeightForWidth())
        self.ln_speed_1250.setSizePolicy(sizePolicy)
        self.ln_speed_1250.setAutoFillBackground(False)
        self.ln_speed_1250.setFrameShape(QtWidgets.QFrame.Box)
        self.ln_speed_1250.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ln_speed_1250.setLineWidth(1)
        self.ln_speed_1250.setSmallDecimalPoint(False)
        self.ln_speed_1250.setDigitCount(3)
        self.ln_speed_1250.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.ln_speed_1250.setProperty("value", 0.0)
        self.ln_speed_1250.setProperty("intValue", 0)
        self.ln_speed_1250.setObjectName("ln_speed_1250")
        self.ln_speed_1050 = QtWidgets.QLCDNumber(self.centralwidget)
        self.ln_speed_1050.setGeometry(QtCore.QRect(580, 210, 121, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ln_speed_1050.sizePolicy().hasHeightForWidth())
        self.ln_speed_1050.setSizePolicy(sizePolicy)
        self.ln_speed_1050.setAutoFillBackground(False)
        self.ln_speed_1050.setFrameShape(QtWidgets.QFrame.Box)
        self.ln_speed_1050.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ln_speed_1050.setLineWidth(1)
        self.ln_speed_1050.setSmallDecimalPoint(False)
        self.ln_speed_1050.setDigitCount(3)
        self.ln_speed_1050.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.ln_speed_1050.setProperty("value", 0.0)
        self.ln_speed_1050.setProperty("intValue", 0)
        self.ln_speed_1050.setObjectName("ln_speed_1050")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(480, 120, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(480, 210, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 130, 31, 121))
        font = QtGui.QFont()
        font.setFamily("04b_21")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_6.setObjectName("label_6")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(370, 80, 20, 231))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(470, 180, 331, 30))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(460, 80, 10, 231))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_5.setLineWidth(1)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.bt_shutdown_2 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_shutdown_2.setGeometry(QtCore.QRect(620, 330, 145, 80))
        self.bt_shutdown_2.setObjectName("bt_shutdown_2")
        self.bt_dir = QtWidgets.QPushButton(self.centralwidget)
        self.bt_dir.setGeometry(QtCore.QRect(90, 230, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.bt_dir.setFont(font)
        self.bt_dir.setDefault(False)
        self.bt_dir.setFlat(False)
        self.bt_dir.setObjectName("bt_dir")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(380, 80, 20, 231))
        self.line_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setObjectName("line_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(720, 130, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(720, 240, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(320, 160, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 330, 751, 120))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NANCHE"))
        self.bt_speedadd.setText(_translate("MainWindow", "速度+"))
        self.bt_speedsub.setText(_translate("MainWindow", "速度-"))
        self.bt_shutdown.setText(_translate("MainWindow", "停止"))
        self.label.setText(_translate("MainWindow", "霍尔传感器便携式测试设备"))
        self.label_2.setText(_translate("MainWindow", "长沙楠车电气设备有限公司  redmorningcn"))
        self.label_3.setText(_translate("MainWindow", "转\n"
"速"))
        self.label_4.setText(_translate("MainWindow", "机车轮径\n"
"1250mm"))
        self.label_5.setText(_translate("MainWindow", "机车轮径\n"
"1050mm"))
        self.label_6.setText(_translate("MainWindow", "速\n"
"度"))
        self.bt_shutdown_2.setText(_translate("MainWindow", "关机"))
        self.bt_dir.setText(_translate("MainWindow", "顺时针方向"))
        self.label_7.setText(_translate("MainWindow", "Km/h"))
        self.label_8.setText(_translate("MainWindow", "Km/h"))
        self.label_9.setText(_translate("MainWindow", "r/min"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:12pt;\">操作说明：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:12pt;\">1、按&quot;速度+&quot;，增加装置转速；</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:12pt;\">2、按&quot;速度-&quot;，降低装置转速；</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:12pt;\">3、低速时，长按&quot;速度-&quot;5秒后，再同时按&quot;速度+&quot;5秒，改变方向；</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:12pt;\">4、速度降为0后，再长按&quot;速度-&quot;5秒，装置准备关机。</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
