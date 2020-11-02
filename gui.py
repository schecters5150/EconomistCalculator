import tkinter as tk
import os

class Application(tk.Frame):
    
    
    rowPA = 3
    rowWI = 4
    rowMI = 5
    rowME = 6
    rowME1 = 7
    rowME2 = 8
    rowNE1 = 9
    rowFL = 10
    rowNC = 11
    rowGA = 12
    rowAZ = 13
    rowTX = 14



    rowBidenProb = 20
    rowOptions = 21

#declare globals
    PA = 0
    FL = 0
    WI = 0
    MI = 0
    NC = 0
    GA = 0
    AZ = 0
    TX = 0
    ME = 0
    ME1 = 0
    ME2 = 0
    NE1 = 0


    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

        

    def create_widgets(self):
        

        self.bidenProbText = tk.StringVar()
        self.paText = tk.StringVar()
        self.flText = tk.StringVar()
        self.wiText = tk.StringVar()
        self.miText = tk.StringVar()
        self.ncText = tk.StringVar()
        self.azText = tk.StringVar()
        self.gaText = tk.StringVar()
        self.txText = tk.StringVar()
        self.meText = tk.StringVar()
        self.me1Text = tk.StringVar()
        self.me2Text = tk.StringVar()
        self.ne1Text = tk.StringVar()

        CURR_DIR = os.path.dirname(os.path.realpath(__file__))
        winProb = open(CURR_DIR + "/win.txt", 'r')
        self.bidenProbText.set("Biden's win probability is " + winProb.read())
        winProb.close()

        self.title2020Lbl = tk.Label(self)
        self.title2020Lbl["text"] = "election 2020"
        self.title2020Lbl.grid(row = 1, column = 1)

        self.titleLbl = tk.Label(self)
        self.titleLbl["text"] = "rachel's hi effort economist calculator   "
        self.titleLbl.grid(row = 1, column = 2)

        self.titleSpaceLbl = tk.Label(self)
        self.titleSpaceLbl["text"] = " "
        self.titleSpaceLbl.grid(row = 2, column = 2)

        self.paBtn = tk.Button(self)
        self.paBtn["text"] = "Pennsylvania"
        self.paBtn["command"] = self.paBtnEvent
        self.paBtn.grid(row = self.rowPA, column = 1)
        self.paLbl = tk.Label(self)
        self.paLbl["textvariable"] = self.paText
        self.paLbl.grid(row = self.rowPA, column = 2)


        self.flBtn = tk.Button(self)
        self.flBtn["text"] = "Florida"
        self.flBtn["command"] = self.flBtnEvent
        self.flBtn.grid(row = self.rowFL, column = 1)
        self.flLbl = tk.Label(self)
        self.flLbl["textvariable"] = self.flText
        self.flLbl.grid(row = self.rowFL, column = 2)


        self.wiBtn = tk.Button(self)
        self.wiBtn["text"] = "Wisconsin"
        self.wiBtn["command"] = self.wiBtnEvent
        self.wiBtn.grid(row = self.rowWI, column = 1)
        self.wiLbl = tk.Label(self)
        self.wiLbl["textvariable"] = self.wiText
        self.wiLbl.grid(row = self.rowWI, column = 2)

        self.miBtn = tk.Button(self)
        self.miBtn["text"] = "Michigan"
        self.miBtn["command"] = self.miBtnEvent
        self.miBtn.grid(row = self.rowMI, column = 1)
        self.miLbl = tk.Label(self)
        self.miLbl["textvariable"] = self.miText
        self.miLbl.grid(row = self.rowMI, column = 2)

        self.ncBtn = tk.Button(self)
        self.ncBtn["text"] = "North Carolina"
        self.ncBtn["command"] = self.ncBtnEvent
        self.ncBtn.grid(row = self.rowNC, column = 1)
        self.ncLbl = tk.Label(self)
        self.ncLbl["textvariable"] = self.ncText
        self.ncLbl.grid(row = self.rowNC, column = 2)

        self.azBtn = tk.Button(self)
        self.azBtn["text"] = "Arizona"
        self.azBtn["command"] = self.azBtnEvent
        self.azBtn.grid(row = self.rowAZ, column = 1)
        self.azLbl = tk.Label(self)
        self.azLbl["textvariable"] = self.azText
        self.azLbl.grid(row = self.rowAZ, column = 2)

        self.gaBtn = tk.Button(self)
        self.gaBtn["text"] = "Georgia"
        self.gaBtn["command"] = self.gaBtnEvent
        self.gaBtn.grid(row = self.rowGA, column = 1)
        self.gaLbl = tk.Label(self)
        self.gaLbl["textvariable"] = self.gaText
        self.gaLbl.grid(row = self.rowGA, column = 2)

        self.txBtn = tk.Button(self)
        self.txBtn["text"] = "Texas"
        self.txBtn["command"] = self.txBtnEvent
        self.txBtn.grid(row = self.rowTX, column = 1)
        self.txLbl = tk.Label(self)
        self.txLbl["textvariable"] = self.txText
        self.txLbl.grid(row = self.rowTX, column = 2)

        self.meBtn = tk.Button(self)
        self.meBtn["text"] = "Maine"
        self.meBtn["command"] = self.meBtnEvent
        self.meBtn.grid(row = self.rowME, column = 1)
        self.meLbl = tk.Label(self)
        self.meLbl["textvariable"] = self.meText
        self.meLbl.grid(row = self.rowME, column = 2)

        self.me1Btn = tk.Button(self)
        self.me1Btn["text"] = "Maine 1"
        self.me1Btn["command"] = self.me1BtnEvent
        self.me1Btn.grid(row = self.rowME1, column = 1)
        self.me1Lbl = tk.Label(self)
        self.me1Lbl["textvariable"] = self.me1Text
        self.me1Lbl.grid(row = self.rowME1, column = 2)

        self.me2Btn = tk.Button(self)
        self.me2Btn["text"] = "Maine 2"
        self.me2Btn["command"] = self.me2BtnEvent
        self.me2Btn.grid(row = self.rowME2, column = 1)
        self.me2Lbl = tk.Label(self)
        self.me2Lbl["textvariable"] = self.me2Text
        self.me2Lbl.grid(row = self.rowME2, column = 2)

        self.ne1Btn = tk.Button(self)
        self.ne1Btn["text"] = "Nebreska 1"
        self.ne1Btn["command"] = self.ne1BtnEvent
        self.ne1Btn.grid(row = self.rowNE1, column = 1)
        self.ne1Lbl = tk.Label(self)
        self.ne1Lbl["textvariable"] = self.ne1Text
        self.ne1Lbl.grid(row = self.rowNE1, column = 2)


        self.winProbLbl = tk.Label(self)
        self.winProbLbl["textvariable"] = self.bidenProbText
        self.winProbLbl.grid(row = self.rowBidenProb, column = 1)

        self.runBtn = tk.Button(self)
        self.runBtn["text"] = "Run NIGHTMARE"
        self.runBtn["command"] = self.runModel
        self.runBtn["bg"] = "red"
        self.runBtn.grid(row = self.rowOptions, column = 1)

        self.quit = tk.Button(self, text="QUIT", 
                              command=self.master.destroy)
        self.quit.grid(row = self.rowOptions, column = 2)


    def updateWinProbLbl(self):
        CURR_DIR = os.path.dirname(os.path.realpath(__file__))
        winProb = open(CURR_DIR + "/win.met", 'r')
        self.bidenProbText.set(winProb.read())


        
    def paBtnEvent(self):
        PA = self.PA
        PA = PA + 1
        if PA > 2:
            PA = 0          
        self.PA = PA 
        
        if PA == 0:
            self.paText.set("Undecided")
        if PA == 1:
            self.paText.set("Biden Win")
        if PA == 2:
            self.paText.set("Trump Win")

    def flBtnEvent(self):
        FL = self.FL
        FL = FL + 1
        if FL > 2:
            FL = 0          
        self.FL = FL 
        
        if FL == 0:
            self.flText.set("Undecided")
        if FL == 1:
            self.flText.set("Biden Win")
        if FL == 2:
            self.flText.set("Trump Win")

    def wiBtnEvent(self):
        WI = self.WI
        WI = WI + 1
        if WI > 2:
            WI = 0          
        self.WI = WI 
        
        if WI == 0:
            self.wiText.set("Undecided")
        if WI == 1:
            self.wiText.set("Biden Win")
        if WI == 2:
            self.wiText.set("Trump Win")

    def miBtnEvent(self):
        MI = self.MI
        MI = MI + 1
        if MI > 2:
            MI = 0          
        self.MI = MI 
        
        if MI == 0:
            self.miText.set("Undecided")
        if MI == 1:
            self.miText.set("Biden Win")
        if MI == 2:
            self.miText.set("Trump Win")

    def ncBtnEvent(self):
        NC = self.NC
        NC = NC + 1
        if NC > 2:
            NC = 0          
        self.NC = NC 
        print(NC)

        if NC == 0:
            self.ncText.set("Undecided")
        if NC == 1:
            self.ncText.set("Biden Win")
        if NC == 2:
            self.ncText.set("Trump Win")

    def azBtnEvent(self):
        AZ = self.AZ
        AZ = AZ + 1
        if AZ > 2:
            AZ = 0          
        self.AZ = AZ 
        print(AZ)

        if AZ == 0:
            self.azText.set("Undecided")
        if AZ == 1:
            self.azText.set("Biden Win")
        if AZ == 2:
            self.azText.set("Trump Win")

    def gaBtnEvent(self):
        GA = self.GA
        GA = GA + 1
        if GA > 2:
            GA = 0          
        self.GA = GA 
        print(GA)

        if GA == 0:
            self.gaText.set("Undecided")
        if GA == 1:
            self.gaText.set("Biden Win")
        if GA == 2:
            self.gaText.set("Trump Win")

    def txBtnEvent(self):
        TX = self.TX
        TX = TX + 1
        if TX > 2:
            TX = 0          
        self.TX = TX 
        print(TX)

        if TX == 0:
            self.txText.set("Undecided")
        if TX == 1:
            self.txText.set("Biden Win")
        if TX == 2:
            self.txText.set("Trump Win")

    def meBtnEvent(self):
        ME = self.ME
        ME = ME + 1
        if ME > 2:
            ME = 0          
        self.ME = ME 
        print(ME)

        if ME == 0:
            self.meText.set("Undecided")
        if ME == 1:
            self.meText.set("Biden Win")
        if ME == 2:
            self.meText.set("Trump Win")

    def me1BtnEvent(self):
        ME1 = self.ME1
        ME1 = ME1 + 1
        if ME1 > 2:
            ME1 = 0          
        self.ME1 = ME1 
        print(ME1)

        if ME1 == 0:
            self.me1Text.set("Undecided")
        if ME1 == 1:
            self.me1Text.set("Biden Win")
        if ME1 == 2:
            self.me1Text.set("Trump Win")

    def me2BtnEvent(self):
        ME2 = self.ME2
        ME2 = ME2 + 1
        if ME2 > 2:
            ME2 = 0          
        self.ME2 = ME2 
        print(ME2)

        if ME2 == 0:
            self.me2Text.set("Undecided")
        if ME2 == 1:
            self.me2Text.set("Biden Win")
        if ME2 == 2:
            self.me2Text.set("Trump Win")

    def ne1BtnEvent(self):
        NE1 = self.NE1
        NE1 = NE1 + 1
        if NE1 > 2:
            NE1 = 0          
        self.NE1 = NE1 
        print(NE1)

        if NE1 == 0:
            self.ne1Text.set("Undecided")
        if NE1 == 1:
            self.ne1Text.set("Biden Win")
        if NE1 == 2:
            self.ne1Text.set("Trump Win")


            
        

    def runModel(self):
        CURR_DIR = os.path.dirname(os.path.realpath(__file__))
        bidenStates = open(CURR_DIR + "/BidenStates.csv", 'w')
        trumpStates = open(CURR_DIR + "/TrumpStates.csv", 'w')


        if self.PA == 1:
            bidenStates.write("PA\n")
        if self.WI == 1:
            bidenStates.write("WI\n")
        if self.MI == 1:
            bidenStates.write("MI\n")
        if self.FL == 1:
            bidenStates.write("FL\n")
        if self.NC == 1:
            bidenStates.write("NC\n")
        if self.GA == 1:
            bidenStates.write("GA\n")
        if self.AZ == 1:
            bidenStates.write("AZ\n")
        if self.TX == 1:
            bidenStates.write("TX\n")
        if self.ME == 1:
            bidenStates.write("ME\n")
        if self.ME1 == 1:
            bidenStates.write("ME1\n")
        if self.ME2 == 1:
            bidenStates.write("ME2\n")
        if self.NE1 == 1:
            bidenStates.write("NE1\n")


        if self.PA == 2:
            trumpStates.write("PA\n")
        if self.WI == 2:
            trumpStates.write("WI\n")
        if self.MI == 2:
            trumpStates.write("MI\n")
        if self.FL == 2:
            trumpStates.write("FL\n")
        if self.NC == 2:
            trumpStates.write("NC\n")
        if self.GA == 2:
            trumpStates.write("GA\n")
        if self.AZ == 2:
            trumpStates.write("AZ\n")
        if self.TX == 2:
            trumpStates.write("TX\n")
        if self.ME == 2:
            trumpStates.write("ME\n")
        if self.ME1 == 2:
            trumpStates.write("ME1\n")
        if self.ME2 == 2:
            trumpStates.write("ME2\n")
        if self.NE1 == 2:
            trumpStates.write("NE1\n")

        bidenStates.close()
        trumpStates.close()


        os.system("rscript EconomistModel.R")
        
        winProb = open(CURR_DIR + "/win.txt", 'r')
        self.bidenProbText.set("Biden's win probability is " + winProb.read())
        winProb.close()

root = tk.Tk()
app = Application(master=root)
app.mainloop()