from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox,QFileDialog, QTableWidgetItem,QAbstractItemView
import xml.etree.ElementTree as ET
from produccion import linea, producto,simulacion,acciones
from lista import dlinkedlist
from os import startfile


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.boton1 = QtWidgets.QPushButton(self.centralwidget)
        self.boton1.setGeometry(QtCore.QRect(20, 20, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(14)
        self.boton1.setFont(font)
        self.boton1.setObjectName("boton1")
        self.boton1.clicked.connect(self.read_file)
        self.file=''
        self.fileS=''
        self.maquina=''
        self.productos=''
        self.simulaciones=dlinkedlist()


        self.boton2 = QtWidgets.QPushButton(self.centralwidget)
        self.boton2.setGeometry(QtCore.QRect(200, 20, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(14)
        self.boton2.setFont(font)
        self.boton2.setObjectName("boton2")
        self.boton2.clicked.connect(self.read_fileS)



        self.boton3 = QtWidgets.QPushButton(self.centralwidget)
        self.boton3.setGeometry(QtCore.QRect(380, 20, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(14)
        self.boton3.setFont(font)
        self.boton3.setObjectName("boton3")
        self.boton3.setEnabled(False)
        self.boton3.clicked.connect(self.exportar_xml)

        self.boton4 = QtWidgets.QPushButton(self.centralwidget)
        self.boton4.setGeometry(QtCore.QRect(560, 20, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(14)
        self.boton4.setFont(font)
        self.boton4.setObjectName("boton4")
        self.boton4.clicked.connect(self.soporte)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 100, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.combo = QtWidgets.QComboBox(self.centralwidget)
        self.combo.setGeometry(QtCore.QRect(290, 110, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(14)
        self.combo.setFont(font)
        self.combo.setObjectName("combo")
        self.combo.activated.connect(self.fabricar_producto)


        self.informacion = QtWidgets.QWidget(self.centralwidget)
        self.informacion.setGeometry(QtCore.QRect(20, 165, 541, 691))
        self.informacion.setObjectName("informacion")
        self.boton5 = QtWidgets.QPushButton(self.informacion)
        self.boton5.setGeometry(QtCore.QRect(0, 505, 525, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(16)
        self.boton5.setFont(font)
        self.boton5.setObjectName("boton5")
        self.boton5.setEnabled(False)
        self.boton5.clicked.connect(self.exportar_html)

        self.boton6 = QtWidgets.QPushButton(self.informacion)
        self.boton6.setGeometry(QtCore.QRect(0, 440, 525, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(16)
        self.boton6.setFont(font)
        self.boton6.setObjectName("boton6")
        self.boton6.setEnabled(False)
        self.boton6.clicked.connect(self.guardar_grafo)


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 100, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.combo2 = QtWidgets.QComboBox(self.centralwidget)
        self.combo2.setGeometry(QtCore.QRect(850, 110, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(14)
        self.combo2.setFont(font)
        self.combo2.setObjectName("combo2")
        self.combo2.activated.connect(self.exportar_htmlS)


        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(570, 160, 531, 550))
        self.tableView.setObjectName("tableView")
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setDragDropOverwriteMode(False)
        self.tableView.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|
                                                          Qt.AlignCenter)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.verticalHeader().setDefaultSectionSize(50)

        self.nombre = QtWidgets.QLabel(self.informacion)
        self.nombre.setGeometry(QtCore.QRect(0, 0, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(16)
        self.nombre.setFont(font)
        self.nombre.setObjectName("nombre")

        self.nombreP = QtWidgets.QLabel(self.informacion)
        self.nombreP.setGeometry(QtCore.QRect(0, 50, 500, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(16)
        self.nombreP.setFont(font)
        self.nombreP.setObjectName("nombreP")

        self.Tiempo = QtWidgets.QLabel(self.informacion)
        self.Tiempo.setGeometry(QtCore.QRect(0, 100, 500, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(16)
        self.Tiempo.setFont(font)
        self.Tiempo.setObjectName("tiempo")

        self.Ensamble = QtWidgets.QLabel(self.informacion)
        self.Ensamble.setGeometry(QtCore.QRect(0, 150, 500, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(16)
        self.Ensamble.setFont(font)
        self.Ensamble.setObjectName("ensamble")

        self.imagen = QtWidgets.QLabel(self.informacion)
        self.imagen.setGeometry(QtCore.QRect(0, 200, 541, 200))
        self.imagen.setObjectName("imagen")
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton1.setText(_translate("MainWindow", "Configurar Máquina"))
        self.boton2.setText(_translate("MainWindow", "Simulaciones"))
        self.boton3.setText(_translate("MainWindow", "Reporte XML"))
        self.boton4.setText(_translate("MainWindow", "Ayuda"))
        self.label.setText(_translate("MainWindow", "Elegir producto a ensamblar:"))
        self.boton5.setText(_translate("MainWindow", "Exportar HTML"))
        self.boton6.setText(_translate("MainWindow", "Guardar grafo"))
        self.label_2.setText(_translate("MainWindow", "Elegir simulación a ejecutar:"))
        self.nombre.setText(_translate("informacion","Información de Producción:"))
        

    def read_file(self):
        buscar = QFileDialog.getOpenFileName()
        print(buscar[0])
        mytree = ET.parse(buscar[0])
        myroot = mytree.getroot()
        self.file=myroot
        self.datosM(self.file)

        self.combo.addItem('-')
        aux=self.productos.first
        while aux:
            self.combo.addItem(aux.dato.getNombre())
            aux=aux.next
        msj = QMessageBox()
        msj.setWindowTitle('Información')
        msj.setText('Datos cargados correctamente')
        msj.exec()

    def read_fileS(self):
        buscar = QFileDialog.getOpenFileName()

        mytree = ET.parse(buscar[0])
        myroot = mytree.getroot()
        self.fileS=myroot

        self.datosS(self.fileS,self.simulaciones)

        self.combo2.clear()
        self.combo2.addItem('-')
        aux=self.simulaciones.first
        while aux:
            self.combo2.addItem(aux.dato.getId())
            aux=aux.next
        
        msj = QMessageBox()
        msj.setWindowTitle('Información')
        msj.setText('Datos cargados correctamente')
        msj.exec()

    def datosM(self,file):
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

        self.maquina=principal
        self.productos=productos

    def datosS(self,file,sim):
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
        
        self.simulaciones=sim

    def fabricar(self,nombre,maquina,productos):
        ensamble=''

        aux = productos.first
        while aux:
            if aux.dato.getNombre()==nombre:
                ensamble=aux.dato.getEnsamblaje()
                aux.dato.Graphviz()
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
                                        t+=int(L.dato.getTiempo())
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
                                t+=int(L.dato.getTiempo())
                                temp.append(acciones(t,'Esperar',''))

                                t+=int(L.dato.getTiempo())
                                temp.append(acciones(t,'Ensamblar',C.dato))
                            else:
                                if com.dato[-1]<com.preview.dato and pos==ensamble.size:
                                    t+=int(L.dato.getTiempo())
                                    temp.append(acciones(t,'Esperar',''))

                                    t+=int(L.dato.getTiempo())
                                    temp.append(acciones(t,'Ensamblar',C.dato))
                                else:
                                    t+=int(L.dato.getTiempo())
                                    temp.append(acciones(t,'Esperar',''))
                                    if t<Taux:
                                        t+=int(L.dato.getTiempo())
                                        temp.append(acciones(t,'Esperar',''))

                                        t+=int(L.dato.getTiempo())
                                        temp.append(acciones(t,'Ensamblar',C.dato))
                                    else:
                                        t+=int(L.dato.getTiempo())
                                        temp.append(acciones(t,'Ensamblar',C.dato))
                        elif esp==-1:
                            t+=int(L.dato.getTiempo())
                            temp.append(acciones(t,'Ensamblar',C.dato))

                            t+=int(L.dato.getTiempo())
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
                        t+=int(L.dato.getTiempo())
                        i+=1
                elif actual > comparador:
                    count=actual-comparador
                    i=1
                    t=L.dato.getTpro()
                    while i<=count:
                        L.next.dato.getMoves().append(acciones(t,'Esperar',''))
                        t+=int(L.dato.getTiempo())
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

    def fabricar_producto(self):
        if self.combo.currentText()!='-':
            self.boton6.setEnabled(True)
            self.boton5.setEnabled(True)
            self.boton3.setEnabled(True)
            aux=self.productos.first

            while aux:
                if aux.dato.getNombre()==self.combo.currentText():
                    self.datosM(self.file)
                    self.fabricar(aux.dato.getNombre(),self.maquina,self.productos)
                aux=aux.next

            self.nombreP.setVisible(True)
            _translate = QtCore.QCoreApplication.translate
            self.nombreP.setText(_translate("informacion","Nombre del Producto: "+str(self.combo.currentText())))
        
            self.tableView.setColumnCount(self.maquina.size+1)
            titulos=["Tiempo"]

            self.imagen.setVisible(True)
            img=QtGui.QImage(self.combo.currentText()+".png")
            pixmap=QtGui.QPixmap.fromImage(img).scaled(525,200)
            self.imagen.setPixmap(pixmap)

            L=self.maquina.first
            while L:
                titulos.append('Linea '+L.dato.getId())
                L=L.next
            self.tableView.setHorizontalHeaderLabels(titulos)
            self.tableView.clearContents()

            tiempoA=self.maquina.first.dato.getMoves().last
            tiempo=tiempoA.dato.getTiempo()
            self.Tiempo.setVisible(True)
            self.Tiempo.setText(_translate("informacion","Tiempo total de producción: "+str(tiempo)+" s"))
            self.Ensamble.setVisible(True)
            self.Ensamble.setText(_translate("informacion","Linea de Ensamblaje: "))

            L=self.maquina.first
            T=L.dato.getMoves().size
            x=1
            fila=0
            while x<=T:
                pro=L.dato.getMoves().first
                columna=0
                self.tableView.insertRow(fila)
                dato=QTableWidgetItem(str(pro.dato.getTiempo())+' s')
                self.tableView.setItem(fila,columna,dato)
                columna+=1
                while L:
                    pro=L.dato.getMoves().first
                    celda=pro.dato.getAccion()+' - '+pro.dato.getComponente()
                    dato=QTableWidgetItem(str(celda))
                    self.tableView.setItem(fila,columna,dato)
                    columna+=1
                    L.dato.getMoves().delete()
                    L=L.next
                columna=0
                fila+=1
                L=self.maquina.first
                x+=1
            
        else:
            self.nombreP.setVisible(False)
            self.tableView.clearContents()
            self.Tiempo.setVisible(False)
            self.Ensamble.setVisible(False)
            self.imagen.setVisible(False)
            self.boton6.setEnabled(False)
            self.boton5.setEnabled(False)
            self.boton3.setEnabled(False)

    def exportar_html(self):
        if self.combo.currentText()!='-':
            aux=self.productos.first
            while aux:
                if aux.dato.getNombre()==self.combo.currentText():
                    self.datosM(self.file)
                    self.fabricar(aux.dato.getNombre(),self.maquina,self.productos)
                    self.html(aux.dato.getNombre())
                aux=aux.next
            msj = QMessageBox()
            msj.setWindowTitle('Información')
            msj.setText('Archivo creado correctamente')
            msj.exec()
            startfile('Reporte '+self.combo.currentText()+'.html')
        
    def html(self,nombre):
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

        L=self.maquina.first
        while L:
            if L.dato.getId()==self.maquina.last.dato.getId():
                contenido+='<th style="border-top-right-radius: 20px;">Linea '+L.dato.getId()+'</th>'
            else:
                contenido+='<th>Linea '+L.dato.getId()+'</th>'
            L=L.next
        contenido+='</tr>'
        contenido+='</thead>'
        
        L=self.maquina.first
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
            L=self.maquina.first
            x+=1

        contenido+='''</table>
                    </div>
                    </body>
                    </html>'''

        file.write(contenido)
        file.close()

    def guardar_grafo(self):
        startfile(self.combo.currentText()+'.png')

    def exportar_xml(self):
        if self.combo.currentText()!='-':
            aux=self.productos.first
            while aux:
                if aux.dato.getNombre()==self.combo.currentText():
                    self.datosM(self.file)
                    self.fabricar(aux.dato.getNombre(),self.maquina,self.productos)
                    self.xml(aux.dato.getNombre())
                aux=aux.next
            msj = QMessageBox()
            msj.setWindowTitle('Información')
            msj.setText('Archivo creado correctamente')
            msj.exec()
            startfile('Salida_'+self.combo.currentText()+'.xml')

    def xml(self,dato):
        raiz=ET.Element('SalidaSimulacion')
    
        listadoP=ET.SubElement(raiz,'ListadoProductos')

        product=ET.SubElement(listadoP,'Producto')
        nombre=ET.SubElement(product,'Nombre')
        nombre.text=dato

        L=self.maquina.first
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
            
            L=self.maquina.first
            x+=1
        
        doc = ET.ElementTree(raiz)
        guardar='Salida_'+dato+'.xml'
        try:
            doc.write(guardar) 
        except IOError as e:
            print(e)

    def exportar_htmlS(self):
        if self.combo2.currentText()!='-':
            aux=self.simulaciones.first
            switch=False
            while aux:
                if aux.dato.getId()==self.combo2.currentText():
                    aux2=aux.dato.getProductos().first
                    while aux2:
                        self.datosM(self.file)
                        self.fabricar(aux2.dato,self.maquina,self.productos)
                        self.htmlS(aux.dato,aux2.dato,'Reporte '+aux.dato.getId()+'.html',switch)
                        self.datosM(self.file)
                        self.fabricar(aux2.dato,self.maquina,self.productos)
                        self.xmlS(aux.dato,aux2.dato,aux.dato.getId()+'.xml',switch)
                        switch=True
                        aux2=aux2.next
                    switch=False
                aux=aux.next

        msj = QMessageBox()
        msj.setWindowTitle('Información')
        msj.setText('Archivo creado correctamente')
        msj.exec()
        startfile('Reporte '+self.combo2.currentText()+'.html')
        startfile(self.combo2.currentText()+'.xml')
        
    def htmlS(self,datoS,dato,archivo,switch):
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

            L=self.maquina.first
            while L:
                if L.dato.getId()==self.maquina.last.dato.getId():
                    contenido+='<th style="border-top-right-radius: 20px;">Linea '+L.dato.getId()+'</th>'
                else:
                    contenido+='<th>Linea '+L.dato.getId()+'</th>'
                L=L.next
            contenido+='</tr>'
            contenido+='</thead>'
        
            L=self.maquina.first
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
                L=self.maquina.first
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
            file=open('Reporte '+datoS.getId()+'.html','w')
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
                                Reporte de '''+datoS.getId()+''' 
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

            L=self.maquina.first
            while L:
                if L.dato.getId()==self.maquina.last.dato.getId():
                    contenido+='<th style="border-top-right-radius: 20px;">Linea '+L.dato.getId()+'</th>'
                else:
                    contenido+='<th>Linea '+L.dato.getId()+'</th>'
                L=L.next
            contenido+='</tr>'
            contenido+='</thead>'
        
            L=self.maquina.first
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
                L=self.maquina.first
                x+=1

            contenido+='''</table>
                    </div>
                    </body>
                    </html>'''

            file.write(contenido)
            file.close()

    def xmlS(self,datoS,dato,archivo,switch):
        if switch:
            mytree = ET.parse(archivo)
            myroot = mytree.getroot()

            product=ET.Element('Producto')
            nombre=ET.SubElement(product,'Nombre')
            nombre.text=dato

            L=self.maquina.first
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
            
                L=self.maquina.first
                x+=1
        
            myroot.append(product)
            doc=ET.ElementTree(myroot)
            guardar=datoS.getId()+'.xml'
            doc.write(guardar)

        else:
            raiz=ET.Element('SalidaSimulacion')
            N=ET.SubElement(raiz,'Nombre')
            N.text=datoS.getId()

            listadoP=ET.SubElement(raiz,'ListadoProductos')

            product=ET.SubElement(listadoP,'Producto')
            nombre=ET.SubElement(product,'Nombre')
            nombre.text=dato

            L=self.maquina.first
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
            
                L=self.maquina.first
                x+=1

            doc = ET.ElementTree(raiz)
            guardar=datoS.getId()+'.xml'
            try:
                doc.write(guardar) 
            except IOError as e:
                print(e)

    def soporte(self):
        ventana = QDialog()
        ventana.setWindowTitle("Soporte")
        ventana.resize(400,500)
        
        info = QtWidgets.QLabel(ventana)
        info.setGeometry(QtCore.QRect(0,0, 400, 500))
        info.setObjectName("soporte")

        img=QtGui.QImage("soporte.png")
        pixmap=QtGui.QPixmap.fromImage(img).scaled(400,500)
        info.setPixmap(pixmap)

        ventana.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
