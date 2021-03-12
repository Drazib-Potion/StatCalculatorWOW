from tkinter import *
errorcount=0
global loadingbar
AlliIsRunning=False
HordeIsRunning=False

def calc(args):
    global errorcount
    global Errormsg
    global NoErrorMsg

    if args == "Alli":
        Errormsg = Label(WinAlli,text="error:Enter numbers only",font='10')
        NoErrorMsg = Label(WinAlli,text="⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
        loadingbar = Label(WinAlli,text="⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
        try:
            APtotal=APalli.get()+Stralli.get()+(Agialli.get()*1.79)+(Hitalli.get()*18)+(Critalli.get()*23)
        except Exception:
            errorcount=1
            NoErrorMsg.destroy()
            loadingbar.destroy()
            Errormsg.grid(row=8,column=3)
        else:
            if errorcount == 1:
                Errormsg.destroy()
                NoErrorMsg.grid(row=8,column=3)
            ResultAlli = Label(WinAlli,text="equivalent AP : "+str(APtotal)).grid(row=6,column=3)
            errorcount=0

            
    if args == "Horde":
        Errormsg = Label(WinHorde,text="error:Enter numbers only",font='10')
        NoErrorMsg = Label(WinHorde,text="⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
        loadingbar = Label(WinHorde,text="⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
        try:
            APtotal=APHorde.get()+StrHorde.get()+(AgiHorde.get()*1.83)+(HitHorde.get()*20)+(CritHorde.get()*24)
        except Exception:
            errorcount=1
            NoErrorMsg.destroy()
            loadingbar.destroy()
            Errormsg.grid(row=8,column=3)
        else:
            if errorcount == 1:
                Errormsg.destroy()
                NoErrorMsg.grid(row=8,column=3)
            ResultHorde = Label(WinHorde,text="equivalent AP : "+str(APtotal)).grid(row=6,column=3)
            errorcount=0
        
def onclick(args):
    if args == "Alli":
        global WinAlli
        global AlliIsRunning
        if AlliIsRunning == True:
            WinAlli.destroy()
        WinAlli =Toplevel(root)
        AlliIsRunning = True
        WinAlli.title('Alli calc')
        WinAlli.geometry("500x200")
        WinAlli.iconbitmap(r'AlliIcon.ico')
        lblAPalli = Label(WinAlli,text="AP:").grid(row=1,column=1)
        lblStralli = Label(WinAlli,text="Str:").grid(row=2,column=1)
        lblAgialli = Label(WinAlli,text="Agi:").grid(row=3,column=1)
        lblHitalli = Label(WinAlli,text="hit%:").grid(row=4,column=1)
        lblCritalli = Label(WinAlli,text="Crit%:").grid(row=5,column=1)
        lblRules=Label(WinAlli,text="fill the rest with 0",font='Helvetica 18 bold').grid(row=7,column=3)
        
        global APalli
        global Stralli
        global Agialli
        global Hitalli
        global Critalli
        Stralli=IntVar()
        APalli=IntVar()
        Agialli=IntVar()
        Hitalli=IntVar()
        Critalli=IntVar()
        
        EntryAPalli = Entry(WinAlli,textvariabl=APalli).grid(row=1,column=2)
        EntryStralli =Entry(WinAlli,textvariabl=Stralli).grid(row=2,column=2)
        EntryAgialli =Entry(WinAlli,textvariabl=Agialli).grid(row=3,column=2)
        EntryHitalli =Entry(WinAlli,textvariabl=Hitalli).grid(row=4,column=2)
        EntryCritalli =Entry(WinAlli,textvariabl=Critalli).grid(row=5,column=2)

        btnCalcAlli=Button(WinAlli,text="Calc AP",height = 2, width = 10,command=lambda:calc("Alli")).grid(row=6,column=1)
        
        loadingbar = Label(WinAlli,text="⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛").grid(row=8,column=3)
        
        
    if args == "Horde":
        global WinHorde
        global HordeIsRunning
        if HordeIsRunning == True:
            WinHorde.destroy()
        WinHorde =Toplevel(root)
        HordeIsRunning = True
        WinHorde.title('Horde calc')
        WinHorde.geometry("500x200")
        WinHorde.iconbitmap(r'HordeIcon.ico')
        lblAPHorde= Label(WinHorde,text="AP:").grid(row=1,column=1)
        lblStrHorde = Label(WinHorde,text="Str:").grid(row=2,column=1)
        lblAgiHorde = Label(WinHorde,text="Agi:").grid(row=3,column=1)
        lblHitHorde = Label(WinHorde,text="hit%:").grid(row=4,column=1)
        lblCritHorde = Label(WinHorde,text="Crit%:").grid(row=5,column=1)
        lblRules=Label(WinHorde,text="fill the rest with 0",font='Helvetica 18 bold').grid(row=7,column=3)

        global APHorde
        global StrHorde
        global AgiHorde
        global HitHorde
        global CritHorde
        StrHorde=IntVar()
        APHorde=IntVar()
        AgiHorde=IntVar()
        HitHorde=IntVar()
        CritHorde=IntVar()

        EntryAPHorde = Entry(WinHorde,textvariabl=APHorde).grid(row=1,column=2)
        EntryStrHorde =Entry(WinHorde,textvariabl=StrHorde).grid(row=2,column=2)
        EntryAgiHorde =Entry(WinHorde,textvariabl=AgiHorde).grid(row=3,column=2)
        EntryHitHorde =Entry(WinHorde,textvariabl=HitHorde).grid(row=4,column=2)
        EntryCritHorde =Entry(WinHorde,textvariabl=CritHorde).grid(row=5,column=2)

        btnCalcAlli=Button(WinHorde,text="Calc AP",height = 2, width = 10,command=lambda:calc("Horde")).grid(row=6,column=1)
        
        loadingbar = Label(WinHorde,text="⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛").grid(row=8,column=3)

    if args == "Info":
        WinInfo =Toplevel(root)
        WinInfo.title('Info')
        WinInfo.geometry("500x200")
        WinInfo.iconbitmap(r'CalcIcon.ico')
        lblAPInfo = Label(WinInfo,text="1AP = 1AP",font='Helvetica 18 bold')
        lblStrInfo = Label(WinInfo,text="1Str.= 1AP",font='Helvetica 18 bold')
        lblAgiInfo = Label(WinInfo,text="1Agi = 1.83AP(Horde)|1.79AP(Alli)",font='Helvetica 18 bold')
        lblHitInfo = Label(WinInfo,text="1Hit% = 20AP(Horde)|18AP(Alli)",font='Helvetica 18 bold')
        lblCritInfo = Label(WinInfo,text="1Crit% = 24AP(Horde)|23AP(Alli)",font='Helvetica 18 bold')
        lblWindInfo = Label(WinInfo,text="(because of Windfury)")
        lblAPInfo.pack()
        lblStrInfo.pack()
        lblAgiInfo.pack()
        lblHitInfo.pack()
        lblCritInfo.pack()
        lblWindInfo.pack()

        
root = Tk()
root.title('StatCalculatorWOW')
root.iconbitmap(r'WOWicon.ico')
root.geometry("500x200")

btnAlli=Button(root, text="Alliance",command=lambda:onclick("Alli"),height=1,width=20,font='Helvetica 18 bold')
btnHorde=Button(root, text="Horde",command=lambda:onclick("Horde"),height=1,width=20,font='Helvetica 18 bold')
btnInfo=Button(root, text="Info",command=lambda:onclick("Info"),height=1,width=20,font='Helvetica 18 bold')
btnAlli.pack()
btnHorde.pack()
btnInfo.pack()


mainloop()
