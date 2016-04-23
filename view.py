import sys
from PyQt4 import QtGui

class View(QtGui.QMainWindow):

	def __init__(self):

		super(View, self).__init__()
		self.initUI()

	def initUI(self):

		text = QtGui.QTextEdit()

		self.setCentralWidget(text)

		exit = QtGui.QAction(QtGui.QIcon('exit.png'), 'Quit', self)
		exit.setStatusTip('Exit')
		exit.triggered.connect(self.close)
		exit.setShortcut('Ctrl+Q')

		self.statusBar()
		menubar = self.menuBar()
		menu = menubar.addMenu('&File')
		menu.addAction(exit)

		toolbar = self.addToolBar('Quit')
		toolbar.addAction(exit)

		self.setGeometry(300, 400, 300, 270)
		self.setWindowTitle('A GUI App')
		self.show()

		text = QtGui.QTextEdit('When in the chronicle of wasted time, I see descriptions of the fairest wights, and beauty making beautiful old rhyme')
		textBlock = QtGui.QTextBlock()
		self.setCentralWidget(text)


def main():
	app = QtGui.QApplication(sys.argv)

	view = View()

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()