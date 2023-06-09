# This Python file uses the following encoding: utf-8
import os, sys
import tkinter as tk
import json
from tkinter import *

strFinal = ''
#codice con calcoli
def sommaBin(lista):
    dim = len(lista)
    for i in range(dim-1, -1,-1):
        if not lista[i]:
            lista[i] = True
            for r in range(i+1, dim):
                lista[r] = False
            break
        
    return lista 

def on_enter(event):
    Calcolo()

#ATENZIONE

def Calcolo():
    Pulisci()
    indexVar = -1
    carUsed = []
    boolVar = []    
    comandoFinale = ''#stringa che conterrà la formula analizzata e codificata correttamente


    for c in Fx_input.get():
        #controllo dei vari possibili  operatori logici
        if c == '*':
            comandoFinale += ('and ')
        if c == '+':
            comandoFinale += ('or ')
        if c == '!':
            comandoFinale += ('not ')

        #controllo varibili
        if ord(c) >= 65 and ord(c) <= 90 or ord(c) >= 97 and ord(c) <= 122:
            try:
                indice = carUsed.index(c.upper())
            except ValueError:
                indexVar+=1
                
                carUsed.append(c.upper())
                boolVar.append(False)
            indice = indexVar

            comandoFinale += ("boolVar["+str(indice)+"] ")

        #controllo se parentesi
        if c == '(':
            comandoFinale += ('( ') 
        
        if c == ')':
            comandoFinale += (' )')

    carUsed.sort()
    FxCalcolata = ''
    strFinal = ''

    for c in carUsed:
            strFinal += c
    strFinal += " Fx"   

    for i in range(pow(2,indexVar+1)):
        if eval(comandoFinale):
            FxCalcolata = '1'
        else:
            FxCalcolata = '0'

        #output
        strFinal+='\n'

        #strFinal = ''

        for r in range(indexVar + 1):
            if boolVar[r]:
                strFinal += "1"
            else:
                strFinal += "0"
        
        strFinal += ' ' + FxCalcolata
        #gestione tabella di verita
        boolVar = sommaBin(boolVar)
    
    print(comandoFinale)
    text_output.config(text=strFinal)
    
    

def Pulisci():
    text_output.config(text="")

def ScriviSuFile(dictFunzioni):
    filejs = open("FunzioniSalvate.json", "w")
    filejs.write(json.dumps(dictFunzioni))
    filejs.close()

def LeggiDalFile():
    filejs = open("FunzioniSalvate.json", "r")
    dictFunzioni = json.loads(filejs.read())
    filejs.close()
    return dictFunzioni

def AggiungiFunzFile():
    datiFileJs = LeggiDalFile()
    datiFileJs["f"+str(datiFileJs["Nfunzioni"])] = (Fx_input.get())
    datiFileJs["Nfunzioni"]=datiFileJs["Nfunzioni"]+1
    ScriviSuFile(datiFileJs)
    AggiornaLista()
    
    return False

def AggiornaLista():
    datiFileJs = LeggiDalFile()
    Lista.delete(0,tk.END)
    for d in datiFileJs:
        if(d != "Nfunzioni"):
            Lista.insert(END,str(datiFileJs[d]))

def Deseleziona():
    selection = Lista.curselection()
    if selection:
        Lista.selection_clear(selection[0])

def Carica():
    index = Lista.curselection()[0]
    selezionato = Lista.get(index)
    Fx_input.insert(0,selezionato)

def Elimina():
    index = Lista.curselection()[0]
    if(index >= 0):
        selezionato = Lista.get(index)
        dictf = LeggiDalFile()
        for c in dictf:
            if(dictf[c] == selezionato):
                del dictf[c]
                dictf["Nfunzioni"] = dictf["Nfunzioni"]-1
                break
        ScriviSuFile(dictf)
        AggiornaLista()
#grafica

window = tk.Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# calcola le dimensioni della finestra in base alle percentuali desiderate
window_width = int(screen_width * 0.8)  # 80% dello schermo
window_height = int(screen_height * 0.6)  # 60% dello schermo

# imposta la geometria della finestra
window.geometry(f"{window_width}x{window_height}+{int((screen_width - window_width)/2)}+{int((screen_height - window_height)/2)}")

#window.geometry("650x1000")
window.title("Calcolatore funzioni logiche")
#window.configure(background="white")

Informazaioni_output = tk.Label(window, text="La variabili della funzione devono essere espresse come delle single lettere, il sistema non è case-sensitive. \nGli operatori logici DEVONO essere espressi con le seguenti forme: \n  AND => * \n  OR => + \n  NOT => ! \n  Usare le parentesi tonde nel caso fosse necessario\n  ")
Informazaioni_output.place(relx=0.25, rely=0.2, anchor="center")


#Informazaioni_output.config(wraplength=window.winfo_width())

Fx_input = tk.Entry()
Fx_input.place(relx=0.25, rely=0.3, anchor="center")#.grid(row=10)
Fx_input.bind("<Return>", on_enter)

bottone_conferma = tk.Button(text="Conferma funzione", command=Calcolo)
bottone_conferma.place(relx=0.25, rely=0.4, anchor="center")#.grid(row=20)

bottone_aggiungi = tk.Button(text="Salva Funzione", command=AggiungiFunzFile)
bottone_aggiungi.place(relx=0.25, rely=0.5, anchor="center")

Lista = Listbox(window)
Lista.place(relx=0.4, rely=0.5, anchor="center")

bottone_carica = tk.Button(text="Carica", command=Carica)
bottone_carica.place(relx=0.25, rely=0.55, anchor="center")

bottone_elimina = tk.Button(text="Elimina", command=Elimina)
bottone_elimina.place(relx=0.25, rely=0.60, anchor="center")

bottone_deselect = tk.Button(text="Deseleziona ", command=Deseleziona)
bottone_deselect.place(relx=0.25, rely=0.65, anchor="center")




AggiornaLista()

text_output = tk.Label(window, text='')
text_output.place(relx=0.75, rely=0.5, anchor="center")#.grid(row = 30)

if __name__ == "__main__":
    window.mainloop() 
