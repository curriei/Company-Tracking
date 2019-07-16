import csv

#Imports the ontology file and puts it in list format for comparisons
## fName - File name containing the ontology ending with .csv
## Returns dic: List of Lists representing the file
def buildOnt(fName):
	dic = []
	with open(fName, "r", newline='', encoding='ISO-8859-1') as csvFile:
		reader = csv.reader(csvFile, skipinitialspace=True)
		for row in reader:
			i = 0
			while i < len(row):
				if row[i] == '':
					del(row[i])
				else:
					row[i]=row[i].strip()
				i += 1
			dic.append(row)
	return dic

#Writes the final updated file
## newValues - list of lists representing the update file after changes are made
## fName - File name of the original file to be updated, ending with .csv
def writeFile(newValues, fName):
	fName = fName.strip(".csv") + "_clean.csv"
	with open(fName, "w", encoding='utf-8-sig') as csvFile:
		writer = csv.writer(csvFile, dialect=csv.excel)
		writer.writerows(newValues)

#Reads the update file and changes values as needed to reflect the ontology
## fName - File name to be updated ending with .csv
## dic - List of Lists representing the ontology
def updateFile(fName, dic):
	newFileList = []
	with open(fName, "r", newline='', encoding='ISO-8859-1') as csvFile:
		reader = csv.reader(csvFile, skipinitialspace=True)
		newFileList.append(next(reader))
		i = newFileList[0].index("Organization")
		for row in reader:
			org = row[i].strip()
			for organization in dic:
				if org in organization:
					row[i] = organization[0]
					break
			while row[-1] == '':
				del(row[-1])
			row[-1], row[0] = row[-1].strip(), row[0].strip()
			newFileList.append(row)
	writeFile(newFileList, fName)

