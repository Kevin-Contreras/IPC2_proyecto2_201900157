from NODO import Nodo,nodoEncabezado
from ENCABEZADO import listaEncabezado
class Matriz:
  t=0
  
  def __init__(self):
    self.eFilas = listaEncabezado()
    self.ecolumnas = listaEncabezado()
  def insertar(self,fila,columna,valor):
    nuevo = Nodo(fila,columna,valor)
    efila= self.eFilas.getEncabezado(fila)
    if efila==None:
      efila = nodoEncabezado(fila)
      efila.accesoNodo = nuevo
      self.eFilas.setEncabezado(efila)
    else:
      if(nuevo.columna<efila.accesoNodo.columna):
        nuevo.derecha = efila.accesoNodo
        efila.accesoNodo.izquieda=nuevo
        efila.accesoNodo=nuevo
      else:
        actual =efila.accesoNodo
        while actual.derecha!=None:
          if(nuevo.columna<actual.derecha.columna):
            nuevo.derecha =actual.derecha
            actual.derecha.izquieda=nuevo
            nuevo.izquierda= actual
            actual.derecha=nuevo
            break
          actual=actual.derecha
        if(actual.derecha == None):
          actual.derecha=nuevo
          nuevo.izquierda =actual
    ecolumna =self.ecolumnas.getEncabezado(columna)
    if(ecolumna==None):
      ecolumna=nodoEncabezado(columna)
      ecolumna.accesoNodo=nuevo
      self.ecolumnas.setEncabezado(ecolumna)
    else:
      if(nuevo.fila<ecolumna.accesoNodo.fila):
        nuevo.abajo=actual.abajo
        ecolumna.accesoNodo.arriba = nuevo
        ecolumna=accesoNodo=nuevo
      else:
        actual=ecolumna.accesoNodo
        while actual.abajo != None:
          if(nuevo.fila<actual.abajo.fila):
            nuevo.abajo=actual.abajo
            actual.abajo.arriba=nuevo
            nuevo.arriba=actual
            actual.abajo=nuevo
            break
          actual=actual.abajo
        if(actual.abajo==None):
          actual.abajo=nuevo
          nuevo.arriba= actual

  def obtnernodo(self,fila,columna):
    i=0
    
    efila= self.eFilas.primero
    for y in range(fila):
      if(efila!=None):
   
        actual= efila.accesoNodo
        for ter in range(int(columna)):
          if actual != None:
            i=i+1
            if(i==columna*fila):
              
              return actual.valor
            actual=actual.derecha
     
        efila=efila.siguiente
  def obtnernodos(self,fila,columna,valord):
    i=0
    
    efila= self.eFilas.primero
    for y in range(fila):
      if(efila!=None):
   
        actual= efila.accesoNodo
        for ter in range(int(columna)):
          if actual != None:
            i=i+1
            if(i==columna*fila):
              actual.valor=valord
              
              return actual.valor
            actual=actual.derecha
     
        efila=efila.siguiente







