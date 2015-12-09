import wx
import os
Task = 200
class Email(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title, size = (350,400))

        panel1 = wx.Panel(self)

        #menu
        fmenu= wx.Menu()
        menubar =wx.MenuBar()
        menubar.Append(fmenu,"File")
        open=fmenu.Append(wx.OPEN,"open\tCtrl+O")
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU,self.onOpen,open)

        self.timer = wx.Timer(self, 1)
        self.count = 0
        self.Bind(wx.EVT_TIMER,self.onTimer,self.timer)

        send = wx.Button(panel1,-1,"send")
        image =wx.Bitmap('msgIcon.png')
        send.SetBitmap(image)
        send.Bind(wx.EVT_BUTTON,self.send)

        from_text = wx.StaticText(panel1,label = "From: ")
        to_text = wx.StaticText(panel1,label = "To: ")
        subject_text = wx.StaticText(panel1,label = "Subject: ")
        msg =  wx.TextCtrl(panel1, style=wx.TE_MULTILINE,size=(400,100))
        self.gauge = wx.Gauge(panel1,range=Task,size=(180,25))

        t = wx.TextCtrl(panel1, size =(250,-1))
        f = wx.TextCtrl(panel1, size =(250,-1))
        s = wx.TextCtrl(panel1, size =(250,-1))
        self.status = wx.StaticText(panel1,label = '')

        grid = wx.GridBagSizer(3,2)
        grid.Add(from_text,pos =(0,0), flag=wx.LEFT, border=15)
        grid.Add(to_text,pos =(1,0), flag=wx.LEFT, border=15)
        grid.Add(subject_text,pos =(2,0), flag=wx.LEFT, border=15)
        grid.Add(f,pos =(0,1), flag=wx.RIGHT, border=15)
        grid.Add(t,pos =(1,1), flag=wx.RIGHT, border=15)
        grid.Add(s,pos =(2,1), flag=wx.RIGHT, border=15)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(grid, flag=wx.EXPAND, border=15)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add((115,-1))
        hbox.Add(send,wx.EXPAND)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add((50,-1))
        hbox1.Add(self.gauge,wx.EXPAND)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add((115,-1))
        hbox2.Add(self.status,wx.EXPAND)

        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox1.Add(msg,wx.EXPAND,20)
        vbox1.Add(hbox,wx.CENTER,20)
        vbox1.Add(hbox1,wx.CENTER,20)
        vbox1.Add(hbox2,wx.CENTER,20)


        vbox.Add(vbox1, flag=wx.EXPAND,border=15)

        self.SetSizer(vbox)
        self.Show(True)

    # functions
    def onTimer(self,e):
        self.count+=1
        self.gauge.SetValue(self.count)
        if self.count>=Task:
            self.timer.Stop()
            self.status.SetLabel( "sent!")

    def send(self,e):
        self.timer.Start()
        self.status.SetLabel("sending...")

    def onOpen(self,e):
        openFileDialog = wx.FileDialog(self, "open", "", "",
                                       "All files (*.*)|*.*",
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog.ShowModal()

        f =open(openFileDialog.GetPath(),'r')
        print f.read()
        openFileDialog.Destroy()
        f.close()

if __name__ == "__main__":
    app = wx.App(False)
    email = Email(None,"Email.py")
    app.MainLoop()