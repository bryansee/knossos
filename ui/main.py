# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Oct 26 02:13:12 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from lib.qt import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(482, 703)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabs = QtGui.QTabWidget(self.centralwidget)
        self.tabs.setObjectName("tabs")
        self.mods = QtGui.QWidget()
        self.mods.setObjectName("mods")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.mods)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtGui.QLabel(self.mods)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.modTree = QtGui.QTreeWidget(self.mods)
        self.modTree.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.modTree.setProperty("showDropIndicator", False)
        self.modTree.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.modTree.setAnimated(True)
        self.modTree.setExpandsOnDoubleClick(False)
        self.modTree.setObjectName("modTree")
        self.verticalLayout_3.addWidget(self.modTree)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.update = QtGui.QPushButton(self.mods)
        self.update.setObjectName("update")
        self.horizontalLayout.addWidget(self.update)
        self.reset_sel = QtGui.QPushButton(self.mods)
        self.reset_sel.setObjectName("reset_sel")
        self.horizontalLayout.addWidget(self.reset_sel)
        self.apply_sel = QtGui.QPushButton(self.mods)
        self.apply_sel.setObjectName("apply_sel")
        self.horizontalLayout.addWidget(self.apply_sel)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.tabs.addTab(self.mods, "")
        self.modweb = QtGui.QWidget()
        self.modweb.setObjectName("modweb")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.modweb)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.webView = QtWebKit.QWebView(self.modweb)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setMinimumSize(QtCore.QSize(100, 10))
        self.webView.setMaximumSize(QtCore.QSize(200, 16777215))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setRenderHints(QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.SmoothPixmapTransform|QtGui.QPainter.TextAntialiasing)
        self.webView.setObjectName("webView")
        self.verticalLayout_6.addWidget(self.webView)
        self.tabs.addTab(self.modweb, "")
        self.fsoSettings = QtGui.QWidget()
        self.fsoSettings.setObjectName("fsoSettings")
        self.tabs.addTab(self.fsoSettings, "")
        self.settings = QtGui.QWidget()
        self.settings.setObjectName("settings")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.settings)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.updateButton = QtGui.QPushButton(self.settings)
        self.updateButton.setObjectName("updateButton")
        self.verticalLayout_5.addWidget(self.updateButton)
        self.label_2 = QtGui.QLabel(self.settings)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.sourceList = QtGui.QListWidget(self.settings)
        self.sourceList.setDragEnabled(True)
        self.sourceList.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.sourceList.setObjectName("sourceList")
        self.verticalLayout_5.addWidget(self.sourceList)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addSource = QtGui.QPushButton(self.settings)
        self.addSource.setObjectName("addSource")
        self.horizontalLayout_2.addWidget(self.addSource)
        self.editSource = QtGui.QPushButton(self.settings)
        self.editSource.setObjectName("editSource")
        self.horizontalLayout_2.addWidget(self.editSource)
        self.removeSource = QtGui.QPushButton(self.settings)
        self.removeSource.setObjectName("removeSource")
        self.horizontalLayout_2.addWidget(self.removeSource)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.enforceDeps = QtGui.QCheckBox(self.settings)
        self.enforceDeps.setChecked(True)
        self.enforceDeps.setObjectName("enforceDeps")
        self.gridLayout.addWidget(self.enforceDeps, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.settings)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.maxDownloads = QtGui.QLineEdit(self.settings)
        self.maxDownloads.setObjectName("maxDownloads")
        self.gridLayout.addWidget(self.maxDownloads, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.settings)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.uiMode = QtGui.QComboBox(self.settings)
        self.uiMode.setObjectName("uiMode")
        self.uiMode.addItem("")
        self.uiMode.addItem("")
        self.uiMode.addItem("")
        self.gridLayout.addWidget(self.uiMode, 3, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.settings)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.versionLabel = QtGui.QLabel(self.settings)
        self.versionLabel.setObjectName("versionLabel")
        self.gridLayout.addWidget(self.versionLabel, 1, 1, 1, 1)
        self.allModVersions = QtGui.QCheckBox(self.settings)
        self.allModVersions.setObjectName("allModVersions")
        self.gridLayout.addWidget(self.allModVersions, 0, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.schemeHandler = QtGui.QPushButton(self.settings)
        self.schemeHandler.setObjectName("schemeHandler")
        self.horizontalLayout_3.addWidget(self.schemeHandler)
        self.gogextractButton = QtGui.QPushButton(self.settings)
        self.gogextractButton.setObjectName("gogextractButton")
        self.horizontalLayout_3.addWidget(self.gogextractButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.tabs.addTab(self.settings, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.aboutLabel = QtGui.QLabel(self.tab)
        self.aboutLabel.setWordWrap(True)
        self.aboutLabel.setObjectName("aboutLabel")
        self.verticalLayout_4.addWidget(self.aboutLabel)
        self.tabs.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabs)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 482, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Mod Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Select mods to install them or deselect them to uninstall them. Click on a mod\'s name to get more information about it.", None, QtGui.QApplication.UnicodeUTF8))
        self.modTree.setSortingEnabled(True)
        self.modTree.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.modTree.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Version", None, QtGui.QApplication.UnicodeUTF8))
        self.modTree.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.update.setText(QtGui.QApplication.translate("MainWindow", "Update List", None, QtGui.QApplication.UnicodeUTF8))
        self.reset_sel.setText(QtGui.QApplication.translate("MainWindow", "Reset Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.apply_sel.setText(QtGui.QApplication.translate("MainWindow", "Install/Uninstall", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.mods), QtGui.QApplication.translate("MainWindow", "Mod Tree", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.modweb), QtGui.QApplication.translate("MainWindow", "Mod List", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.fsoSettings), QtGui.QApplication.translate("MainWindow", "FSO Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.updateButton.setText(QtGui.QApplication.translate("MainWindow", "Update Knossos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Mod Sources:", None, QtGui.QApplication.UnicodeUTF8))
        self.addSource.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.editSource.setText(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.removeSource.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.enforceDeps.setText(QtGui.QApplication.translate("MainWindow", "Enforce dependencies", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Parallel downloads:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "UI Mode:", None, QtGui.QApplication.UnicodeUTF8))
        self.uiMode.setItemText(0, QtGui.QApplication.translate("MainWindow", "Traditional", None, QtGui.QApplication.UnicodeUTF8))
        self.uiMode.setItemText(1, QtGui.QApplication.translate("MainWindow", "Nebula", None, QtGui.QApplication.UnicodeUTF8))
        self.uiMode.setItemText(2, QtGui.QApplication.translate("MainWindow", "Hell", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Version:", None, QtGui.QApplication.UnicodeUTF8))
        self.versionLabel.setText(QtGui.QApplication.translate("MainWindow", "?", None, QtGui.QApplication.UnicodeUTF8))
        self.allModVersions.setText(QtGui.QApplication.translate("MainWindow", "Show all mod versions", None, QtGui.QApplication.UnicodeUTF8))
        self.schemeHandler.setText(QtGui.QApplication.translate("MainWindow", "Install as handler for fso:// links", None, QtGui.QApplication.UnicodeUTF8))
        self.gogextractButton.setText(QtGui.QApplication.translate("MainWindow", "Install FS2 from GoG", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.settings), QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.aboutLabel.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Idea and prototype by Hellzed.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Rewrite in Python by ngld.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For feedback and updates go to:<br /><a href=\"http://www.hard-light.net/forums/index.php?topic=86364\"><span style=\" text-decoration: underline; color:#0000ff;\">http://www.hard-light.net/forums/index.php?topic=86364</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The code is available at:<br /><a href=\"https://github.com/ngld/fs2mod-py\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/ngld/fs2mod-py</span></a><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Dependencies:</p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://python.org\"><span style=\" text-decoration: underline; color:#0000ff;\">Python</span></a> (2 or 3)</li>\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://qt-project.org/wiki/Category:LanguageBindings::PySide\"><span style=\" text-decoration: underline; color:#0000ff;\">PySide</span></a> or <a href=\"http://riverbankcomputing.co.uk/software/pyqt/intro\"><span style=\" text-decoration: underline; color:#0000ff;\">PyQt4</span></a></li>\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://www.7-zip.org/\"><span style=\" text-decoration: underline; color:#0000ff;\">7zip</span></a> (to extract downloaded archives)</li>\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/workhorsy/py-cpuinfo\"><span style=\" text-decoration: underline; color:#0000ff;\">py-cpuinfo</span></a></li>\n"
"<li style=\" text-decoration: underline; color:#0000ff;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pypi.python.org/pypi/semantic_version\">semantic_version</a></li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This tool also uses <a href=\"http://constexpr.org/innoextract/\"><span style=\" text-decoration: underline; color:#0000ff;\">InnoExtract</span></a> to unpack the GOG installer.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

from lib.qt import QtWebKit
