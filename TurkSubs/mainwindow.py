from PyQt4 import uic
from PyQt4.QtCore import *
( Ui_MainWindow, QMainWindow ) = uic.loadUiType( 'mainwindow.ui' )

class MainWindow ( QMainWindow ):
    """MainWindow inherits QMainWindow"""

    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )
        self.connect(self.ui.submitButton, SIGNAL('clicked()'),self.splitFile)

    def __del__ ( self ):
        self.ui = None
    
    @staticmethod
    def urlgen(frames, nSplits):
        '''This function generates a dictionary of URLS, format {index: "url"}
		input dictionary of frames from framegen(minutes, eachLength)'''
        urlTemplate1 = 'https://www.youtube.com/v/Rxg-dYnqxFg?start=' #replace the video id part with our video
        urlTemplate2 = '&end='
        urlTemplate3 = '&version=3'
        urls = {}
        j = 1
        while j < nSplits:
            tempurl = urlTemplate1 + str(frames[j][0]) + urlTemplate2 + str(frames[j][1]) + urlTemplate3
            urls[j] = tempurl
            j += 1
        return urls
        #print urls
    
    @staticmethod
    def framegen(minutes, eachLength):
        '''This function returns a dictionary of time frames in the format
        {index: (start, end)} and the number of splits (nSplits)
        input length of video (minutes) and length of each split (eachLength)'''
        
        lengthInSeconds = minutes*60
        nSplits = lengthInSeconds/eachLength
        
        frames = {}
        #print(nSplits)
        i=1
        while i<nSplits:
            frames[i] = ((i-1)*10,i*10)
            i += 1
        return frames, nSplits
        #print frames

    @pyqtSlot()
    def splitFile(self):
        framesdict,splits = self.framegen(int(self.ui.lengthTextBox.toPlainText()),int(self.ui.splitLengthTextBox.toPlainText()))
        URLs = self.urlgen(framesdict,splits)
        self.ui.plainTextEdit.setPlainText(URLs[50])
        print URLs
