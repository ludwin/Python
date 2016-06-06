#!/usr/bin/python
# -*- coding: utf-8 -*- 
import wx
from time import ctime
import threading
import serial

serialport='/dev/ttyACM0'
baud=9600
arduino = serial.Serial(serialport,baud ) 

###########################################################################
## Class Frame1
###########################################################################

class Frame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 505,349 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer1 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer2 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_Enviar = wx.StaticText( self, wx.ID_ANY, u"Digite", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_Enviar.Wrap( -1 )
		fgSizer2.Add( self.txt_Enviar, 0, wx.ALL, 5 )
		
		self.txt_Escribir = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer2.Add( self.txt_Escribir, 0, wx.ALL, 5 )
		
		self.btn_Accion = wx.Button( self, wx.ID_ANY, u"Accion", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.btn_Accion, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer3.AddSpacer( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.textDisplay = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,250 ), 0|wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
		fgSizer3.Add( self.textDisplay, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_Accion.Bind( wx.EVT_BUTTON, self.Accion )
		

	def Print(self, text):
		wx.CallAfter(self.textDisplay.AppendText, text + "\n")

	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Accion( self, event ):		
		self.thread = threading.Thread(target=self.Escribir)
		self.thread.start()
	def Escribir(self):	
		self.data=str(self.txt_Escribir.GetValue())
		arduino.write(self.data) 
		if (self.data=='H'):
			self.Print("Valor Enviado: "+self.data+" --> Led Encendido")
		elif (self.data=='L'):	 
			self.Print("Valor Enviado: "+self.data+" --> Led Apagado")
		else:
			self.Print("Valor Enviado: "+self.data+" --> Nada Ocurre")
		self.txt_Escribir.SetValue("")	
	


class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)

        self.panel = wx.Panel(self)
        self.text = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)

        self.sizer = wx.BoxSizer()
        self.sizer.Add(self.text, 1, wx.ALL | wx.EXPAND, 5)

        self.panel.SetSizerAndFit(self.sizer)  
        self.Show()

        self.thread = threading.Thread(target=self.Server)
        self.thread.start()

    def Print(self, text):
        wx.CallAfter(self.text.AppendText, text + "\n")

    def Server(self):
        self.Print("Puerto: {}".format(port))

        tcpServer = socket(AF_INET , SOCK_STREAM)
        tcpServer.bind(addr)
        tcpServer.listen(5)
        try:
            while True:
                self.Print("Esperando la conexion...")
                tcpClient, caddr = tcpServer.accept()
                self.Print("Conectado a {}".format(caddr))

                while True:
                    data = tcpClient.recv(bufsiz)
                    if not data:
                        break
                    arduino.write(data)      
                    tcpClient.send('[%s]\nData\n%s' % (ctime(), data))
                    self.Print(data)
                tcpClient.close()

        except KeyboardInterrupt:
            tcpServer.close()

class App(wx.App):
    def OnInit(self):
	
        frame = Frame1(None)
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

if __name__ == "__main__":
    app = App(0)
    app.MainLoop()
