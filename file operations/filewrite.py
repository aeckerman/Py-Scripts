fileName = input("What would you like to name your file?\n")
fileContent = input("What would you like to be the files content?\n")

newFile = open(fileName, 'w')
newFile.write(fileContent)
newFile.close()