from MATRIZ import * 
from tkinter import *
from xml.dom import minidom
from REPORTES import *
import os
from graphviz import Source
from datetime import datetime

class operaciones:
  matriz = Matriz()
  matriz2 = Matriz()
  matriz3=Matriz()
  matriz4=Matriz()
  matriz5=Matriz()
  matriz6=Matriz()
  matriz7=Matriz()
  matriz8=Matriz()
  reporte = Reportes()
  nombres=""
  vacio=""
  tabladoc = open("tabla.dot","w",encoding="utf-8")
  tabladoc2 = open("tabla2.dot","w",encoding="utf-8")
  tabladoc3 = open("tabla3.dot","w",encoding="utf-8")
  tabladoc4 = open("tabla4.dot","w",encoding="utf-8")
  tabladoc5 = open("tabla5.dot","w",encoding="utf-8")
  tabladoc6 = open("tabla6.dot","w",encoding="utf-8")
  tabladoc7 = open("tabla7.dot","w",encoding="utf-8")
  tabladoc8 = open("tabla8.dot","w",encoding="utf-8")
 
 
  contame =0
  contame2=0
  contame3=0
  contame4=0
  contame5=0
  contame6=0
  contame7=0
  contame8=0

  def ImagenHorizontal(self,archivoEntrada,ventana,idr):
    docs = minidom.parse(archivoEntrada)
    imagen=docs.getElementsByTagName("nombre")
    imagenll=docs.getElementsByTagName("nombre")
    now = datetime.now()
    d1 = now.strftime("%d/%m/%Y %H:%M:%S")
    self.nombres= self.nombres+d1+"-IMAGEN HORIZONTAL - MATRICES USADAS:"+imagen[int(idr)-1].firstChild.nodeValue+","
    print(self.nombres)
    self.contame=self.contame+1
    if(self.contame==1):
      m=""
      fila=0
      columna=0
      lleno=0
      nolleno=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      for linea in imagen[int(idr)-1].firstChild.nodeValue:
        if(linea!=" "):
          if(linea!="\n"):
            if(linea=="*"):
              lleno=lleno+1
            else:
              nolleno=nolleno+1
            columna=columna+1
            self.matriz.insertar(fila,columna,linea.replace("-"," "))
          else:
            columna=0
            fila=fila+1
      """OPERACION IMAGEN HORIZONATAL"""
      n=""
      self.tabladoc.write("""
        digraph test {
        graph [ratio=fill];
        node [ fontsize=15, shape=plaintext];
        graph [bb="0,0,352,154"];
        arset [label=<
        <TABLE ALIGN="LEFT">""")
      for i in range(int(docs.getElementsByTagName("filas")[int(idr)-1].firstChild.nodeValue)):
        self.tabladoc.write("""<TR>""")
        for u in range(int(docs.getElementsByTagName("columnas")[int(idr)-1].firstChild.nodeValue)):
            self.tabladoc.write("""<TD>"""+str(self.matriz.obtnernodo(int(docs.getElementsByTagName("filas")[int(idr)-1].firstChild.nodeValue)-i,u+1))+"""</TD>""")
        self.tabladoc.write("""</TR>""")
      self.tabladoc.write("""</TABLE>
        >, ];
              }
        """)
      self.tabladoc.close()
      os.system('dot -Tgif tabla.dot -o random1.gif')

      
          
                  
      for i in range(int(docs.getElementsByTagName("filas")[int(idr)-1].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[int(idr)-1].firstChild.nodeValue)):
         
          n=n+str(self.matriz.obtnernodo(int(docs.getElementsByTagName("filas")[int(idr)-1].firstChild.nodeValue)-i,u+1))+""
        m=m+n+"\n"
        print(n)
        n=""
      
      img = PhotoImage(file="random1.gif")
      Label(ventana, image=img).place(x=350,y=50)
      self.vacio=d1+" - "+imagenll[int(idr)-1].firstChild.nodeValue+" - ESPACIO LLENOS: " + str(lleno)+ "- ESPACIO VACIOS: "+str(nolleno)
      self.ejecutar()
      ventana.mainloop()
      
    else:
      img = PhotoImage(file="random1.gif")
      Label(ventana, image=img).place(x=350,y=50)
      
      os.system('dot -Tgif tabla.dot -o random1.gif')
      ventana.mainloop()
   
  def ImagenVertical(self,archivoEntrada,ventana,idr):
    docs = minidom.parse(archivoEntrada)
    imagen=docs.getElementsByTagName("nombre")
    now = datetime.now()
    d1 = now.strftime("%d/%m/%Y %H:%M:%S")
    self.nombres= self.nombres+d1+"-IMAGEN VERTICAL - MATRICES USADAS:"+imagen[int(idr)-1].firstChild.nodeValue+","
    self.contame2=self.contame2+1
    if(self.contame2==1):
      fila=0
      m=""
      columna=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      for linea in imagen[int(idr)-1].firstChild.nodeValue:
        if(linea!=" "):
          if(linea!="\n"):
            columna=columna+1
            self.matriz2.insertar(fila,columna,linea.replace("-"," "))
          else:
            columna=0
            fila=fila+1
      """OPERACION IMAGEN VERTICAL"""
      for i in range(int(docs.getElementsByTagName("filas")[int(idr)-1].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[int(idr)-1].firstChild.nodeValue)):
          n=n+str(self.matriz2.obtnernodo(i+1,int(docs.getElementsByTagName("columnas")[int(idr)-1].firstChild.nodeValue)-u))+""
        m=m+n+"\n"
        print(n)
        n=""
      self.tabladoc2.write("""
        digraph test {
        graph [ratio=fill];
        node [ fontsize=15, shape=plaintext];
        graph [bb="0,0,352,154"];
        arset [label=<
        <TABLE ALIGN="LEFT">""")
      for i in range(int(docs.getElementsByTagName("filas")[int(idr)-1].firstChild.nodeValue)):
        self.tabladoc2.write("""<TR>""")
        for u in range(int(docs.getElementsByTagName("columnas")[int(idr)-1].firstChild.nodeValue)):
            self.tabladoc2.write("""<TD>"""+str(self.matriz2.obtnernodo(i+1,int(docs.getElementsByTagName("columnas")[int(idr)-1].firstChild.nodeValue)-u))+"""</TD>""")
        self.tabladoc2.write("""</TR>""")
      self.tabladoc2.write("""</TABLE>
        >, ];
              }
        """)
      self.tabladoc2.close()
      os.system('dot -Tgif tabla2.dot -o random2.gif')
   
      img = PhotoImage(file="random2.gif")
      Label(ventana, image=img).place(x=350,y=50)
      self.ejecutar()
      ventana.mainloop()
    else:
      img = PhotoImage(file="random2.gif")
      Label(ventana, image=img).place(x=350,y=50)
      os.system('dot -Tgif tabla2.dot -o random2.gif')
      ventana.mainloop()
  def Traspuesta(self,archivoEntrada,ventana,idr):
    docs = minidom.parse(archivoEntrada)
    imagen=docs.getElementsByTagName("nombre")
    now = datetime.now()
    d1 = now.strftime("%d/%m/%Y %H:%M:%S")
    self.nombres= self.nombres+d1+"-TRASPUESTA - MATRICES USADAS:"+imagen[int(idr)-1].firstChild.nodeValue+","
    self.contame3=self.contame3+1
    if(self.contame3==1):
      fila=0
      columna=0
      m=""
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      for linea in imagen[int(idr)-1].firstChild.nodeValue:
        if(linea!=" "):
          if(linea!="\n"):
            columna=columna+1
            self.matriz3.insertar(fila,columna,linea.replace("-"," "))
          else:
            columna=0
            fila=fila+1
      """OPERACION IMAGEN TRASPUESTA"""
      for i in range(int(docs.getElementsByTagName("filas")[int(idr)-1].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[int(idr)-1].firstChild.nodeValue)):
          n=n+str(self.matriz3.obtnernodo(u+1,i+1))+""
        m=m+n+"\n"
        print(n)
        n=""
      self.tabladoc3.write("""
        digraph test {
        graph [ratio=fill];
        node [ fontsize=15, shape=plaintext];
        graph [bb="0,0,352,154"];
        arset [label=<
        <TABLE ALIGN="LEFT">""")
      for i in range(int(docs.getElementsByTagName("filas")[int(idr)-1].firstChild.nodeValue)):
        self.tabladoc3.write("""<TR>""")
        for u in range(int(docs.getElementsByTagName("columnas")[int(idr)-1].firstChild.nodeValue)):
            self.tabladoc3.write("""<TD>"""+str(self.matriz3.obtnernodo(u+1,i+1))+"""</TD>""")
        self.tabladoc3.write("""</TR>""")
      self.tabladoc3.write("""</TABLE>
        >, ];
              }
        """)
      self.tabladoc3.close()
      os.system('dot -Tgif tabla3.dot -o random3.gif')  
      
      img = PhotoImage(file="random3.gif")
      Label(ventana, image=img).place(x=350,y=50)
      self.ejecutar()
      ventana.mainloop()
    else:
      img = PhotoImage(file="random3.gif")
      Label(ventana, image=img).place(x=350,y=50)
      os.system('dot -Tgif tabla3.dot -o random3.gif')  
      ventana.mainloop()
  def operacionLimpiar(self,archivoEntrada,ventana,idr,y1,x1,y2,x2):
    docs = minidom.parse(archivoEntrada)
    imagen=docs.getElementsByTagName("nombre")
    now = datetime.now()
    d1 = now.strftime("%d/%m/%Y %H:%M:%S")
    self.nombres= self.nombres+d1+"-LIMPIAR AREA - MATRICES USADAS:"+imagen[int(idr)-1].firstChild.nodeValue+","
    self.contame4=self.contame4+1
    if(self.contame4==1):
      fila=0
      m=""
      columna=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      for linea in imagen[int(idr)-1].firstChild.nodeValue:
        if(linea!=" "):
          if(linea!="\n"):
          
            columna=columna+1
            self.matriz4.insertar(fila,columna,linea.replace("-"," "))
          else:
            columna=0
            m=""
            fila=fila+1
      """OPERACION IMAGEN TRASPUESTA"""
      for li in range(int(y2)):
        for colu in range(int(x2)):
          if(li+1>=y1):
            if(colu+1>=x1):
              self.matriz4.obtnernodos(li+1,colu+1," ")

      for i in range(int(docs.getElementsByTagName("filas")[int(idr)-1].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[int(idr)-1].firstChild.nodeValue)):
         
          n=n+str(self.matriz4.obtnernodo(i+1,u+1))+""
        m=m+n+"\n"
        print(n)
        n=""
      self.tabladoc4.write("""
        digraph test {
        graph [ratio=fill];
        node [ fontsize=15, shape=plaintext];
        graph [bb="0,0,352,154"];
        arset [label=<
        <TABLE ALIGN="LEFT">""")
      for i in range(int(docs.getElementsByTagName("filas")[int(idr)-1].firstChild.nodeValue)):
        self.tabladoc4.write("""<TR>""")
        for u in range(int(docs.getElementsByTagName("columnas")[int(idr)-1].firstChild.nodeValue)):
            self.tabladoc4.write("""<TD>"""+str(self.matriz4.obtnernodo(i+1,u+1))+"""</TD>""")
        self.tabladoc4.write("""</TR>""")
      self.tabladoc4.write("""</TABLE>
        >, ];
              }
        """)
      self.tabladoc4.close()
      os.system('dot -Tgif tabla4.dot -o random4.gif')
      
      img = PhotoImage(file="random4.gif")
      Label(ventana, image=img).place(x=350,y=50)
      self.ejecutar()
      ventana.mainloop()
    else:
      img = PhotoImage(file="random4.gif")
      Label(ventana, image=img).place(x=350,y=50)
      os.system('dot -Tgif tabla4.dot -o random4.gif')
      ventana.mainloop()
  def AgregarEnX(self,archivoEntrada,ventana,idr,y,x,cantidad):
    docs = minidom.parse(archivoEntrada)
    imagen=docs.getElementsByTagName("nombre")
    now = datetime.now()
    d1 = now.strftime("%d/%m/%Y %H:%M:%S")
    self.nombres= self.nombres+d1+"-AGREGAR EN X- MATRICES USADAS:"+imagen[int(idr)-1].firstChild.nodeValue+","
    self.contame5=self.contame5+1
    if(self.contame5==1):
      fila=0
      m=""
      columna=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      for linea in imagen[int(idr)-1].firstChild.nodeValue:
        if(linea!=" "):
          if(linea!="\n"):
          
            columna=columna+1
            self.matriz5.insertar(fila,columna,linea.replace("-"," "))
          else:
            columna=0
            
            fila=fila+1
      """OPERACION IMAGEN TRASPUESTA"""
      for ir in range(int(cantidad)):
        self.matriz5.obtnernodos(y,x+ir,"*")

      for i in range(int(docs.getElementsByTagName("filas")[int(idr)-1].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[int(idr)-1].firstChild.nodeValue)):
         
          n=n+str(self.matriz5.obtnernodo(i+1,u+1))+""
        m=m+n+"\n"
        print(n)
        n=""
      self.tabladoc5.write("""
        digraph test {
        graph [ratio=fill];
        node [ fontsize=15, shape=plaintext];
        graph [bb="0,0,352,154"];
        arset [label=<
        <TABLE ALIGN="LEFT">""")
      for i in range(int(docs.getElementsByTagName("filas")[int(idr)-1].firstChild.nodeValue)):
        self.tabladoc5.write("""<TR>""")
        for u in range(int(docs.getElementsByTagName("columnas")[int(idr)-1].firstChild.nodeValue)):
            self.tabladoc5.write("""<TD>"""+str(self.matriz5.obtnernodo(i+1,u+1))+"""</TD>""")
        self.tabladoc5.write("""</TR>""")
      self.tabladoc5.write("""</TABLE>
        >, ];
              }
        """)
      self.tabladoc5.close()
      os.system('dot -Tgif tabla5.dot -o random5.gif')
      img = PhotoImage(file="random5.gif")
      Label(ventana, image=img).place(x=350,y=50)
      self.ejecutar()
      ventana.mainloop()      
    else:
      img = PhotoImage(file="random5.gif")
      Label(ventana, image=img).place(x=350,y=50)
      os.system('dot -Tgif tabla5.dot -o random5.gif')
      ventana.mainloop()
  def AgregarEnY(self,archivoEntrada,ventana,idr,y,x,cantidad):
    docs = minidom.parse(archivoEntrada)
    imagen=docs.getElementsByTagName("nombre")
    now = datetime.now()
    d1 = now.strftime("%d/%m/%Y %H:%M:%S")
    self.nombres= self.nombres+d1+"-AGREGAR EN Y - MATRICES USADAS:"+imagen[int(idr)-1].firstChild.nodeValue+","
    self.contame6=self.contame6+1
    if(self.contame6==1):
      fila=0
      m=""
      columna=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      for linea in imagen[int(idr)-1].firstChild.nodeValue:
        if(linea!=" "):
          if(linea!="\n"):
          
            columna=columna+1
            self.matriz6.insertar(fila,columna,linea.replace("-"," "))
          else:
            columna=0
            fila=fila+1
      """OPERACION IMAGEN TRASPUESTA"""
      for ir in range(int(cantidad)):
        self.matriz6.obtnernodos(y+ir,x,"*")

      for i in range(int(docs.getElementsByTagName("filas")[int(idr)-1].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[int(idr)-1].firstChild.nodeValue)):
         
          n=n+str(self.matriz6.obtnernodo(i+1,u+1))+""
        m=m+n+"\n"
        print(n)
        n=""
      self.tabladoc6.write("""
        digraph test {
        graph [ratio=fill];
        node [ fontsize=15, shape=plaintext];
        graph [bb="0,0,352,154"];
        arset [label=<
        <TABLE ALIGN="LEFT">""")
      for i in range(int(docs.getElementsByTagName("filas")[int(idr)-1].firstChild.nodeValue)):
        self.tabladoc6.write("""<TR>""")
        for u in range(int(docs.getElementsByTagName("columnas")[int(idr)-1].firstChild.nodeValue)):
            self.tabladoc6.write("""<TD>"""+str(self.matriz6.obtnernodo(i+1,u+1))+"""</TD>""")
        self.tabladoc6.write("""</TR>""")
      self.tabladoc6.write("""</TABLE>
        >, ];
              }
        """)
      self.tabladoc6.close()
      os.system('dot -Tgif tabla6.dot -o random6.gif')
      img = PhotoImage(file="random6.gif")
      Label(ventana, image=img).place(x=350,y=50)
      self.ejecutar()
      ventana.mainloop()
    else:
      img = PhotoImage(file="random6.gif")
      Label(ventana, image=img).place(x=350,y=50)
      os.system('dot -Tgif tabla6.dot -o random6.gif')
      ventana.mainloop()
  def AgregarRectangulo(self,archivoEntrada,ventana,idr,y,x,cantidadY,cantidadX):
    docs = minidom.parse(archivoEntrada)
    imagen=docs.getElementsByTagName("nombre")
    now = datetime.now()
    d1 = now.strftime("%d/%m/%Y %H:%M:%S")
    self.nombres= self.nombres+d1+"-AGREGAR RECTANGULO- MATRICES USADAS:"+imagen[int(idr)-1].firstChild.nodeValue+","
    self.contame7=self.contame7+1
    if(self.contame7==1):
      fila=0
      m=""
      columna=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      for linea in imagen[int(idr)-1].firstChild.nodeValue:
        if(linea!=" "):
          if(linea!="\n"):
          
            columna=columna+1
            self.matriz7.insertar(fila,columna,linea.replace("-"," "))
          else:
            columna=0
            fila=fila+1
      """OPERACION IMAGEN AGREGAR EN Y"""
      for ir in range(int(cantidadY)):
        self.matriz7.obtnernodos(y+ir,x,"*")
      for ir in range(int(cantidadY)):
        self.matriz7.obtnernodos(int(y)+ir,int(x)+int(cantidadX)-1,"*")

      
        
    else:
      fila=0
      columna=0
      m=""
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      for ir in range(int(cantidadY)):
        self.matriz7.obtnernodos(y+ir,x,"*")
      for ir in range(int(cantidadY)):
        self.matriz7.obtnernodos(int(y)+ir,int(x)+int(cantidadX)-1,"*")
     
        
    """AGREGAR EN X"""
    if(self.contame7==1):
     
      """OPERACION IMAGEN TRASPUESTA"""
      for ir in range(int(cantidadX)):
        self.matriz7.obtnernodos(y,x+ir,"*")
      for ir in range(int(cantidadX)):
        self.matriz7.obtnernodos(y+cantidadY-1,x+ir,"*")  

      for i in range(int(docs.getElementsByTagName("filas")[int(idr)-1].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[int(idr)-1].firstChild.nodeValue)):
         
          n=n+str(self.matriz7.obtnernodo(i+1,u+1))+""
        m=m+n+"\n"
        n=""
      self.tabladoc7.write("""
        digraph test {
        graph [ratio=fill];
        node [ fontsize=15, shape=plaintext];
        graph [bb="0,0,352,154"];
        arset [label=<
        <TABLE ALIGN="LEFT">""")
      for i in range(int(docs.getElementsByTagName("filas")[int(idr)-1].firstChild.nodeValue)):
        self.tabladoc7.write("""<TR>""")
        for u in range(int(docs.getElementsByTagName("columnas")[int(idr)-1].firstChild.nodeValue)):
            self.tabladoc7.write("""<TD>"""+str(self.matriz7.obtnernodo(i+1,u+1))+"""</TD>""")
        self.tabladoc7.write("""</TR>""")
      self.tabladoc7.write("""</TABLE>
        >, ];
              }
        """)
      self.tabladoc7.close()
      os.system('dot -Tgif tabla7.dot -o random7.gif')
      img = PhotoImage(file="random7.gif")
      Label(ventana, image=img).place(x=350,y=50)
      self.ejecutar()
      ventana.mainloop()
    else:
      img = PhotoImage(file="random7.gif")
      Label(ventana, image=img).place(x=350,y=50)
      os.system('dot -Tgif tabla7.dot -o random6.gif')
      ventana.mainloop()
  def AgregarTriangulo(self,archivoEntrada,ventana,idr,y,x,cantidad):
    docs = minidom.parse(archivoEntrada)
    imagen=docs.getElementsByTagName("nombre")
    now = datetime.now()
    d1 = now.strftime("%d/%m/%Y %H:%M:%S")
    self.nombres= self.nombres+d1+"-AGREGAR TRIANGULO - MATRICES USADAS:"+imagen[int(idr)-1].firstChild.nodeValue+","
    kat=0
    self.contame8=self.contame8+1
    if(self.contame8==1):
      print("holaaaaaaaaaa")
      fila=0
      columna=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      m=""
      for linea in imagen[int(idr)-1].firstChild.nodeValue:
        if(linea!=" "):
          if(linea!="\n"):
           
            columna=columna+1
            self.matriz8.insertar(fila,columna,linea.replace("-"," "))
          else:
            columna=0
            fila=fila+1
      """OPERACION IMAGEN AGREGAR EN Y"""
      for ir in range(int(cantidad)):
        self.matriz8.obtnernodos(y+ir,x,"*")

    else:
      fila=0
      m=""
      columna=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      for ir in range(int(cantidad)):
        self.matriz8.obtnernodos(y+ir,x,"*")
     
     
        
    """AGREGAR EN X"""
    if(self.contame8==1):
     
      """OPERACION IMAGEN TRASPUESTA"""
      

      for ir in range(int(cantidad)):
        
        self.matriz8.obtnernodos(y+cantidad-1,x+ir,"*") 
        self.matriz8.obtnernodos(ir+y,ir+int(x),"*") 
        

      for i in range(int(docs.getElementsByTagName("filas")[int(idr)-1].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[int(idr)-1].firstChild.nodeValue)):
         
          n=n+str(self.matriz8.obtnernodo(i+1,u+1))+""
        m=m+n+"\n"
        print(n)
        n=""
      
      self.tabladoc8.write("""
        digraph test {
        graph [ratio=fill];
        node [ fontsize=15, shape=plaintext];
        graph [bb="0,0,352,154"];
        arset [label=<
        <TABLE ALIGN="LEFT">""")
      for i in range(int(docs.getElementsByTagName("filas")[int(idr)-1].firstChild.nodeValue)):
        self.tabladoc8.write("""<TR>""")
        for u in range(int(docs.getElementsByTagName("columnas")[int(idr)-1].firstChild.nodeValue)):
            self.tabladoc8.write("""<TD>"""+str(self.matriz8.obtnernodo(i+1,u+1))+"""</TD>""")
        self.tabladoc8.write("""</TR>""")
      self.tabladoc8.write("""</TABLE>
        >, ];
              }
        """)
      self.tabladoc8.close()
      os.system('dot -Tgif tabla8.dot -o random8.gif')
      img = PhotoImage(file="random8.gif")
      Label(ventana, image=img).place(x=350,y=50)
      self.ejecutar()
      ventana.mainloop()
      
    else:
      os.system('dot -Tgif tabla8.dot -o random8.gif')
      img = PhotoImage(file="random8.gif")
      Label(ventana, image=img).place(x=350,y=50)
      ventana.mainloop()
  def ejecutar(self):
    print(self.vacio)
    self.reporte.reporteUnaImagen(self.nombres,self.vacio)  
    

