import unidecode
import requests
import pandas
import json
import os
from pandas import DataFrame
from pandas import json_normalize

cwd = os.getcwd()
pathToJson = cwd+'\JSON\\'
pathToCsv = cwd+'\CSV\\'

try:
    os.mkdir('JSON')
    os.mkdir('CSV')
except FileExistsError:
    print('Folders already exists')

def getToken(username, password, instituteCode):
    tokenUrl = 'https://'+instituteCode+'.e-kreta.hu/idp/api/v1/Token'
    headers = {"Content-Type": "application/x-www-form-urlencoded",
               "Accept":"application/json",
               "User-Agent":"Kreta.Ellenorzo/2.9.12.2020042902 (Android; SM-G950F 0.0)"}

    data = ("institute_code="+instituteCode+
            "&userName="+username+
            "&password="+password+
            "&grant_type=password&client_id=919e0c1c-76a2-4646-a2fb-7085bbbf3c56")

    r = requests.post(url=tokenUrl, headers=headers, data=data)
    return r.json()

def getStudentAmiData(accessToken,instituteCode):
    url = 'https://'+instituteCode+'.e-kreta.hu/mapi/api/v1/StudentAmi'
    headers = {'Authorization':'Bearer '+ accessToken,
               'Content-Type':'application/x-www-form-urlencoded',
               'Accept':'application/json',
               'User-Agent':'Kreta.Ellenorzo/2.9.12.2020042902 (Android; SM-G950F 0.0)'}
    response = requests.get(url=url, headers=headers).text
    return response

def getAverageData(accessToken, instituteCode):
    url = 'https://' + instituteCode + '.e-kreta.hu/mapi/api/v1/TantargyiAtlagAmi'
    headers = {'Authorization':'Bearer '+ accessToken,
               'Accept':'application/json',
               'User-Agent':'Kreta.Ellenorzo/2.9.12.2020042902 (Android; SM-G950F 0.0)',
               'Content-Type':'application/x-www-form-urlencoded'}
    response = requests.get(url=url, headers=headers).text
    return response

def convertStudent(jsonData):
    file = open(pathToJson+'studentAmi.json', 'w', encoding='utf-8')
    file.write(jsonData)
    file.close()

    file = open(pathToJson+'studentAmi.json', 'r', encoding='utf-8').read()
    fileCSV = open(pathToCsv+'studentAmi.csv', 'w')
    data = json.loads(file)

    df = pandas.json_normalize(data, 'Evaluations')
    df.to_csv(pathToCsv+r'studentAmi.csv')

def convertNotNormalizedStudent():
    file = open(pathToJson + 'studentAmi.json', 'r', encoding='utf-8').read()
    fileCSV = open(pathToCsv + 'notNormalizedStudentAmi.csv', 'w')
    data = json.loads(file)

    df = pandas.json_normalize(data)
    df.to_csv(pathToCsv + r'notNormalizedStudentAmi.csv')

def convertAverage(jsonData):
    file = open(pathToJson+'averages.json', 'w', encoding='utf-8')
    file.write(jsonData)
    file.close()

    file = open(pathToJson+'averages.json', 'r', encoding='utf-8').read()
    fileCSV = open(pathToCsv+'averages.csv', 'w')
    data = json.loads(file)

    df = pandas.json_normalize(data)
    df.to_csv(cwd+r'\csv\averages.csv')

def convert(jsonData):
    file = open()