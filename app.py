from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QFileDialog
import xml.etree.ElementTree as ET
from produccion import linea, producto,simulacion,acciones
from lista import dlinkedlist


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 866)
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
        self.boton4 = QtWidgets.QPushButton(self.centralwidget)
        self.boton4.setGeometry(QtCore.QRect(560, 20, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(14)
        self.boton4.setFont(font)
        self.boton4.setObjectName("boton4")
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
        self.informacion.setGeometry(QtCore.QRect(20, 160, 541, 691))
        self.informacion.setObjectName("informacion")
        self.boton5 = QtWidgets.QPushButton(self.informacion)
        self.boton5.setGeometry(QtCore.QRect(20, 630, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(16)
        self.boton5.setFont(font)
        self.boton5.setObjectName("boton5")
        self.boton6 = QtWidgets.QPushButton(self.informacion)
        self.boton6.setGeometry(QtCore.QRect(20, 570, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(16)
        self.boton6.setFont(font)
        self.boton6.setObjectName("boton6")
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
        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(570, 160, 531, 681))
        self.tableView.setObjectName("tableView")
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

    def fabricar_producto(self):
        aux=self.productos.first

        while aux:
            if aux.dato.getNombre()==self.combo.currentText():
                self.datosM(self.file)
                self.fabricar(aux.dato.getNombre(),self.maquina,self.productos)
            aux=aux.next

        self.tableView.setColumnCount(self.maquina.size+1)
        titulos=["Tiempo"]
        
        L=self.maquina.first
        while L:
            titulos.append('Linea '+L.dato.getId())
            L=L.next
        self.tableView.setHorizontalHeaderLabels(titulos)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
