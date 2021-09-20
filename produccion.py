from lista import dlinkedlist
class producto:
    def __init__(self,nombre,ensamblaje):
        self.nombre = nombre
        self.ensamblaje = ensamblaje #lista
    
    def getNombre(self):
        return self.nombre

    def getEnsamblaje(self):
        return self.ensamblaje
    
    def setNombre(self,nombre):
        self.nombre = nombre
    
    def setEnsamblaje(self,ensamblaje):
        self.ensamblaje = ensamblaje

class linea:
    def __init__(self,componentes,tiempo,id,acciones,Tp,flot):
        self.componentes = componentes  #lista = [C1, C2, C3....]
        self.tiempo = tiempo
        self.id = id #L1, L2, L3...
        self.moves = acciones
        self.Tproduccion=Tp
        self.flotante=flot

    def getComponentes(self):
        return self.componentes

    def getTiempo(self):
        return self.tiempo

    def getId(self):
        return self.id

    def getMoves(self):
        return self.moves

    def getTpro(self):
        return self.Tproduccion
    
    def getFlotante(self):
        return self.flotante

    def setComponentes(self,componentes):
        self.componentes = componentes
    
    def setTiempo(self,tiempo):
        self.tiempo = tiempo

    def setId(self,id):
        self.id = id

    def setMoves(self,move):
        self.moves = move
    
    def setTpro(self,t):
        self.Tproduccion += t
    
    def setFlotante(self,f):
        self.flotante=f
    
class simulacion:
    def __init__(self,id,productos):
        self.id = id
        self.productos = productos
    
    def getId(self):
        return self.id
    
    def getProductos(self):
        return self.productos

