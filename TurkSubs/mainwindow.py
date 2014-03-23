from PyQt4 import uic
from PyQt4.QtCore import *
( Ui_MainWindow, QMainWindow ) = uic.loadUiType( 'mainwindow.ui' )

class MainWindow ( QMainWindow ):
    """MainWindow inherits QMainWindow"""

    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )
        self.connect(self.ui.pushButton, SIGNAL('clicked()'),self.clickHello)

    def __del__ ( self ):
        self.ui = None
    
    @pyqtSlot()
    def clickHello(self):
        self.ui.textEdit.setText("Hello World")
