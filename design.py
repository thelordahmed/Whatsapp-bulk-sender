# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(894, 1002)
        MainWindow.setMinimumSize(QSize(745, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamily(u"arial")
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"Data/imgs/whatsapp.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"/*-----QWidget-----*/\n"
"\n"
"QWidget\n"
"{\n"
"	\n"
"	background-color: qradialgradient(spread:pad, cx:0.522, cy:0.518, radius:2, fx:0.522273, fy:0.506, stop:0.0227273 rgba(23, 27, 36, 255), stop:1 rgba(0, 0, 0, 255));\n"
"	color: #ffffff;\n"
"	border-color: #051a39;\n"
"	font-family:\"arial\"\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #ffffff;\n"
"font-family:\"arial\"\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel::disabled\n"
"{\n"
"	background-color: transparent;\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenuBar-----*/\n"
"QMenuBar\n"
"{\n"
"	background-color: #0a0a0a;\n"
"	color: #ffffff;\n"
"	border-color: #051a39;\n"
"font-family:\"arial\"\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background-color: #607cf"
                        "f;\n"
"    border: 1px solid #41cd52;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background-color: #4969ff;\n"
"    border: 1px solid #000;\n"
"    margin-bottom: -1px;\n"
"    padding-bottom: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: #121212;\n"
"    border: 1px solid;\n"
"    color: #ffffff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #6d8eff;\n"
"    color: #ffffff;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    min-width : 150px;\n"
"    padding: 3px 20px 3px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    background-color: #4969ff;\n"
"    color: #ffffff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #262626;\n"
"}\n"
"\n"
"\n"
"/*-----QToolTip-----*/\n"
"QToolTip\n"
"{\n"
"	border : 1px solid #000000;\n"
"	background-color: #26264f;\n"
"	color: #ffffff;\n"
"	border"
                        "-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: #607cff;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"font-family:\"arial\"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #8399ff;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #4969ff;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton\n"
"{\n"
"	background-color: #607cff;\n"
"	color: #ffffff;\n"
"	border-width: 1px"
                        ";\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 3px;\n"
"font-family:\"arial\"\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::hover\n"
"{\n"
"	background-color: #8399ff;\n"
"	color: #ffffff;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::pressed\n"
"{\n"
"	background-color: #4969ff;\n"
"	color: #ffffff;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QComboBox-----*/\n"
"QComboBox\n"
"{\n"
"    background-color: #607cff;\n"
"    border: 1px solid;\n"
"    border-radius: 3px;\n"
"    padding-left: 6px;\n"
"    color: #ffffff;\n"
"    height: 20px;\n"
"font-family:\"arial\"\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
""
                        "\n"
"}\n"
"\n"
"\n"
"QComboBox:hover\n"
"{\n"
"    background-color: #8399ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #4969ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #383838;\n"
"    color: #ffffff;\n"
"    border: 1px solid black;\n"
"    selection-background-color: #4969ff;\n"
"    selection-color: #ffffff;\n"
"    outline: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; \n"
"    border-top-right-radius: 3px; \n"
"    border-bottom-right-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"\n"
"/*-----QSpinBox & QDoubleSpinBox & QDateTimeEdit-----*/\n"
"QSpinBox, \n"
"QDoubleSpinBox,\n"
"QDateTimeEdit\n"
"{\n"
"	background-c"
                        "olor: #525251;\n"
"	color: #ffffff;\n"
"	border: 1px solid #051a39;\n"
"	border-radius: 3px;\n"
"	padding : 2px;\n"
"font-family:\"arial\"\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::disabled, \n"
"QDoubleSpinBox::disabled,\n"
"QDateTimeEdit::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox:hover, \n"
"QDoubleSpinBox::hover,\n"
"QDateTimeEdit::hover\n"
"{\n"
"    background-color: #626262;\n"
"    border: 1px solid #607cff;\n"
"    color:  #fff;\n"
"    padding: 2px\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button,\n"
"QDoubleSpinBox::up-button, QDoubleSpinBox::down-button,\n"
"QDateTimeEdit::up-button, QDateTimeEdit::down-button\n"
"{\n"
"    background-color: #607cff;\n"
"	border-radius: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::disabled, \n"
"QDoubleSpinBox::disabled,\n"
"QDateTimeEdit::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-b"
                        "utton:hover, QSpinBox::down-button:hover,\n"
"QDoubleSpinBox::up-button:hover, QDoubleSpinBox::down-button:hover,\n"
"QDateTimeEdit::up-button:hover, QDateTimeEdit::down-button:hover\n"
"{\n"
"    background-color: #8399ff;\n"
"    border: 1px solid #8399ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:disabled, QSpinBox::down-button:disabled,\n"
"QDoubleSpinBox::up-button:disabled, QDoubleSpinBox::down-button:disabled,\n"
"QDateTimeEdit::up-button:disabled, QDateTimeEdit::down-button:disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed,\n"
"QDoubleSpinBox::up-button:pressed, QDoubleSpinBox::down-button::pressed,\n"
"QDateTimeEdit::up-button:pressed, QDateTimeEdit::down-button::pressed\n"
"{\n"
"    background-color: #4969ff;\n"
"    border: 1px solid #4969ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-arrow,\n"
"QDoubleSpinBox::down-arrow,\n"
"QDateTimeEdit::down-arrow\n"
"{\n"
"    imag"
                        "e: url(://arrow-down.png);\n"
"    width: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-arrow,\n"
"QDoubleSpinBox::up-arrow,\n"
"QDateTimeEdit::up-arrow\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"	background-color: #525251;\n"
"	color: #ffffff;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 2px;\n"
"font-family:\"arial\"\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTextEdit-----*/\n"
"QTextEdit\n"
"{\n"
"	background-color: #ffffff;\n"
"	color: #010201;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QTextEdit::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QGroupBox-----*/\n"
"QGroupBox \n"
"{\n"
"    border: "
                        "1px solid;\n"
"    border-color: #607cff;\n"
"    margin-top: 22px;\n"
"font-family:\"arial\"\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::title  \n"
"{\n"
"    background-color: #607cff;\n"
"    color: #ffffff;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 5px;\n"
"	border-top-left-radius: 3px;\n"
"	border-top-right-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::title::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 5px;\n"
"	border-top-left-radius: 3px;\n"
"	border-top-right-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*-----QRadioButton-----*/\n"
"QRadioButton::indicator::unchecked\n"
"{ \n"
"	border: 2px inset gray; \n"
"	border-radius: 5px; \n"
"	background-color:  #fff;\n"
"	width: 9px; \n"
"	height: 9px; \n"
"font-family:\"arial\"\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked:h"
                        "over\n"
"{ \n"
"	border: 2px solid #607cff; \n"
"	border-radius: 5px; \n"
"	background-color:  #fff;\n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::checked\n"
"{ \n"
"	border: 2px inset darkgray; \n"
"	border-radius: 5px; \n"
"	background-color: #4969ff; \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 2px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTableView & QTableWidget-----*/\n"
"QTableView\n"
"{\n"
"    background-color: transparent;\n"
"    border: 1px solid #32414B;\n"
"    color: #f0f0f0;\n"
"    gridline-color: #8faaff;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::disabled\n"
"{\n"
"    background-color: #242526;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QT"
                        "ableView::item:hover \n"
"{\n"
"    background-color: #26264f;\n"
"    color: #f0f0f0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected \n"
"{\n"
"    background-color: #1a1b1c;\n"
"    border: 2px solid #4969ff;\n"
"    color: #F0F0F0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected:disabled\n"
"{\n"
"    background-color: #1a1b1c;\n"
"    border: 2px solid #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: #505050;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #525251;\n"
"    color: #fff;\n"
"    text-align: left;\n"
"	padding: 4px;\n"
"	\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    color: #fff;\n"
"    background-color: #4969ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked:disabled\n"
"{\n"
"    color: #656565;\n"
"    background-color: #5"
                        "25251;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTabWidget-----*/\n"
"QTabBar::tab\n"
"{\n"
"	background-color: transparent;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-top-left-radius: 3px;\n"
"	border-top-right-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane \n"
"{\n"
"	background-color: red;\n"
"	color: #ffffff;\n"
""
                        "    border: 1px solid;\n"
"    border-color: #607cff;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    background-color: #607cff;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-top-left-radius: 3px;\n"
"	border-top-right-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected:disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected \n"
"{\n"
"    background-color: #262626;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected:hover \n"
"{\n"
"    background-color: #8399ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top:!selected \n"
"{\n"
"    margin-top: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:bottom:!selected \n"
"{\n"
"    margin-bottom: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom \n"
"{\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top:selected \n"
"{\n"
"    bo"
                        "rder-bottom-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:bottom:selected \n"
"{\n"
"    border-top-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one \n"
"{\n"
"    margin-right: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left:!selected \n"
"{\n"
"    margin-right: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    margin-left: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right \n"
"{\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left:selected \n"
"{\n"
"    border-left-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:right:selected \n"
"{\n"
"    border-right-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one \n"
"{\n"
"    margin-bottom: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSlider-----*/\n"
"QSli"
                        "der::groove:horizontal \n"
"{\n"
"	background-color: transparent;\n"
"	height: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal \n"
"{\n"
"	background-color: #607cff;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal \n"
"{\n"
"	background-color: #666765;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal \n"
"{\n"
"	background-color: #607cff;\n"
"	width: 14px;\n"
"	margin-top: -6px;\n"
"	margin-bottom: -6px;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:hover \n"
"{\n"
"	background-color: #607cff;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal:disabled \n"
"{\n"
"	background-color: #bbb;\n"
"	border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal:disabled \n"
"{\n"
"	background-color: #eee;\n"
"	border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:disabled \n"
"{\n"
"	background-color: #eee;\n"
"	border: 1px solid #aaa;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::groove:vertical \n"
""
                        "{\n"
"	background-color: transparent;\n"
"	width: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:vertical \n"
"{\n"
"	background-color: #607cff;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:vertical \n"
"{\n"
"	background-color: #666765;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:vertical \n"
"{\n"
"	background-color: #607cff;\n"
"	height: 14px;\n"
"	margin-left: -6px;\n"
"	margin-right: -6px;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:vertical:hover \n"
"{\n"
"	background-color: #607cff;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:vertical:disabled \n"
"{\n"
"	background-color: #bbb;\n"
"	border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:vertical:disabled \n"
"{\n"
"	background-color: #eee;\n"
"	border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:vertical:disabled \n"
"{\n"
"	background-color: #eee;\n"
"	border: 1px solid #aaa;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QDial-----*/\n"
"QDial\n"
"{\n"
"	background-color: #607cff;\n"
""
                        "\n"
"}\n"
"\n"
"\n"
"QDial::disabled\n"
"{\n"
"	background-color: #404040;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal\n"
"{\n"
"    border: 1px solid #222222;\n"
"    background-color: #3d3d3d;\n"
"    height: 13px;\n"
"    margin: 0px 16px 0 16px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background: #607cff;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #607cff;\n"
"    width: 14px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #607cff;\n"
"    width: 14px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-right.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrol"
                        "lBar::left-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-left.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #3d3d3d;\n"
"    width: 13px;\n"
"    margin: 16px 0 16px 0;\n"
"    border: 1px solid #222222;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #607cff;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #607cff;\n"
"    height: 14px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #607cff;\n"
"    height: 14px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:ver"
                        "tical\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QProgressBar-----*/\n"
"QProgressBar\n"
"{\n"
"	background-color: #383838;\n"
"	color: #ffffff;\n"
"	border: 1px solid #607cff;\n"
"	border-radius: 3px;\n"
"	text-align: center;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: #607cff;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk:disabled {\n"
"	background-color: #656565;\n"
"	border: 1px solid #aaa;\n"
"	color: #656565;\n"
"}\n"
"\n"
"\n"
"/*-----QStatusBar-----*/\n"
"QStatusBar\n"
"{\n"
"	background-color: #0a0a0a;\n"
"	color: #ffffff;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"QFrame{\n"
"	background:transparent;\n"
"}")
        self.horizontalLayout_8 = QHBoxLayout(self.main_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, -1, -1)
        self.listWidget = QListWidget(self.main_frame)
        icon1 = QIcon()
        icon1.addFile(u":/white-icons/Data/imgs/white icons/icons8-home-page-500.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qlistwidgetitem.setIcon(icon1);
        icon2 = QIcon()
        icon2.addFile(u":/white-icons/Data/imgs/white icons/icons8-combo-chart-500.png", QSize(), QIcon.Normal, QIcon.Off)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qlistwidgetitem1.setBackground(brush);
        __qlistwidgetitem1.setIcon(icon2);
        icon3 = QIcon()
        icon3.addFile(u":/white-icons/Data/imgs/white icons/icons8-clock-500.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setIcon(icon3);
        icon4 = QIcon()
        icon4.addFile(u":/white-icons/Data/imgs/white icons/icons8-verified-account-500.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem3.setIcon(icon4);
        icon5 = QIcon()
        icon5.addFile(u":/white-icons/Data/imgs/white icons/icons8-idea-500.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem4.setIcon(icon5);
        icon6 = QIcon()
        icon6.addFile(u":/white-icons/Data/imgs/white icons/icons8-about-500.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem5 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem5.setIcon(icon6);
        __qlistwidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy1)
        self.listWidget.setMinimumSize(QSize(200, 0))
        self.listWidget.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamily(u"arial")
        font1.setPointSize(19)
        font1.setBold(True)
        font1.setWeight(75)
        self.listWidget.setFont(font1)
        self.listWidget.setMouseTracking(False)
        self.listWidget.setLayoutDirection(Qt.LeftToRight)
        self.listWidget.setStyleSheet(u"QListView {\n"
"    background:transparent;\n"
"	\n"
"\n"
"}\n"
"\n"
"::item{\n"
"width:100px;\n"
"height:90px;\n"
"\n"
"\n"
"}\n"
"\n"
"::item:disabled{\n"
"width:100px;\n"
"height:130px;\n"
"background:rgb(71, 71, 71)\n"
"}\n"
"\n"
"")
        self.listWidget.setFrameShape(QFrame.Box)
        self.listWidget.setFrameShadow(QFrame.Raised)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setAutoScrollMargin(16)
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setTabKeyNavigation(False)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setDragEnabled(False)
        self.listWidget.setDragDropOverwriteMode(False)
        self.listWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.listWidget.setAlternatingRowColors(False)
        self.listWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.listWidget.setIconSize(QSize(86, 56))
        self.listWidget.setTextElideMode(Qt.ElideMiddle)
        self.listWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.listWidget.setMovement(QListView.Static)
        self.listWidget.setFlow(QListView.TopToBottom)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setResizeMode(QListView.Adjust)
        self.listWidget.setLayoutMode(QListView.SinglePass)
        self.listWidget.setSpacing(0)
        self.listWidget.setViewMode(QListView.ListMode)
        self.listWidget.setModelColumn(0)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setBatchSize(100)
        self.listWidget.setWordWrap(False)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setSortingEnabled(False)

        self.horizontalLayout_8.addWidget(self.listWidget)

        self.tabWidget = QTabWidget(self.main_frame)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget.setStyleSheet(u"\n"
"QTabWidget::tab-bar {\n"
"   height:0;\n"
"	width:0;\n"
"}")
        self.tabWidget.setTabPosition(QTabWidget.East)
        self.tabWidget.setIconSize(QSize(0, 0))
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.main_tab = QWidget()
        self.main_tab.setObjectName(u"main_tab")
        self.main_tab.setMaximumSize(QSize(16777215, 16777215))
        self.main_tab.setAutoFillBackground(False)
        self.verticalLayout_6 = QVBoxLayout(self.main_tab)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.frame = QFrame(self.main_tab)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setSizeIncrement(QSize(0, 0))
        self.frame.setBaseSize(QSize(0, 0))
        self.frame.setFont(font)
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(-1, 20, -1, 0)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"background:transparent;\n"
"}")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 10, -1, 10)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.sheet_le = QLineEdit(self.groupBox)
        self.sheet_le.setObjectName(u"sheet_le")
        self.sheet_le.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.sheet_le)

        self.sheet_btn = QToolButton(self.groupBox)
        self.sheet_btn.setObjectName(u"sheet_btn")

        self.horizontalLayout_4.addWidget(self.sheet_btn)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setFamily(u"arial")
        font2.setBold(True)
        font2.setWeight(75)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color:yellow")

        self.verticalLayout.addWidget(self.label_5)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_2.setFont(font)
        self.horizontalLayout_14 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(5, 5, 5, 5)
        self.frame1 = QFrame(self.groupBox_2)
        self.frame1.setObjectName(u"frame1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy4)
        self.verticalLayout_2 = QVBoxLayout(self.frame1)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.frame1)
        self.label.setObjectName(u"label")
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setMaximumSize(QSize(50, 16777215))
        self.label.setFont(font)

        self.horizontalLayout_5.addWidget(self.label, 0, Qt.AlignHCenter)

        self.messages_sbox = QSpinBox(self.frame1)
        self.messages_sbox.setObjectName(u"messages_sbox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.messages_sbox.sizePolicy().hasHeightForWidth())
        self.messages_sbox.setSizePolicy(sizePolicy5)
        self.messages_sbox.setMaximumSize(QSize(16777215, 16777215))
        self.messages_sbox.setMinimum(0)
        self.messages_sbox.setMaximum(1000)
        self.messages_sbox.setValue(100)

        self.horizontalLayout_5.addWidget(self.messages_sbox, 0, Qt.AlignLeft)

        self.label_2 = QLabel(self.frame1)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setMaximumSize(QSize(120, 16777215))
        self.label_2.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.minutes_sbox = QSpinBox(self.frame1)
        self.minutes_sbox.setObjectName(u"minutes_sbox")
        sizePolicy5.setHeightForWidth(self.minutes_sbox.sizePolicy().hasHeightForWidth())
        self.minutes_sbox.setSizePolicy(sizePolicy5)
        self.minutes_sbox.setMaximumSize(QSize(16777215, 16777215))
        self.minutes_sbox.setMinimum(1)
        self.minutes_sbox.setMaximum(1000)
        self.minutes_sbox.setValue(30)

        self.horizontalLayout_5.addWidget(self.minutes_sbox, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.frame1)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setMaximumSize(QSize(100, 16777215))
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(False)

        self.horizontalLayout_5.addWidget(self.label_4, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.checkBox = QCheckBox(self.frame1)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.repeat_sending = QCheckBox(self.frame1)
        self.repeat_sending.setObjectName(u"repeat_sending")

        self.verticalLayout_2.addWidget(self.repeat_sending)


        self.horizontalLayout_14.addWidget(self.frame1)

        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy6)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.chrome_rb = QRadioButton(self.groupBox_5)
        self.chrome_rb.setObjectName(u"chrome_rb")
        self.chrome_rb.setChecked(True)

        self.verticalLayout_13.addWidget(self.chrome_rb)

        self.firefox_rb = QRadioButton(self.groupBox_5)
        self.firefox_rb.setObjectName(u"firefox_rb")

        self.verticalLayout_13.addWidget(self.firefox_rb)


        self.horizontalLayout_14.addWidget(self.groupBox_5)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMaximumSize(QSize(16777215, 16777215))
        self.formLayout = QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(5)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.attachments_le = QLineEdit(self.groupBox_3)
        self.attachments_le.setObjectName(u"attachments_le")
        self.attachments_le.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.attachments_le)

        self.attachments_btn = QToolButton(self.groupBox_3)
        self.attachments_btn.setObjectName(u"attachments_btn")

        self.horizontalLayout_2.addWidget(self.attachments_btn)


        self.formLayout.setLayout(0, QFormLayout.SpanningRole, self.horizontalLayout_2)

        self.contact_groupbox = QGroupBox(self.groupBox_3)
        self.contact_groupbox.setObjectName(u"contact_groupbox")
        self.contact_groupbox.setMinimumSize(QSize(200, 0))
        self.contact_groupbox.setCheckable(True)
        self.contact_groupbox.setChecked(False)
        self.horizontalLayout = QHBoxLayout(self.contact_groupbox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 5)
        self.contactCard_le = QLineEdit(self.contact_groupbox)
        self.contactCard_le.setObjectName(u"contactCard_le")
        sizePolicy2.setHeightForWidth(self.contactCard_le.sizePolicy().hasHeightForWidth())
        self.contactCard_le.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.contactCard_le)


        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.contact_groupbox)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, -1, -1)
        self.textFirst_rb = QRadioButton(self.groupBox_3)
        self.textFirst_rb.setObjectName(u"textFirst_rb")
        self.textFirst_rb.setChecked(True)

        self.horizontalLayout_12.addWidget(self.textFirst_rb)

        self.textCaption_rb = QRadioButton(self.groupBox_3)
        self.textCaption_rb.setObjectName(u"textCaption_rb")

        self.horizontalLayout_12.addWidget(self.textCaption_rb)


        self.formLayout.setLayout(2, QFormLayout.SpanningRole, self.horizontalLayout_12)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.frame)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.pushButton = QPushButton(self.groupBox_4)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.append_newmessage = QPushButton(self.groupBox_4)
        self.append_newmessage.setObjectName(u"append_newmessage")

        self.horizontalLayout_3.addWidget(self.append_newmessage)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.message_text = QPlainTextEdit(self.groupBox_4)
        self.message_text.setObjectName(u"message_text")
        self.message_text.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_4.addWidget(self.message_text)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.multi_messages_le = QLineEdit(self.groupBox_4)
        self.multi_messages_le.setObjectName(u"multi_messages_le")
        self.multi_messages_le.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.multi_messages_le)

        self.multi_messages_btn = QToolButton(self.groupBox_4)
        self.multi_messages_btn.setObjectName(u"multi_messages_btn")

        self.horizontalLayout_6.addWidget(self.multi_messages_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.verticalLayout_5.addWidget(self.groupBox_4)

        self.verticalLayout_5.setStretch(3, 1)

        self.verticalLayout_6.addWidget(self.frame)

        self.tabWidget.addTab(self.main_tab, "")
        self.report_tab = QWidget()
        self.report_tab.setObjectName(u"report_tab")
        self.verticalLayout_7 = QVBoxLayout(self.report_tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tableWidget = QTableWidget(self.report_tab)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        icon7 = QIcon()
        icon7.addFile(u":/white-icons/Data/imgs/white icons/icons8-contacts-500.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setIcon(icon7);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        icon8 = QIcon()
        icon8.addFile(u":/white-icons/Data/imgs/white icons/icons8-phone-500.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setIcon(icon8);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setIcon(icon6);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(125)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_7.addWidget(self.tableWidget)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.csv_btn = QPushButton(self.report_tab)
        self.csv_btn.setObjectName(u"csv_btn")
        self.csv_btn.setMaximumSize(QSize(150, 16777215))
        icon9 = QIcon()
        icon9.addFile(u":/white-icons/Data/imgs/white icons/icons8-save-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.csv_btn.setIcon(icon9)
        self.csv_btn.setIconSize(QSize(22, 22))

        self.horizontalLayout_9.addWidget(self.csv_btn)

        self.newsession_btn = QPushButton(self.report_tab)
        self.newsession_btn.setObjectName(u"newsession_btn")
        self.newsession_btn.setMaximumSize(QSize(150, 16777215))
        icon10 = QIcon()
        icon10.addFile(u":/white-icons/Data/imgs/white icons/icons8-trash-can-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newsession_btn.setIcon(icon10)
        self.newsession_btn.setIconSize(QSize(19, 18))

        self.horizontalLayout_9.addWidget(self.newsession_btn)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.tabWidget.addTab(self.report_tab, "")
        self.schedule_tab = QWidget()
        self.schedule_tab.setObjectName(u"schedule_tab")
        self.time_groupBox = QGroupBox(self.schedule_tab)
        self.time_groupBox.setObjectName(u"time_groupBox")
        self.time_groupBox.setGeometry(QRect(100, 180, 301, 108))
        self.time_groupBox.setCheckable(True)
        self.time_groupBox.setChecked(False)
        self.verticalLayout_8 = QVBoxLayout(self.time_groupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_3 = QLabel(self.time_groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_10.addWidget(self.label_3)

        self.from_time = QTimeEdit(self.time_groupBox)
        self.from_time.setObjectName(u"from_time")

        self.horizontalLayout_10.addWidget(self.from_time)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_6 = QLabel(self.time_groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_11.addWidget(self.label_6)

        self.to_time = QTimeEdit(self.time_groupBox)
        self.to_time.setObjectName(u"to_time")

        self.horizontalLayout_11.addWidget(self.to_time)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.tabWidget.addTab(self.schedule_tab, "")
        self.recent_tab = QWidget()
        self.recent_tab.setObjectName(u"recent_tab")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.recent_tab.sizePolicy().hasHeightForWidth())
        self.recent_tab.setSizePolicy(sizePolicy7)
        self.verticalLayout_3 = QVBoxLayout(self.recent_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalWidget = QWidget(self.recent_tab)
        self.verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy8)
        self.verticalWidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_14 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, -1, -1, 1)
        self.recent_tablewidgeet = QTableWidget(self.verticalWidget)
        if (self.recent_tablewidgeet.columnCount() < 2):
            self.recent_tablewidgeet.setColumnCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.recent_tablewidgeet.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.recent_tablewidgeet.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        self.recent_tablewidgeet.setObjectName(u"recent_tablewidgeet")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.recent_tablewidgeet.sizePolicy().hasHeightForWidth())
        self.recent_tablewidgeet.setSizePolicy(sizePolicy9)
        self.recent_tablewidgeet.setStyleSheet(u"")
        self.recent_tablewidgeet.horizontalHeader().setMinimumSectionSize(18)
        self.recent_tablewidgeet.horizontalHeader().setDefaultSectionSize(200)
        self.recent_tablewidgeet.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_14.addWidget(self.recent_tablewidgeet)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, -1, -1, 0)
        self.recent_export_btn = QPushButton(self.verticalWidget)
        self.recent_export_btn.setObjectName(u"recent_export_btn")
        sizePolicy10 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.recent_export_btn.sizePolicy().hasHeightForWidth())
        self.recent_export_btn.setSizePolicy(sizePolicy10)
        self.recent_export_btn.setIcon(icon9)
        self.recent_export_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_15.addWidget(self.recent_export_btn)

        self.recent_clear_btn = QPushButton(self.verticalWidget)
        self.recent_clear_btn.setObjectName(u"recent_clear_btn")
        sizePolicy10.setHeightForWidth(self.recent_clear_btn.sizePolicy().hasHeightForWidth())
        self.recent_clear_btn.setSizePolicy(sizePolicy10)
        icon11 = QIcon()
        icon11.addFile(u":/white-icons/Data/imgs/white icons/icons8-trash-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.recent_clear_btn.setIcon(icon11)
        self.recent_clear_btn.setIconSize(QSize(20, 25))

        self.horizontalLayout_15.addWidget(self.recent_clear_btn)

        self.horizontalLayout_15.setStretch(0, 3)
        self.horizontalLayout_15.setStretch(1, 1)

        self.verticalLayout_14.addLayout(self.horizontalLayout_15)


        self.verticalLayout_3.addWidget(self.verticalWidget)

        self.recent_extract_btn = QPushButton(self.recent_tab)
        self.recent_extract_btn.setObjectName(u"recent_extract_btn")
        sizePolicy5.setHeightForWidth(self.recent_extract_btn.sizePolicy().hasHeightForWidth())
        self.recent_extract_btn.setSizePolicy(sizePolicy5)
        self.recent_extract_btn.setStyleSheet(u"padding:10px 30px")

        self.verticalLayout_3.addWidget(self.recent_extract_btn, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.recent_tab, "")
        self.instructions_tab = QWidget()
        self.instructions_tab.setObjectName(u"instructions_tab")
        self.verticalLayout_11 = QVBoxLayout(self.instructions_tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 50, -1, -1)
        self.textBrowser_2 = QTextBrowser(self.instructions_tab)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.verticalLayout_12.addWidget(self.textBrowser_2)


        self.verticalLayout_11.addLayout(self.verticalLayout_12)

        self.tabWidget.addTab(self.instructions_tab, "")
        self.about_tab = QWidget()
        self.about_tab.setObjectName(u"about_tab")
        self.verticalLayout_9 = QVBoxLayout(self.about_tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 50, -1, -1)
        self.textEdit_2 = QTextEdit(self.about_tab)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(16777215, 140))
        self.textEdit_2.setStyleSheet(u"background:transparent;\n"
"color:white;\n"
"\n"
"")
        self.textEdit_2.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_10.addWidget(self.textEdit_2)

        self.textBrowser_4 = QTextBrowser(self.about_tab)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setStyleSheet(u"background:transparent;\n"
"color:white;\n"
"border:transparent\n"
"\n"
"")
        self.textBrowser_4.setOpenExternalLinks(True)

        self.verticalLayout_10.addWidget(self.textBrowser_4)


        self.verticalLayout_9.addLayout(self.verticalLayout_10)

        self.tabWidget.addTab(self.about_tab, "")

        self.horizontalLayout_8.addWidget(self.tabWidget)


        self.gridLayout_2.addWidget(self.main_frame, 0, 0, 1, 3)

        self.buttons_frame = QFrame(self.centralwidget)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setStyleSheet(u"QFrame{\n"
"	background:transparent\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.buttons_frame)
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.start_btn = QPushButton(self.buttons_frame)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setMaximumSize(QSize(16777215, 45))
        icon12 = QIcon()
        icon12.addFile(u":/black-icons/Data/imgs/black icons/icons8-play-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.start_btn.setIcon(icon12)
        self.start_btn.setIconSize(QSize(34, 48))

        self.horizontalLayout_7.addWidget(self.start_btn)

        self.stop_btn = QPushButton(self.buttons_frame)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setMaximumSize(QSize(16777215, 45))
        icon13 = QIcon()
        icon13.addFile(u":/black-icons/Data/imgs/black icons/icons8-stop-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_btn.setIcon(icon13)
        self.stop_btn.setIconSize(QSize(38, 37))

        self.horizontalLayout_7.addWidget(self.stop_btn)


        self.gridLayout_2.addWidget(self.buttons_frame, 1, 1, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, -1)
        self.commandLinkButton = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        sizePolicy11 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.commandLinkButton.sizePolicy().hasHeightForWidth())
        self.commandLinkButton.setSizePolicy(sizePolicy11)
        self.commandLinkButton.setMaximumSize(QSize(16777215, 25))
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"background: transparent;\n"
"border:0")
        icon14 = QIcon()
        iconThemeName = u";"
        if QIcon.hasThemeIcon(iconThemeName):
            icon14 = QIcon.fromTheme(iconThemeName)
        else:
            icon14.addFile(u"../Yellow Pages sg", QSize(), QIcon.Normal, QIcon.Off)
        
        self.commandLinkButton.setIcon(icon14)

        self.horizontalLayout_13.addWidget(self.commandLinkButton, 0, Qt.AlignLeft)

        self.logout_btn = QPushButton(self.centralwidget)
        self.logout_btn.setObjectName(u"logout_btn")
        sizePolicy12 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.logout_btn.sizePolicy().hasHeightForWidth())
        self.logout_btn.setSizePolicy(sizePolicy12)
        font3 = QFont()
        font3.setFamily(u"arial")
        font3.setBold(False)
        font3.setWeight(50)
        self.logout_btn.setFont(font3)
        self.logout_btn.setStyleSheet(u"margin-right : 20px")

        self.horizontalLayout_13.addWidget(self.logout_btn, 0, Qt.AlignRight)


        self.gridLayout_2.addLayout(self.horizontalLayout_13, 3, 0, 1, 3)

        self.license_frame = QFrame(self.centralwidget)
        self.license_frame.setObjectName(u"license_frame")
        sizePolicy.setHeightForWidth(self.license_frame.sizePolicy().hasHeightForWidth())
        self.license_frame.setSizePolicy(sizePolicy)
        self.license_frame.setStyleSheet(u"QFrame{\n"
"	background:transparent\n"
"}")
        self._2 = QVBoxLayout(self.license_frame)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(100, 100, 100, 0)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(-1, 0, -1, -1)
        self.license_le = QLineEdit(self.license_frame)
        self.license_le.setObjectName(u"license_le")
        self.license_le.setStyleSheet(u"padding:7px;\n"
"font-size:14px")

        self.horizontalLayout_25.addWidget(self.license_le)

        self.license_btn = QPushButton(self.license_frame)
        self.license_btn.setObjectName(u"license_btn")
        self.license_btn.setStyleSheet(u"padding:8px;\n"
"font-weight:bold")

        self.horizontalLayout_25.addWidget(self.license_btn)


        self._2.addLayout(self.horizontalLayout_25)

        self.license_status_label = QTextBrowser(self.license_frame)
        self.license_status_label.setObjectName(u"license_status_label")
        sizePolicy7.setHeightForWidth(self.license_status_label.sizePolicy().hasHeightForWidth())
        self.license_status_label.setSizePolicy(sizePolicy7)
        self.license_status_label.setMinimumSize(QSize(0, 100))
        self.license_status_label.setMaximumSize(QSize(16777215, 100))
        self.license_status_label.setStyleSheet(u"color:#e63c41;\n"
"font-weight:bold;\n"
"border:none;\n"
"")

        self._2.addWidget(self.license_status_label)


        self.gridLayout_2.addWidget(self.license_frame, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.listWidget.currentRowChanged.connect(self.tabWidget.setCurrentIndex)

        self.listWidget.setCurrentRow(-1)
        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WhatsApp Bulk Sender 2.0", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Main", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Report", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Schedule", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Ext. Recent", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Instructions", None));
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"About", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Choose the contacts source", None))
        self.sheet_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"xlsx or CSV (comma seperated)", None))
        self.sheet_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"* phone numbers must be in column B", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Send ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Messages Every", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"  Minutes", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Anonymous Sending", None))
        self.repeat_sending.setText(QCoreApplication.translate("MainWindow", u"Repeat sending every 24 hours", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Browser (*must be installed on system)", None))
        self.chrome_rb.setText(QCoreApplication.translate("MainWindow", u"Google Chrome", None))
        self.firefox_rb.setText(QCoreApplication.translate("MainWindow", u"Firefox (QR code not saved)", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Send Attachments", None))
        self.attachments_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Images, videos, documents", None))
        self.attachments_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.contact_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Contacts Card Sending", None))
        self.contactCard_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type numbers seperated by comma \",\" for multiple cards...", None))
        self.textFirst_rb.setText(QCoreApplication.translate("MainWindow", u"Send text before attachments", None))
        self.textCaption_rb.setText(QCoreApplication.translate("MainWindow", u"Send text as caption", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"The Message", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Append {name}", None))
        self.append_newmessage.setText(QCoreApplication.translate("MainWindow", u"new message", None))
        self.multi_messages_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose multiple messages - txt only (optional)", None))
        self.multi_messages_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main_tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.csv_btn.setText(QCoreApplication.translate("MainWindow", u"CSV Export", None))
        self.newsession_btn.setText(QCoreApplication.translate("MainWindow", u"Start New Session", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.report_tab), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.time_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Time Range", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.schedule_tab), QCoreApplication.translate("MainWindow", u"Page", None))
        ___qtablewidgetitem3 = self.recent_tablewidgeet.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem4 = self.recent_tablewidgeet.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
        self.recent_export_btn.setText(QCoreApplication.translate("MainWindow", u"CSV Export", None))
        self.recent_clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.recent_extract_btn.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.recent_tab), QCoreApplication.translate("MainWindow", u"Page", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'arial'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:18pt; font-weight:600; color:#ffffff;\">In the excel sheet ... numbers must be in column B and names (if available) in column A</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:18pt; font-weight:600; color:#ffffff;\">---------------------------------------------------</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; ma"
                        "rgin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:18pt; font-weight:600; color:#ffffff;\">Sending to numbers that are not saved on phone book requires country code with the number, like this (+491721xxxxx) or (491721xxxxx)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:18pt; font-weight:600; color:#ffffff;\">---------------------------------------------------</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:18pt; font-weight:600; color:#ffffff;\">Make sure that you're not opening the software twice on the Task bar</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block"
                        "-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:18pt; font-weight:600; color:#ffffff;\">---------------------------------------------------</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:18pt; font-weight:600; color:#ffffff;\">If you want to open the software twice to send from two numbers, just copy the software folder into another folder and logout by clicking on &quot;Logout from current whatsapp&quot; then sign in with the other number</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.instructions_tab), QCoreApplication.translate("MainWindow", u"Page", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'arial'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:22pt; font-weight:600;\">If you face any problem or requiring a custom functionality, just contact me anytime</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:22pt; font-weight:600;\"><br />Thank You &lt;3</span></p></body></html>", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'arial'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Helvetica'; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Helvetica'; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" styl"
                        "e=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:18pt; font-weight:600;\">- Contact Me -</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Helvetica'; font-size:16pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600; color:#00ff7f;\">Whatsapp</span><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600;\"> : </span><a href=\"https://web.whatsapp.com/send?phone=201120641378\"><span style=\" font-family:'Helvetica'; font-size:12pt; text-decoration: underline; color:#0000ff;\">+201120641378</span></a></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:"
                        "empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Helvetica'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600; color:#5e81ff;\">Facebook</span><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600;\"> : </span><a href=\"https://www.facebook.com/lord.ahmed110\"><span style=\" font-family:'Helvetica'; font-size:12pt; text-decoration: underline; color:#0000ff;\">fb.com/lord.ahmed110</span></a></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Helvetica'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;"
                        " margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600; color:#ffaa00;\">Fiverr</span><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600;\"> : </span><a href=\"https://www.fiverr.com/lordahmed\"><span style=\" font-family:'Helvetica'; font-size:12pt; text-decoration: underline; color:#0000ff;\">Fiverr.com/lordahmed</span></a></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about_tab), QCoreApplication.translate("MainWindow", u"Page", None))
        self.start_btn.setText("")
        self.stop_btn.setText("")
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Copyright 2020 LorDAhmeD", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"Logout from current Whatsapp", None))
        self.license_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your License key", None))
        self.license_btn.setText(QCoreApplication.translate("MainWindow", u"Activate", None))
    # retranslateUi

