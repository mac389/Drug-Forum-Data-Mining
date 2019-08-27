import string 

text = open('snapshot-2015-10-17','r').read().splitlines()
#Eventually make this so it opens the most recent snapshot-
stopwords = set(open('stopwords','r').read().splitlines())
punkt = string.punctuation

#-process text
text = [[word.translate(None,punkt) for word in line.lower().split() if word not in stopwords] 
				for line in text] 

counter = 0
with open('cleaned-snapshot-2015-10-17','w') as outfile:
	#obviously this would write to the cleaned-%s%filename
	for line in text:
		counter +=1
		print>>outfile,' '.join(line)
		if counter%100==0:
			print counter