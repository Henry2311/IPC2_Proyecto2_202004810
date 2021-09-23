
import xml.etree.ElementTree as ET
from produccion import linea, producto,simulacion,acciones
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
        principal.append(linea(cm.dato,time.dato,num.dato,dlinkedlist(),1,''))
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
                if 'L'+str(L.dato.getId())+str(C.dato) == com.dato: 
                    temp.append(acciones(t,'Mover brazo',C.dato))
                    
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
                                    temp.append(acciones(t,'Esperar',''))

                                    t+=int(L.dato.getTiempo())
                                    temp.append(acciones(t,'Ensamblar',C.dato))
                                else:
                                    t+=int(L.dato.getTiempo())
                                    temp.append(acciones(t,'Ensamblar',C.dato))
                            else:
                                t+=int(L.dato.getTiempo())
                                temp.append(acciones(t,'Ensamblar',C.dato))
                        elif com.dato[-1]<com.preview.dato and t>Taux:
                            t+=1
                            temp.append(acciones(t,'Esperar',''))

                            t+=int(L.dato.getTiempo())
                            temp.append(acciones(t,'Ensamblar',C.dato))
                        else:
                            if com.dato[-1]<com.preview.dato and pos==ensamble.size:
                                t+=1
                                temp.append(acciones(t,'Esperar',''))

                                t+=int(L.dato.getTiempo())
                                temp.append(acciones(t,'Ensamblar',C.dato))
                            else:
                                t+=1
                                temp.append(acciones(t,'Esperar',''))
                                if t<Taux:
                                    t+=1
                                    temp.append(acciones(t,'Esperar',''))

                                    t+=int(L.dato.getTiempo())
                                    temp.append(acciones(t,'Ensamblar',C.dato))
                                else:
                                    t+=int(L.dato.getTiempo())
                                    temp.append(acciones(t,'Ensamblar',C.dato))
                    elif esp==-1:
                        t+=int(L.dato.getTiempo())
                        temp.append(acciones(t,'Ensamblar',C.dato))

                        t+=1
                        temp.append(acciones(t,'Esperar',''))
                    else:
                        t+=int(L.dato.getTiempo())
                        temp.append(acciones(t,'Ensamblar',C.dato))
                        
 
                    L.dato.setTpro(t)
                    
                    f=com.dato[-2]+str(int(com.dato[-1])+1)
                    L.dato.setFlotante(f)
                    break

                else:
                    aux=dlinkedlist()
                    if com.dato.find('L'+L.dato.getId())!=-1: 
                        aux.append(str(C.dato)) #L1C1 L1C2 L1C3 
                        if temp.size==0:
                            temp.append(acciones(t,'Mover brazo',C.dato))
                            t+=1
                        else:
                            taux=aux.first
                            while taux: #Estamos C1
                                if taux.dato.find(L.dato.getFlotante())!=-1: #verifica C2
                                    temp.append(acciones(t,'Mover brazo',C.dato))
                                    t+=1  
                                taux=taux.next       
                C=C.next
            L=L.next 
        L=maquina.first
        pos+=1
        com=com.next
        

    pos=1
    t=1

    L=maquina.first
    while L:
        if L.next!=None:
            actual=L.dato.getMoves().size
            comparador=L.next.dato.getMoves().size
            if actual==comparador:
                print('TODO BIEN')
            elif actual < comparador:
                count=comparador-actual
                i=1
                t=L.dato.getTpro()
                while i<=count:
                    L.dato.getMoves().append(acciones(t,'Esperar',''))
                    t+=1
                    i+=1
            elif actual > comparador:
                count=actual-comparador
                i=1
                t=L.dato.getTpro()
                while i<=count:
                    L.next.dato.getMoves().append(acciones(t,'Esperar',''))
                    t+=1
                    i+=1

        L=L.next

    print('---------------')
    L=maquina.first
    
    x=1
    while L:
        print('-----Linea '+str(x)+'-----')
        P=L.dato.getMoves().first
        while P:
            print('Tiempo: ',P.dato.getTiempo(),P.dato.getAccion(),P.dato.getComponente())
            P=P.next
        L=L.next
        x+=1
    
   
