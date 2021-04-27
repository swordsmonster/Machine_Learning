import os

# Getting current directory
CURR_DIR = os.getcwd()

totalData = open("TotalData.csv","w")
totalData.write("Category,Message\n")

# Listing all files and folder in the path
filesAndFolders = os.listdir(CURR_DIR)
# Removing undesired files
i = 0
toRemove = []
# Get all folders where the text files are located
for current in filesAndFolders:
	extension = current.split(".")
	# Removing python files and text files
	print(extension[-1].lower())
	if((extension[-1].lower() == "py") or (extension[-1].lower() == "txt") or (extension[-1].lower() == "csv")):
		#
		toRemove.append(i)
	i = i + 1

# Reversing list to pop objects
toRemove.reverse()
# Removing objects from list
for current in toRemove:
	filesAndFolders.pop(current)

# Iterating each folder to get all files
for folder in filesAndFolders:
	newPath = CURR_DIR + "\\" + folder
	print(folder)
	files = os.listdir(newPath)
	# Iterating list of files
	for file in files:
		readInfo = ""
		# Opening each file to extract the info
		with open(newPath + "\\" + file) as textFile:
			# Reading each line of the file
			for row in textFile:
				# Checking if the line has a end of line character
				lastChar = row[-1]
				if(lastChar == '\n'):
					newRow = row[:-1]
				else:
					newRow = row
				# Storing all the file data in one string
				readInfo = readInfo + newRow + " "
		
		# Writing all the data in the CSV file
		totalData.write(folder + "," + readInfo + "\n")
		print(file)

# Closing the all data file
totalData.close()

