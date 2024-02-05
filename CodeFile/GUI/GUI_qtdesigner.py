# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGraphicsView,
    QGridLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QToolBox, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(902, 678)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.toolBox = QToolBox(self.centralwidget)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setEnabled(True)
        self.toolBox.setGeometry(QRect(370, 10, 521, 551))
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.toolBox.setFont(font)
        self.toolBox.setAutoFillBackground(False)
        self.toolBox.setFrameShadow(QFrame.Sunken)
        self.toolBoxPage1 = QWidget()
        self.toolBoxPage1.setObjectName(u"toolBoxPage1")
        self.toolBoxPage1.setCursor(QCursor(Qt.ArrowCursor))
        self.toolBoxPage1.setTabletTracking(True)
        self.toolBoxPage1.setAutoFillBackground(True)
        self.toolBoxPage1.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.gridLayout_3 = QGridLayout(self.toolBoxPage1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.graphicsView = QGraphicsView(self.toolBoxPage1)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_3.addWidget(self.graphicsView, 0, 0, 1, 1)

        self.toolBox.addItem(self.toolBoxPage1, u"\u0413\u0440\u0430\u0444\u0438\u043a \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u0440\u043e\u0441\u0442\u0430 \u0442\u0440\u0435\u0449\u0438\u043d\u044b \u043e\u0442 \u0446\u0438\u043a\u043b\u043e\u0432")
        self.toolBoxPage2 = QWidget()
        self.toolBoxPage2.setObjectName(u"toolBoxPage2")
        self.gridLayout_4 = QGridLayout(self.toolBoxPage2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.graphicsView_2 = QGraphicsView(self.toolBoxPage2)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.gridLayout_4.addWidget(self.graphicsView_2, 0, 0, 1, 1)

        self.toolBox.addItem(self.toolBoxPage2, u"\u0413\u0440\u0430\u0444\u0438\u043a \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u0440\u043e\u0441\u0442\u0430 \u0442\u0440\u0435\u0449\u0438\u043d\u044b \u0440\u0430\u0437\u043c\u0430\u0445\u0430 \u0438\u043d\u0442\u0435\u043d\u0441\u0438\u0432\u043d\u043e\u0441\u0442\u0438 \u0440\u043e\u0441\u0442\u0430 \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0439")
        self.toolBoxPage3 = QWidget()
        self.toolBoxPage3.setObjectName(u"toolBoxPage3")
        self.toolBox.addItem(self.toolBoxPage3, u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u0434\u0430\u043d\u043d\u044b\u0445")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 120, 311, 475))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 10, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setBold(True)
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 12, 2, 1, 1)

        self.lineEdit_21 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.gridLayout.addWidget(self.lineEdit_21, 16, 1, 1, 1)

        self.lineEdit_15 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout.addWidget(self.lineEdit_15, 11, 3, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 1, 2, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 1)

        self.lineEdit_13 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout.addWidget(self.lineEdit_13, 10, 1, 1, 1)

        self.lineEdit_22 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.gridLayout.addWidget(self.lineEdit_22, 5, 1, 1, 1)

        self.lineEdit_11 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout.addWidget(self.lineEdit_11, 10, 3, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.gridLayout.addWidget(self.label_20, 6, 1, 1, 1)

        self.lineEdit_16 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout.addWidget(self.lineEdit_16, 3, 3, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 3, 1, 1)

        self.label_25 = QLabel(self.gridLayoutWidget)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout.addWidget(self.label_25, 15, 2, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 12, 0, 1, 1)

        self.label_19 = QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 2, 2, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 3, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout.addWidget(self.lineEdit_9, 8, 3, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.lineEdit_20 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.gridLayout.addWidget(self.lineEdit_20, 15, 3, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 10, 2, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout.addWidget(self.label_26, 16, 0, 1, 1)

        self.label_24 = QLabel(self.gridLayoutWidget)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout.addWidget(self.label_24, 15, 0, 1, 1)

        self.lineEdit_17 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.gridLayout.addWidget(self.lineEdit_17, 13, 1, 1, 1)

        self.lineEdit_14 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.gridLayout.addWidget(self.lineEdit_14, 12, 3, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 8, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 9, 1, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.gridLayout.addWidget(self.label_23, 14, 1, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 13, 0, 1, 1)

        self.lineEdit_10 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout.addWidget(self.lineEdit_10, 9, 3, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout.addWidget(self.label_21, 13, 2, 1, 1)

        self.lineEdit_18 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.gridLayout.addWidget(self.lineEdit_18, 13, 3, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 3, 2, 1, 1)

        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 3, 1, 1, 1)

        self.lineEdit_19 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.gridLayout.addWidget(self.lineEdit_19, 15, 1, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 11, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 2, 3, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 11, 2, 1, 1)

        self.lineEdit_7 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout.addWidget(self.lineEdit_7, 8, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout.addWidget(self.lineEdit_8, 12, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 9, 2, 1, 1)

        self.lineEdit_12 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout.addWidget(self.lineEdit_12, 11, 1, 1, 1)

        self.label_30 = QLabel(self.gridLayoutWidget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font1)

        self.gridLayout.addWidget(self.label_30, 4, 1, 1, 1)

        self.label_31 = QLabel(self.gridLayoutWidget)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout.addWidget(self.label_31, 5, 0, 1, 1)

        self.label_32 = QLabel(self.gridLayoutWidget)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout.addWidget(self.label_32, 5, 2, 1, 1)

        self.lineEdit_25 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_25.setObjectName(u"lineEdit_25")

        self.gridLayout.addWidget(self.lineEdit_25, 5, 3, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 600, 309, 24))
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 10, 311, 102))
        self.gridLayout_2 = QGridLayout(self.formLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.comboBox_2 = QComboBox(self.formLayoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_2.addWidget(self.comboBox_2, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.formLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 3, 0, 1, 1)

        self.label_27 = QLabel(self.formLayoutWidget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)

        self.gridLayout_2.addWidget(self.label_27, 0, 2, 1, 1)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_24 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_24.setObjectName(u"lineEdit_24")

        self.gridLayout_2.addWidget(self.lineEdit_24, 1, 2, 1, 1)

        self.label_29 = QLabel(self.formLayoutWidget)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_2.addWidget(self.label_29, 1, 1, 1, 1)

        self.lineEdit_23 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_23.setObjectName(u"lineEdit_23")

        self.gridLayout_2.addWidget(self.lineEdit_23, 2, 2, 1, 1)

        self.label_28 = QLabel(self.formLayoutWidget)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_2.addWidget(self.label_28, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 902, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menu.addSeparator()
        self.menu.addAction(self.action_6)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a...", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.action_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage1), QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u0440\u043e\u0441\u0442\u0430 \u0442\u0440\u0435\u0449\u0438\u043d\u044b \u043e\u0442 \u0446\u0438\u043a\u043b\u043e\u0432", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage2), QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u0440\u043e\u0441\u0442\u0430 \u0442\u0440\u0435\u0449\u0438\u043d\u044b \u0440\u0430\u0437\u043c\u0430\u0445\u0430 \u0438\u043d\u0442\u0435\u043d\u0441\u0438\u0432\u043d\u043e\u0441\u0442\u0438 \u0440\u043e\u0441\u0442\u0430 \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0439", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage3), QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"K1c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043e\u043c\u0435\u0442\u0440\u0438\u044f", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"alpha", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"a_init", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"p", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"NASGRO constant", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"n", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"a_crit", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"K0", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0434\u0438\u0443\u0441", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"K1e", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0421", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"n", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Paris constant", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"C_th+", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"C_th-", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0434\u0438\u0443\u0441 \u044d\u043b", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ak", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Bk", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"q", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0439\u0441\u0442\u0432\u0430 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"YTS", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"UTS", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0451\u0442", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0411\u043e\u043a\u043e\u0432\u0430\u044f \u0441\u043a\u0432\u043e\u0437\u043d\u0430\u044f", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0432\u043e\u0437\u043d\u0430\u044f \u0432 \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u0438", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043b\u043e\u0432\u0430\u044f \u0432 \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u0438", None))
        self.comboBox_2.setItemText(3, "")

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Walker", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"NASGRO", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Walekr and NASGRO", None))

        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0433\u0440\u0443\u0437\u043a\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u0440\u043e\u0441\u0442\u0430 \u0442\u0440\u0435\u0449\u0438\u043d\u044b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c \u0442\u0440\u0435\u0449\u0438\u043d\u044b", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"     R", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Smax", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()