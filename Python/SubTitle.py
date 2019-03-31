
import numpy as np
import math 
 

from OscConnect import OscSender
from pythonosc import osc_message_builder as omb
from pythonosc import dispatcher
from pythonosc import osc_server

 

class SubTitle:	
    

    
    def __init__(self, id, message):
    
        self.state = "R";
    
        
        # use the filename to select the data type
        # mainPath can then be used to decide what to do
                
        
        
        # this array is needed in any case
        self.t      = []
              
        self.nr     = []
        self.text   = []
        
        
    
        self.ID = id
         
        self.disp = dispatcher.Dispatcher()  

        
    def LoadFile(self, oscf):
        
        self.OscFile = oscf         
        
        print("Loading data from: ".__add__(oscf))
 
        
        data        = np.loadtxt(oscf, delimiter='\t', usecols=(0,2))
  
        self.nr     = data[:,0]

        self.t      = data[:,1]

        self.text   = []
       
        with open(oscf, "r+") as f:
                data = f.readlines()
                for line in data:
                    
                    [p1, p2, p3, p4, p5] =  line.split('\t')

                    self.text.append(p4)
             
  
        print("datapoints: "+str(np.size(self.t)))
 
 
        
    def JackPosChange(self, timeVal, parent):
        
      
        tmpIdx = np.argmin(np.abs(np.subtract(self.t , timeVal))) 
      
        outPath = self.text[tmpIdx] 
        
        
        return outPath
         
    def ChangeState(self, msg):
        
        #s = self.f(msg)

#        if msg=="OFF":
#            
#        if msg=="R":
#         
#        if msg=="W":
            
        self.state = msg;
        
        print('CHANGED: '+ self.state)

    
      
      
    def handler_polar_single(self, unused_addr, value):
        #
        """ Designed to process PanoramixApp messages. """
        [o, t, i, p] = unused_addr.split("/")
        
        self.t.append()
         