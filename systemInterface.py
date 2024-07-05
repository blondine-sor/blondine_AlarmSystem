# library to create interface
#from tkinter import Button,Label,Frame
# libary controlled by gpio
from gpiozero import LED,Button
# class sevenseg
from blondine_AlarmSystem.sevenSeg import SevenSeg

from signal import pause


class SysInterface:

    def __CheckStats(self):
        pass

    def __Activate(self):
        """
        Function using the gpio button to activate and deactivate the Alarm System
        """
        if(self.status == False):
            self.status = True
            self.__alarmSys.on()
            self.__sevenSeg.CountUp()
            self.__sevenSeg.ShowA()
        else:
            self.status = False
            self.__alarmSys.off()
            self.__sevenSeg.CountDown( )
            self.__sevenSeg.Show0()    


    def __AlarmZoneActivated(self):
        """
        Alarm Activation for each zone(button) 
        """
        if(self.__btnz1.is_pressed):
           self.__sevenSeg.Show1() 
           self.__alarmSys.blink()
        elif(self.__btnz2.is_pressed):
            self.__sevenSeg.Show2()
            self.__alarmSys.blink()
        elif(self.__btnz3.is_pressed):
            self.__sevenSeg.Show3()
            self.__alarmSys.blinlk()
        elif(self.__btnz4.is_pressed):
            self.__sevenSeg.Show4()
            self.__alarmSys.blink()    


    def __Reset(self):
        """
         Function to reset alarm 
        """
        if(self.status == True ):
            self.__alarmSys.on()
        else:
            pass    
            




   

   

    def __init__(self):
        self.__sevenSeg= SevenSeg(17,13,8,9,10,11,12,0,False)
        #initialize seven seg and zones
        self.__btn = Button(27)
        self.__btnz1 = Button(22)
        self.__btnz2 = Button(5)
        self.__btnz3 = Button(6)
        self.__btnz4 = Button(19)
        self.__btnReset = Button(16)
        self.__alarmSys = LED(2)
        self.status = False
        self.__btn.when_pressed = self.__Activate
        self.__btnz1.when_pressed = self.__AlarmZoneActivated
        self.__btnz2.when_pressed = self.__AlarmZoneActivated
        self.__btnz3.when_pressed = self.__AlarmZoneActivated
        self.__btnz4.when_pressed = self.__AlarmZoneActivated
        self.__btnReset.when_pressed = self.__Reset


       