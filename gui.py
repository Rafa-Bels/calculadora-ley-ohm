from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Calculadora de la Segunda Ley de Newton")

def calculo(event):
    opcion = calcular.get()
    if opcion == "Fuerza":
        fuerza()
    if opcion == "Masa":
        masa()
    if opcion == "Aceleracion":
        aceleracion()

calcular = ttk.Combobox(window, width=10, values=["Fuerza", "Masa", "Aceleracion"], state="readonly")
calcular.current(0)
calcular.bind("<<ComboboxSelected>>", calculo)

fuerza_label = Label(window, text="Fuerza:")
masa_label = Label(window, text="Masa:")
aceleracion_label = Label(window, text="Aceleracion:")

unidad_fuerza = Label(window, text="N")
unidad_masa = Label(window, text="Kg")
unidad_aceleracion = Label(window, text="m/s^2")

fuerza_entry = Entry(window)
masa_entry = Entry(window)
aceleracion_entry = Entry(window)

fuerza_entry.insert(0, "0")
masa_entry.insert(0, "0")
aceleracion_entry.insert(0, "0")

calcular.grid(column=0, row=1, columnspan=2, ipadx=30, pady=15, padx=15)

fuerza_label.grid(column=0, columnspan=2, row=2, ipadx=30, pady=30)
masa_label.grid(column=0, columnspan=2, row=3, ipadx=30)
aceleracion_label.grid(column=0, columnspan=2, row=4, ipadx=30)

fuerza_entry.grid(column=2, row=2, ipadx=20, pady=5, padx=30)
masa_entry.grid(column=2, row=3, ipadx=20, padx=30)
aceleracion_entry.grid(column=2, row=4, ipadx=20, pady=40, padx=30)

unidad_fuerza.grid(column=3, row=2, pady=5, padx=2, ipadx=10)
unidad_masa.grid(column=3, row=3, pady=5, padx=2, ipadx=10)
unidad_aceleracion.grid(column=3, row=4, pady=5, padx=2, ipadx=10)

def fuerza():
    masa = masa_entry.get() 
    masa = float(masa)

    aceleracion = aceleracion_entry.get()
    aceleracion = float(aceleracion)

    fuerza = masa * aceleracion

    fuerza_entry.delete(0, END)
    fuerza_entry.insert(0, f"{fuerza:.3f}")

def masa():
    fuerza = fuerza_entry.get()
    fuerza = float(fuerza)

    aceleracion = aceleracion_entry.get()
    aceleracion = float(aceleracion)

    try:
        masa = fuerza / aceleracion
        masa_entry.delete(0, END)
        masa_entry.insert(0, f"{masa:.2f}")
    except ZeroDivisionError:
        masa_entry.insert(0, "Indefinido")
    
def aceleracion():
    fuerza = fuerza_entry.get()
    fuerza = float(fuerza)

    masa = masa_entry.get()
    masa = float(masa)

    try:
        aceleracion = fuerza / masa
        aceleracion_entry.delete(0, END)
        aceleracion_entry.insert(0, f"{aceleracion:.2f}")
    except ZeroDivisionError:
        aceleracion_entry.insert(0, "Indefinido")
    
def clean_all():
    fuerza_entry.delete(0, END)
    masa_entry.delete(0, END)
    aceleracion_entry.delete(0, END)

    fuerza_entry.insert(0, "0")
    masa_entry.insert(0, "0")
    aceleracion_entry.insert(0, "0")

clean = Button(window, text="Clean All", command=clean_all)
clean.grid(column=3, row=5, pady=5, padx=2, ipadx=10)

window.mainloop()