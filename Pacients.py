#AUTOR -> Rubén Mansanet 2on DAM SEMI
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import re
SCREEN_W = 600
SCREEN_H = 500

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulari Pacients")
        self.setFixedSize(SCREEN_W, SCREEN_H)

        
        #Creem els camps del registre
        #nom
        labelName = QLabel(self)
        labelName.setText("Nom:")
        labelName.move(15,50)
        self.nameField = QLineEdit(self)
        self.nameField.move(60, 50)
        self.nameField.setMaxLength(20)
        self.nameField.setPlaceholderText("Escriu el teu nom")
        
        #dni
        labelDni = QLabel(self)
        labelDni.setText("DNI:")
        labelDni.move(15,100)
        self.dniField = QLineEdit(self)
        self.dniField.move(60,100)
        self.dniField.setMaxLength(10)
        self.dniField.setPlaceholderText("Escriu el teu DNI")

        #sexe
        labelsexe = QLabel(self)
        labelsexe.setText("Sexe:")
        labelsexe.move(15, 150)
        boxSexeMasculi = QRadioButton("Masculí", self)
        boxSexeMasculi.move(60, 150)
        boxSexeFemeni = QRadioButton("Femení", self)
        boxSexeFemeni.move(140, 150)
        boxSexeIndeterminat = QRadioButton("Indeterminat", self)
        boxSexeIndeterminat.setChecked(True)
        boxSexeIndeterminat.move(220, 150)

        #edat
        labelEdat = QLabel(self)
        labelEdat.setText("Edat:")
        labelEdat.move(15, 200)
        edatField = QComboBox(self) 
        edatField.setFixedWidth(120)
        edatField.move(60, 200)
        llistaEdat = ["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90","90-100"]
        edatField.addItems(llistaEdat)

        #altura
        labelAltura = QLabel(self)
        labelAltura.setText("Altura:")
        labelAltura.move(15, 250)
        alturaField = QComboBox(self)
        alturaField.setFixedWidth(120)
        alturaField.move(60, 250)
        llistaAltura = []
        for alt in range(90,121):
            llistaAltura.append(alt)
        
        for i in llistaAltura:
            valor = str(i)
            alturaField.addItem(valor)
        

        #pes
        labelPes = QLabel(self)
        labelPes.setText("Pes:")
        labelPes.move(15, 300)
        pesField = QComboBox(self)
        pesField.setFixedWidth(120)
        pesField.move(60, 300)
        llistaPes = []
        for pes in range(45,126):
            llistaPes.append(float(pes))

        for i in llistaPes:
            valor = str(i)
            pesField.addItem(valor)
        


        #Creem el botó de registrar
        self.btn_registrar = QPushButton("Registrar", self)
        self.btn_registrar.setMaximumWidth(100)
        self.btn_registrar.setMaximumHeight(50)
        self.btn_registrar.move(30, 350)

        #activa el botó de registrar mentres les dades dels camps nom i dni son correctes
        while self.valida_nom() and self.valida_dni():
            print("Funcio de comprobar correcte")
            self.btn_registrar.setDisabled(False)
        
        
        #senyals
        self.nameField.textChanged.connect(self.valida_nom)
        self.dniField.textChanged.connect(self.valida_dni)
        self.btn_registrar.clicked.connect(self.guardar_dades)
            

#funcions  

    def valida_nom(self):
        self.nameValue = []
        self.nameValue = self.nameField.text().split(" ")
        if (len(self.nameValue[0]) <= 2) or (len(self.nameValue[1]) <= 2):
            return False
        elif (len(self.nameValue[0]) > 2) and (len(self.nameValue[1]) > 2):
            return True
        

    
    def valida_dni(self):
        if (re.match('\d{8}[a-zA-Z]$', self.dniField.text())):
            return True
        else:
            return False
        

    def guardar_dades(self):
        if self.valida_nom() and self.valida_dni():            
            fitxer = open("registre.txt", "a")
            fitxer.write("\n")
            fitxer.write(self.nameField.text())
            fitxer.write("\n")
            fitxer.write(self.dniField.text())
            print("Registre correcte")
        else:
            print("Les dades insertades no son correctes")
        self.nameField.clear()
        self.dniField.clear()



if __name__ == '__main__':
    app = QApplication()
    main_window = MainWindow()
    main_window.show()
    app.exec()