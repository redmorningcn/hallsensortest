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
        MainWindow.resize(797, 532)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ln_motorspeed = QtWidgets.QLCDNumber(self.centralwidget)
        self.ln_motorspeed.setGeometry(QtCore.QRect(490, 90, 211, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ln_motorspeed.sizePolicy().hasHeightForWidth())
        self.ln_motorspeed.setSizePolicy(sizePolicy)
        self.ln_motorspeed.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.ln_motorspeed.setAutoFillBackground(False)
        self.ln_motorspeed.setFrameShape(QtWidgets.QFrame.Box)
        self.ln_motorspeed.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ln_motorspeed.setLineWidth(1)
        self.ln_motorspeed.setSmallDecimalPoint(False)
        self.ln_motorspeed.setDigitCount(4)
        self.ln_motorspeed.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.ln_motorspeed.setProperty("value", 0.0)
        self.ln_motorspeed.setProperty("intValue", 0)
        self.ln_motorspeed.setObjectName("ln_motorspeed")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 410, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 70, 71, 121))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 800, 40))
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 280, 800, 20))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setLineWidth(2)
        self.line_2.setMidLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(720, 120, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 320, 781, 191))
        self.textEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setOverwriteMode(False)
        self.textEdit.setObjectName("textEdit")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(630, 30, 54, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_IP = QtWidgets.QLabel(self.centralwidget)
        self.label_IP.setGeometry(QtCore.QRect(670, 30, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_IP.setFont(font)
        self.label_IP.setObjectName("label_IP")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 180, 51, 121))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setObjectName("label_4")
        self.ln_locolspeed = QtWidgets.QLCDNumber(self.centralwidget)
        self.ln_locolspeed.setGeometry(QtCore.QRect(490, 200, 211, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ln_locolspeed.sizePolicy().hasHeightForWidth())
        self.ln_locolspeed.setSizePolicy(sizePolicy)
        self.ln_locolspeed.setAutoFillBackground(False)
        self.ln_locolspeed.setFrameShape(QtWidgets.QFrame.Box)
        self.ln_locolspeed.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ln_locolspeed.setLineWidth(1)
        self.ln_locolspeed.setSmallDecimalPoint(False)
        self.ln_locolspeed.setDigitCount(4)
        self.ln_locolspeed.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.ln_locolspeed.setProperty("value", 0.0)
        self.ln_locolspeed.setProperty("intValue", 0)
        self.ln_locolspeed.setObjectName("ln_locolspeed")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(720, 230, 51, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 180, 61, 121))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_5.setObjectName("label_5")
        self.ln_locol = QtWidgets.QLCDNumber(self.centralwidget)
        self.ln_locol.setGeometry(QtCore.QRect(120, 200, 211, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ln_locol.sizePolicy().hasHeightForWidth())
        self.ln_locol.setSizePolicy(sizePolicy)
        self.ln_locol.setAutoFillBackground(False)
        self.ln_locol.setFrameShape(QtWidgets.QFrame.Box)
        self.ln_locol.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ln_locol.setLineWidth(1)
        self.ln_locol.setSmallDecimalPoint(False)
        self.ln_locol.setDigitCount(4)
        self.ln_locol.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.ln_locol.setProperty("value", 1250.0)
        self.ln_locol.setProperty("intValue", 1250)
        self.ln_locol.setObjectName("ln_locol")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 70, 161, 121))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_6.setObjectName("label_6")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(340, 230, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.com_rotatedir = QtWidgets.QComboBox(self.centralwidget)
        self.com_rotatedir.setGeometry(QtCore.QRect(120, 90, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.com_rotatedir.setFont(font)
        self.com_rotatedir.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.com_rotatedir.setAutoFillBackground(True)
        self.com_rotatedir.setEditable(True)
        self.com_rotatedir.setObjectName("com_rotatedir")
        self.com_rotatedir.addItem("")
        self.com_rotatedir.addItem("")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(383, 70, 20, 221))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(-10, 180, 811, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NANCHE"))
        self.label.setText(_translate("MainWindow", "霍尔传感器便携式测试设备"))
        self.label_2.setText(_translate("MainWindow", "长沙楠车电气设备有限公司  redmorningcn"))
        self.label_3.setText(_translate("MainWindow", "转速"))
        self.label_9.setText(_translate("MainWindow", "r/min"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:12pt;\">操作说明：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:12pt;\">1、</span><span style=\" font-family:\'Arial\'; font-size:12pt; font-weight:600;\">在速度为0时，点击按&quot;功能&quot;按键</span><span style=\" font-family:\'Arial\'; font-size:12pt;\">，循环切换&quot;方向-&quot;、&quot;轮径&quot;、&quot;速度&quot;和&quot;转速&quot;设置功能；确定设置功能后，</span><span style=\" font-family:\'Arial\'; font-size:12pt; font-weight:600;\">&quot;速度+&quot;或&quot;速度-&quot;按键为调整按键</span><span style=\" font-family:\'Arial\'; font-size:12pt;\">，按调整按键，可改变对应设置值。具体如下：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:12pt;\">1.1、在“旋转方向”设置功能时，单击调整按键，循环切换“顺时针方向”、“逆时针方向”；</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:12pt;\">1.2、在“机车轮径”设置功能时，单击调整按键，轮径变化1mm，按键长按2秒后，轮径每秒变化大于15mm；</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:12pt;\">1.3、在“转速”设置功能时，单击调整按键，转速变化1r/min，按键长按2秒后，转速每秒变化大于50r/min；</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:12pt;\">1.4、在“速度”设置功能时，单击调整按键，速度变化0.5km/h，按键长按2秒后，转速每秒变化大于3km/h。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:12pt;\">2、速度值不为0，</span><span style=\" font-family:\'Arial\'; font-size:12pt; font-weight:600; color:#000000;\">双击&quot;功能&quot;按键，速度急停</span><span style=\" font-family:\'Arial\'; font-size:12pt;\">；速度为0时，长按“功能”按键5秒后，设置关机。</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "IP："))
        self.label_IP.setText(_translate("MainWindow", "192.168.1.118"))
        self.label_4.setText(_translate("MainWindow", "速度"))
        self.label_11.setText(_translate("MainWindow", "km/h"))
        self.label_5.setText(_translate("MainWindow", "机车\n"
"轮径"))
        self.label_6.setText(_translate("MainWindow", "旋转\n"
"方向"))
        self.label_12.setText(_translate("MainWindow", "mm"))
        self.com_rotatedir.setItemText(0, _translate("MainWindow", "顺时针方向"))
        self.com_rotatedir.setItemText(1, _translate("MainWindow", "逆时针方向"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
