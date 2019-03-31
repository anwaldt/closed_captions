import argparse
import jack
import os
import time

import threading
import _thread

from os import listdir
from os.path import isfile, join

from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client
from pythonosc import osc_message_builder as omb


from JackTime import JackTime

from SubTitle import SubTitle
 
from PlotWindow import PlotWindow

import sys

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (QMainWindow, QAction, QFileDialog, QCheckBox, QLineEdit)

from PyQt5.QtWidgets import (QApplication, QGridLayout, QGroupBox,QDialog, QSlider, 
        QMenu, QPushButton, QRadioButton, QVBoxLayout,QHBoxLayout, QWidget, QButtonGroup, QAbstractButton, QLabel)


from PyQt5.QtGui import (QIcon, QPixmap, QFont)

 

count = 1


class SubTitleMain(QMainWindow):
    
    """ The main OSC player tning """
    
    glayout = QGridLayout()
        
    def __init__(self, directory):
        
        super().__init__()
        
        self.tmpID = 0
        
        self.initUI()
        
        self.jackPos      = 0
        self.last_jackPos = 0
    
    
        self.fs = 0;
    
        self.SubTitleObjects = []
        
        self.textboxes = []
 
        args.dir     = 0;
                
        self.panoramixOSCclient = udp_client.SimpleUDPClient("127.0.0.1", 4002)        
        self.wonderOSCclient    = udp_client.SimpleUDPClient("192.168.3.1", 58100)


        self.directory = directory

        self.openProject()
        
        
          
        self.jack_client = jack.Client('osc-player')
        self.jack_client.activate();
        
        self.fs = self.jack_client.samplerate;
        
        #_thread.start_new_thread( JackTime, () )
         
       
        t = threading.Thread(target=self.JackClocker)
             
        t.start()


        
    def initUI(self):  
                
        
        #self.setWindowIcon(QIcon('graphics/TU-Berlin-Logo.svg'))
        
        
        
    # Optional, resize window to image size
     
        
        #--------- MENU --------------------------------------------------

 
        self.statusBar()

        openDirectory = QAction(QIcon('open.png'), 'Open', self)
        openDirectory.setShortcut('Ctrl+O')
        openDirectory.setStatusTip('Select Directory for loading project')
        openDirectory.triggered.connect(self.openProject)
        
        
        newDirectory = QAction(QIcon('open.png'), 'New', self)
        newDirectory.setShortcut('Ctrl+O')
        newDirectory.setStatusTip('Chose Directory for creating new project')
        newDirectory.triggered.connect(self.newProject)

    

        menubar = self.menuBar()
        
        fileMenu = menubar.addMenu('&Project')
        fileMenu.addAction(openDirectory)       
        fileMenu.addAction(newDirectory)      
        
    
       
        
        
        
         #--------- BUTTONS on left  --------------------------------------------------
 
 
        
        
        self.b = QCheckBox("Connected?")
        #self.b.stateChanged.connect(self.clickBox)
        self.glayout.addWidget(self.b);

        self.jacktimeBox = QLineEdit(self)  
        self.jacktimeBox.setReadOnly(1);
        self.glayout.addWidget(self.jacktimeBox);
         
        #--------- window setup --------------------------------------------------
 
        
        
    
        wid = QWidget(self)        
        self.setCentralWidget(wid)

            
        self.setGeometry(300, 300, 1900, 1000)
        self.setWindowTitle('OSCollect')
        self.show()
        wid.setLayout(self.glayout)

 
                        
     
###############################################################################################
# 
        
               

###############################################################################################
# 
        
    def openProject(self):


        
            
        self.directory = "../PREP"

        global count
    
        
    
        oscFiles = [f for f in listdir(self.directory) if isfile(join(self.directory, f))]

        #--------- create objects, first --------------------------------------------------


        for f in oscFiles:
            
                  
            
            oscFile = self.directory.__add__("/").__add__(f);
            
            print(oscFile)
            
            print(str(count))
            
            
            [label, j] = f.split(".")
            
            self.Add(count, label);
            
            count += 1

        #--------- load data --------------------------------------------------

        count = 0
        
               

        for f in oscFiles:  
            
                        
            oscFile = self.directory.__add__("/").__add__(f);

                
            self.SubTitleObjects[count].LoadFile(oscFile)
            
            count +=1

###############################################################################################
#  

    def newProject(self):   

        fname = QFileDialog.getExistingDirectory(self, 'Select directory')

        if fname[0]:
            args.dir = fname[0], 'r' 
                
               

###############################################################################################
# 
            
    def showdialog():
       d = QDialog()
       b1 = QPushButton("ok",d)
       b1.move(50,50)
       d.setWindowTitle("Dialog")
       #d.setWindowModality(Qt.ApplicationModal)
       d.exec_()


###############################################################################################


    def Add(self, oscFile, label):
        
        global count
             
        self.SubTitleObjects.append(SubTitle(count, label))
        
        

        if 0 < count <= 16:
            yoff = 0
            xoff = 0
            
        elif 16 < count <= 32:
            yoff  = 4
            xoff  = 16
            
        elif 32 < count <= 48:
            yoff  = 8
            xoff  = 32
            
        elif 48 < count :
            yoff  = 12
            xoff  = 48
                
        #b.clicked.connect(self.Button)
        
        l1 = QLabel()
        l1.setText(label)
            
        font= QFont('Courier', 22, QFont.Bold)
        
        l1.setFont(font)
        
        self.glayout.addWidget(l1,      0+yoff,count-xoff)

        
        tmpBox = QLineEdit(self)
        font= QFont('Courier', 18, QFont.Bold)
        tmpBox.setFont(font)
        
        tmpBox.setAutoFillBackground(True)
        p2 = tmpBox.palette()
        p2.setColor(tmpBox.backgroundRole(), Qt.black)
        p2.setColor(tmpBox.foregroundRole(), Qt.green)

        tmpBox.setPalette(p2)

        self.textboxes.append(tmpBox)
        
       
        self.glayout.addWidget(tmpBox,1+yoff,count-xoff)

        self.glayout.widget
                
        #self.textbox.clear();
        
###############################################################################################
# 
    """ ACID """

    def JackClocker(self):
    
        print("Connecting to Jack server!")

        while 1:
                       
            self.jackPos = self.jack_client.transport_frame
                        
            if self.jackPos != self.last_jackPos:
# 
                Tsec = self.jackPos / self.fs;
                
                self.jacktimeBox.setText('%.2f' % (Tsec));
                
                
                cnt = 0
                for i in self.SubTitleObjects:
                                  
                    if i.state=="R":
 
                            
                       tmpSTR =  i.JackPosChange(Tsec, self)    
                       
                       #self.textbox.setText(tmpSTR)
                       
                       self.textboxes[cnt].setText(tmpSTR)
                        
                       cnt +=1
                         
                self.last_jackPos = self.jackPos;    
        
            time.sleep(0.002)          
   

   
        
        
###############################################################################################
# 
   
if __name__ == "__main__":
    
          
    parser = argparse.ArgumentParser()        
      
    parser.add_argument("--dir",
                          default =".",help="path for prepared subtitle files")
    
    args = parser.parse_args()

    
    app = QApplication(sys.argv)
    ex = SubTitleMain(dir)
    sys.exit(app.exec_())