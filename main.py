import sys
import fire_detection
from PyQt5 import QtWidgets, QtCore, QtGui


class start(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Show logo and start app:
        splash_pix = QtGui.QPixmap("images/.ico/appLogo.ico")
        self.splash = QtWidgets.QSplashScreen(splash_pix)
        self.splash.show()

        # Wait 3s for flash logo:
        QtCore.QTimer.singleShot(3000, self.nothing)

        self.splash.finish(self)
    def nothing(self):
        pass
class Ui_MainWindow():
    def __init__(self, MainWindow):
        super().__init__()

        self.setup_centralWindow(MainWindow)
        self.setup_CamView()
        self.setup_InforView()
        self.setup_hisView()
        # self.setup_menubar()

    def update_frame_gray(self, grayIMG):
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(grayIMG))

    def update_frame_color(self, colorIMG):
        self.label.setPixmap(QtGui.QPixmap.fromImage(colorIMG))

    def setup_centralWindow(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1102, 654)
        MainWindow.setWindowIcon(QtGui.QIcon("images/.ico/appLogo.ico"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: white;")

        self.exit_but = QtWidgets.QPushButton(self.centralwidget)
        self.exit_but.setGeometry(QtCore.QRect(510, 580, 93, 28))
        self.exit_but.setStyleSheet("background-color: red;"
                                    "color: black;")
        self.exit_but.setObjectName("exit_but")
        self.exit_but.clicked.connect(self.close_app)

    def setup_CamView(self):
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 10, 1041, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.cameraView = QtWidgets.QGridLayout(self.gridLayoutWidget)

        self.cameraView.setContentsMargins(0, 0, 0, 0)
        self.cameraView.setObjectName("cameraView")

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.cameraView.addItem(spacerItem, 2, 1, 1, 1)

        self.name_VC = QtWidgets.QLabel(self.gridLayoutWidget)
        self.name_VC.setStyleSheet("")
        self.name_VC.setObjectName("name_VC")
        self.cameraView.addWidget(self.name_VC, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.cameraView.addItem(spacerItem1, 1, 2, 1, 1)

        self.name_VF = QtWidgets.QLabel(self.gridLayoutWidget)
        self.name_VF.setStyleSheet("")
        self.name_VF.setObjectName("name_VF")
        self.cameraView.addWidget(self.name_VF, 0, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        spacerItem2 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.cameraView.addItem(spacerItem2, 1, 0, 1, 1)

        self.widget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget.setObjectName("widget")

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(-6, -5, 521, 311))
        self.label.setStyleSheet("background-color: green;")
        self.label.setText("")
        # self.label.setPixmap(QtGui.QPixmap("../../../Pictures/Screenshots/Screenshot 2023-09-04 225026.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.cameraView.addWidget(self.widget, 2, 0, 1, 1)

        self.widget_2 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget_2.setObjectName("widget_2")

        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(-6, -5, 521, 311))
        self.label_2.setStyleSheet("background-color: green;")
        self.label_2.setText("")
        # self.label_2.setPixmap(QtGui.QPixmap("../../../Pictures/Screenshots/Screenshot 2023-09-04 225026.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.cameraView.addWidget(self.widget_2, 2, 2, 1, 1)

    def setup_InforView(self):
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(60, 390, 982, 169))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")

        self.inforView = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.inforView.setContentsMargins(0, 0, 0, 0)
        self.inforView.setObjectName("inforView")

        self.numInfor = QtWidgets.QGridLayout()
        self.numInfor.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.numInfor.setContentsMargins(-1, -1, 100, -1)
        self.numInfor.setHorizontalSpacing(4)
        self.numInfor.setVerticalSpacing(0)
        self.numInfor.setObjectName("numInfor")

        self.co2LCD = QtWidgets.QLCDNumber(self.gridLayoutWidget_3)
        self.co2LCD.setDigitCount(3)
        self.co2LCD.setProperty("value", 999.0)
        self.co2LCD.setObjectName("co2LCD")
        self.numInfor.addWidget(self.co2LCD, 1, 0, 1, 1)

        self.oAir = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.oAir.setObjectName("oAir")
        self.numInfor.addWidget(self.oAir, 2, 1, 1, 1)

        self.coLCD = QtWidgets.QLCDNumber(self.gridLayoutWidget_3)
        self.coLCD.setDigitCount(3)
        self.coLCD.setProperty("value", 999.0)
        self.coLCD.setObjectName("coLCD")
        self.numInfor.addWidget(self.coLCD, 0, 0, 1, 1)

        self.co2Air = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.co2Air.setObjectName("co2Air")
        self.numInfor.addWidget(self.co2Air, 1, 1, 1, 1)

        self.metanLCD = QtWidgets.QLCDNumber(self.gridLayoutWidget_3)
        self.metanLCD.setDigitCount(3)
        self.metanLCD.setProperty("value", 999.0)
        self.metanLCD.setObjectName("metanLCD")
        self.numInfor.addWidget(self.metanLCD, 3, 0, 1, 1)

        self.metanAir = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.metanAir.setObjectName("metanAir")
        self.numInfor.addWidget(self.metanAir, 3, 1, 1, 1)

        self.o2LCD = QtWidgets.QLCDNumber(self.gridLayoutWidget_3)
        self.o2LCD.setDigitCount(3)
        self.o2LCD.setProperty("value", 999.0)
        self.o2LCD.setObjectName("o2LCD")
        self.numInfor.addWidget(self.o2LCD, 2, 0, 1, 1)

        self.coAir = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.coAir.setObjectName("coAir")
        self.numInfor.addWidget(self.coAir, 0, 1, 1, 1)

        self.inforView.addLayout(self.numInfor, 3, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(450, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.inforView.addItem(spacerItem3, 1, 1, 1, 1)

    def setup_hisView(self):
        self.historyName = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.historyName.setObjectName("historyName")
        self.inforView.addWidget(self.historyName, 0, 1, 1, 1, QtCore.Qt.AlignLeft)

        self.numInforName = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.numInforName.setObjectName("numInforName")
        self.inforView.addWidget(self.numInforName, 0, 3, 1, 1)

        spacerItem4 = QtWidgets.QSpacerItem(137, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.inforView.addItem(spacerItem4, 3, 2, 1, 1)

        spacerItem5 = QtWidgets.QSpacerItem(20, 139, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.inforView.addItem(spacerItem5, 3, 0, 1, 1)

        self.tableView = QtWidgets.QTableView(self.gridLayoutWidget_3)
        self.tableView.setObjectName("tableView")
        self.inforView.addWidget(self.tableView, 3, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fire recognition"))
        self.exit_but.setText(_translate("MainWindow", "Thoát"))
        self.name_VC.setText(_translate("MainWindow", "Real time view"))
        self.name_VF.setText(_translate("MainWindow", "Fire detection view"))
        self.oAir.setText(_translate("MainWindow", "Nồng độ khí Oxi (O₂)"))
        self.co2Air.setText(_translate("MainWindow", "Nồng độ khí Carbon dioxide (CO₂)"))
        self.metanAir.setText(_translate("MainWindow", "Nông độ khí Metan (CH₄)"))
        self.coAir.setText(_translate("MainWindow", "Nồng độ khí Carbon monoxide (CO)"))
        self.historyName.setText(_translate("MainWindow", "Lịch sử:"))
        self.numInforName.setText(_translate("MainWindow", "Thông số thời gian thực:"))

    def close_app(self):
        fire_recog.stop()
        MainWindow.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    flash = start()

    MainWindow = QtWidgets.QMainWindow()
    app_ui = Ui_MainWindow(MainWindow)
    MainWindow.show()

    fire_recog = fire_detection.Fire_smoke_detection()
    fire_recog.start()

    fire_recog.color_imageUpdate.connect(app_ui.update_frame_color)
    fire_recog.gray_imageUpdate.connect(app_ui.update_frame_gray)

    sys.exit(app.exec_())
