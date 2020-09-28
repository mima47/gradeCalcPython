from tkinter import *
from tkinter import ttk
from datetime import *
import kretaApi


userDict = {'Martin':'72461595822','Mirella':'71613483974'}

monthDict = {'Január':'01','Február':'02','Március':'03','Április':'04','Május':'05','Június':'06','Július':'07',
             'Augusztus':'08','Szeptember':'09','Október':'10','November':'11','December':'12','01':'01',
             '02':'02','':'03','04':'04','05':'05','06':'06','07':'07','08':'08',
             '09':'09','10':'10','11':'11','12':'12'}

yearList = ['2019','2020','2021','2022','2023','2024']

monthList = ['Január','Február','Március','Április','Május','Június','Július','Augusztus','Szeptember','Október',
             'November','December']

daylist = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21',
           '22','23','24','25','26','27','28','29','30','31']
def login():
    global userName
    global password
    global institute
    try:
        errorlabel.config(text=' ')
        userName = str(userDict[userEntry.get()])
        password = str(passEntry.get())
        institute = str(instituteEntry.get())

        token = kretaApi.getToken(userName,password,institute)
        jsonData  = kretaApi.getStudentAmiData(token,institute)
        kretaApi.convertStudent(jsonData)
        errorlabel.config(fg='green',text='Success!')
        currMonth()
    except:
        errorlabel.config(fg='red',text='Something \n went wrong')

def query():
    dateFrom = dateFromYear.get() + '-' + monthDict[dateFromMonth.get()] + '-' + dateFromDay.get()
    dateTo = dateToYear.get() + '-' + monthDict[dateToMonth.get()] + '-' + dateToDay.get()
    money = kretaApi.calc(dateFrom,dateTo)
    if money < 0:
        moneyLabel.config(text=str(money) + 'Ft', fg='red')
    else:
        moneyLabel.config(text=str(money) + 'Ft',fg='green')



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

def chooseUser(*args):
    if textvariable.get() == 'Martin':
        passEntry.delete(0,END)
        passEntry.insert(END, '2004-08-26')

        instituteEntry.delete(0,END)
        instituteEntry.insert(END, 'paszc-faller')

    elif textvariable.get() == 'Mirella':
        passEntry.delete(0, END)
        passEntry.insert(END, '2001-01-29')

        instituteEntry.delete(0, END)
        instituteEntry.insert(END, 'klik037935001')
    else:
        print('No such User')

