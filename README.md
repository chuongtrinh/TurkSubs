++++++++++
+TURKSUBS+
++++++++++

TEAM MEMBERS:
Laramie Goode, Ross Hudgins, Chuong Trinh

DESCRIPTION:
TurkSubs is a crowdsourced video captioning program. TurkSubs uses an uploaded Youtube video and sends out HITs to Turkers to transcribe the audio of each individual video segment, picks the best results, and combines them all into a .srt file that can be used as a subtitle. 

REQUIRED INSTALLS:
Make sure you have Python 2.7, Boto, and PyQT4 installed.

Download Links:
Python 2.7: https://www.python.org/download/
Boto:       http://boto.readthedocs.org/en/latest/
PyQT4:      http://www.riverbankcomputing.com/software/pyqt/download

HOW-TO RUN:
Launch main.py, a graphical window should be displayed with TurkSubs near the top.

Enter the link to the Youtube video you want captions for. Make sure the link format is: https://www.youtube.com/v/<videoId> instead of https://www.youtube.com/watch?v=<videoID> (you can just edit out the watch? and replace the = with a / ). If you are wanting to see the subtitles in action, use a Youtube video that is from your own Youtube account so that you can upload the generated subtitles.srt file into your Youtube video page. 

Enter the length of the video to generate subtitles for in terms of minutes. You can specificy a video length shorter than the actual video length if you only want subtitles generated for those first minutes.

Enter the desired length for each video segment in terms of seconds to be sent to Turkers. We used 10 seconds and received good results.

Enter the amount of money to be paid per Turker in terms of dollars. We used $0.05 as our pay for Turkers.

Enter how many Turkers should work on each video segment. We used 5 Turkers per video segment.

Once those values have been entered, hit the Submit button. The console will output some information (not important for run-use). When the bottom text box says "Done", the HITs have been submitted to Amazon MechanicalTurk. You'll have to wait a while for Turkers to work but you can close the program while you wait (we left the jobs up overnight). 

When you have waited long enough, you can re-launch main.py. Before you can receive results, make sure you enter the length of video segments in the Length of each Split text field. You can ignore the other boxes. Click the Hits button and you'll see some more information output in the console. When it is done outputting, navigate to your program folder and look for the file called: subtitles.srt. This file contains the subtitles for the video.

If you own the Youtube account of the video you generated the subtitles for, you can now upload the subtitles file to that video. If you have a copy of the video file locally, you can open the video file and import the subtitles into some video players such as VLC. 

If there has been problem, you can click the Delete Hits button on the running program to disable and get rid of the HITs that were posted by the program and start over. 
