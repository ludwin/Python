#!/usr/bin/python
# -*- coding: utf-8 -*- 
import wx
from time import ctime
import threading
import serial

#define puerto serial y velocidad de transmision en baudios
serialport='/dev/ttyACM0'
baud=9600
#Establecer conexion al arduino
arduino = serial.Serial(serialport,baud ) 

###########################################################################
## Class Frame1
###########################################################################

class Frame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 490,370 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer1 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer2 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_Enviar = wx.StaticText( self, wx.ID_ANY, u"Numero de Lecturas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_Enviar.Wrap( -1 )
		fgSizer2.Add( self.txt_Enviar, 0, wx.ALL, 5 )
		
		self.txt_Escribir = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer2.Add( self.txt_Escribir, 0, wx.ALL, 5 )
		
		self.btn_Accion = wx.Button( self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.btn_Accion, 0, wx.ALL, 5 )
		
		fgSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		
		fgSizer3 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer3.AddSpacer( ( 15, 0), 1, wx.EXPAND, 5 )
		
		self.textDisplay = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,250 ), 0|wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
		fgSizer3.Add( self.textDisplay, 0, wx.ALL, 5 )
		
		self.lbl_Ejecuciones = wx.StaticText( self, wx.ID_ANY, u"Ejecutado:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_Ejecuciones.Wrap( -1 )
		#fgSizer3.AddSpacer( ( 15, 0), 1, wx.EXPAND, 5 )
		fgSizer3.Add( self.lbl_Ejecuciones, 0, wx.ALL, 5 )
		
		self.txt_Ejecuciones = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,  wx.Size( 250,30 ), wx.TE_READONLY )
		fgSizer3.Add( self.txt_Ejecuciones, 0, wx.ALL, 5 )
		
		fgSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )
		

		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_Accion.Bind( wx.EVT_BUTTON, self.Accion )
		
		
	def Print(self, text):
		ejecuciones="ejecuciones: "+text
		wx.CallAfter(self.textDisplay.AppendText, text + "\n")
		
	def __del__( self ):
		arduino.close()
		self.Close(True)

	# Virtual event handlers, overide them in your derived class
	def Accion( self, event ):		
		self.thread = threading.Thread(target=self.Leer)
		self.thread.start()
		self.textDisplay.SetValue("")
	def Leer(self):	
		self.nlecturas=str(self.txt_Escribir.GetValue())
		n=0
		if int(self.nlecturas)>200:
			self.nlecturas=200
		
		for i in range(int(self.nlecturas)):
			n+=1
			self.data=arduino.readline().rstrip('\n')			
			self.Print("Valor Obtenido Arduino: "+self.data)
			self.txt_Ejecuciones.SetValue(str(n))
		self.txt_Escribir.SetValue("")
		self.txt_Ejecuciones.SetValue("Finalizado: "+str(n)+" lecturas")	
		
	
class App(wx.App):
    def OnInit(self):
	
        frame = Frame1(None)
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

if __name__ == "__main__":
    app = App(0)
    app.MainLoop()
