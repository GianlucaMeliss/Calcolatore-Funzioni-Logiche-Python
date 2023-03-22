# This Python file uses the following encoding: utf-8
import os, sys
import tkinter as tk
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

    text_output.config(text=strFinal)
    

def Pulisci():
    text_output.config(text="")

#grafica
window = tk.Tk()
window.geometry("680x700")
window.title("Calcolatore funzioni logiche")
#window.configure(background="white")

Informazaioni_output = tk.Label(window, text="La variabili della funzione devono essere espresse come delle single lettere, il sistema non è case-sensitive. \nGli operatori logici DEVONO essere espressi con le seguenti forme: \n  AND => * \n  OR => + \n  NOT => ! \n  Usare le parentesi tonde nel caso fosse necessario\n  ")
Informazaioni_output.grid(row = 5, padx=10, pady=10, sticky="n") #

#Informazaioni_output.config(wraplength=window.winfo_width())

Fx_input = tk.Entry()
Fx_input.grid(row=10)

bottone_conferma = tk.Button(text="Conferma funzione", command=Calcolo)
bottone_conferma.grid(row=20)


text_output = tk.Label(window, text='')
text_output.grid(row = 30)



if __name__ == "__main__":
    window.mainloop() 
