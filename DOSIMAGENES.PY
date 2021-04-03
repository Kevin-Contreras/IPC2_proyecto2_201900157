from MATRIZ import * 
from xml.dom import minidom
class DosImagenesOperaciones:
  matriz = Matriz()
  matriz2 = Matriz()
  matriz3 = Matriz()
  matriz5 = Matriz()
  matriz6 = Matriz()
  matriz8 = Matriz()
  matriz9 = Matriz()
  contame =0
  contame2 =0
  contame3 =0
  contame4 =0

  def union(self,archivoEntrada,matriz1,matriz2):
    self.contame=self.contame+1
    if(self.contame==1):
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
            columna=columna+1
            self.matriz.insertar(fila,columna,lineas.replace("-"," "))
          else:
            columna=0
            fila=fila+1
      """MATRIZ 2"""
      for linea in imagen[int(matriz2)-1].firstChild.nodeValue:
        if(linea!=" "):
          if(linea!="\n"):
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
      print(variableFilas)
      print(variableColumna)
      for filass in range(variableFilas):
        for columnass in range(variableColumna):
           n=n+str(self.matriz.obtnernodo(filass+1,columnass+1))+""
        print(n)
        n=""
  def inteseccion(self,archivoEntrada,matriz1,matriz2):
    self.contame2=self.contame2+1
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
            
            n=n+self.matriz3.obtnernodo(filass+1,columnass+1)+""
          else:
            n=n+self.matriz2.obtnernodo(filass+1,columnass+1)+""
        print(n)
        n=""
  def diferencia(self,archivoEntrada,matriz1,matriz2):
    self.contame3=self.contame3+1
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
            
            n=n+str(self.matriz5.obtnernodo(filass+1,columnass+1))+""
          else:
            n=n+" "
          
        print(n)
        n=""
  def diferenciaSimetrica(self,archivoEntrada,matriz1,matriz2):
    self.contame4=self.contame4+1
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
            n=n+" "
          else:
            n=n+"*"
        print(n)
        n=""

