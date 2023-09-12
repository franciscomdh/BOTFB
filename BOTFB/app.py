# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:49:29 2023

@author: franm
Doc:
    https://tkdocs.com/pyref/
    https://docs.python.org/3/library/tkinter.html#setting-options
    https://www.youtube.com/watch?v=M80CzDC1Crc
"""

from tkinter import *
raiz=Tk()

raiz.title("Autopublish")

raiz.iconbitmap("fb.ico")
#raiz.geometry("550x360") tamaño ventana
raiz.config(bg="lightblue")
raiz.resizable(0,0)
#Packer options doc para modificar frame
miFrame=Frame(raiz, width=650,height=400,bg="lightblue") #Para acomodar las cajas dentro de la app
miFrame.pack()


# =============================================================================
# Label y Entrys
# =============================================================================

######################## Select group #######################
selectGroup = Entry(miFrame,font=20,width=30)
selectGroup.grid(row=0,column=1,padx=5,pady=10)
selectGroup.config(justify="left")

groupLabel=Label(miFrame,text="Seleccione Grupo:",font=20).grid(row=0,column=0,sticky="w",padx=10,pady=10)


########################## Text #############################

textPub = Text(miFrame,width=40,height=10,font=20)
textPub.grid(row=1,column=1,padx=10,pady=10)

textLabel=Label(miFrame,text="Texto:", font=20).grid(row=1,column=0,sticky="",pady=10)
scrollVert=Scrollbar(miFrame,command=textPub.yview)
scrollVert.grid(row=1,column=2,sticky="nsew")
textPub.config(yscrollcommand=scrollVert.set)

########################## Img #############################
### Lista ##
listLabel = Label(miFrame, text="Lista de Imagenes", font=20)
listLabel.grid(row=0, column=4, sticky="", padx=10, pady=10)

listImg = Listbox(miFrame, width=40)
listImg.grid(row=1, column=4, padx=10, pady=10)

imagen = PhotoImage(file="cpimg_50.png")

imgLabel=Label(miFrame, text="Seleccione imagenes:", font=20)
imgLabel.grid(row=3, column=0, padx=10, pady=10)
botonImg = Button(miFrame, image=imagen)
botonImg.grid(row=3, column=1, padx=10, pady=10)
########################## Date #############################


# =============================================================================
# Buttons
# =============================================================================

    
BotonEnv=Button(miFrame,text="Enviar",width=100,padx=10,pady=10)
BotonEnv.grid(row=5,columnspan=5,padx=5,pady=5)


    








raiz.mainloop()