#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:55:08 2020

@author: anwaldt
"""
from xml.dom import minidom
from os import listdir
from os.path import isfile, join
import xml.etree.ElementTree as ET

in_dir = '/media/anwaldt/ANWALDT_2TB/SOUND/PROJECTS/2020/Closed_Captions/closed_captions/RAW/TOS/'

file_list = [f for f in listdir(in_dir) if isfile(join(in_dir, f))]


tree = ET.parse(in_dir+file_list[0])

root = tree.getroot()

        
        
        
        
        
        
        
        
        
      
doc = minidom.parse(in_dir+file_list[0]) 
        
        
main_node = doc.getElementsByTagName('tt')

items = doc.getElementsByTagName('body')