def write_xml(maquina,simulacion,dato,archivo,switch):

    if switch:
        print('ENTRE AL IF DE WRITE XML') 
        mytree = ET.parse(archivo)
        myroot = mytree.getroot()

        product=ET.Element('Producto')
        nombre=ET.SubElement(product,'Nombre')
        nombre.text=dato

        L=maquina.first
        P=L.dato.getMoves().last
        t=P.dato.getTiempo()
        tiempoTotal=ET.SubElement(product,'TiempoTotal')
        tiempoTotal.text=str(t)

        Elo=ET.SubElement(product,'ElaboracionOptima')
        T=L.dato.getMoves().size
        x=1
        
        while x<=T:
            pro=L.dato.getMoves().first
            tiempo=ET.SubElement(Elo,'Tiempo',NoSegundos=str(pro.dato.getTiempo()))
            while L:
                pro=L.dato.getMoves().first
                LineaE=ET.SubElement(tiempo,'LineaEnsamblaje',Nolinea=str(L.dato.getId()))
                LineaE.text=pro.dato.getAccion()+' - '+pro.dato.getComponente()
                L.dato.getMoves().delete()
                L=L.next
            
            L=maquina.first
            x+=1
        estructura(product)
        
        myroot.append(product)
        doc=ET.ElementTree(myroot)
        guardar=simulacion.getId()+'.xml'
        doc.write(guardar)

    else:
        print('ENTRE AL ELSE DE WRITE XML')   
        raiz=ET.Element('SalidaSimulacion')
        N=ET.SubElement(raiz,'Nombre')
        N.text=simulacion.getId()

        listadoP=ET.SubElement(raiz,'ListadoProductos')

        product=ET.SubElement(listadoP,'Producto')
        nombre=ET.SubElement(product,'Nombre')
        nombre.text=dato

        L=maquina.first
        P=L.dato.getMoves().last
        t=P.dato.getTiempo()
        tiempoTotal=ET.SubElement(product,'TiempoTotal')
        tiempoTotal.text=str(t)

        Elo=ET.SubElement(product,'ElaboracionOptima')
        T=L.dato.getMoves().size
        x=1
        
        while x<=T:
            pro=L.dato.getMoves().first
            tiempo=ET.SubElement(Elo,'Tiempo',NoSegundos=str(pro.dato.getTiempo()))
            while L:
                pro=L.dato.getMoves().first
                LineaE=ET.SubElement(tiempo,'LineaEnsamblaje',Nolinea=str(L.dato.getId()))
                LineaE.text=pro.dato.getAccion()+' - '+pro.dato.getComponente()
                L.dato.getMoves().delete()
                L=L.next
            
            L=maquina.first
            x+=1
        
        estructura(raiz)
        doc = ET.ElementTree(raiz)
        guardar=simulacion.getId()+'.xml'
        try:
            doc.write(guardar) 
        except IOError as e:
            print(e)
    
def create_html(nombre,maquina):
    file=open('Reporte '+nombre+'.html','w')
    contenido='''<!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta http-equiv="X-UA-Compatible" content="IE=edge">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <link rel="stylesheet" href="style.css">
                            <title>Reporte</title>
                        </head>
                        <body>
                        <div class="container-table">
                            <div class="table__title1">
                                Elaboracion de '''+nombre+''' 
                            </div>
                        </div> '''

    contenido+='<div id="main-container">' 
    contenido+='''<table>
                    <thead>
                        <tr>'''
    
    contenido+='<th style="border-top-left-radius: 20px;">Tiempo (s)</th>'

    L=maquina.first
    while L:
        if L.dato.getId()==maquina.last.dato.getId():
            contenido+='<th style="border-top-right-radius: 20px;">Linea '+L.dato.getId()+'</th>'
        else:
            contenido+='<th>Linea '+L.dato.getId()+'</th>'
        L=L.next
    contenido+='</tr>'
    contenido+='</thead>'
        
    L=maquina.first
    T=L.dato.getMoves().size
    x=1  
    while x<=T:
        pro=L.dato.getMoves().first
        contenido+='<tr>'
        contenido+='<td>'+str(pro.dato.getTiempo())+'</td>'
        while L:
            pro=L.dato.getMoves().first
            contenido+='<td>'+pro.dato.getAccion()+' - '+pro.dato.getComponente()+'</td>'

            L.dato.getMoves().delete()
            L=L.next
        contenido+='</tr>'   
        L=maquina.first
        x+=1

    contenido+='''</table>
                    </div>
                    </body>
                    </html>'''

    file.write(contenido)
    file.close()
    

