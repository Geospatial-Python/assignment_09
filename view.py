from PyQt5 import QtCore, QtWidgets
import sys


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(434, 316)

        self.setupUi()

    def setupUi(self):

        self.setupMenuBar()
        self.setupStatusBar()


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.widget = QtWidgets.QWidget(self.centralwidget)

        # place widgets here
        self.editText = QtWidgets.QTextEdit(self.widget)


        self.MainWindow.setCentralWidget(self.centralwidget)

    def setupMenuBar(self):

        exitAction = QtWidgets.QAction(self.MainWindow)
        exitAction.setText('Exit')
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(QtWidgets.qApp.quit)

        menubar = QtWidgets.QMenuBar(self.MainWindow)
        menuFile = QtWidgets.QMenu(menubar)
        menuFile.setTitle('File')
        self.MainWindow.setMenuBar(menubar)

        menuFile.addAction(exitAction)
        menubar.addAction(menuFile.menuAction())

    def setupStatusBar(self):
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.MainWindow.setStatusBar(self.statusbar)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

