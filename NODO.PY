class Nodo:
  def __init__(self,fila,columna,valor):
    self.fila=fila
    self.columna=columna
    self.valor= valor 
    self.derecha=None
    self.izquierda=None
    self.abajo=None
    self.arriba=None
class nodoEncabezado:
  def __init__(self,ids):
    self.ids=ids
    self.siguiente = None
    self.anterior = None
    self.accesoNodo = None


    