def openAverages():

    global userName
    global password
    global institute
    averageWindow = Toplevel(root,padx=5, pady=5)
    averageWindow.title('Averages')
    averageWindow.resizable(width=FALSE, height=FALSE)
    try:
        averageDict = kretaApi.getAverageDict(userName,password,institute)
    #========fizika==================================================
        fizikaFrame = Frame(averageWindow, pady=5, padx=5)
        fizikaFrame.grid(row = 0, column = 0)

        fizikaLabel = Label(fizikaFrame, text='Fizika', font=('Bahnschrift Light', 24))
        fizikaLabel.grid(row = 0, column = 0)

        fizikaAverageLabel = Label(fizikaFrame, text = averageDict['Fizika'], font=('Bahnschrift Light', 46), bd=2, relief='groove')
        fizikaAverageLabel.grid(row = 1, column = 0)
    #================================================================

    #========IT alapok===============================================
        itAlapFrame = Frame(averageWindow, pady=5, padx=5)
        itAlapFrame.grid(row=0, column=1)

        itAlapLabel = Label(itAlapFrame, text='IT alapok', font=('Bahnschrift Light', 24))
        itAlapLabel.grid(row=0, column=0)

        itAlapAverageLabel = Label(itAlapFrame, text=averageDict['IT alapok'], font=('Bahnschrift Light', 46), bd=2, relief='groove')
        itAlapAverageLabel.grid(row=1, column=0)
    #================================================================

    #=======IT alapok Gyakorlat======================================
        itAlapGyakFrame = Frame(averageWindow, pady=5, padx=5)
        itAlapGyakFrame.grid(row=0, column=2)

        itAlapGyakLabel = Label(itAlapGyakFrame, text='IT gyak.', font=('Bahnschrift Light', 24))
        itAlapGyakLabel.grid(row=0, column=0)

        itAlapGyakAverageLabel = Label(itAlapGyakFrame, text=averageDict['IT alapok gyakorlat'], font=('Bahnschrift Light', 46), bd=2, relief='groove')
        itAlapGyakAverageLabel.grid(row=1, column=0)
    #================================================================

    #========Szakmai Angol===========================================
        itAngolFrame = Frame(averageWindow, pady=5, padx=5)
        itAngolFrame.grid(row=0, column=3)

        itAngolLabel = Label(itAngolFrame, text='IT Ang.', font=('Bahnschrift Light', 24))
        itAngolLabel.grid(row=0, column=0)

        itAngolAverageLabel = Label(itAngolFrame, text=averageDict['IT szakmai angol nyelv'], font=('Bahnschrift Light', 46), bd=2, relief='groove')
        itAngolAverageLabel.grid(row=1, column=0)
    #================================================================

    #=======Angol====================================================
        angolFrame = Frame(averageWindow, pady=5, padx=5)
        angolFrame.grid(row=0, column=4)

        angolLabel = Label(angolFrame, text='Angol', font=('Bahnschrift Light', 24))
        angolLabel.grid(row=0, column=0)

        angolAverageLabel = Label(angolFrame, text=averageDict['Idegen nyelv (Angol)'], font=('Bahnschrift Light', 46), bd=2, relief='groove')
        angolAverageLabel.grid(row=1, column=0)
    #================================================================

    #======Informatika===============================================
        infoFrame = Frame(averageWindow, pady=5, padx=5)
        infoFrame.grid(row=0, column=5)

        infoLabel = Label(infoFrame, text='Info', font=('Bahnschrift Light', 24))
        infoLabel.grid(row=0, column=0)

        infoAverageLabel = Label(infoFrame, text=averageDict['Informatika'], font=('Bahnschrift Light', 46), bd=2, relief='groove')
        infoAverageLabel.grid(row=1, column=0)
    #================================================================

    #=======KKT======================================================
        kktFrame = Frame(averageWindow, pady=5, padx=5)
        kktFrame.grid(row=0, column=6)

        kktLabel = Label(kktFrame, text='KKT', font=('Bahnschrift Light', 24))
        kktLabel.grid(row=0, column=0)

        kktAverageLabel = Label(kktFrame, text=averageDict['Kotelezo Komplex termeszettudomanyos tantargy'], font=('Bahnschrift Light', 46), bd=2, relief='groove')
        kktAverageLabel.grid(row=1, column=0)
    #================================================================

    #=======Magyar===================================================
        magyarFrame = Frame(averageWindow, pady=5, padx=5)
        magyarFrame.grid(row=1, column=0)

        magyarLabel = Label(magyarFrame, text='Magyar', font=('Bahnschrift Light', 24))
        magyarLabel.grid(row=0, column=0)

        magyarAverageLabel = Label(magyarFrame, text=averageDict['Magyar nyelv es irodalom'], font=('Bahnschrift Light', 46), bd=2, relief='groove')
        magyarAverageLabel.grid(row=1, column=0)
    #================================================================

    #=====Matek======================================================
        matekFrame = Frame(averageWindow, pady=5, padx=5)
        matekFrame.grid(row=1, column=1)

        matekLabel = Label(matekFrame, text='Matek', font=('Bahnschrift Light', 24))
        matekLabel.grid(row=0, column=0)

        matekAverageLabel = Label(matekFrame, text=averageDict['Matematika'], font=('Bahnschrift Light', 46), bd=2, relief='groove')
        matekAverageLabel.grid(row=1, column=0)
    #================================================================

    #======Muveszet==================================================
        muveszetFrame = Frame(averageWindow, pady=5, padx=5)
        muveszetFrame.grid(row=1, column=2)

        muveszetLabel = Label(muveszetFrame, text='Muv.', font=('Bahnschrift Light', 24))
        muveszetLabel.grid(row=0, column=0)

        muveszetAverageLabel = Label(muveszetFrame, text=averageDict['Muveszetek'], font=('Bahnschrift Light', 46), bd=2, relief='groove')
        muveszetAverageLabel.grid(row=1, column=0)
    #================================================================

    #======Progamozas================================================
        progFrame = Frame(averageWindow, pady=5, padx=5)
        progFrame.grid(row=1, column=3)

        progLabel = Label(progFrame, text='Prog', font=('Bahnschrift Light', 24))
        progLabel.grid(row=0, column=0)

        progAverageLabel = Label(progFrame, text=averageDict['Programozas'], font=('Bahnschrift Light', 46), bd=2, relief='groove')
        progAverageLabel.grid(row=1, column=0)
    #================================================================

    #=====ProgramozasGyakorlat=======================================
        progGyakFrame = Frame(averageWindow, pady=5, padx=5)
        progGyakFrame.grid(row=1, column=4)

        progGyakLabel = Label(progGyakFrame, text='ProgGyak', font=('Bahnschrift Light', 24))
        progGyakLabel.grid(row=0, column=0)

        progGyakAverageLabel = Label(progGyakFrame, text=averageDict['Programozas gyakorlat'], font=('Bahnschrift Light', 46), bd=2, relief='groove')
        progGyakAverageLabel.grid(row=1, column=0)
    #================================================================

    #======Testneveles===============================================
        tesiFrame = Frame(averageWindow, pady=5, padx=5)
        tesiFrame.grid(row=1, column=5)

        tesiLabel = Label(tesiFrame, text='Tesi', font=('Bahnschrift Light', 24))
        tesiLabel.grid(row=0, column=0)

        tesiAverageLabel = Label(tesiFrame, text=averageDict['Testneveles'], font=('Bahnschrift Light', 46), bd=2, relief='groove')
        tesiAverageLabel.grid(row=1, column=0)
    #================================================================

    #======Tortenelem================================================
        toriFrame = Frame(averageWindow, pady=5, padx=5)
        toriFrame.grid(row=1, column=6)

        toriLabel = Label(toriFrame, text='Tori', font=('Bahnschrift Light', 24))
        toriLabel.grid(row=0, column=0)

        toriAverageLabel = Label(toriFrame, text=averageDict['Tortenelem'], font=('Bahnschrift Light', 46), bd=2, relief='groove')
        toriAverageLabel.grid(row=1, column=0)
    #================================================================
    except:
        averageErrorLabel = Label(averageWindow, fg = 'red', text='Something went wrong, make sure you are signed in, and reopen this window')
        averageErrorLabel.pack()


