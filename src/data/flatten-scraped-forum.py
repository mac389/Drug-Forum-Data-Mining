import os, json

#Move files (takes to long in bash)

starting_dir = './forums-scraped'
ending_dir = './forums-denuded'
for folder in os.listdir(starting_dir):
	if os.path.isdir(os.path.join(starting_dir,folder)):
		filenames = os.listdir(os.path.join(starting_dir,folder))
		for filename in filenames:
			os.rename(os.path.join(starting_dir,folder,filename),os.path.join(ending_dir,filename))
