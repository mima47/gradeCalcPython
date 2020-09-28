import sqlite3
import pandas
from datetime import date

def connectStudent():
    global db
    db = sqlite3.connect('student.db')
    df = pandas.read_csv('studentAmi.csv')
    df.to_sql('studentAmi', db, if_exists='replace', index=False)

def connectAverages():
    global db
    db = sqlite3.connect('student.db')
    df = pandas.read_csv('averages.csv')
    df.to_sql('averages', db, if_exists='replace', index=False)

def getAverageSubjects():
    global db
    cursor = db.cursor()
    cursor.execute("SELECT Subject FROM averages")
    values = cursor.fetchall()

    subjects = []
    for row in values:
        subjects.append(row[0])
    return subjects

def getAverageValues():
    global db
    cursor = db.cursor()
    cursor.execute("SELECT Value FROM averages")
    values = cursor.fetchall()
    averages = []
    for row in values:
       averages.append(row[0])
    return averages

def calculate(dateFrom,dateTo):
    global db
    cursor=db.cursor()
    cursor.execute("SELECT Weight, NumberValue FROM studentAmi WHERE Subject NOT IN ('Művészetek', 'Testnevelés',"
                   "'Testnevelés és sport','Művészetek: zeneművészet') AND JellegNev NOT IN ('Magatartas', 'Szorgalom')"
                   "AND CreatingTime BETWEEN '" + dateFrom + "' AND '" + dateTo + "' AND NumberValue IN ('5', '4', '1')"
                   " AND Type IN ('MidYear');")
    weight = cursor.fetchall()
#    print(cursor.rowcount)


    weightNumbers = []
    for row in weight:
        weightNumbers.append(row[0])
#    print(weightNumbers)

    gradeNumbers = []
    gradeFive = 0
    gradeFour = 0
    gradeOne = 0
    for row in weight:
        gradeNumbers.append(int(row[1]))
        if int(row[1]) == 5:
            gradeFive += 1
        elif int(row[1]) == 4:
            gradeFour += 1
        else:
            gradeOne += 1
#    print(gradeNumbers)
#    print('# of five grades: '+str(gradeFive))
#    print('# of four grades: '+str(gradeFour))
#    print('# of one grades: '+str(gradeOne))
#    print('-----------------')


    doubleweightindexes = [i for i,x in enumerate(weightNumbers) if x=='200%']
#    print(doubleweightindexes)

    doubleGradeValList = []
    indexval=0
    while indexval < len(doubleweightindexes):
        doubleGradeValList.append(gradeNumbers[doubleweightindexes[indexval]]*100*2)
        indexval += 1



    weightindexes = [i for i,x in enumerate(weightNumbers) if x=='100%']
#    print(weightindexes)

    gradeValList = []
    indexval=0
    while indexval < len(weightindexes):
        gradeValList.append(gradeNumbers[weightindexes[indexval]]*100)
        indexval += 1


    gradeOneIndexes = [i for i,x in enumerate(gradeNumbers) if x==1]
#    print(gradeOneIndexes)

    gradeOneList=[]
    indexval=0
    while indexval < len(gradeOneIndexes):
        gradeOneList.append(gradeNumbers[gradeOneIndexes[indexval]])
        indexval += 1


    gradeOneValue = (sum(gradeOneList)*1000)
    gradeValue = sum(gradeValList)
#    print(gradeValue)
    doubleGradeValue = sum(doubleGradeValList)
#    print(doubleGradeValue)
    totalValue = gradeValue + doubleGradeValue - gradeOneValue - len(gradeOneIndexes)*100
#    print(totalValue)
    return totalValue