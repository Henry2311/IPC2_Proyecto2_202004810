import xml.etree.ElementTree as ET
from produccion import linea, producto,simulacion
from lista import dlinkedlist

def read_xml(root):
    mytree = ET.parse(root)
    myroot = mytree.getroot()
    return myroot

def datosM(file):
    principal=dlinkedlist()
    productos=dlinkedlist()
    numero=dlinkedlist()
    coms=dlinkedlist()
    tiempo=dlinkedlist()
    components=dlinkedlist()
    
    for c in file.findall('./ListadoLineasProduccion/LineaProduccion/Numero'):
        numero.append(c.text)
    
    for c in file.findall('./ListadoLineasProduccion/LineaProduccion/CantidadComponentes'):
        coms.append(c.text)

    for c in file.findall('./ListadoLineasProduccion/LineaProduccion/TiempoEnsamblaje'):
        tiempo.append(c.text)
    
    aux = coms.first
    while aux:
        limit=int(aux.dato)
        temp=dlinkedlist()
        for i in range(1,limit+1):
            temp.append('C'+str(i))

        components.append(temp)    
        temp=dlinkedlist()
        aux=aux.next

    num=numero.first
    cm=components.first
    time=tiempo.first
    while num and cm and time:
        principal.append(linea(cm.dato,time.dato,'L'+num.dato,dlinkedlist(),1,''))
        num = num.next
        cm = cm.next
        time = time.next

    nombre=dlinkedlist()
    ensamble=dlinkedlist()
    for c in file.findall('./ListadoProductos/Producto/nombre'):
        nombre.append(c.text)
    
    for c in file.findall('./ListadoProductos/Producto/elaboracion'):
        temp=dlinkedlist()
        x=c.text+' '
        temporal=''
        for i in x:
            if i == ' ':
                temp.append(temporal)
                temporal=''
            else:
                temporal+=i

        ensamble.append(temp)

    name=nombre.first
    ens=ensamble.first
    while name and ens:
        productos.append(producto(name.dato,ens.dato))
        name=name.next
        ens=ens.next
    
    return principal,productos
    
def datosS(file,sim):
    indice=''
    productos=dlinkedlist()

    for c in file.findall('./Nombre'):
        indice+=c.text
    
    for c in file.findall('./ListadoProductos/Producto'):
        productos.append(c.text)

    
    if sim.size==0:
        sim.append(simulacion(indice,productos))
    else:
        sim.append(simulacion(indice,productos))
        
    return sim

def find(maquina,com):
    L=maquina.first
    pos=1
    while L:
        C=L.dato.getComponentes().first
        while C:
            if str(L.dato.getId())+str(C.dato) == com:
                return True, pos
            else:
                pos+=1
            C=C.next
        L=L.next
    
    return False, com

