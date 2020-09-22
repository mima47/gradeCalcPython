import mysqlfetch
import requests
import sqlite3
import pandas
import json
from pandas import DataFrame
from pandas import json_normalize

def getToken(userName, password, instituteCode):
    tokenUrl = 'https://'+instituteCode+'.e-kreta.hu/idp/api/v1/Token'
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept":"application/json",
               "User-Agent":"Kreta.Ellenorzo/2.9.12.2020042902 (Android; SM-G950F 0.0)"}
    data = "institute_code="+instituteCode+"&userName="+userName+"&password="+password+"&grant_type=password&client_id=919e0c1c-76a2-4646-a2fb-7085bbbf3c56"

    r = requests.post(url=tokenUrl, headers=headers, data=data)
    dict = r.json()
    return dict['access_token']

def getStudentAmiData(accessToken,instituteCode):
    url = 'https://'+instituteCode+'.e-kreta.hu/mapi/api/v1/StudentAmi'
    headers = {'Authorization':'Bearer '+ accessToken, 'Content-Type':'application/x-www-form-urlencoded',
               'Accept':'application/json', 'User-Agent':'Kreta.Ellenorzo/2.9.12.2020042902 (Android; SM-G950F 0.0)'}
    response = requests.get(url=url, headers=headers).text
    return response

def responseStatus(accessToken):
    url = 'https://paszc-faller.e-kreta.hu/mapi/api/v1/StudentAmi'
    headers = {'Authorization': 'Bearer ' + accessToken, 'Content-Type': 'application/x-www-form-urlencoded',
               'Accept': 'application/json', 'User-Agent': 'Kreta.Ellenorzo'}
    response = requests.get(url=url, headers=headers).status_code
    return response

def convert(jsonData):
    file = open('studentAmi.json', 'w', encoding='utf-8')
    file.write(jsonData)
    file.close()

    file = open('studentAmi.json', 'r', encoding='utf-8').read()
    fileCSV = open('studentAmi.csv', 'w')
    data = json.loads(file)

    df = pandas.json_normalize(data, 'Evaluations')
    df.to_csv(r'studentAmi.csv')

def calc(datefrom, dateto):
    mysqlfetch.connect()
    return mysqlfetch.calculate(datefrom,dateto)


#print(responseStatus(getToken('72461595822','2004-08-26','paszc-faller')))