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
		self.connect(self.ui.resultButton, SIGNAL('clicked()'),self.get_hit_result)

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
 
	def startHit(self,Url,index):
		#--------------- CREATE THE HIT -------------------
		mtc = MTurkConnection(aws_access_key_id=ACCESS_ID, aws_secret_access_key=SECRET_KEY, host=HOST)
		title = 'Translate a short movie clip ' + str(index)
		description = ('Watch a short clip and write down a transcript or screenplay of the clip\n' 
			   'If there is no speech to translate, please describe what is happening in the clip') 
		keywords = 'video, transcript, translate'
		print Url
		print Url.replace('&','&amp;')
		#---------------  BUILD OVERVIEW -------------------
		overview = Overview()
		overview.append_field('Title', 'Translate a short video clip')
		overview.append(FormattedContent('<a target="_blank"'' href="http://www.toforge.com"></a>'))
		#---------------  BUILD MOVIE CLIP -------------------
		qc1 = QuestionContent() # I will modify this to embed some codes indicating time frame
		qc1.append_field('FormattedContent','<![CDATA[<iframe width="600" height="400" src="'+ Url.replace('&','&amp;') + '">No video supported</iframe>]]>')
		fta1 =  FreeTextAnswer()
		q1 = Question(identifier='design',content=qc1,answer_spec=AnswerSpecification(fta1),is_required=True)
		#--------------- BUILD THE QUESTION FORM ------------------#
		question_form = QuestionForm()
		question_form.append(overview)
		question_form.append(q1)
		my_hit = mtc.create_hit(questions=question_form, lifetime=60*5, max_assignments=1, title=title, description=description, keywords=keywords, duration = 5*60,reward=0.00, response_groups= 'Minimal')
		my_hit_id = my_hit[0].HITTypeId
		print my_hit_id
		#mtc.disable_hit(my_hit_id)

	@staticmethod
	def get_all_reviewable_hits(mtc):
		page_size = 50
		hits = mtc.get_reviewable_hits(page_size=page_size)
		print "Total results to fetch %s " % hits.TotalNumResults
		print "Request hits page %i" % 1
		total_pages = float(hits.TotalNumResults)/page_size
		int_total= int(total_pages)
		if(total_pages-int_total>0):
			total_pages = int_total+1
		else:
			total_pages = int_total
		pn = 1
		while pn < total_pages:
			pn = pn + 1
			print "Request hits page %i" % pn
			temp_hits = mtc.get_reviewable_hits(page_size=page_size,page_number=pn)
			hits.extend(temp_hits)
		return hits    

	def get_hit_result(self):
		hits = self.get_all_reviewable_hits(mtc) 
		for hit in hits:
			assignments = mtc.get_assignments(hit.HITId)
			for assignment in assignments:
				print "Answers of the worker %s" % assignment.WorkerId
				for question_form_answer in assignment.answers[0]:
					for value in question_form_answer.fields: 
						#turker hit result, timeframe value will be included here also
						#for frame,value in in question_form_answer.fields:
						#handling all the results here!!!!!
						print "%s" % (value) 
				print "--------------------"
		self.ui.plainTextEdit.setPlainText("Done")
 
	@pyqtSlot()
	def splitFile(self):
		framesdict,splits = self.framegen(int(self.ui.lengthTextBox.toPlainText()),int(self.ui.splitLengthTextBox.toPlainText()))
		URLs = self.urlgen(framesdict,splits)
		for x in range(10,13): #a list of urls to put on mturk
			print URLs[x]
			self.startHit(URLs[x],x)
		self.ui.plainTextEdit.setPlainText(URLs[10])
		print mtc.get_account_balance()[0]
