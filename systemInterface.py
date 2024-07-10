# library to create interface
from tkinter import Button as Btntk,Label,Frame,Tk
# libary controlled by gpio
from gpiozero import LED,Button as Btnz
# class sevenseg
from sevenSeg import SevenSeg

from signal import pause


class SysInterface:


    def __Activate(self):
        """
        Function using the gpio button to activate and deactivate the Alarm System
        """
        if(self.status == False):
            self.status = True
            self.__alarmSys.on()
            self.__sevenSeg.CountUp()
            self.__sevenSeg.ShowA()
            self.lblsysStatus.config(text="On", background="#64FF46")
          
        else:
            self.status = False
            self.__alarmSys.off()
            self.__sevenSeg.CountDown( )
            self.__sevenSeg.Show0()
            self.lblsysStatus.config(text="Off", background="#FF4846")
            # eteint toute zone actif
            self.AllNeutralZone()


    def __AlarmZoneActivated(self):
        """
        Alarm Activation for each zone(button) 
        """
        if(self.__btnz1.is_pressed):
           self.__sevenSeg.Show1() 
           self.__alarmSys.blink()
           self.__ActifZoneState() 
        elif(self.__btnz2.is_pressed):
            self.__sevenSeg.Show2()
            self.__alarmSys.blink()
            self.__ActifZoneState() 
        elif(self.__btnz3.is_pressed):
            self.__sevenSeg.Show3()
            self.__alarmSys.blink()
            self.__ActifZoneState() 
        elif(self.__btnz4.is_pressed):
            self.__sevenSeg.Show4()
            self.__alarmSys.blink()
            self.__ActifZoneState() 
  
  
    def AllNeutralZone(self):
        """
        Function to put-off all zones
        """
        self.lblzone1.config(bg="#5729b3")
        self.lblzone2.config(bg="#5729b3")
        self.lblzone3.config(bg="#5729b3")
        self.lblzone4.config(bg="#5729b3")
        
    def __ActifZoneState(self):
        """
        Function which returns the state of a zone whent activated
        """
        if(self.__btnz1.is_pressed):
            #zone1 actif
            self.lblzone1.config(bg="#64FF46")
            self.lblzone2.config(bg="#5729b3")
            self.lblzone3.config(bg="#5729b3")
            self.lblzone4.config(bg="#5729b3") 
        elif(self.__btnz2.is_pressed):
            #zone2 actif
            self.lblzone1.config(bg="#5729b3")
            self.lblzone2.config(bg="#64FF46")
            self.lblzone3.config(bg="#5729b3")
            self.lblzone4.config(bg="#5729b3") 
        elif(self.__btnz3.is_pressed):
            #zone3 actif
            self.lblzone1.config(bg="#5729b3")
            self.lblzone2.config(bg="#5729b3")
            self.lblzone3.config(bg="#64FF46")
            self.lblzone4.config(bg="#5729b3") 
        elif(self.__btnz4.is_pressed):
            #zone4 actif
            self.lblzone1.config(bg="#5729b3")
            self.lblzone2.config(bg="#5729b3")
            self.lblzone3.config(bg="#5729b3")
            self.lblzone4.config(bg="#64FF46")
    

    def __Reset(self):
        """
         Function to reset alarm 
        """
        if(self.status == True ):
            self.__alarmSys.on()
        else:
            pass    
            




   

   

    def __init__(self,tk):
        self.__sevenSeg= SevenSeg(8,9,10,11,12,13,17,0,False)
        #initialize seven seg and zones
        self.__btn = Btnz(27)
        self.__btnz1 = Btnz(22)
        self.__btnz2 = Btnz(5)
        self.__btnz3 = Btnz(6)
        self.__btnz4 = Btnz(19)
        self.__btnReset = Btnz(16)
        self.__alarmSys = LED(2)
        self.status = False
        self.__sevenSeg.Show0()
        self.__btn.when_pressed = self.__Activate
        self.__btnz1.when_pressed = self.__AlarmZoneActivated
        self.__btnz2.when_pressed = self.__AlarmZoneActivated
        self.__btnz3.when_pressed = self.__AlarmZoneActivated
        self.__btnz4.when_pressed = self.__AlarmZoneActivated
        self.__btnReset.when_pressed = self.__Reset
        self.__root = tk
        #creation of interface
        self.header = Label(self.__root,text="Pi Security GUI",padx=20,pady=20,font="Times 12")
        self.frameR = Frame(self.__root,border=1,background="#968f8d",width=150,height=200,padx=15,pady=20)
        self.frameL = Frame(self.__root,border=1,background="#968f8d",width=150,height=300,padx=15,pady=20)
        self.lblzone1 = Label(self.frameR,text="Z1",background="#5729b3",fg="white",borderwidth=20,padx=5,pady=5)
        self.lblzone2 = Label(self.frameR,text="Z2",background="#5729b3",fg="white",borderwidth=20,padx=5,pady=5)
        self.lblzone3 = Label(self.frameR,text="Z3",background="#5729b3",fg="white",borderwidth=20,padx=5,pady=5)
        self.lblzone4 = Label(self.frameR,text="Z4",background="#5729b3",fg="white",borderwidth=20,padx=5,pady=5)
        self.lblsysStatus = Label(self.frameR,text="On/Off",background="#5729b3",fg="white",borderwidth=40,padx=5,pady=5)
        self.btnOn = Btntk(self.frameL,text="Activate",padx=10,pady=10,background ="#f7c6c7", command=lambda: self.__Activate())
        self.btnOff = Btntk(self.frameL,text="Deactivate",padx=10,pady=10,background="#f7c6c7",command=lambda:self.__Activate())
        self.btnResetTk = Btntk(self.frameL,text="Reset",padx=10,pady=10,background="#f7c6c7", command=lambda: self.__Reset())

        self.header.grid(row=0, column=0,columnspan=6,padx=20,pady=20)
        self.frameL.grid(row=1,column=1,columnspan=3,padx=20,pady=20)
        self.frameR.grid(row=1,column=7,columnspan=3,padx=20,pady=20)
        self.btnOn.grid(row=0,column=0,padx=10,pady=10)
        self.btnOff.grid(row=1,column=0,padx=10,pady=10)
        self.btnResetTk.grid(row=2,column=0)
        self.lblzone1.grid(row=1,column=0,padx=5,pady=5)
        self.lblzone2.grid(row=1,column=1,padx=5,pady=5)
        self.lblzone3.grid(row=3,column=0,padx=5,pady=5)
        self.lblzone4.grid(row=3,column=1,padx=5,pady=5)
        self.lblsysStatus.grid(row=5,column=0,columnspan=3,padx=5,pady=5)

        self.__root.mainloop()



       
