from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
root = Tk()
root.geometry("900x900")
root.config(bg = "orchid1")
root.title("Traductor Galáctico")

languaje = list(LANGUAGES.values())
title_label = Label(root, text = "TRADUCTOR GALÁCTICO", bg = "sky blue", font = ("Sylfaen",18,"bold","italic"))
title_label.place(relx=0.5, rely=0.1, anchor=CENTER)

input_label = Label(root, text = "Ingresar texto", bg = "sky blue", font = ("Arial", 13, "bold"))
input_label.place(relx=0.02, rely=0.2, anchor=W)

src_lang = ttk.Combobox(root, values = language, width = 22, state = "readonly")
src.lang.place(relx=0.13, rely=0.2, anchor=W)
src_lang.set("spanish")

output_label = Label(root, text = "Output", bg = "sky blue", font = ("Arial", 13, "bold"))
output_label.place(relx=0.81, rely=0.2, anchor=E)
dest_lang = ttk.Combobox(root, values = language, width = 22, state = "readonly")
dest_lang.place(relx=0.98,rely=0.2,anchor=E)
dest_lang.set("Elige el idioma que recibirás")

Input_text = Text(root, font = ("arial 10"), height = 11, wrap = WORD, padx = 5, pady = 5, width = 60, bg = "DarkOrchid1", bd = 0)
Input_text.place(relx=0.02,rely=0.5,anchor=W)
Output_text = Text(root, font = ("arial 10"), height = 11, wrap = WORD, padx = 5, pady = 5, width = 60, bg = "DarkOrchid1", bd = 0)
Output_text.place(relx=0.98,rely=0.5,anchor=W)

trans_btn = Button(root, text = "Traducir", font = ("Arial", 12, "bold"), pady = 5, bg = "chocolate3", activebackground = "goldenrod1", relief = FLAT)
trans_btn.place(relx=0.5, rely=0.85, anchor=CENTER)
footer_label = Label(root, text = "Creado por Diego, y la ayuda de Ivonne", font = ("Arial", 10, "italic"), bg = "light slate blue")
footer_label.place(relx=0.5, rely=0.97, anchor=CENTER)

root.mainloop()