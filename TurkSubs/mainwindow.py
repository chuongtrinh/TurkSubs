from PyQt4 import uic
from PyQt4.QtCore import *
( Ui_MainWindow, QMainWindow ) = uic.loadUiType( 'mainwindow.ui' )
from boto.mturk.connection import MTurkConnection
from boto.mturk.question import *
 
ACCESS_ID = ''
SECRET_KEY = ''
HOST = 'mechanicalturk.sandbox.amazonaws.com'

mtc = MTurkConnection(aws_access_key_id=ACCESS_ID, aws_secret_access_key=SECRET_KEY, host=HOST)

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
	
    def startHit(self,Url):
		#--------------- CREATE THE HIT -------------------
		mtc = MTurkConnection(aws_access_key_id=ACCESS_ID, aws_secret_access_key=SECRET_KEY, host=HOST)
		title = 'Translate a short movie clip'
		description = ('Watch a short clip and write down a transcript or screenplay of the clip\n' 
               'If there is no speech to translate, please describe what is happening in the clip') 
		keywords = 'video, transcript, translate'
		print Url
		#---------------  BUILD OVERVIEW -------------------
		overview = Overview()
		overview.append_field('Title', 'Translate a short video clip')
		overview.append(FormattedContent('<a target="_blank"'' href="http://www.toforge.com"></a>'))
		#---------------  BUILD MOVIE CLIP -------------------
		qc1 = QuestionContent()
		#html_question = '<![CDATA[<iframe width="600" height="400" src="'+ Url '"</iframe>]]>'
		#print html_question
		qc1.append_field('FormattedContent','<![CDATA[<iframe width="600" height="400" src="https://www.youtube.com/v/Rxg-dYnqxFg?start=200&amp;end=210&amp;version=3">s</iframe>]]>')
		#qc1.append_field('FormattedContent',html_question)		
		fta1 =  FreeTextAnswer()
		q1 = Question(identifier='design',content=qc1,answer_spec=AnswerSpecification(fta1),is_required=True)
		#--------------- BUILD THE QUESTION FORM ------------------#
		question_form = QuestionForm()
		question_form.append(overview)
		question_form.append(q1)
		mtc.create_hit(questions=question_form, max_assignments=1, title=title, description=description, keywords=keywords, duration = 5*60,reward=0.00)
    
    @pyqtSlot()
    def splitFile(self):
        framesdict,splits = self.framegen(int(self.ui.lengthTextBox.toPlainText()),int(self.ui.splitLengthTextBox.toPlainText()))
        URLs = self.urlgen(framesdict,splits)
        self.startHit(URLs[10])
        self.ui.plainTextEdit.setPlainText(URLs[10])
        print mtc.get_account_balance()[0]



