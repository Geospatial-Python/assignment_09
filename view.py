import sys
from PyQt4 import QtGui

'''
Create a GUI application that can be launched from a script named view.py.
The GUI should include:
A single window (QMainWindow or QWidget)
A File menu with at least one entry - Quit.
The quit item should exit the program.
The code should be presented using the following conventions:
    a. Include an if '__name__' == __main__: block
    b. Write your GUI in a class, inhereting from QMainWindow, QWidget, or
       another appropriate parent.
       You should have at least an __init__ method and a init_ui method.
    c. Call a function called main when the application is launched and an
       instance of your GUI class is created
'''


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.init_ui()

    def init_ui(self):

        text_edit = QtGui.QTextEdit()
        self.setCentralWidget(text_edit)

        exit_action = QtGui.QAction(QtGui.QIcon('exit24.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.close)

        self.statusBar()

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(exit_action)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exit_action)

        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('Assignment 9 Main Window')
        self.show()

    def main():

        app = QtGui.QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())

    if __name__ == '__main__':
        main()
