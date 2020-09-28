# import ui
from tkinter import *
import sqlfetch
import unidecode
import math
# root = Toplevel(ui.root)

def manualCalc():
    averages = sqlfetch.getAverageDictForHalfYear()
    print(averages)

    roundFrom = float(input())  #Where to round the numbers up from (Eg. 0.75)

    halfYearGradesList = [] #this is the list all the integers will get put into, and returned
    for item in averages.keys():    #Loop through the subjects
        f = averages[item]  #F is equals to the value of the item-th key (-> the current subject)
        if f - (int(f)) >= roundFrom:   #subtract the integer form of the float from the float to get only the decimals (Eg. 4.67 - 4 = 0.67)
            roundedAverage = item + ': ' + str(averages[item]) + ' = ' + str(math.ceil(f))
            halfYearGradesList.append(math.ceil(f)) #than round up to the closest bigger whole integer
            print(roundedAverage)
        else:   #else, (if the average is lower than the specified number we want to round up from)
            halfYearGradesList.append(int(f))   #round down (Eg. 4.4 < 4.75 so 4.4 will get rounded to 4 (integer))
            print(item + ': ' + str(averages[item]) + ' = ' + str(int(f)))
    return halfYearGradesList   #return all of the rounded numbers


#---Setting up tkinter window---
root = Tk()
root.config(padx=10, pady=10)
#-------------------------------

#---Formatting the subjects---
values = list(sqlfetch.getHalfYearGrades().values())
subjects = list(sqlfetch.getHalfYearGrades().keys())
for i in subjects:  #loops through all of the subjects
    index = subjects.index(i)   #get the index of current subject in the subjects list
    splitSubjects = subjects[index].split(' ')  #splitting the current subject at spaces thus creating splitSubjects list
    for item in splitSubjects:  #loops through the current subject's parts (separated by whitespace)
        index = splitSubjects.index(item)   #get the index of the current part
        item = item.replace('(', '').replace(')', '').replace(':', '').replace('-', '').capitalize()    #remove the unwanted things
        item = unidecode.unidecode(item)    #remove accents
        splitSubjects[index] = item
    subjects[index] = ''.join(splitSubjects)    #finally, join the parts of the subjects (remove spaces) and put it into subjects list
#----------------------------------------

#---Creating dictionary from subjects and grades---
gradesDict = dict(zip(subjects, values))
# print(gradesDict)
#--------------------------------------------------
halfYearGradesList = manualCalc()
# halfYearGradesList = list(sqlfetch.getHalfYearGrades().values())

print(sqlfetch.calculateHalfYearGrades(halfYearGradesList))

# root.mainloop()