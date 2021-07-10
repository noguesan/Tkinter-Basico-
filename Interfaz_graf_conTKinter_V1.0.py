"""
DESCRIPCION:
Esta es una aplicacion con lo basico de la libreria Tkinter, a modo ejemplo para entendimiento 
de su funcionamiento.
Se utilizan varios Frames, Entrys, Labels, Text, Radio buttons, Check buttons, Photoimages, Buttons, etc.
"""


#IMPORTACION 

from tkinter import *

from matplotlib.pyplot import text
from sqlalchemy import column

#---------------------------------------------------------------------------------------
#VENTANA PRINCIPAL
raiz = Tk()
raiz.title("Intefas grafica basica")

miFrame1=Frame(raiz, width=1200, height=600)
miFrame1.pack(fill='both', expand = 'True', side = "top")

miFrame2=Frame(raiz, width=1200, height=600)
miFrame2.pack(fill='both', expand = 'True', side = "top")

miFrame3=Frame(raiz, width=1200, height=600)
miFrame3.pack(fill='both', expand = 'True', side = "top")
# Parámetros	Valores
# mi_Frame.pack(fill=”valor”)	‘x’, ‘y’, ‘both’, ‘none’
# mi_Frame.pack(expand=”valor”)	0, 1, “True”, “False”
# mi_Frame.pack(side=”valor”)	‘left’, ‘right’, ‘top’, ‘bottom’

#---------------------------------------------------------------------------------------
#DEFINICION VARIABLES

# Variables de los entrys
minombre = StringVar()
miapellido = StringVar()
micontrasena = StringVar()
midireccion = StringVar()
micomentario = StringVar()
varOpcion = IntVar()


# variables para los check bottons
op1 = IntVar()
op2 = IntVar()
op3 = IntVar()

#---------------------------------------------------------------------------------------
#FUNCIONES

def codigoBoton():
    """
    Es la funcion del boton de borrar que pone todas las cosas como al inicio (borra el contenido de todo)
    """

    minombre.set("")
    miapellido.set("")
    micontrasena.set("")
    midireccion.set("")
    micomentario.set("")
    comentarioText.delete('1.0', END)
    varOpcion.set(None)
    op1.set(None)
    op2.set(None)
    op3.set(None)

def optionsRadioButtons():
    """
    Devuelve un mensaje al final ve la ventan raiz, con la 
    opcion elegida en los CHECK BUTTONS
    """
    
    opcionEscogida=""

    if (op1.get()==1):
        opcionEscogida+=" escogio 1"

    if (op2.get()==1):
        opcionEscogida+=" escogio 2"

    if (op3.get()==1):
        opcionEscogida+=" escogio 3"

    textoFinal.config(text=opcionEscogida)





#---------------------------------------------------------------------------------------
# ENTRADAS PARA INTRODUCIR TEXTO

nombreEntry = Entry(miFrame1, textvariable=minombre)
nombreEntry.grid(row=0, column=1, padx=10, pady=10)
# pad es para distanciar de los otros elementos cierto numero de pixeles
nombreEntry.config(fg="red", justify="center")

apellidoEntry = Entry(miFrame1, textvariable=miapellido)
apellidoEntry.grid(row=1, column=1, padx=10, pady=10)

direccionEntry = Entry(miFrame1, textvariable=midireccion)
direccionEntry.grid(row=2, column=1, padx=10, pady=10)

contrasenaEntry = Entry(miFrame1, textvariable=micontrasena)
contrasenaEntry.grid(row=3, column=1, padx=10, pady=10)
contrasenaEntry.config(show="*")
#show: es para mostrar lo que se asigne en lugar de lo que se escribe

#---------------------------------------------------------------------------------------
# LABELS AL COSTADO IZQUIERDO DE LAS ENTRADAS O TEXTOS SEGUN CORRESPONDA

nombreLabel=Label(miFrame1, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10) 
#Sticky es para oriental el label y que quede pegado en la direccion este

apellidoLabel=Label(miFrame1, text="Apellido:")
apellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame1, text="Direccion:")
direccionLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

contrasenaLabel=Label(miFrame1, text="Password:")
contrasenaLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

contrasenaLabel=Label(miFrame1, text="Comentarios:")
contrasenaLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

#---------------------------------------------------------------------------------------
#TEXTO, PARA LA INTRODUCION DE TEXTOS "LARGOS"

comentarioText = Text(miFrame1, width=16, height=5)
comentarioText.grid(row=4, column=1, padx=10, pady=10)

#scrollbar asociado al texto
scrollVert=Scrollbar(miFrame1, command=comentarioText.yview)
scrollVert.grid(row=4, column=2, sticky= "nsew")
#nsew: le da un tamano mas "amigable" al Scrollbar
comentarioText.config(yscrollcommand=scrollVert.set) #"asocia el tamano" del Texto al ScrolVert

#---------------------------------------------------------------------------------------
#RADIOBUTTONS (BOTONES PARA ELEGIR OPCIONES)

generoLabel = Label(miFrame2,text="Genero:")
generoLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

mascRB = Radiobutton(miFrame2, text="Masculino", variable=varOpcion, value=1)
mascRB.grid(row=0, column=1, sticky="w", padx=10, pady=10)

femRB = Radiobutton(miFrame2, text="Femenino", variable=varOpcion, value=2)
femRB.grid(row=1, column=1, sticky="w", padx=10, pady=10)

otroRB =Radiobutton(miFrame2, text="Otro", variable=varOpcion, value=3)
otroRB.grid(row=2, column=1, sticky="w", padx=10, pady=10)

#---------------------------------------------------------------------------------------
#CHECKBUTTONS, PARA ELEGIR OPCIONES
checkbottonLable = Label(miFrame3,text="Check Bottons:")
checkbottonLable.grid(row=0, column=0, sticky="e", padx=10, pady=10)

cb1 = Checkbutton(miFrame3, text="CB 1", variable=op1, onvalue=1, offvalue=0, command= optionsRadioButtons)
cb1.grid(row=1, column=0, sticky="e", padx=10, pady=10)

cb2 = Checkbutton(miFrame3, text="CB 2", variable=op2, onvalue=1, offvalue=0, command= optionsRadioButtons)
cb2.grid(row=1, column=1, sticky="e", padx=10, pady=10)

cb3 = Checkbutton(miFrame3, text="CB 3", variable=op3, onvalue=1, offvalue=0, command= optionsRadioButtons)
cb3.grid(row=1, column=2, sticky="e", padx=10, pady=10)

# Es para que ande la funcion optionsRadioButtons, asi devuelve el mensaje al final
textoFinal=Label(raiz)
textoFinal.pack()

#---------------------------------------------------------------------------------------
#IMAGENES, IMAGENES CON EL NUMERO DE CADA OPCION DE LOS CHECK BUTTONS

foto1 = PhotoImage(file="1.png")
foto1Label= Label(miFrame3, image=foto1)
foto1Label.grid(row=2,column=0)

foto2 = PhotoImage(file="2.png")
foto2Label= Label(miFrame3, image=foto2)
foto2Label.grid(row=2,column=1)

foto3 = PhotoImage(file="3.png")
foto3Label= Label(miFrame3, image=foto3)
foto3Label.grid(row=2,column=2)

#---------------------------------------------------------------------------------------
#BOTONES

botonEnvio=Button(raiz, text = "Borrar todo", command=codigoBoton)
#raiz: para ubicarlo fuera del frame, asi no se sigue con la organizacion modo grilla
#command le asigna la funcion codigoBoton al boton
botonEnvio.pack()


#---------------------------------------------------------------------------------------



raiz.mainloop()
