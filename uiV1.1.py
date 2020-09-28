from tkinter import *
from tkinter import ttk
from datetime import *
import gradeCalc


userDict = {'Martin':'72461595822','Mirella':'71613483974'}
monthDict = {'Január':'01','Február':'02','Március':'03','Április':'04','Május':'05','Június':'06','Július':'07',
             'Augusztus':'08','Szeptember':'09','Október':'10','November':'11','December':'12','01':'01',
             '02':'02','':'03','04':'04','05':'05','06':'06','07':'07','08':'08',
             '09':'09','10':'10','11':'11','12':'12'}

def login():
    errorlabel.config(text=' ')
    userName = str(userDict[userEntry.get()])
    password = str(passEntry.get())
    institute = str(instituteEntry.get())

    token = gradeCalc.getToken(userName,password,institute)
    jsonData  = gradeCalc.getStudentAmiData(token,institute)
    gradeCalc.convert(jsonData)
    errorlabel.config(text='Success!')
    currMonth()

def query():
    dateFrom = dateFromYear.get() + '-' + monthDict[dateFromMonth.get()] + '-' + dateFromDay.get()
    dateTo = dateToYear.get() + '-' + monthDict[dateToMonth.get()] + '-' + dateToDay.get()
    money = gradeCalc.calc(dateFrom,dateTo)
    if money < 0:
        moneyLabel.config(text=money, fg='red')
    else:
        moneyLabel.config(text=money,fg='green')

yearList = ['2019','2020','2021','2022','2023','2024']
monthList = ['Január','Február','Március','Április','Május','Június','Július','Augusztus','Szeptember','Október',
             'November','December']
daylist = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21',
           '22','23','24','25','26','27','28','29','30','31']

def currMonth():
    currentDate = datetime.date(datetime.now())
    currentYear = str(currentDate.year)
    currentMonth = str(currentDate.month)
    currentDay = str(currentDate.day)

    if len(currentDay) == 1:
        currentDay = '0'+ currentDay

    if len(currentMonth) == 1:
        currentMonth = '0' + currentMonth

    dateFromYear.delete(0, END)
    dateFromYear.insert(END,currentYear)
    dateFromMonth.delete(0, END)
    dateFromMonth.insert(END,currentMonth)
    dateFromDay.delete(0, END)
    dateFromDay.insert(END,'01')

    dateToYear.delete(0, END)
    dateToYear.insert(END,currentYear)
    dateToMonth.delete(0, END)
    dateToMonth.insert(END,currentMonth)
    dateToDay.delete(0, END)
    dateToDay.insert(END,currentDay)
    query()

def lastMonth():
    currentDate = datetime.date(datetime.now())
    currentYear = str(currentDate.year)
    currentMonth = str(currentDate.month)
    currentDay = str(currentDate.day)

    lastMonth = str(currentDate.month - 1)

    if len(currentDay) == 1:
        currentDay = '0' + currentDay

    if len(currentMonth) == 1:
        currentMonth = '0' + currentMonth

    if len (lastMonth) == 1:
        lastMonth = '0' + lastMonth

    dateFromYear.delete(0, END)
    dateFromYear.insert(END, currentYear)
    dateFromMonth.delete(0, END)
    dateFromMonth.insert(END, lastMonth)
    dateFromDay.delete(0, END)
    dateFromDay.insert(END, '01')

    dateToYear.delete(0, END)
    dateToYear.insert(END, currentYear)
    dateToMonth.delete(0, END)
    dateToMonth.insert(END, currentMonth)
    dateToDay.delete(0, END)
    dateToDay.insert(END, '01')
    query()

root = Tk()
root.geometry('850x370')
root.resizable(height=FALSE,width=FALSE)

#-----------------LOGINframe--------------------------------------------------------

#----FRAME----
loginFrame = Frame(root,bd=2,relief='groove',padx=5)
loginFrame.grid(row=0,column=0,padx=5,pady=5)
loginLabel = Label(loginFrame,text='Login',width=10,bd=2,relief='groove').grid(row=0,column=0,pady=5)

#----ENTRIES----
userEntry = ttk.Combobox(loginFrame,width=15, values = ['Martin','Mirella'])
userEntry.insert(END,'Martin')
userEntry.grid(column=1,row=1,pady=2)

passEntry = ttk.Combobox(loginFrame,width=15, values = ['2004-08-26','2001-01-29'])
passEntry.insert(END,'2004-08-26')
passEntry.grid(column=1,row=2,pady=2)

