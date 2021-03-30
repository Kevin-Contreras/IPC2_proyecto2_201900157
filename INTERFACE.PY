from tkinter import *
from tkinter import filedialog as dialogo
from ARCHIVO import *
from OPERACIONES import * 
class Interface:
  ventana = Tk()
  frame2 = Text(ventana,width=30,height=350)
  frame3=Text(ventana,width=30,height=350)
  opera = operaciones()
  archivoXml = Archivo()
  ruta=""
  
  def rotacionHorizontal(self):
    self.opera.ImagenHorizontal(self.ruta,self.frame3,self.ventana)
  def rotacionVertical(self):
    self.opera.ImagenVertical(self.ruta,self.frame3,self.ventana)
  def transpuestaImagen(self):
    self.opera.Traspuesta(self.ruta,self.frame3,self.ventana)
  def limpiar(self):
    self.opera.operacionLimpiar(self.ruta,self.frame3,self.ventana,2,6,3,8)
  def agregarX(self):
    self.opera.AgregarEnX(self.ruta,self.frame3,self.ventana,6,3,5)
  def agregarY(self):
    self.opera.AgregarEnY(self.ruta,self.frame3,self.ventana,3,4,5)
  def rectangulo(self):
    self.opera.AgregarRectangulo(self.ruta,self.frame3,self.ventana,2,6,3,3)
  def triangulo(self):
    self.opera.AgregarTriangulo(self.ruta,self.frame3,self.ventana,2,6,4)
  def ventanaOperacinesUnaImagen(self):
    ventanaOperaciones2 = Tk()
    ventanaOperaciones2.geometry("880x160")
    boton1 = Button(ventanaOperaciones2,text="ROTACION HORIZONTAL",command=self.rotacionHorizontal )
    boton1.place(x=20,y=20 ,width=200, height=40)
    boton2 = Button(ventanaOperaciones2,text="ROTACION VERTICAL", command=self.rotacionVertical )
    boton2.place(x=230,y=20,width=200, height=40)
    boton3 = Button(ventanaOperaciones2,text="TRASPUESTA DE UNA IMAGEN" ,command=self.transpuestaImagen)
    boton3.place(x=440,y=20,width=200, height=40)
    boton4 = Button(ventanaOperaciones2,text="LIMPIAR ZONA DE UNA IMAGEN", command = self.limpiar)
    boton4.place(x=660,y=20,width=200, height=40)
    boton5 = Button(ventanaOperaciones2,text="AGREGAR LINEAS HORIZONTALES" ,command= self.agregarX )
    boton5.place(x=20 ,y=80,width=200, height=40)
    boton6 = Button(ventanaOperaciones2,text="AGREGAR LINEAS VERTICALES",command= self.agregarY)
    boton6.place(x=230,y=80,width=200, height=40)
    boton7 = Button(ventanaOperaciones2,text="AGREGAR RECTANGULO",command=self.rectangulo )
    boton7.place(x=440 ,y=80,width=200, height=40)
    boton8 = Button(ventanaOperaciones2,text="AGREGAR TRIANGULO RECTANGULO",command=self.triangulo )
    boton8.place(x=660,y=80,width=200, height=40)
  def dosImagenes(self):
    ventanaOperaciones3 = Tk()
    ventanaOperaciones3.geometry("880x160")
    boton1 = Button(ventanaOperaciones3,text="UNION A,B" )
    boton1.place(x=20,y=20 ,width=200, height=40)
    boton2 = Button(ventanaOperaciones3,text="INTERSECCION A,B" )
    boton2.place(x=230,y=20,width=200, height=40)
    boton3 = Button(ventanaOperaciones3,text="DIFERENCIA A,B" )
    boton3.place(x=440,y=20,width=200, height=40)
    boton4 = Button(ventanaOperaciones3,text="DIFERENCIA SIMETRICA A,B" )
    boton4.place(x=660,y=20,width=200, height=40)
   
  def funcionBoton1(self):
    self.ruta = dialogo.askopenfilename(title="ARCHIVO")
    
    
  def operaciones(self):
    ventanaOperaciones = Tk()
    ventanaOperaciones.geometry("250x300")
    boton1 = Button(ventanaOperaciones,text="OPERACIONES SOBRE UNA IMAGEN" ,command=self.ventanaOperacinesUnaImagen)
    boton1.place(x=20,y=110 ,width=200, height=40)
    boton1 = Button(ventanaOperaciones,text="OPERACIONES SOBRE DOS IMAGENES",command= self.dosImagenes)
    boton1.place(x=20 ,y=170 ,width=220, height=40)
   
    
  def funcionBoton3(self):
    dialogo.askopenfilename(title="ARCHIVO")
  def funcionBoton4(self):
    dialogo.askopenfilename(title="ARCHIVO")
  def ventanaEmergente(self):
    miFrame = Frame()
    self.ventana.title("PROYECTO 2")
    self.ventana.geometry("650x350")
    self.ventana.resizable(True,True)
    miFrame.pack(fill="both", expand="true")
    miFrame.config(width="300px",height="40px")
    self.frame2.pack(side='left',padx=20,pady=20)
    self.frame3.pack(side='right',padx=20,pady=20)
   
  
    boton1 = Button(miFrame,text="CARGAR ARCHIVO" ,command=self.funcionBoton1)
    boton1.place(x=20 ,width=150, height=40)
    boton2 = Button(miFrame,text="OPERACIONES" ,command=self.operaciones)
    boton2.place(x=170,width=150, height=40)
    boton3 = Button(miFrame,text="REPORTES" ,command=self.funcionBoton3)
    boton3.place(x=320,width=150, height=40)
    boton4 = Button(miFrame,text="AYUDA" ,command=self.funcionBoton4)
    boton4.place(x=470 ,width=150, height=40)
    
    
  
    
    self.ventana.mainloop()
  
Interface().ventanaEmergente()

    
    
    
    
