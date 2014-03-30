from PyQt4 import uic
from PyQt4.QtCore import *
( Ui_MainWindow, QMainWindow ) = uic.loadUiType( 'mainwindow.ui' )
from boto.mturk.connection import MTurkConnection
from boto.mturk.question import *
import operator
import fuzzyStrings
 
ACCESS_ID = ''
SECRET_KEY = ''
HOST = 'mechanicalturk.sandbox.amazonaws.com'

mtc = MTurkConnection(aws_access_key_id=ACCESS_ID, aws_secret_access_key=SECRET_KEY, host=HOST)
class MainWindow ( QMainWindow ):
    """MainWindow inherits QMainWindow"""
    hit_time_frame = dict()
    hit_result = dict()
    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )
        self.connect(self.ui.submitButton, SIGNAL('clicked()'),self.splitFile)
        self.connect(self.ui.resultButton, SIGNAL('clicked()'),self.get_hit_result)

    def __del__ ( self ):
        self.ui = None
    
    @staticmethod
    def urlgen(frames, nSplits, url):
        '''This function generates a dictionary of URLS, format {index: "url"}
        input dictionary of frames from framegen(minutes, eachLength)'''
        #url for Tinyhearts: https://www.youtube.com/v/xTZepKsJ_ns
        urlTemplate1 = '?start=' 
        urlTemplate2 = '&end='
        urlTemplate3 = '&version=3'
        urls = {}
        j = 1
        urls = {}
        j = 1
        while j < nSplits:
            tempurl = url + urlTemplate1 + str(frames[j][0]) + urlTemplate2 + str(frames[j][1]) + urlTemplate3
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
        #---------------  BUILD OVERVIEW -------------------
        overview = Overview()
        overview.append_field('Title', 'Translate a short video clip')
        overview.append(FormattedContent('<a target="_blank"'' href="http://www.toforge.com"></a>'))
        #---------------  BUILD MOVIE CLIP -------------------
        qc1 = QuestionContent() # I will modify this to embed some codes indicating time frame
        qc1.append_field('FormattedContent','<![CDATA[<iframe width="600" height="400" src="'+ Url.replace('&','&amp;') + '">No video supported</iframe>]]>')
        fta1 =  FreeTextAnswer()
        q1 = Question(identifier='design',content=qc1,answer_spec=AnswerSpecification(fta1),is_required=True)
        #looking for start time
        #The end time can be computed by +10
        
        
        start = Url.find('start=') +6
        end = Url.find('&end',start)
        time_frame = [('Time',Url[start:end])]
        qc2 = QuestionContent()
        qc2.append_field('Title',' ')
        fta2 = SelectionAnswer(min=1,max=1, style='dropdown',selections=time_frame,type='text',other=False)
        q2 = Question(identifier='extra',content=qc2,answer_spec=AnswerSpecification(fta2),is_required=False)        
        
        #--------------- BUILD THE QUESTION FORM ------------------#
        question_form = QuestionForm()
        question_form.append(overview)
        question_form.append(q1)
        question_form.append(q2)
        my_hit = mtc.create_hit(questions=question_form, lifetime=60*5, max_assignments=3, title=title, description=description, keywords=keywords, duration = 5*60,reward=0.00, response_groups= 'Minimal')
        #--------------- ASSIGN HITID TO ARRAY OF TIMEFRAME --------#
        my_hit_id = my_hit[0].HITTypeId
        print "Hit type id 1: %s" % my_hit[0].HITTypeId

        #print self.hit_time_frame[my_hit_id]
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

    def make_hit_decision(self,hit_results):
        #for hit in hit_results:
        if hit_results[4] >= 0.75:
            mtc.approve_assignment(hit_results[1])
        else:
            mtc.reject_assignment(hit_results[1])
   

    def get_hit_result(self):
        hits = self.get_all_reviewable_hits(mtc)
        data = []
        for hit in hits:
            assignments = mtc.get_assignments(hit.HITId)
            for assignment in assignments:
                tempRow = []
                print "Answers of the worker %s" % assignment.WorkerId
                print "Hit id %s" % hit.HITId
                assignmentID = assignment.AssignmentId
                time_frame = assignment.answers[0][1].fields[0]
                turker_answer = assignment.answers[0][0].fields[0]
                print "assignment: %s" % assignmentID
                print "time frame: %s" % time_frame
                print "answer: %s" % turker_answer
                tempRow.append(int(time_frame))
                tempRow.append(str(hit.HITId))
                tempRow.append(str(turker_answer))
                tempRow.append(str(assignmentID))
                data.append(tempRow)
                #mtc.disable_hit(hit.HITId)
            print "--------------------"
        self.ui.plainTextEdit.setPlainText("Done")
        sortedData = []
        sortedData = sorted(data)
        #fuzzyStrings.printMatrix(sortedData)
        
        tuples = []
        timeFrames = []
        primedData = []
        bestData = []
        scoredData = []
        anotherList = []
        
        for row in sortedData:
            if row[0] not in timeFrames:
                timeFrames.append(row[0])
                primedData.append([0])
                scoredData.append([0])
        
        for row in sortedData:
            tuples.append(tuple(row))
        
        for index in range(0, len(timeFrames)):
            temp = [x for x in tuples if x[0] == timeFrames[index]]
            primedData[index] = temp
        
        for row in primedData:
            strings = []
            scores = []
            
            for column in row:
                strings.append(column[2])
            index = fuzzyStrings.pickBestIndex(strings)
            scores = fuzzyStrings.scoreStrings(strings)
            
            for i in range(0, len(scores)):
                a = row[i]
                b = scores[i][2]
                tempList = list(a)
                tempList.append(b)
                temp = tuple(tempList)
                anotherList.append(temp)
                #print(">>>> %s" %str(temp))
        
        #print(anotherList)
        
        for index in range(0, len(timeFrames)):
            temp = [x for x in anotherList if x[0] == timeFrames[index]]
            scoredData[index] = temp    
            
        #print(scoredData)                
        #return scoredData
        fuzzyStrings.printMatrix(anotherList)
        
        for row in anotherList:
            #make_hit_decision(self, row)
            if row[4] >= 0.75:
                mtc.approve_assignment(row[3])
                print("Approved >> %s" %row)
            else:
                mtc.reject_assignment(row[3])
                print("Rejected >> %s" %row)
    
    @pyqtSlot()
    def splitFile(self):
        framesdict,splits = self.framegen(int(self.ui.lengthTextBox.toPlainText()),int(self.ui.splitLengthTextBox.toPlainText()))
        #URLs = self.urlgen(framesdict,splits,self.ui.linkTextBox.toPlainText())
        URLs = self.urlgen(framesdict,splits,"https://www.youtube.com/v/xTZepKsJ_ns")
        turkerPerClip = int(self.ui.numTurkerTextBox.toPlainText())
        for x in range(1,4): #a list of urls to put on mturk
            for y in range(0, turkerPerClip):
                print URLs[x]
                self.startHit(URLs[x],x)
        self.ui.plainTextEdit.setPlainText(URLs[10])
        print mtc.get_account_balance()[0]
