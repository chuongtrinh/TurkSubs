def timeformat(secs):
	'''return string in format hh:mm:ss,ddd'''
	m, s = divmod(secs, 60)
	h, m = divmod(m, 60)
	return "%02i:%02i:%02i,000" % (h,m,s)

def buildsrt(turkedsubs, eachclip):
	'''turkedsubtitles dictionary of the format: {index/key:(start, subs)}'''
	file = open('subtitles.srt', 'w+')
	out = ""
	#srt format:
		#index
		#start --> start + eachclip
		#subs
		#(empty line)
	i = 1
	while i <= len(turkedsubs):
		start = int(turkedsubs[i][0])
		end = int(turkedsubs[i][0]) + eachclip
		out += str(i) + "\n" + timeformat(start) + " --> " + timeformat(end) + "\n" + turkedsubs[i][1] + "\n\n"		
		i += 1
	file.write(out)
	file.close()
	
def main():
	testsubs = {1:(0,"this is the first segment of subtitles"), 2:(11,"this is the second segment"), 3:(21,"this is the third segment")}
	buildsrt(testsubs, 10)
	
if __name__ == "__main__":
	main()