#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 14:59:13 2023

@author: anwaldt
"""

import os
from xml.etree.ElementTree import ElementTree


raw_dir  = "/media/anwaldt/ANWALDT_DATA/SOUND/PROJECTS/2020/Closed_Captions/closed_captions/RAW/TOS/S03/"
prep_dir = "/media/anwaldt/ANWALDT_DATA/SOUND/PROJECTS/2020/Closed_Captions/closed_captions/PREP/TOS/S03/"


####################################################################################################
#
####################################################################################################

def print_line(id, start, text):
    
    scaleFactor = 0.4*180000000
    
    start = int(start)
    
    printString = str(id)+"\t"+str(start/scaleFactor)+"\t"+text[1:-1]+"\n"

    #print()

    f.write(printString)

        

####################################################################################################
#
####################################################################################################


xmlFiles   = []

for filename in os.listdir(raw_dir):
    f = os.path.join(raw_dir, filename)
    # checking if it is a file
    xmlFiles.append(f)


####################################################################################################
#
####################################################################################################


for file in xmlFiles:
    
    try: 
        os.mkdir(prep_dir) 
    except OSError as error: 
        print(error) 
    
    #os.makedirs(prep_dir)

    basename = os.path.splitext(os.path.basename(file))[0] 
         
    f = open(prep_dir+basename+".sub", "w")

    tree = ElementTree()    
    tree.parse(file)    
    root = tree.getroot() 
    
    print_line(0, 0, "----")
    
        
    ## all caption elements
    for elem in root.iter('{http://www.w3.org/ns/ttml}p'):
        
        # grab start index and ommit "t":
        start = elem.attrib.get('begin')[0:-1]
        stop  = elem.attrib.get('end')[0:-1]
        text  = elem.text
        
        if text!=None:
            if text[0]=="(":
                if len(text)>1:
                    print_line(1, start,text)
                    print_line(0, stop,"----")
        
    
    # another format
    for elem in root.iter('{http://www.w3.org/2006/10/ttaf1}p'):
                    
        # grab start index and ommit "t":
        start = elem.attrib.get('begin')[0:-1]
        stop  = elem.attrib.get('end')[0:-1]
        text  = elem.text
        
        if text!=None:
            if  text[0]=="[" :
                if len(text)>1:
                    print_line(1, start,text)
                    print_line(0, stop,"----")
    
                
    f.close()
                
                
    