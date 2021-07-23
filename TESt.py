import os
name = 'THIS IS SO FUCKING BROKEN'
score = '1241423614'


dir = os.path.dirname(__file__) # Find the directory of the current file
filename = os.path.join(dir, 'scores',str('Hard.csv').lower()) # Finds the csv file
f = open(filename,'a') # opens the csv file

f.write("\n" + str(name) + ": " + str(score))
f.close() # close the file