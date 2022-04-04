# Hecho por Rafael Alejandro Beltran Santos
from tkinter import *

window = Tk()
window.title("Calculadora Ley del Ohm")
window.geometry("325x250")

def select():
    option = opcion.get()

    if option == 1:   # Voltaje
        voltage(input_resistance.get(), input_intensity.get())
    if option == 2:   # Resistencia
        intensity(input_voltage.get(), input_resistance.get())
    if option == 3:   # Intensidad
        resistance(input_voltage.get(), input_intensity.get())

opcion = IntVar()
# Menu de opciones
voltage = Radiobutton(window, text="Voltaje", variable=opcion, value=1, command=select).place(x=30, y= 35, anchor="center")
intensity = Radiobutton(window, text="Intensidad", variable=opcion, value=2, command=select).place(x=42, y=55, anchor="center")
resistance = Radiobutton(window, text="Resistencia", variable=opcion, value=3, command=select).place(x=44, y=75, anchor="center")

menu = Label(window, text="Calcular:")
menu.config(width=10)
menu.place(x=30, y=15, anchor="center")

def menor_0(value, mili, micro, nano):
    if value <= 0.999 and value > 0.000999:
        operacion = value * 1000
        return f"{operacion:.2f} {mili}"

    elif value <= 0.000999 and value > 0.000000999:
        operacion = value * 1000000
        return f"{operacion:.2f} {micro}"
    
    elif value <= 0.000000999:
        operacion = value * 1000000000
        return f"{operacion:.2f} {nano}"

def mayor_1000(value, kilo, mega, giga):
    if value >= 1000 and value < 1000000:
        operacion = value / 1000
        return f"{operacion:.2f} {kilo}"

    elif value >= 1000000 and value < 1000000000:
        operacion = value / 1000000
        return f"{operacion:.2f} {mega}"
    
    elif value >= 1000000000:
        operacion = value / 1000000000
        return f"{operacion:.2f} {giga}"
        
def voltage(r, i):
    resistance = float(r)
    intensity = float(i)
    v = resistance * intensity
    if v <= 0.999:
        if v == 0:
            input_voltage.delete(0, END)
            input_voltage.insert(0, f"{v} V")
        else:
            input_voltage.delete(0, END)
            input_voltage.insert(0, f"{menor_0(v, 'mV', 'µV', 'nV')}")
    elif v >= 1000:
        input_voltage.delete(0, END)
        input_voltage.insert(0, f"{mayor_1000(v, 'kV', 'MV', 'GV')}")
    else:
        input_voltage.delete(0, END)
        input_voltage.insert(0, f"{v} V")

    power = v * intensity
    if power <= 0.999:
        if power == 0:
            input_power.delete(0, END)
            input_power.insert(0, f"{power:.2f} W")
        else:
            input_power.delete(0, END)
            input_power.insert(0, f"{menor_0(power, 'mW', 'µW', 'nW')}")
    elif power >= 1000:
        input_power.delete(0, END)
        input_power.insert(0, f"{mayor_1000(power, 'kW', 'MW', 'GW')}")
    else:
        input_power.delete(0, END)
        input_power.insert(0, f"{power:.2f} W")

def intensity(v, r):
    voltage = float(v)
    resistance = float(r)

    try:
        i = voltage / resistance
        if i <= 0.999:
            if i == 0:
                input_intensity.delete(0, END)
                input_intensity.insert(0, f"{i} A")
            else:
                input_intensity.delete(0, END)
                input_intensity.insert(0, f"{menor_0(i, 'mA', 'µA', 'nA')}")
        elif i >= 1000:
            input_intensity.delete(0, END)
            input_intensity.insert(0, f"{mayor_1000(i, 'kA', 'MA', 'GA')}")
        else:
            input_intensity.delete(0, END)
            input_intensity.insert(0, f"{i} A")
        
        power = voltage * i
        if power <= 0.999:
            if power == 0:
                input_power.delete(0, END)
                input_power.insert(0, f"{power:.2f} W")
            else: 
                input_power.delete(0, END)
                input_power.insert(0, f"{menor_0(power, 'mW', 'µW', 'nW')}")
        elif power >= 1000:
            input_power.delete(0, END)
            input_power.insert(0, f"{mayor_1000(power, 'kW', 'MW', 'GW')}")
        else:
            input_power.delete(0, END)
            input_power.insert(0, f"{power} W")

    except ZeroDivisionError:
        input_intensity.delete(0, END)
        input_intensity.insert(0, "INDEFINIDO")
        input_power.delete(0, END)
        input_power.insert(0, "0 W")


def resistance(v, i):
    voltage = float(v)
    intensity = float(i)
    try:
        r = voltage / intensity
        if r <= 0.999:
            if r == 0:
                input_resistance.delete(0, END)
                input_resistance.insert(0, f"{r} Ω")
            else:
                input_resistance.delete(0, END)
                input_resistance.insert(0, f"{menor_0(r, 'mΩ', 'µΩ', 'nΩ')}")
        elif r >= 1000:
            input_resistance.delete(0, END)
            input_resistance.insert(0, f"{menor_0(r, 'kΩ', 'MΩ', 'GΩ')}")
        else:
            input_resistance.delete(0, END)
            input_resistance.insert(0, f"{r} Ω")
        
        power = voltage * intensity
        if power <= 0.999:
            if power == 0:
                input_power.delete(0, END)
                input_power.insert(0, f"{power:.2f} W")
            else:
                input_power.delete(0, END)
                input_power.insert(0, f"{menor_0(power, 'mW', 'µW', 'nW')}")
        elif power >= 1000:
            input_power.delete(0, END)
            input_power.insert(0, f"{mayor_1000(i, 'kW', 'MW', 'GW')}")
        else:
            input_power.delete(0, END)
            input_power.insert(0, f"{power} W")

    except ZeroDivisionError:
        input_resistance.delete(0, END)
        input_resistance.insert(0, "INDEFINIDO")
        input_power.delete(0, END) 
        input_power.insert(0, "0 W")

# Etiqueta y entrada para el valor del voltaje
voltage_label = Label(window, text="Voltaje:").place(x=190, y=15, anchor="center")
input_voltage = Entry(window, width=15)
input_voltage.place(x=222, y=35, anchor="center")
input_voltage.insert(0, "0")


# Etiqueta y entrada para el valor de la intensidad
intensity_label = Label(window, text="Intensidad:").place(x=200, y=65, anchor="center")
input_intensity = Entry(window, width=15)
input_intensity.place(x=222, y=85, anchor="center")
input_intensity.insert(0, "0")

# Etiqueta y entrada para el valor de la resistencia
resistance_label = Label(window, text="Resistencia:").place(x=200, y=115, anchor="center")
input_resistance = Entry(window, width=15)
input_resistance.place(x=222, y=135, anchor="center")
input_resistance.insert(0, "0")

# Etiqueta y entrada para el valor de la potencia
power_label = Label(window, text="Potencia:").place(x=195, y=165, anchor="center")
input_power = Entry(window, width=15)
input_power.place(x=222, y=185, anchor="center")
input_power.insert(0, "0")


# Clean all button
def clean():
    input_voltage.delete(0, END)
    input_intensity.delete(0, END)
    input_resistance.delete(0, END)
    input_power.delete(0, END)
    
    input_voltage.insert(0, "0")
    input_intensity.insert(0, "0")
    input_resistance.insert(0, "0")
    input_power.insert(0, "0")

clean_all = Button(window, text="Clean All", command=clean)
clean_all.place(x=185, y=210)

# Funcion para cuando el usuario elija calcular el voltaje
window.mainloop()