def create_htmlS(maquina,simulacion,dato,archivo,switch):
    if switch:
        file=open(archivo,'r')
        contenido=file.read()
        contenido.replace('</body>','')
        contenido.replace('</html>','')

        contenido+='''<div class="container-table">
                            <div class="table__title1">
                                Elaboracion de '''+dato+''' 
                            </div>
                        </div> '''
        contenido+='<div id="main-container">' 
        contenido+='''<table>
                       <thead>
                        <tr>'''
    
        contenido+='<th style="border-top-left-radius: 20px;">Tiempo (s)</th>'

        L=maquina.first
        while L:
            if L.dato.getId()==maquina.last.dato.getId():
                contenido+='<th style="border-top-right-radius: 20px;">Linea '+L.dato.getId()+'</th>'
            else:
                contenido+='<th>Linea '+L.dato.getId()+'</th>'
            L=L.next
        contenido+='</tr>'
        contenido+='</thead>'
        
        L=maquina.first
        T=L.dato.getMoves().size
        x=1  
        while x<=T:
            pro=L.dato.getMoves().first
            contenido+='<tr>'
            contenido+='<td>'+str(pro.dato.getTiempo())+'</td>'
            while L:
                pro=L.dato.getMoves().first
                contenido+='<td>'+pro.dato.getAccion()+' - '+pro.dato.getComponente()+'</td>'

                L.dato.getMoves().delete()
                L=L.next
            contenido+='</tr>'   
            L=maquina.first
            x+=1

        contenido+='''</table>
                    </div>
                    </body>
                    </html>'''
        newfile=open(archivo,'w')
        newfile.write(contenido)
        file.close()
        newfile.close()

    else:
        file=open('Reporte '+simulacion.getId()+'.html','w')
        contenido='''<!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta http-equiv="X-UA-Compatible" content="IE=edge">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <link rel="stylesheet" href="style.css">
                            <title>Reporte</title>
                        </head>
                        <body>
                        <div class="container-table">
                            <div class="table__title1">
                                Reporte de '''+simulacion.getId()+''' 
                            </div>
                        </div> '''
        contenido+='''<div class="container-table">
                            <div class="table__title1">
                                Elaboracion de '''+dato+''' 
                            </div>
                        </div> '''
        contenido+='<div id="main-container">' 
        contenido+='''<table>
                       <thead>
                        <tr>'''
    
        contenido+='<th style="border-top-left-radius: 20px;">Tiempo (s)</th>'

        L=maquina.first
        while L:
            if L.dato.getId()==maquina.last.dato.getId():
                contenido+='<th style="border-top-right-radius: 20px;">Linea '+L.dato.getId()+'</th>'
            else:
                contenido+='<th>Linea '+L.dato.getId()+'</th>'
            L=L.next
        contenido+='</tr>'
        contenido+='</thead>'
        
        L=maquina.first
        T=L.dato.getMoves().size
        x=1  
        while x<=T:
            pro=L.dato.getMoves().first
            contenido+='<tr>'
            contenido+='<td>'+str(pro.dato.getTiempo())+'</td>'
            while L:
                pro=L.dato.getMoves().first
                contenido+='<td>'+pro.dato.getAccion()+' - '+pro.dato.getComponente()+'</td>'

                L.dato.getMoves().delete()
                L=L.next
            contenido+='</tr>'   
            L=maquina.first
            x+=1

        contenido+='''</table>
                    </div>
                    </body>
                    </html>'''

        file.write(contenido)
        file.close()

        

def estructura(root, tab='  '):
    aux = [(0, root)]
    while aux:
        line, e = aux.pop(0)
        lista = [(line + 1, c) for c in list(e)]
        if lista:
            e.text = '\n' + tab * (line+1)
        if aux:
            e.tail = '\n' + tab * aux[0][0]
        else:
            e.tail = '\n' + tab * (line-1) 
        aux[0:0] = lista 

if __name__ == "__main__":
    global file
    ruta='D:\Henry\GitHub\proyecto2-IPC2\Archivos de prueba - Proyecto 2\maquina.xml'
    file=read_xml(ruta)
    maquina,productos=datosM(file)

    ruta2='D:\Henry\GitHub\proyecto2-IPC2\Archivos de prueba - Proyecto 2\simulacion_1.xml'
    file2=read_xml(ruta2)
    sim=dlinkedlist()
    sim=datosS(file2,sim)
    
    ruta3='D:\Henry\GitHub\proyecto2-IPC2\Archivos de prueba - Proyecto 2\simulacion_2.xml'
    file3=read_xml(ruta3)
    sim=datosS(file3,sim)

    aux=sim.first
    switch=False
    while aux:
        aux2=aux.dato.getProductos().first
        xd=aux.dato.getId()
        print('id de simulacion',xd)
        
        while aux2:
            print('producto',aux2.dato)
            fabricar(aux2.dato,maquina,productos)
            create_htmlS(maquina,aux.dato,aux2.dato,'Reporte '+aux.dato.getId()+'.html',switch)
            maquina,productos=datosM(file)
            switch=True
            aux2=aux2.next
            
        switch=False
        aux=aux.next

    
    

    '''print('datos de la segunda simulacion añadidos')
    aux = sim.first
    while aux:
        xd=aux.dato.getId()
        print(xd)
        aux.dato.getProductos().recorrer_inicio()
        aux=aux.next'''

    

    

