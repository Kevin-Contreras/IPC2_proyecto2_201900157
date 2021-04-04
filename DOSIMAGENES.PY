from MATRIZ import * 
from xml.dom import minidom
from tkinter import *
import os
from datetime import datetime
from REPORTES import *
class DosImagenesOperaciones:
  matriz = Matriz()
  matriz2 = Matriz()
  matriz3 = Matriz()
  matriz4= Matriz()
  matriz5 = Matriz()
  matriz6 = Matriz()
  matriz7=Matriz()
  matriz8 = Matriz()
  matriz9 = Matriz()
  matriz10 = Matriz()
  matriz11 = Matriz()
  reporte = Reportes()
  nombres=""
  vacio=""
  vacio2=""
  contame =0
  contame2 =0
  contame3 =0
  contame4 =0
  tabladoc5 = open("tabla5.dot","w",encoding="utf-8")
  tabladoc6 = open("tabla6.dot","w",encoding="utf-8")
  tabladoc7 = open("tabla7.dot","w",encoding="utf-8")
  tabladoc8 = open("tabla8.dot","w",encoding="utf-8")
  def union(self,archivoEntrada,ventana,matriz1,matriz2):
    self.contame=self.contame+1
    docs = minidom.parse(archivoEntrada)
    imagen=docs.getElementsByTagName("nombre")
    imagenll=docs.getElementsByTagName("nombre")
    now = datetime.now()
    d1 = now.strftime("%d/%m/%Y %H:%M:%S")
    self.nombres= self.nombres+d1+"-UNION - MATRICES USADAS:("+imagen[int(matriz1)-1].firstChild.nodeValue+","+imagen[int(matriz2)-1].firstChild.nodeValue+")"+"*"
    if(self.contame==1):
      m=""
      fila=0
      fila2=0
      n=""
      columna=0
      nolleno=0
      lleno=0
      nolleno2=0
      lleno2=0
      columna2=0
      variableFilas=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      filasArchivo=docs.getElementsByTagName("filas")
      columnasArchivo=docs.getElementsByTagName("columnas")
      variableColumna=0
      if(int(filasArchivo[int(matriz1)-1].firstChild.nodeValue)>int(filasArchivo[int(matriz2)-1].firstChild.nodeValue)):
        variableFilas=int(filasArchivo[int(matriz1)-1].firstChild.nodeValue)
        print(variableFilas)
      else:
        
        variableFilas=int(filasArchivo[int(matriz2)-1].firstChild.nodeValue)
        print(variableFilas)
      if(int(columnasArchivo[int(matriz1)-1].firstChild.nodeValue)>int(columnasArchivo[int(matriz2)-1].firstChild.nodeValue)):
        variableColumna=int(columnasArchivo[int(matriz1)-1].firstChild.nodeValue)
        print(variableColumna)
      else:
        variableColumna=int(columnasArchivo[int(matriz2)-1].firstChild.nodeValue)
        print(variableColumna)
      """MATRIZ 1"""
      for lineas in imagen[int(matriz1)-1].firstChild.nodeValue:
        if(lineas!=" "):
          if(lineas!="\n"):
            if(lineas=="*"):
              lleno=lleno+1
            else:
              nolleno=nolleno+1
            columna=columna+1
            self.matriz.insertar(fila,columna,lineas.replace("-"," "))
          else:
            columna=0
            fila=fila+1
      """MATRIZ 2"""
      for linea in imagen[int(matriz2)-1].firstChild.nodeValue:
        if(linea!=" "):
          if(linea!="\n"):
            if(linea=="*"):
              lleno2=lleno2+1
            else:
              nolleno2=nolleno2+1
            columna2=columna2+1
            if(int(filasArchivo[int(matriz1)-1].firstChild.nodeValue)<fila2 or int(columnasArchivo[int(matriz1)-1].firstChild.nodeValue)<columna2 ):
              self.matriz.insertar(fila2,columna2,linea.replace("-"," "))
              print(self.matriz.obtnernodo(fila2,columna2))
            else:
              if(str(linea)=="*"):
                self.matriz.obtnernodos(fila2,columna2,"*")
           
          else:
            columna2=0
            fila2=fila2+1

      for filass in range(variableFilas):
        for columnass in range(variableColumna):
           self.matriz4.insertar(filass+1,columnass+1,self.matriz.obtnernodo(filass+1,columnass+1))
      self.tabladoc5.write("""
        digraph test {
        graph [ratio=fill];
        node [ fontsize=15, shape=plaintext];
        graph [bb="0,0,352,154"];
        arset [label=<
        <TABLE ALIGN="LEFT">""")
      for i in range(variableFilas):
        self.tabladoc5.write("""<TR>""")
        for u in range(variableColumna):
            self.tabladoc5.write("""<TD>"""+str(self.matriz4.obtnernodo(i+1,u+1))+"""</TD>""")
        self.tabladoc5.write("""</TR>""")
      self.tabladoc5.write("""</TABLE>
        >, ];
              }
        """)
      self.tabladoc5.close()
      os.system('dot -Tgif tabla5.dot -o random1.gif')
      img = PhotoImage(file="random1.gif")
      Label(ventana, image=img).place(x=350,y=50)
      self.vacio=d1+" - "+imagenll[int(matriz1)-1].firstChild.nodeValue+" - ESPACIO LLENOS: " + str(lleno)+ "- ESPACIO VACIOS: "+str(nolleno)
      self.vacio2=d1+" - "+imagenll[int(matriz2)-1].firstChild.nodeValue+" - ESPACIO LLENOS: " + str(lleno2)+ "- ESPACIO VACIOS: "+str(nolleno2)
      self.ejecutar()
      ventana.mainloop()      
    else:
      img = PhotoImage(file="random1.gif")
      Label(ventana, image=img).place(x=350,y=50)
      
      
      ventana.mainloop()
      os.system('dot -Tgif tabla5.dot -o random.gif') 
  def inteseccion(self,archivoEntrada,ventana,matriz1,matriz2):
    self.contame2=self.contame2+1
    docs = minidom.parse(archivoEntrada)
    imagen=docs.getElementsByTagName("nombre")
    imagenll=docs.getElementsByTagName("nombre")
    now = datetime.now()
    d1 = now.strftime("%d/%m/%Y %H:%M:%S")
    self.nombres= self.nombres+d1+"-INTERSECCION - MATRICES USADAS:("+imagen[int(matriz1)-1].firstChild.nodeValue+","+imagen[int(matriz2)-1].firstChild.nodeValue+")"+"*"
    if(self.contame2==1):
      m=""
      fila=0
      fila2=0
      n=""
      columna=0
      
      columna2=0
      variableFilas=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      filasArchivo=docs.getElementsByTagName("filas")
      columnasArchivo=docs.getElementsByTagName("columnas")
      variableColumna=0
      if(int(filasArchivo[int(matriz1)-1].firstChild.nodeValue)<int(filasArchivo[int(matriz2)-1].firstChild.nodeValue)):
        variableFilas=int(filasArchivo[int(matriz1)-1].firstChild.nodeValue)
        print(variableFilas)
      else:
        
        variableFilas=int(filasArchivo[int(matriz2)-1].firstChild.nodeValue)
        print(variableFilas)
      if(int(columnasArchivo[int(matriz1)-1].firstChild.nodeValue)<int(columnasArchivo[int(matriz2)-1].firstChild.nodeValue)):
        variableColumna=int(columnasArchivo[int(matriz1)-1].firstChild.nodeValue)
        print(variableColumna)
      else:
        variableColumna=int(columnasArchivo[int(matriz2)-1].firstChild.nodeValue)
        print(variableColumna)
      """MATRIZ 1"""
      for lineas in imagen[int(matriz1)-1].firstChild.nodeValue:
        if(lineas!=" "):
          if(lineas!="\n"):
            
            columna=columna+1
            self.matriz2.insertar(fila,columna,lineas.replace("-"," "))
          else:
            columna=0
            fila=fila+1
      """MATRIZ 2"""
      for linea in imagen[int(matriz2)-1].firstChild.nodeValue:
        if(linea!=" "):
          if(linea!="\n"):
            
            columna2=columna2+1
            self.matriz3.insertar(fila2,columna2,linea.replace("-"," "))
           
          else:
            columna2=0
            fila2=fila2+1
      print(variableFilas)
      print(variableColumna)
      for filass in range(variableFilas):
        for columnass in range(variableColumna):
          if(str(self.matriz3.obtnernodo(filass+1,columnass+1)) and str(self.matriz2.obtnernodo(filass+1,columnass+1)) =="*" ):
            
            self.matriz7.insertar(filass+1,columnass+1, self.matriz3.obtnernodo(filass+1,columnass+1))
          else:
             self.matriz7.insertar(filass+1,columnass+1, self.matriz2.obtnernodo(filass+1,columnass+1))
      self.tabladoc6.write("""
        digraph test {
        graph [ratio=fill];
        node [ fontsize=15, shape=plaintext];
        graph [bb="0,0,352,154"];
        arset [label=<
        <TABLE ALIGN="LEFT">""")
      for i in range(variableFilas):
        self.tabladoc6.write("""<TR>""")
        for u in range(variableColumna):
            self.tabladoc6.write("""<TD>"""+str(self.matriz7.obtnernodo(i+1,u+1))+"""</TD>""")
        self.tabladoc6.write("""</TR>""")
      self.tabladoc6.write("""</TABLE>
        >, ];
              }
        """)
      self.tabladoc6.close()
      os.system('dot -Tgif tabla6.dot -o random2.gif')
      img = PhotoImage(file="random2.gif")
      Label(ventana, image=img).place(x=350,y=50)
      
      self.ejecutar()
      ventana.mainloop()      
    else:
      os.system('dot -Tgif tabla6.dot -o random2.gif')
      img = PhotoImage(file="random2.gif")
      Label(ventana, image=img).place(x=350,y=50)
      ventana.mainloop()    
  def diferencia(self,archivoEntrada,ventana,matriz1,matriz2):
    self.contame3=self.contame3+1
    docs = minidom.parse(archivoEntrada)
    imagen=docs.getElementsByTagName("nombre")
    imagenll=docs.getElementsByTagName("nombre")
    now = datetime.now()
    d1 = now.strftime("%d/%m/%Y %H:%M:%S")
    self.nombres= self.nombres+d1+"- DIFERENCIA - MATRICES USADAS:("+imagen[int(matriz1)-1].firstChild.nodeValue+","+imagen[int(matriz2)-1].firstChild.nodeValue+")"+"*"
    if(self.contame3==1):
      m=""
      fila=0
      fila2=0
      n=""
      columna=0
      columna2=0
      variableFilas=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      filasArchivo=docs.getElementsByTagName("filas")
      columnasArchivo=docs.getElementsByTagName("columnas")
      variableColumna=0
      if(int(filasArchivo[int(matriz1)-1].firstChild.nodeValue)<int(filasArchivo[int(matriz2)-1].firstChild.nodeValue)):
        variableFilas=int(filasArchivo[int(matriz1)-1].firstChild.nodeValue)
        print(variableFilas)
      else:
        
        variableFilas=int(filasArchivo[int(matriz2)-1].firstChild.nodeValue)
        print(variableFilas)
      if(int(columnasArchivo[int(matriz1)-1].firstChild.nodeValue)<int(columnasArchivo[int(matriz2)-1].firstChild.nodeValue)):
        variableColumna=int(columnasArchivo[int(matriz1)-1].firstChild.nodeValue)
        print(variableColumna)
      else:
        variableColumna=int(columnasArchivo[int(matriz2)-1].firstChild.nodeValue)
        print(variableColumna)
      """MATRIZ 1"""
      for lineas in imagen[int(matriz1)-1].firstChild.nodeValue:
        if(lineas!=" "):
          if(lineas!="\n"):
            columna=columna+1
            self.matriz5.insertar(fila,columna,lineas.replace("-"," "))
          else:
            columna=0
            fila=fila+1
      """MATRIZ 2"""
      for linea in imagen[int(matriz2)-1].firstChild.nodeValue:
        if(linea!=" "):
          if(linea!="\n"):
            columna2=columna2+1
            self.matriz6.insertar(fila2,columna2,linea.replace("-"," "))
           
          else:
            columna2=0
            fila2=fila2+1
      print(variableFilas)
      print(variableColumna)
      for filass in range(variableFilas):
        for columnass in range(variableColumna):
          if(str(self.matriz5.obtnernodo(filass+1,columnass+1)) != str(self.matriz6.obtnernodo(filass+1,columnass+1)) ):
            
            self.matriz10.insertar(filass+1,columnass+1, self.matriz5.obtnernodo(filass+1,columnass+1))
          else:
             self.matriz10.insertar(filass+1,columnass+1, " ")
      self.tabladoc7.write("""
        digraph test {
        graph [ratio=fill];
        node [ fontsize=15, shape=plaintext];
        graph [bb="0,0,352,154"];
        arset [label=<
        <TABLE ALIGN="LEFT">""")
      for i in range(variableFilas):
        self.tabladoc7.write("""<TR>""")
        for u in range(variableColumna):
            self.tabladoc7.write("""<TD>"""+str(self.matriz10.obtnernodo(i+1,u+1))+"""</TD>""")
        self.tabladoc7.write("""</TR>""")
      self.tabladoc7.write("""</TABLE>
        >, ];
              }
        """)
      self.tabladoc7.close()
      os.system('dot -Tgif tabla7.dot -o random3.gif')
      img = PhotoImage(file="random3.gif")
      Label(ventana, image=img).place(x=350,y=50)
      self.ejecutar()
      ventana.mainloop()      
    else:
      os.system('dot -Tgif tabla7.dot -o random3.gif')     
      img = PhotoImage(file="random3.gif")
      Label(ventana, image=img).place(x=350,y=50)
      ventana.mainloop()         
  def diferenciaSimetrica(self,archivoEntrada,ventana,matriz1,matriz2):
    self.contame4=self.contame4+1
    docs = minidom.parse(archivoEntrada)
    imagen=docs.getElementsByTagName("nombre")
    imagenll=docs.getElementsByTagName("nombre")
    now = datetime.now()
    d1 = now.strftime("%d/%m/%Y %H:%M:%S")
    self.nombres= self.nombres+d1+"-DIFERENCIA SIMETRICA - MATRICES USADAS:("+imagen[int(matriz1)-1].firstChild.nodeValue+","+imagen[int(matriz2)-1].firstChild.nodeValue+")"+"*"
    if(self.contame4==1):
      m=""
      fila=0
      fila2=0
      n=""
      columna=0
      columna2=0
      variableFilas=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      filasArchivo=docs.getElementsByTagName("filas")
      columnasArchivo=docs.getElementsByTagName("columnas")
      variableColumna=0
      if(int(filasArchivo[int(matriz1)-1].firstChild.nodeValue)<int(filasArchivo[int(matriz2)-1].firstChild.nodeValue)):
        variableFilas=int(filasArchivo[int(matriz1)-1].firstChild.nodeValue)
        print(variableFilas)
      else:
        variableFilas=int(filasArchivo[int(matriz2)-1].firstChild.nodeValue)
        print(variableFilas)
      if(int(columnasArchivo[int(matriz1)-1].firstChild.nodeValue)<int(columnasArchivo[int(matriz2)-1].firstChild.nodeValue)):
        variableColumna=int(columnasArchivo[int(matriz1)-1].firstChild.nodeValue)
        print(variableColumna)
      else:
        variableColumna=int(columnasArchivo[int(matriz2)-1].firstChild.nodeValue)
        print(variableColumna)
      """MATRIZ 1"""
      for lineas in imagen[int(matriz1)-1].firstChild.nodeValue:
        if(lineas!=" "):
          if(lineas!="\n"):
            columna=columna+1
            self.matriz8.insertar(fila,columna,lineas.replace("-"," "))
          else:
            columna=0
            fila=fila+1
      """MATRIZ 2"""
      for linea in imagen[int(matriz2)-1].firstChild.nodeValue:
        if(linea!=" "):
          if(linea!="\n"):
            columna2=columna2+1
            self.matriz9.insertar(fila2,columna2,linea.replace("-"," "))
           
          else:
            columna2=0
            fila2=fila2+1
      print(variableFilas)
      print(variableColumna)
      for filass in range(variableFilas):
        for columnass in range(variableColumna):
          if(str(self.matriz8.obtnernodo(filass+1,columnass+1)) == str(self.matriz9.obtnernodo(filass+1,columnass+1)) ):
            self.matriz11.insertar(filass+1,columnass+1," ")
          else:
            self.matriz11.insertar(filass+1,columnass+1,"*")
      self.tabladoc8.write("""
        digraph test {
        graph [ratio=fill];
        node [ fontsize=15, shape=plaintext];
        graph [bb="0,0,352,154"];
        arset [label=<
        <TABLE ALIGN="LEFT">""")
      for i in range(variableFilas):
        self.tabladoc8.write("""<TR>""")
        for u in range(variableColumna):
            self.tabladoc8.write("""<TD>"""+str(self.matriz11.obtnernodo(i+1,u+1))+"""</TD>""")
        self.tabladoc8.write("""</TR>""")
      self.tabladoc8.write("""</TABLE>
        >, ];
              }
        """)
      self.tabladoc8.close()
      os.system('dot -Tgif tabla8.dot -o random4.gif')
      img = PhotoImage(file="random4.gif")
      Label(ventana, image=img).place(x=350,y=50)
      self.ejecutar()
      ventana.mainloop()      
    else:
      os.system('dot -Tgif tabla8.dot -o random4.gif')  
      img = PhotoImage(file="random4.gif")
      Label(ventana, image=img).place(x=350,y=50)
      ventana.mainloop()   
  def ejecutar(self):
    self.reporte.dosImagenes(self.nombres,self.vacio,self.vacio2)
