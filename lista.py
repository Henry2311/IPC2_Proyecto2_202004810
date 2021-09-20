from nodo import nodo
class dlinkedlist:
    def __init__(self):
        self.first=None
        self.last=None
        self.size=0

    def empty(self):
        return self.first == None
    
    def append(self,dato):
        if self.empty():
            self.first = self.last = nodo(dato)
        else: 
            aux = self.last
            self.last = aux.next = nodo(dato)
            self.last.preview = aux
        self.size+=1

    def delete(self):
        if self.empty():
            print('No hay datos')
        elif self.first.next == None:
            self.first = self.last = None
            self.size = 0
        else:
            self.first = self.first.next
            self.first.preview = None
            self.size -= 1

    def recorrer_inicio(self):
        aux = self.first
        while aux:
            print(aux.dato)
            aux = aux.next

