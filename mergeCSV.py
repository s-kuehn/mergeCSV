import csv
import glob

# Loop through files in input directory
# Ask if you want to include header
# If yes add the first line to list
# Loop through line in files (ignore 1st line)
# Add each line to a list
# Append list to a new CSV file

combinedList = []
header = ['NAME:','EMAIL:','COMPANY:','PROFILE PAGE:','LOCATION:','JOB TITLE:']
combinedList.append(header)

for fname in glob.glob('./input/*.csv'):
	fileList = list(csv.reader(open(fname)))

	for row in fileList[1:]: 
		if row[-2] == 'Columbus Ohio':
			combinedList.append(row)

	print(combinedList)

	with open('./output/combinedList.csv','w+') as output:
		csvWriter = csv.writer(output)
		for row in combinedList:
			csvWriter.writerow(row)
