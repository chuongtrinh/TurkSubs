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