root = Tk()
root.title('Grade Calculator')
#root.geometry('850x370')
root.resizable(height=FALSE,width=FALSE)
root.config(pady=10)

#-----------------LOGINframe--------------------------------------------------------

#----FRAME----
loginFrame = Frame(root,bd=2,relief='groove',padx=5)
loginFrame.grid(row=0,column=0,padx=5,pady=5)
loginLabel = Label(loginFrame,text='Login',width=10,bd=2,relief='groove').grid(row=0,column=0,pady=5)

#----ENTRIES----
textvariable = StringVar(root)
textvariable.set("Select User")
textvariable.trace('w', chooseUser)
userEntry = ttk.Combobox(loginFrame,width=15, values = ['Martin','Mirella'],textvariable=textvariable)
#userEntry.insert(END,'Martin')
userEntry.grid(column=1,row=1,pady=2)

passEntry = ttk.Combobox(loginFrame,width=15, values = ['2004-08-26','2001-01-29'])
#passEntry.insert(END,'2004-08-26')
passEntry.grid(column=1,row=2,pady=2)

instituteEntry = ttk.Combobox(loginFrame,width=15, values = ['paszc-faller','klik037935001'])
#instituteEntry.insert(END, 'paszc-faller')
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
moneyLabel = Label(moneyLabelFrame, text='-------',font=('Bahnschrift Light','129'))
moneyLabel.grid(row=0,column=0)
#-----------------------------------------------------------------------------------


monthButtonFrame = Frame(root, bd=2,relief='groove', padx=5,pady=5)
monthButtonFrame.grid(row=1,column=3, padx=5,pady=5)

currMonthButton = Button(monthButtonFrame, text='Current \n Month',command=currMonth, height=5,width=7)
currMonthButton.grid(row=0,column=0)
lastMonthButton = Button(monthButtonFrame, text='Last \n Month',command=lastMonth,height=5,width=7)
lastMonthButton.grid(row=1,column=0)


#--------Menubar--------------------------------------------------------------------

menubar = Menu(root)
otherMenu = Menu(menubar, tearoff = False)

otherMenu.add_command(label = 'Show averages',command = openAverages)
menubar.add_cascade(label = 'Other',menu = otherMenu)
root.config(menu=menubar)
#-----------------------------------------------------------------------------------

try:
    currMonth()
except FileNotFoundError:
    print('No CSV file')
root.mainloop()