import socket
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Apr 20 2016)
## http://www.wxformbuilder.org/
##
## Socket and Wxpython
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Cliente Socket Python", pos = wx.DefaultPosition, size = wx.Size( 681,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer0 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer0.SetFlexibleDirection( wx.BOTH )
		fgSizer0.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer1 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer1.AddSpacer( ( 100, 20), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.AddSpacer( ( 100, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Enviar mensajes  con Sockets a traves Python", wx.Point( 100,-1 ), wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		
		fgSizer0.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 1, 6, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer2.AddSpacer( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"IP Server", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.txt_Ip = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 150,-1 ), 0 )
		fgSizer2.Add( self.txt_Ip, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Puerto", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.txt_Puerto = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		fgSizer2.Add( self.txt_Puerto, 0, wx.ALL, 5 )
		self.btn_Conex = wx.Button( self, wx.ID_ANY, u"Conectar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.btn_Conex, 0, wx.ALL, 5 )
		
		fgSizer0.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 1, 4, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer3.AddSpacer( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Mensaje", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.txt_Mensaje = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 315,-1 ), 0 )
		fgSizer3.Add( self.txt_Mensaje, 0, wx.ALL, 5 )
		
		self.btn_Enviar = wx.Button( self, wx.ID_ANY, u"Enviar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.btn_Enviar, 0, wx.ALL, 5 )
		
		
		fgSizer0.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer0 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_Enviar.Bind( wx.EVT_BUTTON, self.Enviar )
		self.btn_Conex.Bind( wx.EVT_BUTTON, self.Conectar )
		self.port =8080

		self.txt_Puerto.SetValue(str(self.port))
		self.txt_Ip.SetValue('localhost')
	def __del__( self ):
		#pass
		self.client.shutdown(socket.SHUT_RDWR)
		self.client.close()	
	
	# Virtual event handlers, overide them in your derived class
	def Conectar( self, event ):
		self.ip=str(self.txt_Ip.GetValue())
		self.port =int(self.txt_Puerto.GetValue())
		self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.client.connect((self.ip, self.port))		
			
	def Enviar( self, event ):
		self.port =int(self.txt_Puerto.GetValue())
		self.ip=str(self.txt_Ip.GetValue())
		#self.client.close()	
		#self.client.connect((self.ip, self.port))
		#def sendSocketMessage(message):
		"""Send a message to a socket"""
		try:
			#port = random.randint(1025,36000)
			self.message=self.txt_Mensaje.GetValue()			
			if self.message=='salir':
				self.Close()
			else:
				self.client.send(self.message)
			
				self.txt_Mensaje.SetValue("")
		except Exception, msg:
			print msg	
#----------------------------------------------------------------------
# end of class MyFrame
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame1(None)
        self.SetTopWindow(frame)
        frame.Show()
        return 1

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
        
#if __name__ == "__main__":
    #sendSocketMessage("Python rocks!")
    
