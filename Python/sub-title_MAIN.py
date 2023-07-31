#!/usr/bin/env python3

import argparse
#import jack
import os
import time

import threading
import _thread

from os import listdir
from os.path import isfile, join

#from pythonosc import dispatcher
#from pythonosc import osc_server
#from pythonosc import udp_client
#from pythonosc import osc_message_builder as omb

 
from SubTitle import SubTitle
 
import sys

from PyQt5.QtCore import (Qt)

from PyQt5.QtWidgets import (QMainWindow, QAction, QFileDialog, QCheckBox, QLineEdit, QTextEdit, QSpacerItem, QSizePolicy)

from PyQt5.QtWidgets import (QApplication, QGridLayout, QDialog,  
        QMenu, QPushButton, QRadioButton, QVBoxLayout,QHBoxLayout, QWidget, QButtonGroup, QAbstractButton, QLabel)


from PyQt5.QtGui import (QIcon, QFont)

from math import floor



count = 1


class SubTitleMain(QMainWindow):
    
    """ The main OSC player tning """
    
    glayout = QGridLayout()
        
    def __init__(self, file_list):
        
        super().__init__()
        
        self.timeScale = 0.8

        
        self.tmpID = 0
        
        self.initUI()
        
        self.t_rel  = 0
        self.last_t = 0
    
        self.is_playing = 0
    
        self.fs = 0;
    
        self.SubTitleObjects = []
        
        self.textboxes = []
 
        args.dir     = 0;
                
        #self.panoramixOSCclient = udp_client.SimpleUDPClient("127.0.0.1", 4002)        
        #self.wonderOSCclient    = udp_client.SimpleUDPClient("192.168.3.1", 58100)


        #self.directory = directory
        
        self.file_list = file_list

        self.openProject()
       
        t = threading.Thread(target=self.clocker)
             
        t.start()

        self.show 
        #self.showFullScreen()
        
    def initUI(self):  
                

        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)
        
        
         #--------- BUTTONS on left  --------------------------------------------------
  
    
        #self.glayout.addWidget(self.jacktimeBox);
         
        #--------- window setup --------------------------------------------------
 
        wid = QWidget(self)        
        self.setCentralWidget(wid)

            
        self.setGeometry(300, 300, 1800, 900)
        self.setWindowTitle('Closed Captions')
        self.show()
        wid.setLayout(self.glayout)
        self.glayout.setVerticalSpacing(5)
  
 
        self.pBut =  QPushButton("Play")
        self.glayout.addWidget(self.pBut)        
        self.pBut.clicked.connect(self.handle_playbutton)
        self.glayout.addWidget(self.pBut,  0, 0)       
        
        self.sBut =  QPushButton("Stop")
        self.glayout.addWidget(self.sBut)     
        self.sBut.clicked.connect(self.handle_stopbutton)

        self.glayout.addWidget(self.sBut,  0, 2)  
        
        #self.rBut =  QPushButton("Reset")
        #self.glayout.addWidget(self.rBut)     
        #self.glayout.addWidget(self.rBut,  0, 2)  
        
        
        
        self.jacktimeBox = QLabel(self)
        
        
        font = QFont('Courier', 33, QFont.Bold) 
        self.jacktimeBox.setFont(font) 
        
        p2 = self.jacktimeBox.palette()
        p2.setColor(self.jacktimeBox.foregroundRole(), Qt.yellow)
        self.jacktimeBox.setPalette(p2)
        
        #self.jacktimeBox.setReadOnly(1);
        self.glayout.addWidget(self.jacktimeBox,  1, 1)  

        #self.pBut.clicked.connect(self.handleAddButton)
        
        
        
        
        
    def handle_playbutton(self):
        
        self.t_start = time.time();
        self.is_playing = 1
        
        
            
        
    def handle_stopbutton(self):
        
        #self.t_start = time.time();
        self.is_playing = 0  
        
        cnt=0
        for i in self.SubTitleObjects:
                                       
            self.textboxes[cnt].setText(' ')
                            
            cnt +=1
         
###############################################################################################
# 
         
    def openProject(self):
 
        global count
             
        xmlFiles   = []

        with open(self.file_list, "r+") as f:

                data = f.readlines()

                for line in data:
                    xmlFiles.append(line.replace('\n', ''))
             
        #xmlFiles = [f for f in listdir(self.directory) if isfile(join(self.directory, f))]

        #--------- create objects, first --------------------------------------------------


        for f in xmlFiles:
            
            #oscFile = self.directory.__add__("/").__add__(f);
            oscFile = f
            
            print(str(count)+': '+oscFile)            
            

            label = os.path.splitext(os.path.basename(oscFile))[0]  

#            [label, j] = f.split(".")
            
            self.Add(count, label);
            
            count += 1

        #--------- load data --------------------------------------------------

        count = 0

        for f in xmlFiles:                                      
            
#            oscFile = f #self.directory.__add__("/").__add__(f);
            

            self.SubTitleObjects[count].LoadFile(f)
            
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
        
      
        box1 = QVBoxLayout()
        
        l1   = QLabel()                    
        font = QFont('Courier', 30, QFont.Bold)
        l1.setText(label+':')        
        l1.setFont(font)        
        p2 = l1.palette()
        p2.setColor(l1.foregroundRole(), Qt.white)
        l1.setPalette(p2)

        tmpBox = QLabel()
        font   = QFont('Courier', 30, QFont.Bold)
        tmpBox.setFont(font)
        tmpBox.setWordWrap(True)
        tmpBox.setFixedSize(400, 250)
                
        tmpBox.setAutoFillBackground(True)
        p2 = tmpBox.palette()
        p2.setColor(tmpBox.backgroundRole(), Qt.black)
        p2.setColor(tmpBox.foregroundRole(), Qt.green)
        tmpBox.setPalette(p2)
        
      
        box1.addWidget(l1)
        box1.addWidget(tmpBox)




        self.textboxes.append(tmpBox)
        
        y = floor((count-1) / 3) *3
 
        self.glayout.addWidget(l1,      y+2, (count-1) % 3)
        self.glayout.addWidget(tmpBox,  y+3, (count-1) % 3)
            
        
        verticalSpacer = QSpacerItem(10, 10,1, QSizePolicy.Expanding)
        
        self.glayout.addItem(verticalSpacer,  y+4, (count-1) % 3)


        self.glayout.widget
                
        #self.textbox.clear();
        
###############################################################################################
# 
    """ ACID """

    def clocker(self):
    
        

        while 1:
            
            if self.is_playing == 1:
            
                self.t_rel = time.time() - self.t_start
              
                if self.t_rel != self.last_t:
    # 
                    self.jacktimeBox.setText('%.2f' % (self.t_rel));
                            
                    cnt = 0
                    
                    for i in self.SubTitleObjects:
                                      
                        if i.state=="R":
        
                           tmpSTR =  i.JackPosChange(self.t_rel, self)    
                           
                           self.textboxes[cnt].setText(tmpSTR[0:len(tmpSTR)])
                            
                           cnt +=1
                             
                    self.last_t = self.t_rel;    
        
            time.sleep(0.02)          
   
      
###############################################################################################
# 
   
if __name__ == "__main__":
    
          
    parser = argparse.ArgumentParser()        
      
    #parser.add_argument("--dir",
    #                      default =".",help="path for prepared subtitle files")
    
    parser.add_argument("--file",
                          default =".",help="path to file list")
    
    args = parser.parse_args()

    
    app = QApplication(sys.argv)
    ex = SubTitleMain(args.file)
    sys.exit(app.exec_())
