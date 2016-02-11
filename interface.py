
import random
import time
import sys
from PyQt4 import QtGui, QtCore


#Code pour le 1e jeu

class Fenetre1(QtGui.QDialog):
    def __init__(self, temps, parent=None):
        super(Fenetre1, self).__init__(parent)

        msgBox = QtGui.QMessageBox()
        msgBox.setText('Votre temps : '+str(temps)+' secondes')
        msgBox.setInformativeText('Voulez vous rejouer ?')
        button_oui = QtGui.QPushButton('Oui')
        #button_oui.clicked.connect(self.reponse)
        button_non = QtGui.QPushButton('Non')
        #button_non.clicked.connect(self.reponse)
        msgBox.addButton(button_oui, QtGui.QMessageBox.YesRole)
        msgBox.addButton(button_non, QtGui.QMessageBox.NoRole)
        ret = msgBox.exec_();

        if msgBox.clickedButton() == button_oui:
            inter.initUI()
        elif msgBox.clickedButton() == button_non:
            je1.close()
            inter.close()



class MyButton(QtGui.QPushButton):
    def __init__(self, n, p):
        super().__init__("")
        self._position = p
        self.name = n
        #self.setGeometry(100,100,100,100)
        self.setFixedSize(100,100)
        #region = QtGui.QRegion(QtCore.QRect(0,30,0,30), QtGui.QRegion.Ellipse)
        #self.setMask(region)
        
    def position(self):
        return self._position

    def couleur(self):

        icones = ["banane.png", "ananas.png", "fraise.png", "cerise.png", "pomme.png", "raisin.png", "orange.png"]

        icon1 = QtGui.QIcon()
        pixmap = QtGui.QPixmap(icones[int(self.name)])
        icon1.addPixmap(pixmap,QtGui.QIcon.Normal, 
                                        QtGui.QIcon.On)
        self.setIconSize(QtCore.QSize(85,85))
        self.setIcon(icon1)

 
class MyButton2(QtGui.QPushButton):
    def __init__(self, n):
        super().__init__(n)
        self.setGeometry(3,3,3,3) 

class MyButton3(QtGui.QPushButton):
    def __init__(self, n, p):
        super().__init__("")
        self._position = p
        self.name = n
        self.setText(n)

