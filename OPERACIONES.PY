from MATRIZ import * 
from tkinter import *
from xml.dom import minidom
class operaciones:
  matriz = Matriz()
  matriz2 = Matriz()
  matriz3=Matriz()
  matriz4=Matriz()
  matriz5=Matriz()
  matriz6=Matriz()
  matriz7=Matriz()
  matriz8=Matriz()
  
  contame =0
  contame2=0
  contame3=0
  contame4=0
  contame5=0
  contame6=0
  contame7=0
  contame8=0

  def ImagenHorizontal(self,archivoEntrada,frame,ventana):
    self.contame=self.contame+1
    if(self.contame==1):
      m=""
      fila=0
      columna=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")

      for linea in imagen[0].firstChild.nodeValue:
        if(linea!=" "):
          if(linea!="\n"):
          
            columna=columna+1
            self.matriz.insertar(fila,columna,linea.replace("-"," "))
          else:
            columna=0
            fila=fila+1
      """OPERACION IMAGEN HORIZONATAL"""
      n=""
      for i in range(int(docs.getElementsByTagName("filas")[0].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[0].firstChild.nodeValue)):
          n=n+str(self.matriz.obtnernodo(int(docs.getElementsByTagName("filas")[0].firstChild.nodeValue)-i,u+1))+""
        m=m+n+"\n"
        print(n)
        n=""
      texto=frame.delete('1.0', END)  
      texto=frame.insert(INSERT, m)
    else:
      m=""
      fila=0
      columna=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      for iy in range(int(docs.getElementsByTagName("filas")[0].firstChild.nodeValue)):
        for ue in range(int(docs.getElementsByTagName("columnas")[0].firstChild.nodeValue)):
          n=n+str(self.matriz.obtnernodo(int(docs.getElementsByTagName("filas")[0].firstChild.nodeValue)-iy,ue+1))+""
        m=m+n+"\n" 
        print(n)
        n=""
      texto=frame.delete('1.0', END)
      texto=frame.insert(INSERT, m)
    
  def ImagenVertical(self,archivoEntrada,frame,ventana):
    self.contame2=self.contame2+1
    if(self.contame2==1):
      fila=0
      m=""
      columna=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      for linea in imagen[0].firstChild.nodeValue:
        if(linea!=" "):
          if(linea!="\n"):
          
            columna=columna+1
            self.matriz2.insertar(fila,columna,linea.replace("-"," "))
          else:
            columna=0
            fila=fila+1
      """OPERACION IMAGEN VERTICAL"""
      for i in range(int(docs.getElementsByTagName("filas")[0].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[0].firstChild.nodeValue)):
          n=n+str(self.matriz2.obtnernodo(i+1,int(docs.getElementsByTagName("columnas")[0].firstChild.nodeValue)-u))+""
        m=m+n+"\n"
        print(n)
        n=""
      texto=frame.delete('1.0', END)
      texto=frame.insert(INSERT, m)
    else:
      fila=0
      m=""
      columna=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      for i in range(int(docs.getElementsByTagName("filas")[0].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[0].firstChild.nodeValue)):
          n=n+str(self.matriz2.obtnernodo(i+1,int(docs.getElementsByTagName("columnas")[0].firstChild.nodeValue)-u))+""
        m=m+n+"\n"
        print(n)
        n=""
      texto=frame.delete('1.0', END)
      texto=frame.insert(INSERT, m)  
  def Traspuesta(self,archivoEntrada,frame,ventana):
    self.contame3=self.contame3+1
    if(self.contame3==1):
      fila=0
      columna=0
      m=""
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      for linea in imagen[0].firstChild.nodeValue:
        if(linea!=" "):
          if(linea!="\n"):
          
            columna=columna+1
            self.matriz3.insertar(fila,columna,linea.replace("-"," "))
          else:
            columna=0
            fila=fila+1
      """OPERACION IMAGEN TRASPUESTA"""
      for i in range(int(docs.getElementsByTagName("filas")[0].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[0].firstChild.nodeValue)):
          n=n+str(self.matriz3.obtnernodo(u+1,i+1))+""
        m=m+n+"\n"
        print(n)
        n=""
        
      texto=frame.delete('1.0', END)  
      texto=frame.insert(INSERT, m)
    else:
      fila=0
      m=""
      columna=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      for i in range(int(docs.getElementsByTagName("filas")[0].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[0].firstChild.nodeValue)):
          n=n+str(self.matriz3.obtnernodo(u+1,i+1))+""
        m=m+n+"\n"
        print(n)
        n=""
      texto=frame.delete('1.0', END)
      texto=frame.insert(INSERT, m)
  def operacionLimpiar(self,archivoEntrada,frame,ventana,y1,x1,y2,x2):
    self.contame4=self.contame4+1
    if(self.contame4==1):
      fila=0
      m=""
      columna=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      for linea in imagen[0].firstChild.nodeValue:
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

      for i in range(int(docs.getElementsByTagName("filas")[0].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[0].firstChild.nodeValue)):
         
          n=n+str(self.matriz4.obtnernodo(i+1,u+1))+""
        m=m+n+"\n"
        print(n)
        n=""
      texto=frame.delete('1.0', END) 
      texto=frame.insert(INSERT, m)
    else:
      
      fila=0
      columna=0
      m=""
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      for li in range(int(y2)):
        for colu in range(int(x2)):
          if(li+1>=y1):
            if(colu+1>=x1):
              self.matriz4.obtnernodos(li+1,colu+1," ")
      for i in range(int(docs.getElementsByTagName("filas")[0].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[0].firstChild.nodeValue)):
          n=n+str(self.matriz4.obtnernodo(i+1,u+1))+""
        m=m+n+"\n"
        print(n)
        n=""
      texto=frame.delete('1.0', END)
      texto=frame.insert(INSERT, m)
  def AgregarEnX(self,archivoEntrada,frame,ventana,y,x,cantidad):
    self.contame5=self.contame5+1
    if(self.contame5==1):
      fila=0
      m=""
      columna=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      for linea in imagen[0].firstChild.nodeValue:
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

      for i in range(int(docs.getElementsByTagName("filas")[0].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[0].firstChild.nodeValue)):
         
          n=n+str(self.matriz5.obtnernodo(i+1,u+1))+""
        m=m+n+"\n"
        print(n)
        n=""
      texto=frame.delete('1.0', END)  
      texto=frame.insert(INSERT, m)
    else:
      m=""
      fila=0
      columna=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      for ir in range(int(cantidad)):
        self.matriz5.obtnernodos(y,x+ir,"*")
      for i in range(int(docs.getElementsByTagName("filas")[0].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[0].firstChild.nodeValue)):
          n=n+str(self.matriz5.obtnernodo(i+1,u+1))+""
        m=m+n+"\n"
        print(n)
        n=""
      texto=frame.delete('1.0', END)
      texto=frame.insert(INSERT, m)
  def AgregarEnY(self,archivoEntrada,frame,ventana,y,x,cantidad):
    self.contame6=self.contame6+1
    if(self.contame6==1):
      fila=0
      m=""
      columna=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      for linea in imagen[0].firstChild.nodeValue:
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

      for i in range(int(docs.getElementsByTagName("filas")[0].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[0].firstChild.nodeValue)):
         
          n=n+str(self.matriz6.obtnernodo(i+1,u+1))+""
        m=m+n+"\n"
        print(n)
        n=""
      texto=frame.delete('1.0', END)  
      texto=frame.insert(INSERT, m)
    else:
      fila=0
      columna=0
      m=""
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      for ir in range(int(cantidad)):
        self.matriz6.obtnernodos(y+ir,x,"*")
      for i in range(int(docs.getElementsByTagName("filas")[0].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[0].firstChild.nodeValue)):
          n=n+str(self.matriz6.obtnernodo(i+1,u+1))+""
        m=m+n+"\n"
        print(n)
        n=""
      texto=frame.delete('1.0', END)
      texto=frame.insert(INSERT, m)
  def AgregarRectangulo(self,archivoEntrada,frame,ventana,y,x,cantidadY,cantidadX):
    self.contame7=self.contame7+1
    if(self.contame7==1):
      fila=0
      m=""
      columna=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      for linea in imagen[0].firstChild.nodeValue:
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

      for i in range(int(docs.getElementsByTagName("filas")[0].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[0].firstChild.nodeValue)):
         
          n=n+str(self.matriz7.obtnernodo(i+1,u+1))+""
        m=m+n+"\n"
        print(n)
        n=""
      texto=frame.delete('1.0', END)
      texto=frame.insert(INSERT, m)
    else:
      fila=0
      m=""
      columna=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      for ir in range(int(cantidadX)):
        self.matriz7.obtnernodos(y,x+ir,"*")
      for ir in range(int(cantidadX)):
        self.matriz7.obtnernodos(y+cantidadY-1,x+ir,"*")  
      for i in range(int(docs.getElementsByTagName("filas")[0].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[0].firstChild.nodeValue)):
          n=n+str(self.matriz7.obtnernodo(i+1,u+1))+""
        print(n)
        m=m+n+"\n"
        n=""
      texto=frame.delete('1.0', END)
      texto=frame.insert(INSERT, m)
  def AgregarTriangulo(self,archivoEntrada,frame,ventana,y,x,cantidad):
    kat=0
    self.contame8=self.contame8+1
    if(self.contame8==1):
      fila=0
      columna=0
      
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      m=""
      for linea in imagen[0].firstChild.nodeValue:
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
        

      for i in range(int(docs.getElementsByTagName("filas")[0].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[0].firstChild.nodeValue)):
         
          n=n+str(self.matriz8.obtnernodo(i+1,u+1))+""
          
        
        m=m+n+"\n"
        n=""
      texto=frame.delete('1.0', END)
      texto=frame.insert(INSERT, m)
    else:
      fila=0
      m=""

      columna=0
      docs = minidom.parse(archivoEntrada)
      imagen=docs.getElementsByTagName("imagen")
      n=""
      for ir in range(int(cantidad)):
        self.matriz8.obtnernodos(y+cantidad-1,x+ir,"*")  
      for i in range(int(docs.getElementsByTagName("filas")[0].firstChild.nodeValue)):
        for u in range(int(docs.getElementsByTagName("columnas")[0].firstChild.nodeValue)):
          n=n+str(self.matriz8.obtnernodo(i+1,u+1))+""
        m=m+n+"\n"
        n=""
      texto=frame.delete('1.0', END)
      texto=frame.insert(INSERT, m)
      
    
    

