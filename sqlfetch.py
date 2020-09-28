import sqlite3
import pandas
import os
from datetime import date

cwd = os.getcwd()
pathToDB = cwd+'\DATABASE\student.db'
pathToCsv = cwd+'\CSV\\'

db = sqlite3.connect(pathToDB)
cursor = db.cursor()

# try:
#     os.mkdir('DATABASE')
#     os.mkdir('CSV')
# except FileExistsError:
#     print('Folders already exist')

def connect():
    df = pandas.read_csv(pathToCsv+'studentAmi.csv')
    df.to_sql('studentAmi', db, if_exists='replace', index=False)

    df = pandas.read_csv(pathToCsv+'averages.csv')
    df.to_sql('averages', db, if_exists='replace', index=False)

    df = pandas.read_csv(pathToCsv + 'notNormalizedStudentAmi.csv')
    df.to_sql('studentInfo', db, if_exists='replace', index=False)

def getAverageDict():
    import unidecode
    cursor.execute("SELECT Subject, Value FROM averages WHERE Subject NOT IN ('Magatartás', 'Szorgalom')")
    values = cursor.fetchall()

    subjects = []
    for row in values:
        subjects.append(unidecode.unidecode(row[0]))

    averages = []
    for row in values:
        averages.append(row[1])

    return dict(zip(subjects, averages))

def getAverageDictForHalfYear():
    import unidecode
    cursor.execute("SELECT Subject, Value FROM averages WHERE Subject NOT IN ('Magatartás', 'Szorgalom', 'Művészetek',"
                   " 'Testnevelés', 'Testnevelés és sport','Művészetek: zeneművészet')"
                   " AND Value NOT IN ('NULL')")
    values = cursor.fetchall()

    subjects = []
    for row in values:
        subjects.append(unidecode.unidecode(row[0]))

    averages = []
    for row in values:
        averages.append(row[1])

    return dict(zip(subjects, averages))

def getHalfYearGrades():
    cursor.execute("SELECT Subject, NumberValue FROM studentAmi WHERE Subject NOT IN "
                   "('Magatartás', 'Szorgalom', 'Művészetek', 'Testnevelés',"
                   " 'Testnevelés és sport','Művészetek: zeneművészet') "
                   "AND Type IN ('HalfYear') "
                   "AND NumberValue IN ('5', '4')")
    values = cursor.fetchall()

    grades = []
    for row in values:
        grades.append(row[1])

    subjects = []
    for row in values:
        subjects.append(row[0])

    halfYearGrades = dict(zip(subjects, grades))
    return halfYearGrades

def calculateHalfYearGrades(halfYearGrades):

    gradeMoneyValues = []
    for i in halfYearGrades:
        if i == 5:
            gradeMoneyValues.append(5*500)
        elif i == 4:
            gradeMoneyValues.append(5*400)
        else:
            gradeMoneyValues.append(0)

    return sum(gradeMoneyValues)
    
def getCurrentStudentID():
    cursor.execute("SELECT StudentID FROM studentInfo")
    values = cursor.fetchall()

    studentID = []
    for row in values:
        studentID.append(row[0])
    return str(studentID[0])

def getCurrentStudentName():
    cursor.execute("SELECT Name FROM studentInfo")
    values = cursor.fetchall()

    studentName = []
    for row in values:
        studentName.append(row[0])
    return str(studentName[0])

def calculate(dateFrom,dateTo):
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