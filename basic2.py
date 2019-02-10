from PyQt5.QtWidgets import  *
from sys import exit
from PyQt5 import QtGui, QtCore


#CLass difinition for the container

class Window(QMainWindow):
	
	def __init__(self):
		super(Window,self).__init__()
		self.resize(600,500)
		self.move(600,500)
		self.setWindowTitle("Formal Application_01")
		
		self.Menus()

		action_toolBar = QAction('MOVE',self)

		toolBar = self.addToolBar('CoolBar')
		toolBar.addAction(action_toolBar)		
		self.buttons()
		self.text()
		self.show()

	def Menus(self):
		action = QAction("Export",self)
		action.setShortcut('ctrl+Q')
		action.setStatusTip("Export yourself Out!")
		action.triggered.connect(exit)
		
		action1 = QAction("copy",self)

		self.statusBar()

		menu = self.menuBar() # can also use QMenuBar(self)
		munu_1 = menu.addMenu('&File')
		munu_1.addAction(action)
		menu_2 = menu.addMenu('&Tools')
		menu_2.addAction(action1)

	def buttons(self):
		btn1 = QPushButton('Quit',self) # pass self as second parameter for the widgets to appear on qwidget object/instance	 
		btn1.resize(200,50)
		btn1.move(200,320)
		btn1.clicked.connect(self.Button_Actions)
	def text(self):
		txt1 = QLabel('Viz tool',self)
		txt1.move(250,100)
		#txt1.show()
	def Button_Actions(self):
		msg1 = QMessageBox.question(self,'Quit App',"are you sure?",QMessageBox.Yes,QMessageBox.No)
		if msg1 == QMessageBox.Yes:
			exit()
		else:
			print('Unable to Exit! Use the option under File menu')
			#msg1.exec_()
		#exit()

		

def run_app():
	app = QApplication([])
	window = Window()
	exit(app.exec_())
run_app()