def fabricar(nombre,maquina,productos):
    ensamble=''

    aux = productos.first
    while aux:
        if aux.dato.getNombre()==nombre:
            ensamble=aux.dato.getEnsamblaje()
        aux=aux.next

    print('Ensamblar: '+nombre)
    print('Con componentes: ')
    ensamble.recorrer_inicio()
    
    L = maquina.first
    com=ensamble.first
    
    esp=0
    pos=1
    while com:
        while L:
            C=L.dato.getComponentes().first
            temp=L.dato.getMoves()
            
            t=L.dato.getTpro()
            if L.preview!=None:
                Taux=L.preview.dato.getTpro()
            else:
                Taux=0

            while C:
                if str(L.dato.getId())+str(C.dato) == com.dato:
                    temp.append('Tiempo: '+str(t)+'s Moverse a: '+str(L.dato.getId())+str(C.dato))
                    
                    if pos==1:
                        esp=0
                    elif pos<=ensamble.size:
                        if ensamble.size-pos==1:
                            esp=-1
                        elif pos==ensamble.size:
                            esp=int(L.dato.getTiempo())
                        else:
                            esp=int(L.dato.getTiempo())
                                       
                    
                    if esp>0:
                        if com.dato[-1]>com.preview.dato[-1]:
                            if  pos==ensamble.size:
                                
                                if t>Taux:
                                    t+=1
                                    temp.append('Tiempo: '+str(t)+'s Esperar')

                                    t+=int(L.dato.getTiempo())
                                    temp.append('Tiempo: '+str(t)+'s Ensamblar: '+str(L.dato.getId())+str(C.dato))
                                else:

                                    t+=int(L.dato.getTiempo())
                                    temp.append('Tiempo: '+str(t)+'s Ensamblar: '+str(L.dato.getId())+str(C.dato))
                            else:
                                t+=int(L.dato.getTiempo())
                                temp.append('Tiempo: '+str(t)+'s Ensamblar: '+str(L.dato.getId())+str(C.dato))
                        elif com.dato[-1]<com.preview.dato and t>Taux:
                            print(str(t),str(Taux))
                            t+=1
                            temp.append('Tiempo: '+str(t)+'s Esperar')

                            t+=int(L.dato.getTiempo())
                            temp.append('Tiempo: '+str(t)+'s Ensamblar: '+str(L.dato.getId())+str(C.dato))
                        else:
                            if com.dato[-1]<com.preview.dato and pos==ensamble.size:
                                t+=1
                                temp.append('Tiempo: '+str(t)+'s Esperar')

                                t+=int(L.dato.getTiempo())
                                temp.append('Tiempo: '+str(t)+'s Ensamblar: '+str(L.dato.getId())+str(C.dato))
                            else:
                                t+=1
                                temp.append('Tiempo: '+str(t)+'s Esperar')
                                if t<Taux:
                                    t+=1
                                    temp.append('Tiempo: '+str(t)+'s Esperar')

                                    t+=int(L.dato.getTiempo())
                                    temp.append('Tiempo: '+str(t)+'s Ensamblar: '+str(L.dato.getId())+str(C.dato))
                                else:
                            
                                    t+=int(L.dato.getTiempo())
                                    temp.append('Tiempo: '+str(t)+'s Ensamblar: '+str(L.dato.getId())+str(C.dato))
                    elif esp==-1:
                        t+=int(L.dato.getTiempo())
                        temp.append('Tiempo: '+str(t)+'s Ensamblar: '+str(L.dato.getId())+str(C.dato))

                        t+=1
                        temp.append('Tiempo: '+str(t)+'s Esperar')
                    else:
                        t+=int(L.dato.getTiempo())
                        temp.append('Tiempo: '+str(t)+'s Ensamblar: '+str(L.dato.getId())+str(C.dato))
                    
                    
                    
                    
                    L.dato.setTpro(t)
                    
                    f=com.dato[-2]+str(int(com.dato[-1])+1)
                    
                    L.dato.setFlotante(f)
                    break

                else:
                    aux=dlinkedlist()
                    xd=t
                    if com.dato.find(L.dato.getId())!=-1: 
                        aux.append('Tiempo: '+str(t)+'s Moverse a: '+str(L.dato.getId())+str(C.dato))
                        xd+=1
                        if temp.size==0:
                            
                            temp.append('Tiempo: '+str(t)+'s Moverse a: '+str(L.dato.getId())+str(C.dato))
                            t+=1
                        else:
                            taux=aux.first
                            while taux:
                                if taux.dato.find(L.dato.getFlotante())!=-1:
                                    temp.append('Tiempo: '+str(t)+'s Moverse a: '+str(L.dato.getId())+str(C.dato))
                                    t+=1
                                        
                                    
                                taux=taux.next
                            
                        
                    
                C=C.next
            
           
            L=L.next 
            
            
              
        
        L=maquina.first
        pos+=1
        com=com.next
        

    pos=1
    t=1
    print('---------------')
    L=maquina.first
    
    x=1
    while L:
        print('-----Linea '+str(x)+'-----')
        L.dato.getMoves().recorrer_inicio()
        L=L.next
        x+=1
    
   
    
    
        


if __name__ == "__main__":
    global file
    ruta='D:\Henry\GitHub\proyecto2-IPC2\Archivos de prueba - Proyecto 2\maquina.xml'
    file=read_xml(ruta)
    maquina,productos=datosM(file)

    ruta2='D:\Henry\GitHub\proyecto2-IPC2\Archivos de prueba - Proyecto 2\simulacion_1.xml'
    file2=read_xml(ruta2)
    sim=dlinkedlist()
    sim=datosS(file2,sim)

    '''print('primera simulacion')
    aux = sim.first
    while aux:
        xd=aux.dato.getId()
        print(xd)
        aux.dato.getProductos().recorrer_inicio()
        aux=aux.next'''

    ruta3='D:\Henry\GitHub\proyecto2-IPC2\Archivos de prueba - Proyecto 2\simulacion_2.xml'
    file3=read_xml(ruta3)
    sim=datosS(file3,sim)

    '''print('datos de la segunda simulacion añadidos')
    aux = sim.first
    while aux:
        xd=aux.dato.getId()
        print(xd)
        aux.dato.getProductos().recorrer_inicio()
        aux=aux.next'''

    

    fabricar('Smartwatch',maquina,productos)
    maquina,productos=datosM(file)
    fabricar('Camara',maquina,productos)
    maquina,productos=datosM(file)
    fabricar('USBStick',maquina,productos)
    

    

