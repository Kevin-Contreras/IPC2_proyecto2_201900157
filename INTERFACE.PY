from tkinter import *
from tkinter import filedialog as dialogo
from ARCHIVO import *
from tkinter import messagebox
from OPERACIONES import * 
class Interface:
  ventana = Tk()
  frame2 = Text(ventana,width=30,height=350)
  frame3=Text(ventana,width=30,height=350)
  opera = operaciones()
  archivoXml = Archivo()
  mensaje=""
  mensajew=""
  ruta=""
  
  def rotacionHorizontal(self):
    self.opera.ImagenHorizontal(self.ruta,self.frame3,self.ventana,self.mensaje)
  def rotacionVertical(self):
    self.opera.ImagenVertical(self.ruta,self.frame3,self.ventana,self.mensaje)
  def transpuestaImagen(self):
    self.opera.Traspuesta(self.ruta,self.frame3,self.ventana,self.mensaje)
  def limpiar(self):
    self.opera.operacionLimpiar(self.ruta,self.frame3,self.ventana,self.mensaje,2,6,3,8)
  def agregarX(self):
    self.opera.AgregarEnX(self.ruta,self.frame3,self.ventana,self.mensaje,6,3,5)
  def agregarY(self):
    self.opera.AgregarEnY(self.ruta,self.frame3,self.ventana,self.mensaje,3,4,5)
  def rectangulo(self):
    self.opera.AgregarRectangulo(self.ruta,self.frame3,self.ventana,self.mensaje,2,6,3,3)
  def triangulo(self):
    self.opera.AgregarTriangulo(self.ruta,self.frame3,self.ventana,self.mensaje,2,2,4)
  def ventanaOperacinesUnaImagen(self):
    uy=0
    uy2=0
    uyw=0
    filas=0
    ti=0
    columna=0
    letraco=0
    docs = minidom.parse(self.ruta)
    imagen=docs.getElementsByTagName("nombre")
    imagen2=docs.getElementsByTagName("imagen")[int(self.mensajew.get(1.0,"end-1c"))-1]
    fila= docs.getElementsByTagName("filas")[int(self.mensajew.get(1.0,"end-1c"))-1].firstChild.nodeValue
    columnass= docs.getElementsByTagName("columnas")[int(self.mensajew.get(1.0,"end-1c"))-1].firstChild.nodeValue
   
    for nombre2 in imagen:
      uy2=uy2+1
      if(imagen[int(self.mensajew.get(1.0,"end-1c"))-1].firstChild.nodeValue==nombre2.firstChild.nodeValue):
        if(uy2<=int(self.mensajew.get(1.0,"end-1c"))):
          uy=uy+1
      
    for linea in imagen2.firstChild.nodeValue:
     if(linea!=" "):
          if(linea!="\n"):
            columna=columna+1
          else:
            ti=ti+1
            if(2==ti):
              letraco=columna
            columna=0
            filas=filas+1
    
    if(int(filas-1)*1==int(fila) and int(letraco)==int(columnass)):
     
      uy2=0        
      if(uy!=1):
        messagebox.showinfo(message="LA MATRIZ YA EXISTE NO SE PUEDE PROCESAR", title="MATRIZ")
      elif(uy==1):
        ventanaOperaciones2 = Tk()
        self.mensaje=self.mensajew.get(1.0,"end-1c")
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
    else:
         messagebox.showinfo(message="LAS DIMENSIONES NO SON CORRECTAS", title="MATRIZ")
    uy=0
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
    
  def elegir(self):
    ventanaElegir =Tk()
    i=0
    docs = minidom.parse(self.ruta)
    imagen=docs.getElementsByTagName("nombre")
    Label(ventanaElegir,text="SELECCIONE LA MATRIZ QUE QUIERE PROCESAR:").pack()
    for linea in imagen:
      i=i+1
      Label(ventanaElegir,text= str(i)+") "+linea.firstChild.nodeValue).pack()
   
    ventanaElegir.geometry("500x250")
    self.mensajew=Text(ventanaElegir,width=30,height=2)
    botonElegir = Button(ventanaElegir,text="ACEPTAR" ,command=self.ventanaOperacinesUnaImagen)
    botonElegir.place(x=150,y=200,width=220,height=40)
    self.mensajew.pack()
  def operaciones(self):
    ventanaOperaciones = Tk()
    ventanaOperaciones.geometry("250x300")
    boton1 = Button(ventanaOperaciones,text="OPERACIONES SOBRE UNA IMAGEN" ,command=self.elegir)
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

    
    
    
    
