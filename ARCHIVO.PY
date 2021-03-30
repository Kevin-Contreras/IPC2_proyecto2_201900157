from xml.dom import minidom
from MATRIZ import * 
class Archivo:
  matriz = Matriz()
  def modificar(self,archivoEntrada):
    fila=0
    columna=0
    docs = minidom.parse(archivoEntrada)
    imagen=docs.getElementsByTagName("imagen")
    for linea in imagen[1].firstChild.nodeValue:
      if(linea!=" "):
        if(linea!="\n"):
          
          columna=columna+1
          self.matriz.insertar(fila,columna,linea.replace("-"," "))
        else:
          columna=0
          fila=fila+1
    self.matriz.obtnernodo(2,8)
          
    
    



     
     

