#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 18:57:33 2023

@author: anwaldt
"""



import os

from xml.etree.ElementTree import ElementTree

raw_dir = "/media/anwaldt/ANWALDT_DATA/SOUND/PROJECTS/2020/Closed_Captions/closed_captions/RAW/TOS/"

xmlFiles   = ["/media/anwaldt/ANWALDT_DATA/SOUND/PROJECTS/2020/Closed_Captions/closed_captions/RAW/TOS/S01/TOS_S01_E12.xml"]

for filename in os.listdir(raw_dir):
    f = os.path.join(raw_dir, filename)
    # checking if it is a file
    xmlFiles.append(f)


for file in xmlFiles:
    
    tree = ElementTree()
    tree.parse(file)    
    root = tree.getroot() 

#    # another format
#    for elem in root.iter():
#        print(elem.tag)


    for child in root:
        print(child.tag, child.attrib)
    
    