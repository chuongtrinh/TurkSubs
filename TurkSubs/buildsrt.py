import pysrt

def buildsrt(turkedsubtitles):
	'''turkedsubtitles will be of the format: {1:(start, end, subs)}'''
	subs = pysrt.open('subtitles.srt')
	i = 1
	while (i < len(subs)):
		subs[i].text = turkedsubtitles[i][0]
		subs[i].start.seconds = turkedsubtitles[i][1]
		subs[i].end.seconds = turkedsubtitles[i][2]
		
	subs.save('subtitles.srt')