#!/usr/bin/env python3

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

 

from SubTitle import SubTitle
 
import sys

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (QMainWindow, QAction, QFileDialog, QCheckBox, QLineEdit)

from PyQt5.QtWidgets import (QApplication, QGridLayout, QDialog,  
        QMenu, QPushButton, QRadioButton, QVBoxLayout,QHBoxLayout, QWidget, QButtonGroup, QAbstractButton, QLabel)


from PyQt5.QtGui import (QIcon, QFont)

from math import floor

count = 1


class SubTitleMain(QMainWindow):
    
    """ The main OSC player tning """
    
    glayout = QGridLayout()
        
    def __init__(self, directory):
        
        super().__init__()
        
        self.tmpID = 0
        
        self.initUI()
        
        self.t_rel  = 0
        self.last_t = 0
    
    
        self.fs = 0;
    
        self.SubTitleObjects = []
        
        self.textboxes = []
 
        args.dir     = 0;
                
        self.panoramixOSCclient = udp_client.SimpleUDPClient("127.0.0.1", 4002)        
        self.wonderOSCclient    = udp_client.SimpleUDPClient("192.168.3.1", 58100)


        self.directory = directory

        self.openProject()
       
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
        #self.glayout.addWidget(self.b);

        self.jacktimeBox = QLineEdit(self)  
        self.jacktimeBox.setReadOnly(1);
        #self.glayout.addWidget(self.jacktimeBox);
         
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


        
            
        #self.directory = "../PREP"

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
        
 
                
        # b.clicked.connect(self.Button)
        
        box1 = QVBoxLayout()
        
        l1   = QLabel()                    
        font = QFont('Courier', 22, QFont.Bold)
        l1.setText(label+':')        
        l1.setFont(font)        


        tmpBox = QLineEdit(self)
        font   = QFont('Courier', 18, QFont.Bold)
        tmpBox.setFont(font)
        
        
        
        
        tmpBox.setAutoFillBackground(True)
        p2 = tmpBox.palette()
        p2.setColor(tmpBox.backgroundRole(), Qt.black)
        p2.setColor(tmpBox.foregroundRole(), Qt.green)
        tmpBox.setPalette(p2)
        
      
        box1.addWidget(l1)
        box1.addWidget(tmpBox)




        self.textboxes.append(tmpBox)
        
        y = floor((count-1) / 3) *2
 
        self.glayout.addWidget(l1,      y, (count-1) % 3)
        self.glayout.addWidget(tmpBox,  y+1, (count-1) % 3)

        self.glayout.widget
                
        #self.textbox.clear();
        
###############################################################################################
# 
    """ ACID """

    def JackClocker(self):
    
        t_start = time.time();

        while 1:
                    
            self.t_rel = time.time() - t_start
  
                        
            if self.t_rel != self.last_t:
# 
                 
                
                self.jacktimeBox.setText('%.2f' % (self.t_rel));
                
                
                cnt = 0
                for i in self.SubTitleObjects:
                                  
                    if i.state=="R":
    
                       tmpSTR =  i.JackPosChange(self.t_rel, self)    
                       
                       self.textboxes[cnt].setText(tmpSTR)
                        
                       cnt +=1
                         
                self.last_t = self.t_rel;    
        
            time.sleep(0.02)          
   
      
###############################################################################################
# 
   
if __name__ == "__main__":
    
          
    parser = argparse.ArgumentParser()        
      
    parser.add_argument("--dir",
                          default =".",help="path for prepared subtitle files")
    
    args = parser.parse_args()

    
    app = QApplication(sys.argv)
    ex = SubTitleMain(args.dir)
    sys.exit(app.exec_())