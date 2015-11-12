import wx
import wx.lib.mixins.listctrl as listmix
import libvirt

conn=libvirt.open("qemu:///system")

class CheckListCtrl(wx.ListCtrl, listmix.CheckListCtrlMixin, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, *args, **kwargs):
        wx.ListCtrl.__init__(self, *args, **kwargs)
        listmix.CheckListCtrlMixin.__init__(self)
        listmix.ListCtrlAutoWidthMixin.__init__(self)
        self.setResizeColumn(2)

class MainWindow(wx.Frame):

    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.panel = wx.Panel(self)
        self.list = CheckListCtrl(self.panel, style=wx.LC_REPORT)
        self.list.InsertColumn(0, "Check", width = 175)
        self.Bind(wx.EVT_LIST_COL_CLICK, self.OnColClick, self.list)

        self.list.InsertColumn(1,"Max Mem", width = 100)
        self.list.InsertColumn(2,"# of vCPUs", width = 100)

        for i,id in enumerate(conn.listDefinedDomains()):
            dom = conn.lookupByName(id)
            infos = dom.info()
            pos = self.list.InsertStringItem(1,dom.name()) 
            self.list.SetStringItem(pos,1,str(infos[1]))
            self.list.SetStringItem(pos,2,str(infos[3]))

        self.StrButton = wx.Button(self.panel, label="Start")
        self.Bind(wx.EVT_BUTTON, self.onStrButton, self.StrButton)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.list, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        self.sizer.Add(self.StrButton, flag=wx.EXPAND | wx.ALL, border=5)
        self.panel.SetSizerAndFit(self.sizer)
        self.Show()

    def onStrButton(self, event):
        if self.StrButton.GetLabel() == "Start":
            num = self.list.GetItemCount()
            for i in range(num):
                if self.list.IsChecked(i):
                    dom = conn.lookupByName(self.list.GetItem(i, 0).Text)
                    dom.create()
                    print ("%d started" % dom.ID())
 
    def OnColClick(self, event):
         item = self.list.GetColumn(0)
         if item is not None:
             if item.GetText() == "Check":
                 item.SetText("Uncheck")
                 self.list.SetColumn(0, item)
                 num = self.list.GetItemCount()
                 for i in range(num):
                     self.list.CheckItem(i,True)
             else:
                 item.SetText("Check")
                 self.list.SetColumn(0, item)
                 num = self.list.GetItemCount()
                 for i in range(num):
                     self.list.CheckItem(i,False)

         event.Skip()
 
app = wx.App(False)
win = MainWindow(None)
app.MainLoop()
