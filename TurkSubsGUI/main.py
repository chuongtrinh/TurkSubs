import sys

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from mainwindow import *
from loginDialog import *

if __name__ == '__main__':

    # create application
    app = QApplication( sys.argv )
    app.setApplicationName( 'TurkSubs' )

    # create widget
    w = MyWindow()
    w.setWindowTitle( 'TurkSubs' )
    
    # dialog window
    dialogWindow = MyDialog()
    d = Ui_Dialog()
    d.setupUi(dialogWindow)
    dialogWindow.exec_()
    
    w.ui.userString.setText("User: " + d.usernameField.text())
    w.show()
    
    # connection
    QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )

    # execute application
    sys.exit( app.exec_() )
