from gpiozero import LED
from time import sleep

class SevenSeg :
    def __init__(self,sega,segb,segc,segd,sege,segf,segg,pd,type):
        self.__sa = LED(sega)
        self.__sb = LED(segb)
        self.__sc = LED(segc)
        self.__sd = LED(segd)
        self.__se = LED(sege)
        self.__sf = LED(segf)
        self.__sg = LED(segg)
        self.__pd = LED(pd)
        self.__type = type

    def Show0(self):
        if(self.__type == True):
             #0
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.off()
            self.__pd.off()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.on()
            self.__pd.on()

    def Show1(self):
        if(self.__type == True):
             #1
            self.__sa.off()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()
            self.__pd.off()
        else:
            self.__sa.on()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
            self.__pd.on()

    def Show2(self):
        if(self.__type == True):
             #2
            self.__sa.on()
            self.__sb.on()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
            self.__sf.off()
            self.__sg.on()
            self.__pd.off()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.on()
            self.__sd.off()
            self.__se.off()
            self.__sf.on()
            self.__sg.off()
            self.__pd.on()

    def Show3(self):
        if(self.__type == True):
             #3
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.on()
            self.__se.off()
            self.__sf.off()
            self.__sg.on()
            self.__pd.off()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.off()
            self.__se.on()
            self.__sf.on()
            self.__sg.off()
            self.__pd.on()

    def Show4(self):
        if(self.__type == True):
             #4
            self.__sa.off()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.off()
            self.__sf.on()
            self.__sg.on()
            self.__pd.off()
        else:
            self.__sa.on()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
            self.__sf.off()
            self.__sg.off()
            self.__pd.on()

    def Show5(self):
        if(self.__type == True):
             #5
            self.__sa.on()
            self.__sb.off()
            self.__sc.on()
            self.__sd.on()
            self.__se.off()
            self.__sf.on()
            self.__sg.on()
            self.__pd.off()
        else:
            self.__sa.off()
            self.__sb.on()
            self.__sc.off()
            self.__sd.off()
            self.__se.on()
            self.__sf.off()
            self.__sg.off()
            self.__pd.on()        

    def Show6(self):
        if(self.__type == True):
             #6
            self.__sa.on()
            self.__sb.off()
            self.__sc.on()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
            self.__pd.off()
        else:
            self.__sa.off()
            self.__sb.on()
            self.__sc.off()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()
            self.__pd.on()    

    def Show7(self):
        if(self.__type == True):
             #7
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()
            self.__pd.off()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
            self.__pd.on()     

    def Show8(self):
        if(self.__type == True):
             #8
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
            self.__pd.off()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()
            self.__pd.on() 

    def Show9(self):
        if(self.__type == True):
             #9
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.off()
            self.__sf.on()
            self.__sg.on()
            self.__pd.off()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
            self.__sf.off()
            self.__sg.off()
            self.__pd.on()                 

    def ShowA(self):
        if(self.__type == True):
             #1A
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
            self.__pd.off()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()
            self.__pd.on() 

    def ShowB(self):
        if(self.__type == True):
             #B
            self.__sa.off()
            self.__sb.off()
            self.__sc.on()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
            self.__pd.off()
        else:
            self.__sa.on()
            self.__sb.on()
            self.__sc.off()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()
            self.__pd.on()

    def ShowC(self):
        if(self.__type == True):
             #C
            self.__sa.on()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.off()
            self.__pd.off()
        else:
            self.__sa.off()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.on()
            self.__pd.on() 

    def ShowD(self):
        if(self.__type == True):
             #D
            self.__sa.off()
            self.__sb.on()
            self.__sc.on()
            self.__sd.on()
            self.__se.on()
            self.__sf.off()
            self.__sg.on()
            self.__pd.off()
        else:
            self.__sa.on()
            self.__sb.off()
            self.__sc.off()
            self.__sd.off()
            self.__se.off()
            self.__sf.on()
            self.__sg.off()
            self.__pd.on() 

    def ShowE(self):
        if(self.__type == True):
             #E
            self.__sa.on()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
            self.__pd.off()
        else:
            self.__sa.off()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()
            self.__pd.on() 

    def ShowF(self):
        if(self.__type == True):
             #F
            self.__sa.on()
            self.__sb.off()
            self.__sc.off()
            self.__sd.off()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
            self.__pd.off()
        else:
            self.__sa.off()
            self.__sb.on()
            self.__sc.on()
            self.__sd.on()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()
            self.__pd.on() 

    def ShowL(self):
        if(self.__type == True):
             #L
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.off()
            self.__pd.off()
        else:
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.on()
            self.__pd.on()  

    def ShowH(self):
        if(self.__type == True):
             #H
            self.__sa.off()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
            self.__pd.off()
        else:
            self.__sa.on()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()
            self.__pd.on()  

    def ShowDecimal(self):
        if(self.__type == True):
            self.__pd.on()
        else:
            self.__pd.off()     

    @property
    def SA(self):
        if(self.__sa.on == True):
            return True
        else:
            return False 
         
    
    @property
    def SB(self):
        if(self.__sb.on == True):
            return True
        else:
            return False 
        
    
    @property
    def SC(self):
        if(self.__sc.on == True):
            return True
        else:
            return False   
    
    @property
    def SD(self):
        if(self.__sd.on == True):
            return True
        else:
            return False 
    
    @property
    def SE(self):
        if(self.__se.on == True):
            return True
        else:
            return False 

    @property
    def SF(self):
        if(self.__sf.on == True):
            return True
        else:
            return False 

    @property
    def SG(self):
        if(self.__sg.on == True):
            return True
        else:
            return False      

    @property
    def PD(self):
        if(self.__pd.on == True):
            return True
        else:
            return False 

    @property
    def Type(self):
        return self.__type     

    @SA.setter
    def SA(self,newsa):
        if(newsa == True):
            self.__sa.on
        else:
            self.__sa.off  

    @SB.setter
    def SB(self,newsb):
        if(newsb == True):
            self.__sb.on
        else:
            self.__sb.off  

    @SC.setter
    def SC(self,newsc):
        if(newsc == True):
            self.__sc.on
        else:
            self.__sc.off 

    @SD.setter
    def SD(self,newsd):
        if(newsd == True):
            self.__sd.on
        else:
            self.__sd.off 
   
    @SE.setter
    def SE(self,newse):
        if(newse == True):
            self.__se.on
        else:
            self.__se.off 

    @SF.setter
    def SF(self,newsf):
        if(newsf == True):
            self.__sf.on
        else:
            self.__sf.off 

    @SG.setter
    def SG(self,newsg):
        if(newsg == True):
            self.__sg.on
        else:
            self.__sg.off           

    def CountUp(self):
        #0
        self.Show0()
        sleep(1)

        #1
        self.Show1()    
        sleep(1)

        #2
        self.Show2() 
        sleep(1)

        #3
        self.Show3()  
        sleep(1)
            
        #4
        self.Show4()
        sleep(1)

        #5
        self.Show5()
        sleep(1)

        #6
        self.Show6() 
        sleep(1)

        #7
        self.Show7() 
        sleep(1)


        #8
        self.Show8()  
        sleep(1)


        #9
        self.Show9()
        sleep(1)

    def CountDown(self):
         #9
        self.Show9    
        sleep(1)

        #8
        self.Show8()  
        sleep(1)

        #7
        self.Show7()   
        sleep(1)

        #6
        self.Show6()  
        sleep(1)

        #5
        self.Show5() 
        sleep(1)

        #4
        self.Show4()  
        sleep(1)

        #3
        self.Show3()    
        sleep(1)

        #2
        self.Show2()  
        sleep(1)

        #1
        self.Show1()    
        sleep(1)
        
        #0
        self.Show0()
        sleep(1)


    def Flash0(self):
         # Flash0
         if(self.__type == True):
            self.__sa.blink()
            self.__sb.blink()
            self.__sc.blink()
            self.__sd.blink()
            self.__se.blink()
            self.__sf.blink()
            self.__sg.off()
            self.__pd.off()
         else:
            self.__sa.blink()
            self.__sb.blink()
            self.__sc.blink()
            self.__sd.blink()
            self.__se.blink()
            self.__sf.blink()
            self.__sg.on()
            self.__pd.on()
       
    
    def Flash1(self):
         #Flash2
        if(self.__type == True):
             #1
            self.__sa.off()
            self.__sb.blink()
            self.__sc.blink()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()
            self.__pd.off()
        else:
            self.__sa.on()
            self.__sb.blink()
            self.__sc.blink()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
            self.__pd.on()
        
    def Flash2(self):
         #Flash2
         if(self.__type == True):
            self.__sa.blink()
            self.__sb.blink()
            self.__sc.off()
            self.__sd.blink()
            self.__se.blink()
            self.__sf.off()
            self.__sg.blink()
            self.__pd.off()
         else:
            self.__sa.blink()
            self.__sb.blink()
            self.__sc.on()
            self.__sd.blink()
            self.__se.blink()
            self.__sf.on()
            self.__sg.blink()
            self.__pd.on()    

    def Flash3(self):
         #Flash3
         if(self.__type == True):
            self.__sa.blink()
            self.__sb.blink()
            self.__sc.blink()
            self.__sd.blink()
            self.__se.off()
            self.__sf.off()
            self.__sg.blink()
            self.__pd.off() 
         else:
            self.__sa.blink()
            self.__sb.blink()
            self.__sc.blink()
            self.__sd.blink()
            self.__se.on()
            self.__sf.on()
            self.__sg.blink()
            self.__pd.on()  
                
          

    def Flash4(self):
             #Flash4
        if(self.__type == True):     
            self.__sa.off()
            self.__sb.blink()
            self.__sc.blink()
            self.__sd.off()
            self.__se.off()
            self.__sf.blink()
            self.__sg.blink()
            self.__pd.off() 
        else:
            self.__sa.on()
            self.__sb.blink()
            self.__sc.blink()
            self.__sd.on()
            self.__se.on()
            self.__sf.blink()
            self.__sg.blink()
            self.__pd.on()     

    def Flash5(self):
             #Flash5
        if(self.__type == True):     
            self.__sa.blink()
            self.__sb.off()
            self.__sc.blink()
            self.__sd.blink()
            self.__se.off()
            self.__sf.blink()
            self.__sg.blink()
            self.__pd.off()
        else:
            self.__sa.blink()
            self.__sb.on()
            self.__sc.blink()
            self.__sd.blink()
            self.__se.on()
            self.__sf.blink()
            self.__sg.blink()
            self.__pd.on()    


    def Flash6(self):
             #Flash6
        if(self.__type ==True):
            self.__sa.blink()
            self.__sb.off()
            self.__sc.blink()
            self.__sd.blink()
            self.__se.blink()
            self.__sf.blink()
            self.__sg.blink()
            self.__pd.off() 
        else:
            self.__sa.blink()
            self.__sb.on()
            self.__sc.blink()
            self.__sd.blink()
            self.__se.blink()
            self.__sf.blink()
            self.__sg.blink()
            self.__pd.on()    

    def Flash7(self):
             #Flash7
        if(self.__type == True):     
            self.__sa.blink()
            self.__sb.blink()
            self.__sc.blink()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()
            self.__pd.off() 
        else:
            self.__sa.blink()
            self.__sb.blink()
            self.__sc.blink()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
            self.__pd.on() 
                   

    def Flash8(self):
             #8
        if(self.__type == True):     
            self.__sa.blink()
            self.__sb.blink()
            self.__sc.blink()
            self.__sd.blink()
            self.__se.blink()
            self.__sf.blink()
            self.__sg.blink()
            self.__pd.off()
        else:
            self.__sa.blink()
            self.__sb.blink()
            self.__sc.blink()
            self.__sd.blink()
            self.__se.blink()
            self.__sf.blink()
            self.__sg.blink()
            self.__pd.on()    
        

    def Flash9(self):
             #Flash9
        if(self.__type == True):     
            self.__sa.blink()
            self.__sb.blink()
            self.__sc.blink()
            self.__sd.off()
            self.__se.off()
            self.__sf.blink()
            self.__sg.blink()
            self.__pd.off()
        else:
            self.__sa.blink()
            self.__sb.blink()
            self.__sc.blink()
            self.__sd.on()
            self.__se.on()
            self.__sf.blink()
            self.__sg.blink()
            self.__pd.on()
                       

    def FlashA(self):
             #FlashA
        if(self.__type == True):     
            self.__sa.blink()
            self.__sb.blink()
            self.__sc.blink()
            self.__sd.off()
            self.__se.blink()
            self.__sf.blink()
            self.__sg.blink()
            self.__pd.off()
        else:
            self.__sa.blink()
            self.__sb.blink()
            self.__sc.blink()
            self.__sd.on()
            self.__se.blink()
            self.__sf.blink()
            self.__sg.blink()
            self.__pd.on()

    def FlashB(self):
             #FlashB
        if(self.__type == True):     
            self.__sa.off()
            self.__sb.off()
            self.__sc.blink()
            self.__sd.blink()
            self.__se.blink()
            self.__sf.blink()
            self.__sg.blink()
            self.__pd.off()
        else:
            self.__sa.on()
            self.__sb.on()
            self.__sc.blink()
            self.__sd.blink()
            self.__se.blink()
            self.__sf.blink()
            self.__sg.blink()
            self.__pd.on()

    def FlashC(self):  
             #FlashC
        if(self.__type == True):     
            self.__sa.blink()
            self.__sb.off()
            self.__sc.off()
            self.__sd.blink()
            self.__se.blink()
            self.__sf.blink()
            self.__sg.off()
            self.__pd.off()
        else:
            self.__sa.blink()
            self.__sb.on()
            self.__sc.on()
            self.__sd.blink()
            self.__se.blink()
            self.__sf.blink()
            self.__sg.on()
            self.__pd.on()

    def FlashD(self):
             #FlashD
        if(self.__type == True):     
            self.__sa.off()
            self.__sb.blink()
            self.__sc.blink()
            self.__sd.blink()
            self.__se.blink()
            self.__sf.off()
            self.__sg.blink()
            self.__pd.off()
        else:
            self.__sa.on()
            self.__sb.blink()
            self.__sc.blink()
            self.__sd.blink()
            self.__se.blink()
            self.__sf.on()
            self.__sg.blink()
            self.__pd.on()

    def FlashE(self):
             #FlashE
        if(self.__type == True):     
            self.__sa.blink()
            self.__sb.off()
            self.__sc.off()
            self.__sd.blink()
            self.__se.blink()
            self.__sf.blink()
            self.__sg.blink()
            self.__pd.off()
        else:
            self.__sa.blink()
            self.__sb.on()
            self.__sc.on()
            self.__sd.blink()
            self.__se.blink()
            self.__sf.blink()
            self.__sg.blink()
            self.__pd.on()

    def FlashF(self):
             #FlashF
        if(self.__type == True):     
            self.__sa.blink()
            self.__sb.off()
            self.__sc.off()
            self.__sd.off()
            self.__se.blink()
            self.__sf.blink()
            self.__sg.blink()
            self.__pd.off()
        else:
            self.__sa.blink()
            self.__sb.on()
            self.__sc.on()
            self.__sd.on()
            self.__se.blink()
            self.__sf.blink()
            self.__sg.blink()
            self.__pd.on()

    def FlashL(self):
             #FlashL
        if(self.__type == True):     
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.blink()
            self.__se.blink()
            self.__sf.blink()
            self.__sg.off()
            self.__pd.off()
        else:
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.blink()
            self.__se.blink()
            self.__sf.blink()
            self.__sg.on()
            self.__pd.on()

    def FlashH(self):
             #FlashH
        if(self.__type == True):     
            self.__sa.off()
            self.__sb.blink()
            self.__sc.blink()
            self.__sd.off()
            self.__se.blink()
            self.__sf.blink()
            self.__sg.blink()
            self.__pd.off()
        else:
            self.__sa.on()
            self.__sb.blink()
            self.__sc.blink()
            self.__sd.on()
            self.__se.blink()
            self.__sf.blink()
            self.__sg.blink()
            self.__pd.on()    
         

    def FlashDecimal(self):
        #FlashDecimal   
        self.__pd.blink()
            
 