# library to create interface
from tkinter import Button,Label,Frame
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
            




   

   

    def __init__(self,tk):
        self.__sevenSeg= SevenSeg(17,13,8,9,10,11,12,0,False)
        #initialize seven seg and zones
        self.__btn = gpiozero.Button(27)
        self.__btnz1 = gpiozero.Button(22)
        self.__btnz2 = gpiozero.Button(5)
        self.__btnz3 = gpiozero.Button(6)
        self.__btnz4 = gpiozero.Button(19)
        self.__btnReset = gpiozero.Button(16)
        self.__alarmSys = LED(2)
        self.status = False
        self.__btn.when_pressed = self.__Activate
        self.__btnz1.when_pressed = self.__AlarmZoneActivated
        self.__btnz2.when_pressed = self.__AlarmZoneActivated
        self.__btnz3.when_pressed = self.__AlarmZoneActivated
        self.__btnz4.when_pressed = self.__AlarmZoneActivated
        self.__btnReset.when_pressed = self.__Reset
        self.__root = tk
        #creation of interface
        self.header = Label(self.__root,text="Pi Security GUI",padding=20,font="Times 12")
        self.frameR = Frame(self.__root,border=1,background="#968f8d",width=150,height=200,padx=15,pady=20)
        self.frameL = Frame(self.__root,border=1,background="#968f8d",width=150,height=300,padx=15,pady=20)
        self.lblzone1 = Label(self.frameR,text="Z1",background="#5729b3",fg="white",borderwidth=40,padx=5,pady=5)
        self.lblzone2 = Label(self.frameR,text="Z2",background="#5729b3",fg="white",borderwidth=40,padx=5,pady=5)
        self.lblzone3 = Label(self.frameR,text="Z3",background="#5729b3",fg="white",borderwidth=40,padx=5,pady=5)
        self.lblzone4 = Label(self.frameR,text="Z4",background="#5729b3",fg="white",borderwidth=40,padx=5,pady=5)
        self.lblsysStatus = Label(self.frameR,text="On/Off",background="#5729b3",fg="white",borderwidth=40,padx=5,pady=5)
        self.btnOn = tkinter.Button(self.frameL,text="Activate",padx=10,pady=10,background ="#f7c6c7",borderless=1, command=lambda: self.__Activate())
        self.btnOff = tkinter.Button(self.frameL,text="Deactivate",padx=10,pady=10,background="#f7c6c7", borderless=1,command=lambda:self.__Activate())
        self.btnResetTk = tkinter.Button(self.frameL,text="Reset",padx=10,pady=10,background="#f7c6c7", borderless=1,command=lambda: self.__Reset())

        self.header.grid(row=0, column=0,columnspan=6)
        self.frameL.grid(row=1,rowspan=4,column=0,columnspan=3)
        self.frameR.grid(row=1,rowspan=4,column=1,columnspan=3)

        self.__root.mainloop()



       