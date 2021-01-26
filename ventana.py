import tkinter as tk
import mcd as m
from mcd import maximoDivisor
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

class ventana:
    def enviar(self):
        entry1 = self.a.get()
        entry2 = self.b.get()
        entry3 = self.c.get()
        entry4 = self.d.get()

        if not entry1 or not entry2 or not entry3  or not entry4:
            messagebox.showinfo(message="Uno o mas espacios estan vacios", title="Alerta")
        else:
            mc = m.maximoDivisor()
            self.texto.config(state = NORMAL)
            self.texto.delete('1.0',END)
            b,e = mc.prueba(int(entry1),int(entry2))
            c,e = mc.prueba(int(entry3),int(entry4))
            a,e = mc.prueba(b,c)
            self.texto.insert(INSERT,e)
            
            x = "La combinación lineal entre " + entry1 + " y " + entry2 + " es: \n"
            r1 = mc.extended_euclid_gcd(int(entry1),int(entry2))
            res1 = entry1 + "(" + str(r1[1]) +")" + " + " + entry2 + "(" +str(r1[2])+ ")" + " = " + str(r1[0]) + "\n"
            self.texto.insert(INSERT,x)
            self.texto.insert(INSERT,res1)
            
            x = "La combinación lineal entre " + entry3 + " y " + entry4 + " es: \n"
            r2 = mc.extended_euclid_gcd(int(entry3),int(entry4))
            res2 = entry3 + "(" + str(r2[1]) +")" + " + " + entry4 + "(" +str(r2[2])+ ")" + " = " + str(r2[0]) + "\n"
            self.texto.insert(INSERT,x)
            self.texto.insert(INSERT,res2)
            
            x = "La combinación lineal entre " + str(b) + " y " + str(c) + " es: \n"
            r3 = mc.extended_euclid_gcd(b,c)
            res3 = str(b) + "(" + str(r3[1]) +")" + " + " + str(c) + "(" +str(r3[2])+ ")" + " = " + str(r3[0]) + "\n"
            self.texto.insert(INSERT,x)
            self.texto.insert(INSERT,res3)

            x = "La combinacion lineal entre todos los numeros es: \n"
            res4 = "(" + entry1 + "(" + str(r1[1]) +")" + " + " + entry2 + "(" +str(r1[2])+ ")" + ")" + "(" + str(r3[1]) +")" + " + " + "(" + entry3 + "(" + str(r2[1]) +")" + " + " + entry4 + "(" +str(r2[2])+ ")" + ")" + "(" +str(r3[2])+ ")" + " = " + str(r3[0]) + "\n"
            self.texto.insert(INSERT,x)
            self.texto.insert(INSERT,res4)
            
            b = "El mcd es: " + str(a)
            self.texto.insert(INSERT,b)
            self.texto.config(state = DISABLED)

        
    def __init__(self):
        ventana = tk.Tk()
        ventana.geometry("500x500")

        labelNombre = tk.Label(ventana, text = "Cristhian Camilo Martinez Rey - 20181020021")
        labelNumeros = tk.Label(ventana, text = "Teoria de numeros")
        labelEuclides = tk.Label(ventana, text = "Algoritmo de Euclides")
        labelNombre.place(x=10,y=10)
        labelNumeros.place(x=10,y=30)
        labelEuclides.place(x=180,y=50)

        validate_entry = lambda text: text.isdecimal()
        
        labelPrimer = tk.Label(ventana, text = "Primer numero")
        labelPrimer.place(x=50,y=80)
        self.a  = ttk.Entry(validate="key",validatecommand=(ventana.register(validate_entry), "%S"))
        self.a.place(x=50,y=100)
        labelSegundo = tk.Label(ventana, text = "Segundo numero")
        labelSegundo.place(x=300,y=80)
        self.b = ttk.Entry(validate="key",validatecommand=(ventana.register(validate_entry), "%S"))
        self.b.place(x=300,y=100)
        labelTercero = tk.Label(ventana, text = "Tercer numero")
        labelTercero.place(x=50,y=130)
        self.c  = ttk.Entry(validate="key",validatecommand=(ventana.register(validate_entry), "%S"))
        self.c.place(x=50,y=150)
        labelCuarto= tk.Label(ventana, text = "Cuarto numero")
        labelCuarto.place(x=300,y=130)
        self.d  = ttk.Entry(validate="key",validatecommand=(ventana.register(validate_entry), "%S"))
        self.d.place(x=300,y=150)

        boton = tk.Button(ventana, text = "Enviar", command = self.enviar)
        boton.place(x=220,y=160)

        self.texto = tk.Text(ventana, width = 50, height = 15)
        self.texto.place(x=50,y=200)
        self.texto.config(state = DISABLED)

        
        


