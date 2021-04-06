from tkinter import *
from tkinter import filedialog as dialogo
from ARCHIVO import *
from tkinter import messagebox
from OPERACIONES import *
from DOSIMAGENES import * 
from MATRIZ import * 
from datetime import datetime
from REPORTES import *
import os
import webbrowser as wb
class Interface:
  ventana = Tk()
  frame2 = Text(ventana,width=30,height=350)
  frame3=Text(ventana,width=30,height=350)
  opera = operaciones()
  archivoXml = Archivo()
  reporte=Reportes()
  nombres1=""
  nombres=""
  label2=""
  operacionesDosImagenes= DosImagenesOperaciones()
  mensaje=""
  mensajew=""
  ruta=""
  matrizw=Matriz()
  matrizw1=Matriz()
  matrizw2=Matriz()
  mensaje2=""
  mensaje3=""
  mensaje2w=""
  mensaje3w=""
  """"BOTON LIMPIAR"""
  limpiar2=""
  limpiar3=""
  limpiar4=""
  limpiar5=""
  """AGREGAR X"""
  agregary1=""
  agregary2=""
  agregary3=""
  """AGREGAR Y"""
  agregarx1=""
  agregarx2=""
  agregarx3=""
  contador=0
  """AGREGAR RECTANGULO"""
  agregarR1=""
  agregarR2=""
  agregarR3=""
  agregarR4=""
  """AGREGAR RECTANGULO"""
  agregarT1=""
  agregarT2=""
  agregarT3=""
  contador=0
  def rotacionHorizontal(self):
    
    self.opera.ImagenHorizontal(self.ruta,self.ventana,self.mensaje)
  def rotacionVertical(self):
    self.opera.ImagenVertical(self.ruta,self.ventana,self.mensaje)
  def transpuestaImagen(self):
    self.opera.Traspuesta(self.ruta,self.ventana,self.mensaje)
  def limpiar1(self):
    self.opera.operacionLimpiar(self.ruta,self.ventana,self.mensaje,int(self.limpiar2.get(1.0,"end-1c")),int(self.limpiar3.get(1.0,"end-1c")),int(self.limpiar4.get(1.0,"end-1c")),int(self.limpiar5.get(1.0,"end-1c")))
  def limpiar(self):
    ventanaLimpiar = Tk()
    ventanaLimpiar.geometry("450x300")
    titulo=Label(ventanaLimpiar,text="LIMPIAR AREA")
    titulo.place(x=200,y=20)
    primeraFila=Label(ventanaLimpiar,text="PRIMERA FILA")
    primeraFila.place(x=200,y=60)
    self.limpiar2=Text(ventanaLimpiar)
    self.limpiar2.place(x=150,y=80,width=200, height=20)
    primeraColumna=Label(ventanaLimpiar,text="PRIMERA COLUMNA")
    primeraColumna.place(x=200,y=100)
    self.limpiar3=Text(ventanaLimpiar)
    self.limpiar3.place(x=150,y=120,width=200, height=20)
    ultimaFila=Label(ventanaLimpiar,text="ULTIMA FILA")
    ultimaFila.place(x=200,y=140)
    self.limpiar4=Text(ventanaLimpiar)
    self.limpiar4.place(x=150,y=160,width=200, height=20)
    ultimaColumna=Label(ventanaLimpiar,text="UTLIMA COLUMNA")
    ultimaColumna.place(x=200,y=180)
    self.limpiar5=Text(ventanaLimpiar)
    self.limpiar5.place(x=150,y=200,width=200, height=20)
    boton = Button(ventanaLimpiar,text="ACEPTAR",command=self.limpiar1)
    boton.place(x=150,y=230,width=200, height=20)
    

  def agregarXS(self):
    self.opera.AgregarEnX(self.ruta,self.ventana,self.mensaje,int(self.agregarx1.get(1.0,"end-1c")),int(self.agregarx2.get(1.0,"end-1c")),int(self.agregarx3.get(1.0,"end-1c")))
  def agregarX(self):
    ventanaX = Tk()
    ventanaX.geometry("450x300")
    titulo=Label(ventanaX,text="AGREGAR EM X")
    titulo.place(x=200,y=20)
    primeraFila=Label(ventanaX,text="FILA")
    primeraFila.place(x=200,y=60)
    self.agregarx1=Text(ventanaX)
    self.agregarx1.place(x=150,y=80,width=200, height=20)
    primeraColumna=Label(ventanaX,text="COLUMNA")
    primeraColumna.place(x=200,y=100)
    self.agregarx2=Text(ventanaX)
    self.agregarx2.place(x=150,y=120,width=200, height=20)
    ultimaFila=Label(ventanaX,text="CANTIDAD")
    ultimaFila.place(x=200,y=140)
    self.agregarx3=Text(ventanaX)
    self.agregarx3.place(x=150,y=160,width=200, height=20)
 
    boton = Button(ventanaX,text="ACEPTAR",command=self.agregarXS)
    boton.place(x=150,y=230,width=200, height=20)
  def agregarYS(self):
    self.opera.AgregarEnY(self.ruta,self.ventana,self.mensaje,int(self.agregary1.get(1.0,"end-1c")),int(self.agregary2.get(1.0,"end-1c")),int(self.agregary3.get(1.0,"end-1c")))  
  def agregarY(self):
    ventanaY = Tk()
    ventanaY.geometry("450x300")
    titulo=Label(ventanaY,text="AGREGAR EN Y")
    titulo.place(x=200,y=20)
    primeraFila=Label(ventanaY,text="FILA")
    primeraFila.place(x=200,y=60)
    self.agregary1=Text(ventanaY)
    self.agregary1.place(x=150,y=80,width=200, height=20)
    primeraColumna=Label(ventanaY,text="COLUMNA")
    primeraColumna.place(x=200,y=100)
    self.agregary2=Text(ventanaY)
    self.agregary2.place(x=150,y=120,width=200, height=20)
    ultimaFila=Label(ventanaY,text="CANTIDAD")
    ultimaFila.place(x=200,y=140)
    self.agregary3=Text(ventanaY)
    self.agregary3.place(x=150,y=160,width=200, height=20)
    boton = Button(ventanaY,text="ACEPTAR",command=self.agregarYS)
    boton.place(x=150,y=230,width=200, height=20)
  def r(self):
    self.opera.AgregarRectangulo(self.ruta,self.ventana,self.mensaje,int(self.agregarR1.get(1.0,"end-1c")),int(self.agregarR2.get(1.0,"end-1c")),int(self.agregarR3.get(1.0,"end-1c")),int(self.agregarR4.get(1.0,"end-1c")))
  def rectangulo(self):
    ventanaRectangulo = Tk()
    ventanaRectangulo.geometry("450x300")
    titulo=Label(ventanaRectangulo,text="AGREGAR RECTANGULO")
    titulo.place(x=200,y=20)
    primeraFila=Label(ventanaRectangulo,text="PRIMERA FILA")
    primeraFila.place(x=200,y=60)
    self.agregarR1=Text(ventanaRectangulo)
    self.agregarR1.place(x=150,y=80,width=200, height=20)
    primeraColumna=Label(ventanaRectangulo,text="PRIMERA COLUMNA")
    primeraColumna.place(x=200,y=100)
    self.agregarR2=Text(ventanaRectangulo)
    self.agregarR2.place(x=150,y=120,width=200, height=20)
    ultimaFila=Label(ventanaRectangulo,text=" CANTIDAD ANCHO")
    ultimaFila.place(x=200,y=140)
    self.agregarR3=Text(ventanaRectangulo)
    self.agregarR3.place(x=150,y=160,width=200, height=20)
    ultimaColumna=Label(ventanaRectangulo,text="CANTIDAD ALTO")
    ultimaColumna.place(x=200,y=180)
    self.agregarR4=Text(ventanaRectangulo)
    self.agregarR4.place(x=150,y=200,width=200, height=20)
    boton = Button(ventanaRectangulo,text="ACEPTAR",command=self.r)
    boton.place(x=150,y=230,width=200, height=20)
    
  def agregart(self):
    self.opera.AgregarTriangulo(self.ruta,self.ventana,self.mensaje,int(self.agregarT1.get(1.0,"end-1c")),int(self.agregarT2.get(1.0,"end-1c")),int(self.agregarT3.get(1.0,"end-1c")))
  def triangulo(self):
    ventanaTriangulo = Tk()
    ventanaTriangulo.geometry("450x300")
    titulo=Label(ventanaTriangulo,text="AGREGAR TRIENGULO")
    titulo.place(x=200,y=20)
    primeraFila=Label(ventanaTriangulo,text="FILA")
    primeraFila.place(x=200,y=60)
    self.agregarT1=Text(ventanaTriangulo)
    self.agregarT1.place(x=150,y=80,width=200, height=20)
    primeraColumna=Label(ventanaTriangulo,text="COLUMNA")
    primeraColumna.place(x=200,y=100)
    self.agregarT2=Text(ventanaTriangulo)
    self.agregarT2.place(x=150,y=120,width=200, height=20)
    ultimaFila=Label(ventanaTriangulo,text="LONGUITUD")
    ultimaFila.place(x=200,y=140)
    self.agregarT3=Text(ventanaTriangulo)
    self.agregarT3.place(x=150,y=160,width=200, height=20)
 
    boton = Button(ventanaTriangulo,text="ACEPTAR",command=self.agregart)
    boton.place(x=150,y=230,width=200, height=20)
    
  def ventanaOperacinesUnaImagen(self):
    uy=0
    uy2=0
    uyw=0
    filas=0
    ti=0
    filap=0
    columnap=0
    columna=0
    letraco=0
    tabladoc23 = open("tablaprimera.dot","w") 
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
        docs = minidom.parse(self.ruta)
        imagen=docs.getElementsByTagName("nombre")
        imagenll=docs.getElementsByTagName("nombre")
        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y %H:%M:%S")
        self.nombres= self.nombres+d1+"-YA EXISTE EL NOMBRE DE LA MATRIZ-"+"-IGUALADAD DE MATRICES-"+imagen[int(self.mensajew.get(1.0,"end-1c"))-1].firstChild.nodeValue+","
        self.ejecutar()
      elif(uy==1):
        for lineae in imagen2.firstChild.nodeValue:
          if(lineae!=" "):
            if(lineae!="\n"):
              columnap=columnap+1
              self.matrizw.insertar(filap,columnap,lineae.replace("-"," "))
            else:
              columnap=0
              filap=filap+1
        tabladoc23.write("""
        digraph test {
        graph [ratio=fill];
        node [ fontsize=15, shape=plaintext];
        graph [bb="0,0,352,154"];
        arset [label=<
        <TABLE ALIGN="LEFT">""")
        for i in range(int(fila)):
          tabladoc23.write("""<TR>""")
          for u in range(int(columnass)):
            print(str(self.matrizw.obtnernodo(i+1,u+1)))
            tabladoc23.write("""<TD>"""+str(self.matrizw.obtnernodo(i+1,u+1))+"""</TD>""")
          tabladoc23.write("""</TR>""")
        tabladoc23.write("""</TABLE>
          >, ];
              }
          """)
        tabladoc23.close()
        os.system('dot -Tgif tablaprimera.dot -o primera.gif')
        img = PhotoImage(file="primera.gif")
        Label(self.ventana, image=img).place(x=90,y=50)
        
        ventanaOperaciones2 = Tk()
        print(self.mensajew.get(1.0,"end-1c"))
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
        self.ventana.mainloop()
    else:
        messagebox.showinfo(message="LAS DIMENSIONES NO SON CORRECTAS", title="MATRIZ")
        docs = minidom.parse(self.ruta)
        imagen=docs.getElementsByTagName("nombre")
        imagenll=docs.getElementsByTagName("nombre")
        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y %H:%M:%S")
        self.nombres1= self.nombres1+d1+"-LAS DIMENSIONES DE LA MATRIZ NO COICIDEN -"+"-DIMENSIONES-"+imagen[int(self.mensajew.get(1.0,"end-1c"))-1].firstChild.nodeValue+","
        self.ejecutar()
    uy=0
  """OPERACIONES CON DOS IMAGENES"""
  def unionw(self):
    print(self.mensaje3)
    print(self.mensaje2)
    self.operacionesDosImagenes.union(self.ruta,self.ventana,self.mensaje2,self.mensaje3)
  
  def interseccion(self):
    self.operacionesDosImagenes.inteseccion(self.ruta,self.ventana,self.mensaje2,self.mensaje3)
  
  def diferencia(self):
    self.operacionesDosImagenes.diferencia(self.ruta,self.ventana,self.mensaje2,self.mensaje3)
    
  def diferenciaSimetrica(self):
    print(self.mensaje2)
    self.operacionesDosImagenes.diferenciaSimetrica(self.ruta,self.ventana,self.mensaje2,self.mensaje3)
    
  def dosImagenes(self):
    uy=0
    uy2=0
    uyw=0
    filas=0
    kevin=0
    kevin2=0
    ti=0
    columna=0
    letraco=0
    tabladoc33 = open("tablaprimera1.dot","w")
    tabladoc24 = open("tablaprimera2.dot","w")  
    docs = minidom.parse(self.ruta)
    imagen=docs.getElementsByTagName("nombre")
    imagen2=docs.getElementsByTagName("imagen")[int(self.mensajew2.get(1.0,"end-1c"))-1]
    fila= docs.getElementsByTagName("filas")[int(self.mensajew2.get(1.0,"end-1c"))-1].firstChild.nodeValue
    columnass= docs.getElementsByTagName("columnas")[int(self.mensajew2.get(1.0,"end-1c"))-1].firstChild.nodeValue
   
    for nombre2 in imagen:
      uy2=uy2+1
      if(imagen[int(self.mensajew2.get(1.0,"end-1c"))-1].firstChild.nodeValue==nombre2.firstChild.nodeValue):
        if(uy2<=int(self.mensajew2.get(1.0,"end-1c"))):
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
      kevin2=1
      uy2=0        
      if(uy!=1):
        messagebox.showinfo(message="LA MATRIZ YA EXISTE NO SE PUEDE PROCESAR22", title="MATRIZ")
        docs = minidom.parse(self.ruta)
        imagen=docs.getElementsByTagName("nombre")
        imagenll=docs.getElementsByTagName("nombre")
        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y %H:%M:%S")
        self.nombres= self.nombres+d1+"-YA EXISTE EL NOMBRE DE LA MATRIZ-"+"-IGUALADAD DE MATRICES-"+imagen[int(self.mensajew2.get(1.0,"end-1c"))-1].firstChild.nodeValue+","
        self.ejecutar()
      elif(uy==1):
        kevin=1
    else:
        messagebox.showinfo(message="LAS DIMENSIONES NO SON CORRECTAS22", title="MATRIZ")
        docs = minidom.parse(self.ruta)
        imagen=docs.getElementsByTagName("nombre")
        imagenll=docs.getElementsByTagName("nombre")
        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y %H:%M:%S")
        self.nombres= self.nombres+d1+"-LAS DIMENSIONES DE LA MATRIZ NO COICIDEN -"+"-DIMENSIONES-"+imagen[int(self.mensajew2.get(1.0,"end-1c"))-1].firstChild.nodeValue+","
        self.ejecutar()
         
    uy=0
    """----------------------------------------------------------------"""
    uy2=0
    uy22=0
    uyw2=0
    filas2=0
    kevin2w=0
    kevin22=0
    ti2=0
    columna2=0
    columnap=0
    filap=0
    columnaps=0
    filaps=0
    letraco2=0
    docs = minidom.parse(self.ruta)
    imagen23=docs.getElementsByTagName("nombre")
    imagen22=docs.getElementsByTagName("imagen")[int(self.mensajew3.get(1.0,"end-1c"))-1]
    fila2= docs.getElementsByTagName("filas")[int(self.mensajew3.get(1.0,"end-1c"))-1].firstChild.nodeValue
    columnass2= docs.getElementsByTagName("columnas")[int(self.mensajew3.get(1.0,"end-1c"))-1].firstChild.nodeValue
   
    for nombre2 in imagen23:
      uy22=uy22+1
      if(imagen23[int(self.mensajew3.get(1.0,"end-1c"))-1].firstChild.nodeValue==nombre2.firstChild.nodeValue):
        if(uy22<=int(self.mensajew3.get(1.0,"end-1c"))):
          uy2=uy2+1
      
    for linea2 in imagen22.firstChild.nodeValue:
     if(linea2!=" "):
          if(linea2!="\n"):
            columna2=columna2+1
          else:
            ti2=ti2+1
            if(2==ti2):
              letraco2=columna2
            columna2=0
            filas2=filas2+1
            
    if(int(filas2-1)*1==int(fila2) and int(letraco2)==int(columnass2)):
      kevin22=1
      uy22=0        
      if(uy2!=1):
        messagebox.showinfo(message="LA MATRIZ YA EXISTE NO SE PUEDE PROCESAR", title="MATRIZ")
        docs = minidom.parse(self.ruta)
        imagen=docs.getElementsByTagName("nombre")
        imagenll=docs.getElementsByTagName("nombre")
        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y %H:%M:%S")
        self.nombres1= self.nombres1+d1+"-YA EXISTE EL NOMBRE DE LA MATRIZ-"+"-IGUALADAD DE MATRICES-"+imagen[int(self.mensajew3.get(1.0,"end-1c"))-1].firstChild.nodeValue+","
        self.ejecutar()
      elif(uy2==1):
        kevin2w=1
    else:
        messagebox.showinfo(message="LAS DIMENSIONES NO SON CORRECTAS", title="MATRIZ")
        docs = minidom.parse(self.ruta)
        imagen=docs.getElementsByTagName("nombre")
        imagenll=docs.getElementsByTagName("nombre")
        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y %H:%M:%S")
        self.nombres1= self.nombres1+d1+"-LAS DIMENSIONES DE LA MATRIZ NO COICIDEN -"+"-DIMENSIONES-"+imagen[int(self.mensajew3.get(1.0,"end-1c"))-1].firstChild.nodeValue+","
        self.ejecutar()
    uy22=0
    if(kevin2==kevin22 and kevin==kevin2w):
      for lineae in imagen2.firstChild.nodeValue:
          if(lineae!=" "):
            if(lineae!="\n"):
              columnap=columnap+1
              self.matrizw1.insertar(filap,columnap,lineae.replace("-"," "))
            else:
              columnap=0
              filap=filap+1
      tabladoc33.write("""
        digraph test {
        graph [ratio=fill];
        node [ fontsize=15, shape=plaintext];
        graph [bb="0,0,352,154"];
        arset [label=<
        <TABLE ALIGN="LEFT">""")
      for i in range(int(fila)):
        tabladoc33.write("""<TR>""")
        for u in range(int(columnass)):
          tabladoc33.write("""<TD>"""+str(self.matrizw1.obtnernodo(i+1,u+1))+"""</TD>""")
        tabladoc33.write("""</TR>""")
      tabladoc33.write("""</TABLE>
          >, ];
              }
          """)
      tabladoc33.close()
      os.system('dot -Tgif tablaprimera1.dot -o primera2.gif')
      img2 = PhotoImage(file="primera2.gif")
      Label(self.ventana, image=img2).place(x=90,y=50)

      """---------------------------------------------"""
      for lineao in imagen22.firstChild.nodeValue:
        if(lineao!=" "):
          if(lineao!="\n"):
            
            columnaps=columnaps+1
            self.matrizw2.insertar(filaps,columnaps,lineao.replace("-"," "))
          else:
            columnaps=0
            filaps=filaps+1
      tabladoc24.write("""
        digraph test {
        graph [ratio=fill];
        node [ fontsize=15, shape=plaintext];
        graph [bb="0,0,352,154"];
        arset [label=<
        <TABLE ALIGN="LEFT">""")
      for i in range(int(fila2)):
        tabladoc24.write("""<TR>""")
        for u in range(int(columnass2)):
          tabladoc24.write("""<TD>"""+str(self.matrizw2.obtnernodo(i+1,u+1))+"""</TD>""")
        tabladoc24.write("""</TR>""")
      tabladoc24.write("""</TABLE>
          >, ];
              }
          """)
      tabladoc24.close()
      os.system('dot -Tgif tablaprimera2.dot -o primera3.gif')
      img = PhotoImage(file="primera3.gif")
      Label(self.ventana, image=img).place(x=90,y=420)
      self.label2.place(x=110,y=830)
      self.ventana.geometry("650x900")
      self.mensaje3=self.mensajew3.get(1.0,"end-1c")
      self.mensaje2=self.mensajew2.get(1.0,"end-1c")
      ventanaOperaciones3 = Tk()
      ventanaOperaciones3.geometry("880x160")
      boton1 = Button(ventanaOperaciones3,text="UNION A,B",command=self.unionw)
      boton1.place(x=20,y=20 ,width=200, height=40)
      boton2 = Button(ventanaOperaciones3,text="INTERSECCION A,B" ,command=self.interseccion)
      boton2.place(x=230,y=20,width=200, height=40)
      boton3 = Button(ventanaOperaciones3,text="DIFERENCIA A,B" ,command=self.diferencia)
      boton3.place(x=440,y=20,width=200, height=40)
      boton4 = Button(ventanaOperaciones3,text="DIFERENCIA SIMETRICA A,B" ,command=self.diferenciaSimetrica)
      boton4.place(x=660,y=20,width=200, height=40)
      self.ventana.mainloop()
    else:
      messagebox.showinfo(message="UNA DE LAS DOS MATRICES NO ESTA CORRECTA", title="MATRIZ")
      self.ejecutar()
  def ejecutar(self):
    self.reporte.errores(self.nombres,self.nombres1)
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
  def elegirDosImagenes(self):
    ventanaElegir2 =Tk()
    i=0
    docs = minidom.parse(self.ruta)
    imagen=docs.getElementsByTagName("nombre")
    Label(ventanaElegir2,text="SELECCIONE LA MATRIZ QUE QUIERE PROCESAR:").pack()
    for linea in imagen:
      i=i+1
      Label(ventanaElegir2,text= str(i)+") "+linea.firstChild.nodeValue).pack()
   
    ventanaElegir2.geometry("500x250")
    Label(ventanaElegir2,text="ELIJA PRIMERA IMAGEN:").pack()
    self.mensajew2=Text(ventanaElegir2,width=30,height=2)
    Label(ventanaElegir2,text="ELIJA SEGUNDA IMAGEN:").pack()
    self.mensajew3=Text(ventanaElegir2,width=30,height=2)
    botonElegir = Button(ventanaElegir2,text="ACEPTAR" ,command=self.dosImagenes)
    botonElegir.place(x=150,y=200,width=220,height=40)
    self.mensajew2.pack()
    self.mensajew3.pack()
  def operaciones(self):
    ventanaOperaciones = Tk()
    ventanaOperaciones.geometry("250x300")
    boton1 = Button(ventanaOperaciones,text="OPERACIONES SOBRE UNA IMAGEN" ,command=self.elegir)
    boton1.place(x=20,y=110 ,width=200, height=40)
    boton1 = Button(ventanaOperaciones,text="OPERACIONES SOBRE DOS IMAGENES",command= self.elegirDosImagenes)
    boton1.place(x=20 ,y=170 ,width=220, height=40)
  def funcionBoton3(self):
    self.reporte.desplegar()
  def yo(self):
    ayuda2 = Tk()
    ayuda2.geometry("250x50")
    Label(ayuda2,text="CARNET:201900157").pack()
    Label(ayuda2,text="NOMBRE:KEVIN ALEXIS LOPEZ CONTRERAS").pack()
  def documentacion(self):
    wb.open_new("DOCUMENTACION\DOCUMENTACION.pdf")
  def funcionBoton4(self):
    ayuda = Tk()
    ayuda.geometry("250x300")
    boton1 = Button(ayuda,text="DOCUMENTACION" ,command=self.documentacion)
    boton1.place(x=20,y=110 ,width=200, height=40)
    boton1 = Button(ayuda,text="DATOS DEL DEL ESTUDIANTE",command= self.yo)
    boton1.place(x=20 ,y=170 ,width=220, height=40)

  def ventanaEmergente(self):
    miFrame = Frame()
    self.ventana.title("PROYECTO 2")
    
    self.ventana.geometry("650x500")
    self.ventana.resizable(True,True)
    miFrame.pack(fill="both", expand="true")
    miFrame.config(width="300px",height="40px")
    label1 = Label(self.ventana,text="IMAGEN RESULTANTE")
    self.label2 = Label(self.ventana,text="IMAGEN ORIGINAL")
    label1.place(x=400,y=450)
    self.label2.place(x=100,y=450)

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

    
    
    
    
