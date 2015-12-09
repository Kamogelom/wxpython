import wx

class Calculator(wx.Frame):
    def __init__(self,parent,title):
        self.screen = ''
        self.operatorStrings = ["+","-","*","/","C","="]
        wx.Frame.__init__(self,parent,title=title, size= (300,600))

        self.CreateStatusBar()

        menubar = wx.MenuBar()
        file = wx.Menu()
        scientific = file.Append(wx.ID_ANY,"scientific","better caculator with more functions")
        menubar.Append(file,"File")
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU,self.scientific,scientific)

        #dsplay screen
        self.screen = wx.TextCtrl(self,style=wx.TE_MULTILINE,pos=(10,20))

        #button,sizers and all that mess
        sizer = wx.GridSizer(rows=5, cols=3, hgap=5, vgap=5)
        ver = wx.BoxSizer(wx.VERTICAL)
        buttons = []
        operators=[]

        # add buttons to sizers
        for i in range(1,4):
            buttons.append(wx.Button(self,i,str(i)))
            sizer.Add(buttons[i-1],0, wx.EXPAND)

        for i in range(4,7):
            buttons.append(wx.Button(self,i,str(i)))
            sizer.Add(buttons[i-1],0, wx.EXPAND)


        for i in range(7,10):
            buttons.append(wx.Button(self,i,str(i)))
            sizer.Add(buttons[i-1],0, wx.EXPAND)

        j =0
        id =10
        for i in self.operatorStrings:
            operators.append(wx.Button(self,id,i))
            sizer.Add(operators[j],0,wx.EXPAND)
            j+=1
            id+=1

        #magic
        ver.Add(self.screen,1,wx.EXPAND)
        ver.Add(sizer,1,wx.EXPAND)

        self.SetSizer(ver)
        self.Show(True)

        # actual work for buttons (fuctionality)
        for i in range(9):
            self.Bind(wx.EVT_BUTTON,self.number,buttons[i])

        for i in range(6):
            self.Bind(wx.EVT_BUTTON,self.operator,operators[i])


    def number(self,e):
        self.screen.AppendText(str(e.Id))

    def operator(self,e):
        if e.Id== 10:
            self.screen.AppendText("+")
        elif e.Id== 11:
            self.screen.AppendText("-")
        elif e.Id== 12:
            self.screen.AppendText("*")
        elif e.Id== 13:
            self.screen.AppendText("/")
        elif e.Id== 14:
            self.screen.Clear()
        elif e.Id== 15:
            x = str(self.screen.GetValue())
            while "\n" in x:
                 x = x[x.find("\n")+1:]
            self.screen.AppendText("= ")
            if not self.check_equation(x):
                self.screen.AppendText("error! \n")
            else:
                self.screen.AppendText(str(eval(x))+"\n")

    def check_equation(self,x):
        list = str(x)
        if (list[0] or list[len(list)-1]) in self.operatorStrings:
            return False
        return True

    def scientific(self,e):
        dailog = wx.MessageDialog(self,"I don't like the smell of your face!","Just kidding!!",wx.OK)
        dailog.ShowModal() # Shows it
        dailog.Destroy() # finally destroy it when finished.



#bookkeeping
app = wx.App()
calc = Calculator(None,"Calculator")
app.MainLoop()