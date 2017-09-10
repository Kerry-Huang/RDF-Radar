from PyQt4 import QtGui, QtCore
from UI import *
import sys,time

class MainWindow(QtGui.QWidget): 

    def __init__(self,parent=None):

        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self) 
		
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_E:
            myapp.ui.screen.setPixmap(QtGui.QPixmap("./screen.jpg").scaled(240,240))
			
	
if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    myapp=MainWindow()
    myapp.show()
    pe = QtGui.QPalette()
    pe.setColor(QtGui.QPalette.WindowText,QtCore.Qt.white)
    myapp.ui.label_2.setPalette(pe)
    myapp.ui.screen.setPixmap(QtGui.QPixmap("./screen.jpg").scaled(240,240))
    movie = QtGui.QMovie("./loading.gif")
    myapp.ui.screen.setMovie(movie)
    movie.start()
    app.exec_()