instituteEntry = ttk.Combobox(loginFrame,width=15, values = ['paszc-faller','klik037935001'])
instituteEntry.insert(END, 'paszc-faller')
instituteEntry.grid(column=1,row=3,pady=2)

#----LABELS----
userLabel = Label(loginFrame,text='Username: ').grid(column=0,row=1)
passLabel = Label(loginFrame,text='Password: ').grid(column=0,row=2)
instuteLabel = Label(loginFrame,text='Institute ID: ').grid(column=0,row=3)
errorlabel = Label(loginFrame,text='')
errorlabel.grid(column=1, row=4)

#----BUTTON----
loginButton = Button(loginFrame, text='Login',width=10,command=login).grid(column=0,row=4,pady=10)
#-----------------------------------------------------------------------------------

#--------dateFROMframe--------------------------------------------------------------

#--FRAME--
dateFromFrame = Frame(root, bd=2,relief='groove',padx=5,pady=16)
dateFromFrame.grid(row=0,column=1)
dateStartLabel = Label(dateFromFrame,text='Enter starting date',bd=2,relief='groove').grid(row=0, column=0,padx=5,pady=0)

#------COMBOBOXES------
dateFromYear = ttk.Combobox(dateFromFrame, values=yearList)
dateFromYear.grid(row=1,column=1)
yearFromLabel = Label(dateFromFrame,text='Year: ').grid(row=1,column=0,pady=5)

dateFromMonth = ttk.Combobox(dateFromFrame,values=monthList)
dateFromMonth.grid(row=2,column=1)
monthFromLabel = Label(dateFromFrame,text='Month: ').grid(row=2,column=0,pady=5)

dateFromDay = ttk.Combobox(dateFromFrame, values=daylist)
dayFromLabel = Label(dateFromFrame,text='Day: ').grid(row=3, column=0)
dateFromDay.grid(row=3,column=1,pady=5)
#-----------------------------------------------------------------------------------

#-------dateTOframe-----------------------------------------------------------------

#----FRAME----
dateToFrame = Frame(root, bd=2,relief='groove',padx=5,pady=16)
dateToFrame.grid(row=0,column=2,padx=5)
dateStartLabel = Label(dateToFrame,text='Enter ending date',bd=2,relief='groove').grid(row=0, column=0,padx=5,pady=0)

#----COMBOBOXES----
dateToYear = ttk.Combobox(dateToFrame, values=yearList)
dateToYear.grid(row=1,column=1)
yearToLabel = Label(dateToFrame,text='Year: ').grid(row=1,column=0,pady=5)

dateToMonth = ttk.Combobox(dateToFrame, values=monthList)
dateToMonth.grid(row=2,column=1)
monthToLabel = Label(dateToFrame,text='Month: ').grid(row=2,column=0,pady=5)

dateToDay = ttk.Combobox(dateToFrame, values=daylist)
dateToDay.grid(row=3,column=1)
dayToLabel = Label(dateToFrame,text='Day: ').grid(row=3,column=0,pady=5)
#-----------------------------------------------------------------------------------

queryFrame = Frame(root, bd=2, relief='groove',padx=5,pady=5)
queryFrame.grid(row=0, column=3)
queryButton = Button(queryFrame,text='Make \n Query',height=9, width=7, command=query).grid(row=0,column=0)


#----------moneyLabelFrame----------------------------------------------------------

#----FRAME----
moneyLabelFrame = Frame(root, bd=2, relief='groove')
moneyLabelFrame.grid(row=1, column=0,columnspan=3,rowspan=2)

#----LABEL----
moneyLabel = Label(moneyLabelFrame, text='-------',font=('Courier','129'))
moneyLabel.grid(row=0,column=0)
#-----------------------------------------------------------------------------------


monthButtonFrame = Frame(root, bd=2,relief='groove', padx=5,pady=5)
monthButtonFrame.grid(row=1,column=3, padx=5,pady=5)

currMonthButton = Button(monthButtonFrame, text='Current \n Month',command=currMonth, height=5,width=7)
currMonthButton.grid(row=0,column=0)
lastMonthButton = Button(monthButtonFrame, text='Last \n Month',command=lastMonth,height=5,width=7)
lastMonthButton.grid(row=1,column=0)


try:
    currMonth()
except FileNotFoundError:
    print('No CSV file')
root.mainloop()