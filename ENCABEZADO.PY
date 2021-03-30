from NODO import Nodo, nodoEncabezado
class listaEncabezado:
  def __init__(self,primero=None):
    self.primero=primero
  def setEncabezado(self,nuevo):
    if(self.primero==None):
      self.primero=nuevo
    elif(nuevo.ids<self.primero.ids):
      nuevo.siguiente=self.primero
      self.primero.anterior = nuevo
      self.primero = nuevo
    else:
      actual = self.primero
      while actual.siguiente !=None:
        if(nuevo.ids<actual.siguiente.ids):
          actual.siguiente.anterior=nuevo
          nuevo.siguiente=actual
          actual.siguiente=nuevo
          break
        actual =actual.siguiente
      if actual.siguiente==None:
        actual.siguiente = nuevo
        nuevo.anterior = actual
  def getEncabezado(self,ids):
    actual= self.primero
    while actual !=None:
      if actual.ids ==ids:
        return actual
      actual=actual.siguiente
    return None
      
