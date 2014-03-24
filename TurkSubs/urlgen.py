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