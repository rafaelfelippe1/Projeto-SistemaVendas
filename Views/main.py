# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(QtCore.QSize(900, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 700))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/icon.ico"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow {\n"
                                 "background: url(\"Images/bg.png\") 0 0 no-repeat #0884c2\n"
                                 "}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.wd_topo = QtWidgets.QWidget(self.centralwidget)
        self.wd_topo.setGeometry(QtCore.QRect(0, 0, 1000, 60))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.wd_topo.sizePolicy().hasHeightForWidth())
        self.wd_topo.setSizePolicy(sizePolicy)
        self.wd_topo.setStyleSheet("background: #4E4E4E")
        self.wd_topo.setObjectName("wd_topo")
        self.lb_Data = QtWidgets.QLabel(self.wd_topo)
        self.lb_Data.setGeometry(QtCore.QRect(590, 10, 70, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_Data.setFont(font)
        self.lb_Data.setStyleSheet("color: #fff")
        self.lb_Data.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_Data.setObjectName("lb_Data")
        self.lb_DiaSemana = QtWidgets.QLabel(self.wd_topo)
        self.lb_DiaSemana.setGeometry(QtCore.QRect(590, 35, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        self.lb_DiaSemana.setFont(font)
        self.lb_DiaSemana.setStyleSheet("color: #fff")
        self.lb_DiaSemana.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_DiaSemana.setObjectName("lb_DiaSemana")
        self.bt_Home = QtWidgets.QPushButton(self.wd_topo)
        self.bt_Home.setGeometry(QtCore.QRect(5, 5, 50, 50))
        self.bt_Home.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_Home.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Home.setStyleSheet("QPushButton{\n"
                                   "\n"
                                   "border: none;\n"
                                   "color: #FFF\n"
                                   "}\n"
                                   "QPushButton:hover {\n"
                                   "background: #7AB32E\n"
                                   "}")
        self.bt_Home.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../RSP/Images/home.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_Home.setIcon(icon1)
        self.bt_Home.setFlat(True)
        self.bt_Home.setObjectName("bt_Home")
        self.lb_NomeFantasia = QtWidgets.QLabel(self.wd_topo)
        self.lb_NomeFantasia.setGeometry(QtCore.QRect(60, 10, 220, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_NomeFantasia.setFont(font)
        self.lb_NomeFantasia.setStyleSheet("color: #FFF")
        self.lb_NomeFantasia.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_NomeFantasia.setObjectName("lb_NomeFantasia")
        self.lb_NomeFantasia2 = QtWidgets.QLabel(self.wd_topo)
        self.lb_NomeFantasia2.setGeometry(QtCore.QRect(60, 30, 220, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lb_NomeFantasia2.setFont(font)
        self.lb_NomeFantasia2.setStyleSheet("color: #FFF")
        self.lb_NomeFantasia2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_NomeFantasia2.setObjectName("lb_NomeFantasia2")
        self.bt_Exit = QtWidgets.QPushButton(self.wd_topo)
        self.bt_Exit.setGeometry(QtCore.QRect(950, 5, 50, 50))
        self.bt_Exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_Exit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Exit.setWhatsThis("")
        self.bt_Exit.setStyleSheet("QPushButton{\n"
                                   "\n"
                                   "border: none;\n"
                                   "color: #FFF\n"
                                   "}\n"
                                   "QPushButton:hover {\n"
                                   "background: #7AB32E\n"
                                   "}")
        self.bt_Exit.setText("")
        self.bt_Exit.setFlat(True)
        self.bt_Exit.setObjectName("bt_Exit")
        self.lb_userName = QtWidgets.QLabel(self.wd_topo)
        self.lb_userName.setGeometry(QtCore.QRect(670, 30, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        self.lb_userName.setFont(font)
        self.lb_userName.setStyleSheet("color: #FFF")
        self.lb_userName.setText("")
        self.lb_userName.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lb_userName.setObjectName("lb_userName")
        self.bt_logout = QtWidgets.QPushButton(self.wd_topo)
        self.bt_logout.setGeometry(QtCore.QRect(900, 5, 50, 50))
        self.bt_logout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_logout.setStyleSheet("QPushButton{\n"
                                     "\n"
                                     "border: none;\n"
                                     "color: #FFF\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "background: #cacaca\n"
                                     "}")
        self.bt_logout.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Images/Images/logout.svg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_logout.setIcon(icon2)
        self.bt_logout.setIconSize(QtCore.QSize(50, 40))
        self.bt_logout.setObjectName("bt_logout")
        self.lb_userName_2 = QtWidgets.QLabel(self.wd_topo)
        self.lb_userName_2.setGeometry(QtCore.QRect(670, 10, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_userName_2.setFont(font)
        self.lb_userName_2.setStyleSheet("color: #FFF")
        self.lb_userName_2.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lb_userName_2.setObjectName("lb_userName_2")
        self.bt_alterSenha = QtWidgets.QPushButton(self.wd_topo)
        self.bt_alterSenha.setGeometry(QtCore.QRect(840, 5, 50, 50))
        self.bt_alterSenha.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_alterSenha.setStyleSheet("QPushButton{\n"
                                         "\n"
                                         "border: none;\n"
                                         "color: #FFF\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #cacaca\n"
                                         "}")
        self.bt_alterSenha.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(
            ":/Images/Images/altersenha.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_alterSenha.setIcon(icon3)
        self.bt_alterSenha.setIconSize(QtCore.QSize(50, 40))
        self.bt_alterSenha.setObjectName("bt_alterSenha")
        self.wd_menu = QtWidgets.QWidget(self.centralwidget)
        self.wd_menu.setGeometry(QtCore.QRect(0, 60, 1000, 40))
        self.wd_menu.setStyleSheet("background: #40a286")
        self.wd_menu.setObjectName("wd_menu")
        self.bt_MainProdutos = QtWidgets.QPushButton(self.wd_menu)
        self.bt_MainProdutos.setGeometry(QtCore.QRect(420, 0, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.bt_MainProdutos.setFont(font)
        self.bt_MainProdutos.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_MainProdutos.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_MainProdutos.setAutoFillBackground(False)
        self.bt_MainProdutos.setStyleSheet("QPushButton{\n"
                                           "background: 40A286 ;\n"
                                           "border: none;\n"
                                           "color: #FFF\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "background: #7AB32E\n"
                                           "}\n"
                                           "QPushButton:disabled {\n"
                                           "background: #7AB32E\n"
                                           "}")
        self.bt_MainProdutos.setFlat(True)
        self.bt_MainProdutos.setObjectName("bt_MainProdutos")
        self.bt_Vendas = QtWidgets.QPushButton(self.wd_menu)
        self.bt_Vendas.setGeometry(QtCore.QRect(140, 0, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.bt_Vendas.setFont(font)
        self.bt_Vendas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_Vendas.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Vendas.setAutoFillBackground(False)
        self.bt_Vendas.setStyleSheet("QPushButton{\n"
                                     "background: 40A286 ;\n"
                                     "border: none;\n"
                                     "color: #FFF\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "background: #7AB32E\n"
                                     "}\n"
                                     "QPushButton:disabled {\n"
                                     "background: #7AB32E\n"
                                     "}")
        self.bt_Vendas.setFlat(True)
        self.bt_Vendas.setObjectName("bt_Vendas")
        self.bt_Compras = QtWidgets.QPushButton(self.wd_menu)
        self.bt_Compras.setGeometry(QtCore.QRect(560, 0, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.bt_Compras.setFont(font)
        self.bt_Compras.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_Compras.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Compras.setAutoFillBackground(False)
        self.bt_Compras.setStyleSheet("QPushButton{\n"
                                      "background: 40A286 ;\n"
                                      "border: none;\n"
                                      "color: #FFF\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "background: #7AB32E\n"
                                      "}\n"
                                      "QPushButton:disabled {\n"
                                      "background: #7AB32E\n"
                                      "}")
        self.bt_Compras.setFlat(True)
        self.bt_Compras.setObjectName("bt_Compras")
        self.bt_Financeiro = QtWidgets.QPushButton(self.wd_menu)
        self.bt_Financeiro.setGeometry(QtCore.QRect(700, 0, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.bt_Financeiro.setFont(font)
        self.bt_Financeiro.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_Financeiro.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Financeiro.setAutoFillBackground(False)
        self.bt_Financeiro.setStyleSheet("QPushButton{\n"
                                         "background: 40A286 ;\n"
                                         "border: none;\n"
                                         "color: #FFF\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #7AB32E\n"
                                         "}\n"
                                         "QPushButton:disabled {\n"
                                         "background: #7AB32E\n"
                                         "}")
        self.bt_Financeiro.setFlat(True)
        self.bt_Financeiro.setObjectName("bt_Financeiro")
        self.bt_Conf = QtWidgets.QPushButton(self.wd_menu)
        self.bt_Conf.setGeometry(QtCore.QRect(840, 0, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.bt_Conf.setFont(font)
        self.bt_Conf.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_Conf.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Conf.setAutoFillBackground(False)
        self.bt_Conf.setStyleSheet("QPushButton{\n"
                                   "background: 40A286 ;\n"
                                   "border: none;\n"
                                   "color: #FFF\n"
                                   "}\n"
                                   "QPushButton:hover {\n"
                                   "background: #7AB32E\n"
                                   "}\n"
                                   "QPushButton:disabled {\n"
                                   "background: #7AB32E\n"
                                   "}")
        self.bt_Conf.setFlat(True)
        self.bt_Conf.setObjectName("bt_Conf")
        self.bt_Clientes = QtWidgets.QPushButton(self.wd_menu)
        self.bt_Clientes.setGeometry(QtCore.QRect(0, 0, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.bt_Clientes.setFont(font)
        self.bt_Clientes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_Clientes.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Clientes.setAutoFillBackground(False)
        self.bt_Clientes.setStyleSheet("QPushButton{\n"
                                       "background: 40A286 ;\n"
                                       "border: none;\n"
                                       "color: #FFF\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "background: #7AB32E\n"
                                       "}\n"
                                       "QPushButton:disabled {\n"
                                       "background: #7AB32E\n"
                                       "}\n"
                                       "QPushButton::menu-indicator {\n"
                                       "     image: url(\'down.png\');\n"
                                       "     subcontrol-origin: padding;\n"
                                       "     subcontrol-position: bottom right;\n"
                                       " }")
        self.bt_Clientes.setFlat(True)
        self.bt_Clientes.setObjectName("bt_Clientes")
        self.bt_Fornecedor = QtWidgets.QPushButton(self.wd_menu)
        self.bt_Fornecedor.setGeometry(QtCore.QRect(280, 0, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.bt_Fornecedor.setFont(font)
        self.bt_Fornecedor.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_Fornecedor.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Fornecedor.setAutoFillBackground(False)
        self.bt_Fornecedor.setStyleSheet("QPushButton{\n"
                                         "background: 40A286 ;\n"
                                         "border: none;\n"
                                         "color: #FFF\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #7AB32E\n"
                                         "}\n"
                                         "QPushButton:disabled {\n"
                                         "background: #7AB32E\n"
                                         "}")
        self.bt_Fornecedor.setFlat(True)
        self.bt_Fornecedor.setObjectName("bt_Fornecedor")
        self.ct_conteudo = QtWidgets.QFrame(self.centralwidget)
        self.ct_conteudo.setGeometry(QtCore.QRect(0, 100, 1000, 600))
        self.ct_conteudo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ct_conteudo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ct_conteudo.setObjectName("ct_conteudo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.bt_Exit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Sistema de Vendas"))
        self.lb_Data.setText(_translate("MainWindow", "25/11"))
        self.lb_DiaSemana.setText(_translate("MainWindow", "DOMINGO"))
        self.bt_Home.setToolTip(_translate("MainWindow", "Tela Inicial"))
        self.lb_NomeFantasia.setText(_translate("MainWindow", "Titulo"))
        self.lb_NomeFantasia2.setText(_translate("MainWindow", "Subtitulo"))
        self.bt_Exit.setToolTip(_translate("MainWindow", "Sair"))
        self.bt_logout.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p>Logout</p></body></html>"))
        self.lb_userName_2.setText(_translate("MainWindow", "Bem Vindo"))
        self.bt_alterSenha.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p>Meus Dados</p></body></html>"))
        self.bt_MainProdutos.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p>Produtos</p></body></html>"))
        self.bt_MainProdutos.setWhatsThis(_translate(
            "MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.bt_MainProdutos.setText(_translate("MainWindow", "Produtos"))
        self.bt_MainProdutos.setShortcut(_translate("MainWindow", "F2"))
        self.bt_Vendas.setText(_translate("MainWindow", "Vendas"))
        self.bt_Vendas.setShortcut(_translate("MainWindow", "F3"))
        self.bt_Compras.setText(_translate("MainWindow", "Compras"))
        self.bt_Compras.setShortcut(_translate("MainWindow", "F7"))
        self.bt_Financeiro.setText(_translate("MainWindow", "Financeiro"))
        self.bt_Financeiro.setShortcut(_translate("MainWindow", "F5"))
        self.bt_Conf.setText(_translate("MainWindow", "Configuração"))
        self.bt_Conf.setShortcut(_translate("MainWindow", "F6"))
        self.bt_Clientes.setText(_translate("MainWindow", "Clientes"))
        self.bt_Clientes.setShortcut(_translate("MainWindow", "F7"))
        self.bt_Fornecedor.setText(_translate("MainWindow", "Fornecedor"))
        self.bt_Fornecedor.setShortcut(_translate("MainWindow", "F6"))
