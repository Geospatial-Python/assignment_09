"""
Instructions:
A single window (QMainWindow or QWidget)
A File menu with at least one entry - Quit. The quit item should exit the program.
The code should be presented using the following conventions:
a. Include an if '__name__' == __main__: block
b. Write your GUI in a class, inheriting from QMainWindow, QWidget, or another appropriate parent.
    You should have at least an __init__ method and a init_ui method.
c. Call a function called main when the application is launched and an instance of your GUI class is created

A central widget. This can be an empty widget, a text box, a graphic - we will replace this
next week with something else, so the important part for now is having something in the window.

Original code sample: http://zetcode.com/gui/pyqt4/menusandtoolbars/
"""

import sys
from PyQt4 import QtGui


class View(QtGui.QMainWindow):

    def __init__(self):
        super(View, self).__init__()
        self.init_ui()

    def init_ui(self):
        # This is the central empty widget, to be replaced in a future assignment.
        text_edit = QtGui.QTextEdit()
        self.setCentralWidget(text_edit)

        # Define the exit action for use in the toolbar and file menu.
        exit_action = QtGui.QAction(QtGui.QIcon('exit-24.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.close)

        # Add a status bar.
        self.statusBar()

        # Add a menu bar, and add a file menu to that.
        menu_bar = self.menuBar()
        # Set the mnemonic to Alt-F.
        # Details: https://msdn.microsoft.com/en-us/library/system.windows.forms.label.usemnemonic(v=vs.110).aspx
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(exit_action)

        # Add an exit item to the toolbar.
        tool_bar = self.addToolBar('Exit')
        tool_bar.addAction(exit_action)

        # x, y, width, height
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main Window')
        self.show()

        # Put the window in the middle of the screen.
        self.center()

    def center(self):
        geometry = self.frameGeometry()
        center = QtGui.QDesktopWidget().availableGeometry().center()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())


def main():
    app = QtGui.QApplication(sys.argv)
    view = View()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()