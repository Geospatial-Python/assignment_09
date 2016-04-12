import sys
from PyQt4 import QtGui


class Assignment9(QtGui.QMainWindow):
    
    def __init__(self):
        
        super(Assignment9, self).__init__()
        self.initUI()
        
        
    
    def initUI(self):               
        
        #create the exit aciton
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect((QtGui.qApp.quit))
        
        
        #set statusBar
        self.statusBar()
        
        #create the textEdit
        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)
        
        
        #self.setCentralWidget(a_botton)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        
        self.setGeometry(300, 300, 300, 200)
        
        #set the titile
        self.setWindowTitle('Assignment9')    
        #make the window in the center
        
        self.center()
        self.show()
        
        
    def closeEvent(self, event):
        """
        
        Show a message box when the user close the window.
        """
        
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        
        
    def center(self):
        """
        
        Set the window on the center of deskp.
        """
        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Assignment9()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()