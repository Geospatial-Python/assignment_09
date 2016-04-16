'''
Created on Apr 15, 2016

@author: Prad
'''
from PyQt4 import QtGui
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


class View(QtGui.QMainWindow):
    
    def __init__(self):
        super(View, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QtGui.QAction(QtGui.QIcon('exit24.png'), 'Quit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Quit')
        toolbar.addAction(exitAction)
        
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')    
        self.show()
        
        textEdit = QtGui.QTextEdit('Hello World!')
        textBox= QtGui.QTextBlock()
        self.setCentralWidget(textEdit)
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = View()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    