class Jeu1(QtGui.QWidget):
    
    def __init__(self):
        super(Jeu1, self).__init__()
        
        self.matrice_clicks = [0 for i in range(49)]
        self.names = [str(random.randint(0,6)) for i in range(0, 49)]
        self.grid = QtGui.QGridLayout() 
        self.score = 0
        self.initUI()
        
    def initUI(self):
        
        self.setLayout(self.grid)
        self.temps_depart = time.time()
        
        positions = [(i,j) for i in range(7) for j in range(7)]
        
        for position, name in zip(positions, self.names):
            button = MyButton(name, position)
            button.setStyleSheet("font-size:40px;background-color:#ECECEC;\
        border: 0px solid #ECECEC")
            button.clicked.connect(self.clicks)
            button.clicked.connect(self.gravity_2)
            button.couleur()
            self.grid.addWidget(button, *position)


        
        button = MyButton3("Aide", (7,6))
        button.clicked.connect(self.Help)
        #button = MyButton("Go!", (7,0))
        self.grid.addWidget(button, *(7,6))
        label = QtGui.QLabel("Score :")
        #label.setText("Temps : ")
        self.grid.addWidget(label, *(7,0))
        label_score = QtGui.QLabel(str(self.score))
        label_score.setStyleSheet("font-size:40px;background-color:#ECECEC;\
        border: 0px solid #ECECEC")
        self.grid.addWidget(label_score, *(7,1))
            
        self.move(300, 150)
        self.setWindowTitle('Jeu')
        self.gravity_2()
        self.show()
        self.score = 0
        self.affiche_score()

    def fct_score(self):
        if self.score > 200:
            temps_arrivee = time.time() - self.temps_depart
            self.close()
            #On garde une précision au 10e de seconde
            temps_arrivee *= 10
            temps_arrivee = int(temps_arrivee)
            temps_arrivee /= 10
            fen = Fenetre1(temps_arrivee)


    def affiche_score(self):
        #removeWidget(self.label_score)
        #self.label_score = QtGui.QLabel(str(self.score))
        #self.grid.addWidget(self.label_score, *(7,1))
        label_score = QtGui.QLabel(str(self.score))
        label_score.setStyleSheet("font-size:40px;background-color:#ECECEC;\
        border: 0px solid #ECECEC")
        self.grid.addWidget(label_score, *(7,1))

    def clicks(self):

        (lig1, col1) = self.sender().position()
        self.matrice_clicks[7*lig1+col1] = 1
        
        # Maintenant on regarde tous les voisins pour voir si 1 n'a pas ete aussi selectionne

        lig2 = lig1
        col2 = col1
        booleen = True
        if(lig1<6 and self.matrice_clicks[(lig1+1)*7+col1] == 1) :
            lig2 = lig1 + 1
            self.matrice_clicks = [0 for i in range(49)]
            self.echange(lig1, lig2, col1, col2)
            booleen = False
        if(self.matrice_clicks[(lig1-1)*7+col1] == 1) :
            lig2 = lig1 - 1
            self.matrice_clicks = [0 for i in range(49)]
            self.echange(lig1, lig2, col1, col2)
            booleen = False
        if(col1<6 and self.matrice_clicks[lig1*7+(col1+1)] == 1) :
            col2 = col1 + 1
            self.matrice_clicks = [0 for i in range(49)]
            self.echange(lig1, lig2, col1, col2)
            booleen = False
        if(self.matrice_clicks[lig1*7+(col1-1)] == 1) :
            col2 = col1 - 1
            self.matrice_clicks = [0 for i in range(49)]
            self.echange(lig1, lig2, col1, col2)
            booleen = False
        #if((lig1 == 6 or self.matrice_clicks[(lig1+1)*7+col1] != 1) and (lig1 == 0 or self.matrice_clicks[(lig1-1)*7+col1] != 1) and (col1 == 6 or self.matrice_clicks[lig1*7+(col1+1)] != 1) and (col1 == 0 or self.matrice_clicks[lig1*7+(col1-1)] != 1)) :
        if booleen :
            self.matrice_clicks = [0 for i in range(49)]
            self.matrice_clicks[7*lig1+col1] = 1


    def echange(self, lig1, lig2, col1, col2):
        tmp1 = self.names[lig1*7+col1]
        tmp2 = self.names[lig2*7+col2]
        self.names[lig1*7+col1] = tmp2
        self.names[lig2*7+col2] = tmp1

        button = MyButton(self.names[lig1*7+col1], (lig1, col1))
        button.setStyleSheet("font-size:40px;background-color:#ECECEC;\
        border: 0px solid #ECECEC")
        button.clicked.connect(self.clicks)
        button.clicked.connect(self.gravity_2)
        button.couleur()
        self.grid.addWidget(button, *(lig1, col1))

        button = MyButton(self.names[lig2*7+col2], (lig2, col2))
        button.setStyleSheet("font-size:40px;background-color:#ECECEC;\
        border: 0px solid #ECECEC")
        button.clicked.connect(self.clicks)
        button.clicked.connect(self.gravity_2)
        button.couleur()
        self.grid.addWidget(button, *(lig2, col2))

        self.score -= 5
        self.affiche_score()
        self.fct_score()
        self.gravity_2()

    def alignes_lig(self):
        booleen = False
        for lig in range(0,7):
            for ind in range(0,5):
                booleen = (self.names[7*lig+ind] == self.names[7*lig+ind+1] and self.names[7*lig+ind+1] == self.names[7*lig+ind+2])
                if booleen :
                    break
            if booleen :
                break
        if booleen == False :
            (lig, ind) = (10,10)
        return (lig, ind)

    def alignes_col(self):
        for col in range(0,7):
            for ind in range(0,5):
                booleen = (self.names[7*ind+col] == self.names[7*(ind+1)+col] and self.names[7*(ind+1)+col] == self.names[7*(ind+2)+col])
                if booleen :
                    break
            if booleen :
                break
        if booleen == False :
            (ind, col) = (10,10)
        return (ind, col)


    def gravity_2(self):

        (lig, col) = self.alignes_lig()
        #s'il y a trois elements de la meme ligne alignes
        if(lig<9):
            #On regarde combien d'éléments sont alignés (s'il y en a plus que 3)

            c0 = col+2
            while(c0<7 and self.names[7*lig+col]==self.names[7*lig+c0]):
                c0 += 1
                self.score += 10
            for i in range(col, c0):
                self.un_cran_vers_le_bas(lig, i)


            self.score += 10
            self.affiche_score()
            self.fct_score()
            self.gravity_2()

        (lig, col) = self.alignes_col()
        #s'il y a trois elements de la meme colonne alignes
        if(lig<9):

            l0 = lig+2
            while(l0<7 and self.names[7*lig+col]==self.names[7*l0+col]):
                l0 += 1
                self.score += 10
            for i in range(lig, l0):
                self.un_cran_vers_le_bas(i, col)

            self.score += 10
            self.affiche_score()
            self.fct_score()
            self.gravity_2()

    def un_cran_vers_le_bas(self, lig, col):
        for i in range(0, lig):
            self.names[col+7*(lig-i)] = self.names[col+7*(lig-i-1)]
            button = MyButton(self.names[col+7*(lig-i)], (lig-i, col))
            button.setStyleSheet("font-size:40px;background-color:#ECECEC;\
        border: 0px solid #ECECEC")
            button.clicked.connect(self.gravity_2)
            button.clicked.connect(self.clicks)
            button.couleur()
            self.grid.addWidget(button, *(lig-i, col))
        #on attribue une nouvelle valeur a l'element tout en haut
        self.names[col] = str(random.randint(0,6))
        button = MyButton(self.names[col], (0, col))
        button.setStyleSheet("font-size:40px;background-color:#ECECEC;\
        border: 0px solid #ECECEC")
        button.clicked.connect(self.clicks)
        button.clicked.connect(self.gravity_2)
        button.couleur()
        self.grid.addWidget(button, *(0, col))
            
    def Help(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setText('Règles')
        msgBox.setInformativeText('La règle est simple : il faut aligner trois fruits identiques pour gagner le plus de points possible ! Vous ne pouvez déplacer un fruit seulement échangeant sa position avec celle de son voisin de droite, de gauche, d en haut ou en bas. Chaque déplacement vous coutera 5 points; faire disparaitre 3 fruits alignés vous rapportera 20 points. Si plus de 3 fruits sont alignés, vous gagnerez 10 points bonus par fruit supplémentaire. Le jeu se finit lorsque vous atteignez 200 points. Finissez le plus rapidement possible !' )
        ret = msgBox.exec_();
        


#Code pour le 2e jeu, très similaire


class Fenetre2(QtGui.QDialog):
    def __init__(self, temps, parent=None):
        super(Fenetre2, self).__init__(parent)

        msgBox = QtGui.QMessageBox()
        msgBox.setText('Votre score : '+str(temps))
        msgBox.setInformativeText('Voulez vous rejouer ?')
        button_oui = QtGui.QPushButton('Oui')
        #button_oui.clicked.connect(self.reponse)
        button_non = QtGui.QPushButton('Non')
        #button_non.clicked.connect(self.reponse)
        msgBox.addButton(button_oui, QtGui.QMessageBox.YesRole)
        msgBox.addButton(button_non, QtGui.QMessageBox.NoRole)
        ret = msgBox.exec_();

        if msgBox.clickedButton() == button_oui:
            inter.initUI()
        elif msgBox.clickedButton() == button_non:
            je2.close()
            inter.close()


class Jeu2(QtGui.QWidget):
    
    def __init__(self):
        super(Jeu2, self).__init__()
        
        self.matrice_clicks = [0 for i in range(49)]
        self.names = [str(random.randint(0,6)) for i in range(0, 49)]
        self.grid = QtGui.QGridLayout() 
        self.score = 0
        self.initUI()
        
    def initUI(self):
        
        self.setLayout(self.grid)
        self.temps_depart = time.time()
        
        positions = [(i,j) for i in range(7) for j in range(7)]
        
        for position, name in zip(positions, self.names):
            button = MyButton(name, position)
            button.setStyleSheet("font-size:40px;background-color:#ECECEC;\
        border: 0px solid #ECECEC")
            button.clicked.connect(self.clicks)
            button.clicked.connect(self.gravity_2)
            button.couleur()
            self.grid.addWidget(button, *position)


        
        button = MyButton3("Aide", (7,6))
        button.clicked.connect(self.Help)
        #button = MyButton("Go!", (7,0))
        self.grid.addWidget(button, *(7,6))
        label = QtGui.QLabel("Score :")
        self.grid.addWidget(label, *(7,0))
        #label.setText("Temps : ")
        label_score = QtGui.QLabel(str(self.score))
        label_score.setStyleSheet("font-size:40px;background-color:#ECECEC;\
        border: 0px solid #ECECEC")
        self.grid.addWidget(label_score, *(7,1))
            
        self.move(300, 150)
        self.setWindowTitle('Jeu')
        self.gravity_2()
        self.show()
        self.score = 0
        self.affiche_score()

    def fct_stop(self):
        temps_arrivee = time.time() - self.temps_depart
        if temps_arrivee > 60:
            self.close()
            fen = Fenetre2(self.score)


    def affiche_score(self):
        #removeWidget(self.label_score)
        #self.label_score = QtGui.QLabel(str(self.score))
        #self.grid.addWidget(self.label_score, *(7,1))
        label_score = QtGui.QLabel(str(self.score))
        label_score.setStyleSheet("font-size:40px;background-color:#ECECEC;\
        border: 0px solid #ECECEC")
        self.grid.addWidget(label_score, *(7,1))

    def clicks(self):

        (lig1, col1) = self.sender().position()
        self.matrice_clicks[7*lig1+col1] = 1
        
        # Maintenant on regarde tous les voisins pour voir si 1 n'a pas ete aussi selectionne

        lig2 = lig1
        col2 = col1
        booleen = True
        if(lig1<6 and self.matrice_clicks[(lig1+1)*7+col1] == 1) :
            lig2 = lig1 + 1
            self.matrice_clicks = [0 for i in range(49)]
            self.echange(lig1, lig2, col1, col2)
            booleen = False
        if(self.matrice_clicks[(lig1-1)*7+col1] == 1) :
            lig2 = lig1 - 1
            self.matrice_clicks = [0 for i in range(49)]
            self.echange(lig1, lig2, col1, col2)
            booleen = False
        if(col1<6 and self.matrice_clicks[lig1*7+(col1+1)] == 1) :
            col2 = col1 + 1
            self.matrice_clicks = [0 for i in range(49)]
            self.echange(lig1, lig2, col1, col2)
            booleen = False
        if(self.matrice_clicks[lig1*7+(col1-1)] == 1) :
            col2 = col1 - 1
            self.matrice_clicks = [0 for i in range(49)]
            self.echange(lig1, lig2, col1, col2)
            booleen = False
        #if((lig1 == 6 or self.matrice_clicks[(lig1+1)*7+col1] != 1) and (lig1 == 0 or self.matrice_clicks[(lig1-1)*7+col1] != 1) and (col1 == 6 or self.matrice_clicks[lig1*7+(col1+1)] != 1) and (col1 == 0 or self.matrice_clicks[lig1*7+(col1-1)] != 1)) :
        if booleen :
            self.matrice_clicks = [0 for i in range(49)]
            self.matrice_clicks[7*lig1+col1] = 1


    def echange(self, lig1, lig2, col1, col2):
        tmp1 = self.names[lig1*7+col1]
        tmp2 = self.names[lig2*7+col2]
        self.names[lig1*7+col1] = tmp2
        self.names[lig2*7+col2] = tmp1

        button = MyButton(self.names[lig1*7+col1], (lig1, col1))
        button.setStyleSheet("font-size:40px;background-color:#ECECEC;\
        border: 0px solid #ECECEC")
        button.clicked.connect(self.clicks)
        button.clicked.connect(self.gravity_2)
        button.couleur()
        self.grid.addWidget(button, *(lig1, col1))

        button = MyButton(self.names[lig2*7+col2], (lig2, col2))
        button.setStyleSheet("font-size:40px;background-color:#ECECEC;\
        border: 0px solid #ECECEC")
        button.clicked.connect(self.clicks)
        button.clicked.connect(self.gravity_2)
        button.couleur()
        self.grid.addWidget(button, *(lig2, col2))

        self.score -= 5
        self.affiche_score()
        self.fct_stop()
        self.gravity_2()

    def alignes_lig(self):
        booleen = False
        for lig in range(0,7):
            for ind in range(0,5):
                #print(self.names[7*lig+ind],self.names[7*lig+ind+1],self.names[7*lig+ind+2])
                booleen = (self.names[7*lig+ind] == self.names[7*lig+ind+1] and self.names[7*lig+ind+1] == self.names[7*lig+ind+2])
                if booleen :
                    break
            if booleen :
                break
        if booleen == False :
            (lig, ind) = (10,10)
        return (lig, ind)

    def alignes_col(self):
        for col in range(0,7):
            for ind in range(0,5):
                #print(self.names[7*lig+ind],self.names[7*lig+ind+1],self.names[7*lig+ind+2])
                #print(self.names[7*ind+col], self.names[7*(ind+1)+col], self.names[7*(ind+2)+col])
                booleen = (self.names[7*ind+col] == self.names[7*(ind+1)+col] and self.names[7*(ind+1)+col] == self.names[7*(ind+2)+col])
                if booleen :
                    break
            if booleen :
                break
        #print(ind, col)
        if booleen == False :
            (ind, col) = (10,10)
        return (ind, col)


    def gravity_2(self):

        (lig, col) = self.alignes_lig()
        #s'il y a trois elements de la meme ligne alignes
        if(lig<9):
            #On regarde combien d'éléments sont alignés (s'il y en a plus que 3)

            c0 = col+2
            while(c0<7 and self.names[7*lig+col]==self.names[7*lig+c0]):
                c0 += 1
                self.score += 10
            for i in range(col, c0):
                self.un_cran_vers_le_bas(lig, i)


            self.score += 10
            self.affiche_score()
            self.fct_stop()
            self.gravity_2()

        (lig, col) = self.alignes_col()
        #s'il y a trois elements de la meme colonne alignes
        if(lig<9):

            l0 = lig+2
            while(l0<7 and self.names[7*lig+col]==self.names[7*l0+col]):
                l0 += 1
                self.score += 10
            for i in range(lig, l0):
                self.un_cran_vers_le_bas(i, col)

            self.score += 10
            self.affiche_score()
            self.fct_stop()
            self.gravity_2()

    def un_cran_vers_le_bas(self, lig, col):
        for i in range(0, lig):
            self.names[col+7*(lig-i)] = self.names[col+7*(lig-i-1)]
            button = MyButton(self.names[col+7*(lig-i)], (lig-i, col))
            button.setStyleSheet("font-size:40px;background-color:#ECECEC;\
        border: 0px solid #ECECEC")
            button.clicked.connect(self.gravity_2)
            button.clicked.connect(self.clicks)
            button.couleur()
            self.grid.addWidget(button, *(lig-i, col))
        #on attribue une nouvelle valeur a l'element tout en haut
        self.names[col] = str(random.randint(0,6))
        button = MyButton(self.names[col], (0, col))
        button.setStyleSheet("font-size:40px;background-color:#ECECEC;\
        border: 0px solid #ECECEC")
        button.clicked.connect(self.clicks)
        button.clicked.connect(self.gravity_2)
        button.couleur()
        self.grid.addWidget(button, *(0, col))
            
    def Help(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setText('Règles')
        msgBox.setInformativeText('La règle est simple : il faut aligner trois fruits identiques pour gagner le plus de points possible ! Vous ne pouvez déplacer un fruit seulement échangeant sa position avec celle de son voisin de droite, de gauche, d en haut ou en bas. Chaque déplacement vous coutera 5 points; faire disparaitre 3 fruits alignés vous rapportera 20 points. Si plus de 3 fruits sont alignés, vous gagnerez 10 points bonus par fruit supplémentaire. Le jeu se finit au bout d une minute. Faites le plus de points possible !' )
        ret = msgBox.exec_();







class Interface(QtGui.QWidget):
    
    def __init__(self):
        super(Interface, self).__init__()
        self.grid = QtGui.QGridLayout() 
        self.initUI()
        
    def initUI(self):
        self.setLayout(self.grid)
        label = QtGui.QLabel("À quel jeu souhaitez-vous jouer ?")
        self.grid.addWidget(label, *(0,0))
        button = MyButton3("200 points", (1,0))
        button.setFixedSize(200,30)
        button.clicked.connect(self.lien1)
        self.grid.addWidget(button, *(1,0))
        button2 = MyButton3("Contre la montre", (1,1))
        button2.setFixedSize(200,30)
        button2.clicked.connect(self.lien2)
        self.grid.addWidget(button2, *(1,1))

        image = QtGui.QLabel(" ")
        pixmap = QtGui.QPixmap("banane.png")
        image.setPixmap(pixmap.scaled(50,50))
        self.grid.addWidget(image, *(0,1))

        self.show()

    def lien1(self):
        global je1
        je1 = Jeu1()
        je1.initUI()

    def lien2(self):
        global je2
        je2 = Jeu2()
        je2.initUI()



def main():
    global app
    app = QtGui.QApplication(sys.argv)
    global inter
    inter = Interface()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()