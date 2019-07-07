import time
import RPi.GPIO as gpio
from tkinter import *

#GPIO Bezeichnungsmodus festlegen:
gpio.setmode(gpio.BOARD)
             
#PINS definieren:
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
# Da nur eine Drehrichtung möglich ist bleibt PIN 11 immer false!
gpio.output(11, False)

#Startwert für Prüfvariable definieren (Ausgangszustand)
status = "aus"

#Pumpe ein- bzw ausschalten
def Pumpe_ausloesen():
    #Prüfvariable soll in Funktion überschrieben werden
    #=> hier als globale Variable definieren!
    global status
    if status == "aus":
        #Die Pumpe starten:
        gpio.output(13, True)
        print("Pflanze wird jetzt gegossen!")
        #Button umbeschriften
        ActivateB.config(text='STOP!')
        #Prüfvariable ändern
        status = "an"
    else:
        #Die Pumpe stoppen
        gpio.output(13, False)
        print("Gießvorgang abgeschlossen.")
        #Button umbeschriften
        ActivateB.config(text='Gießen!')
        #Prüfvariable ändern
        status = "aus"

#Beenden und Fenster schließen
def Beenden():
    #Fenster schließen
    Fenster.quit()
    #Fenster vernichten
    Fenster.destroy()
    #GPIOs zurücksetzen muss hier nicht passieren, sonst doppelt!
    #Wird ja bei beenden der mainloop sowieso unten aufgerufen!
      
#DAS DIALOGFENSTER
#--------------------------
#Hauptfenster erstellen
Fenster = Tk()
Fenster.geometry("400x300")
Fenster.title('Gießcontrollcenter')
#Hauptfenster in Rahmen packen
Frame(Fenster).pack(padx=10, pady=5, side="top")

#Hauptüberschrift erstellen
HeaderHAUPT = Label(Fenster, text='Gießcontrollcenter', font=('Arial',20))
HeaderHAUPT.pack()
#Anzeige Feuchtigkeit
HeaderFEU = Label(Fenster, text='Bodenfeuchtigkeit :', font=('Arial',14))
HeaderFEU.pack(anchor="w", padx="10")
AnzeigeFEU = Label(Fenster, text='kein Wert', font=('Arial',14))
AnzeigeFEU.pack(anchor="center")
#Anzeige Prüfintervall
HeaderPRUEF = Label(Fenster, text='Prüfintervall :', font=('Arial',14))
HeaderPRUEF.pack(anchor="w", padx="10")
AnzeigePRUEF = Label(Fenster, text='nicht gesetzt', font=('Arial',14))
AnzeigePRUEF.pack(anchor="center")


#Gießknopf erstellen
ActivateB = Button(Fenster, text='Gießen!', command=Pumpe_ausloesen)
ActivateB.pack(padx="20", pady="5", side="left")
#Knopf zum beenden erstellen
EndB = Button(Fenster, text='Beenden', command=Beenden)
EndB.pack(padx="20", pady="5", side="right")

#Dialogprozedur starten
Fenster.mainloop()

if Fenster.mainloop() == None:
    #GPIOs zurücksetzen
    gpio.cleanup()
    print("GPIOs zurückgesetzt")
    


