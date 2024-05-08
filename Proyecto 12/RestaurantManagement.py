from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def teclear_boton(numero):
    global operador
    operador = operador+numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END,operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0,END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(0,resultado)
    operador = ''

def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get()=='0':
                cuadros_comida[x].delete(0,END)
            cuadros_comida[x].focus()
        elif variables_comida[x].get() == 0:
            texto_comida[x].set('0')
            cuadros_comida[x].config(state=DISABLED)
        x += 1

    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        elif variables_bebida[x].get() == 0:
            texto_bebida[x].set('0')
            cuadros_bebida[x].config(state=DISABLED)
        x += 1

    x = 0
    for c in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0, END)
            cuadros_postre[x].focus()
        elif variables_postre[x].get() == 0:
            texto_postre[x].set('0')
            cuadros_postre[x].config(state=DISABLED)
        x += 1

def total():
    sub_total_comida = 0
    p=0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + float(cantidad.get()) * precios_comida[p]
        p+=1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + float(cantidad.get()) * precios_bebida[p]
        p += 1

    sub_total_postres = 0
    p = 0
    for cantidad in texto_postre:
        sub_total_postres = sub_total_postres + float(cantidad.get()) * precios_postres[p]
        p += 1

    subtotal = sub_total_comida+sub_total_bebida+sub_total_postres
    impuestos = subtotal*0.07
    total = subtotal + impuestos

    var_costo_comida.set((f'${round(sub_total_comida,2)}'))
    var_costo_bebida.set((f'${round(sub_total_bebida, 2)}'))
    var_costo_postre.set((f'${round(sub_total_postres, 2)}'))
    var_subtotal.set((f'${round(subtotal,2)}'))
    var_impuesto.set(f'${round(impuestos,2)}')
    var_total.set(f'${round(total,2)}')

def recibo():
    texto_recibo.delete(1.0,END)
    num_recibo = f'N# - {random.randint(0,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END,f'Datos: \t{num_recibo}\t{fecha_recibo}\n')
    texto_recibo.insert(END,f'*'*66+'\n')
    texto_recibo.insert(END,'Items \t\tCant.\tCosto Items\n')
    texto_recibo.insert(END,f'-'*78)

    x= 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END,f'{lista_comidas[x].capitalize()}\t\t{comida.get()}\t${round(int(comida.get())*precios_comida[x],2)}\n')
        x+=1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END,
                                f'{lista_bebidas[x].capitalize()}\t\t{bebida.get()}\t${round(int(bebida.get()) * precios_bebida[x], 2)}\n')
        x += 1

    x = 0
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END,
                                f'{lista_postres[x].capitalize()}\t\t{postre.get()}\t${round(int(postre.get()) * precios_postres[x], 2)}\n')
        x += 1

    texto_recibo.insert(END, f'-' * 78+'\n')
    texto_recibo.insert(END,f'Costo de la comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de la bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo del postre: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 78 + '\n')
    texto_recibo.insert(END, f'Subtotal: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 66 + '\n')
    texto_recibo.insert(END, 'Vuelva pronto')

def guardar():
    info_recibo = texto_recibo.get(1.0,END)
    archivo = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información','Su archivo ha sido guardado')

def resetear():
    texto_recibo.delete(0.1,END)
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)

    for var in variables_comida:
        var.set(0)
    for var in variables_bebida:
        var.set(0)
    for var in variables_postre:
        var.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')

# Iniciarlizar tkinter
aplicacion = Tk()

# Ajustar el tamaño de la ventana - Ajustar a 200+100 si es sola una pantalla
aplicacion.geometry('1230x630+2300+150')

# No se podrá maximizar
aplicacion.resizable(0, 0)

#titulo de la ventana
aplicacion.title('Restaurante - Sistema de Facturación')

# Fondo de la ventana, tomar un color de la página
# https://es.wikibooks.org/wiki/Python/Interfaz_gr%C3%A1fica_con_Tkinter/Los_nombres_de_los_colores

aplicacion.config(bg='AntiqueWhite')

# panel superior
panel_superior = Frame(aplicacion, bg='black', bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# etiqueta de titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturación', fg='azure4',
                        font=("Segoe UI", 58, "normal"), bg='AntiqueWhite', width=22)
etiqueta_titulo.grid(row=0, column=0)

# Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel de costos
panel_costos = Frame(panel_izquierdo, bg='azure4', bd=1, relief=FLAT, padx=101)
panel_costos.pack(side=BOTTOM)

#Panel comida
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Segoe UI', 17, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Segoe UI', 17, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# Panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Segoe UI', 17, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# Panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Panel de calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='AntiqueWhite')
panel_calculadora.pack()

# Panel de recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='AntiqueWhite')
panel_recibo.pack()

# Panel de botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='AntiqueWhite')
panel_botones.pack()

# Lista de productos
lista_comidas = ['Ensalada', 'Pizza', 'Hamburguesa', 'Hot Dogs', 'Hot cakes', 'Burritos', 'Tacos', 'Flautas']
lista_bebidas = ['Agua', 'Soda', 'jugo', 'cola', 'vino', 'Vodka', 'Cerveza', 'Whisky']
lista_postres = ['Pastel', 'Fruta', 'Brownies', 'Flan', 'Mousse', 'Batidos', 'Milkshakes', 'Helado']

# Generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    # Crear checkbuttons
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Segoe UI', 17, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)

    # Crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Segoe UI', 16, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)
    contador += 1

# Generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []

contador = 0
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Segoe UI', 17, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador,
                column=0,
                sticky=W)

    # Crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Segoe UI', 16, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)
    contador += 1

variables_postre = []
cuadros_postre = []
texto_postre = []
contador = 0
for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Segoe UI', 17, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postre[contador],
                         command=revisar_check)
    postre.grid(row=contador,
                column=0,
                sticky=W)

    # Crear los cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres,
                                     font=('Segoe UI', 16, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador,
                                  column=1)
    contador += 1

# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# etiquetas de costo y entradas comida
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Segoe UI', 12, 'bold'),
                              bg='azure4',
                              fg='White')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Segoe UI', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

# etiquetas de costo y entradas bebida
etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebida',
                              font=('Segoe UI', 12, 'bold'),
                              bg='azure4',
                              fg='White')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Segoe UI', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

# etiquetas de costo y entradas
etiqueta_costo_postre = Label(panel_costos,
                              text='Costo Postre',
                              font=('Segoe UI', 12, 'bold'),
                              bg='azure4',
                              fg='White')
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costos,
                           font=('Segoe UI', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)

# etiquetas de subtotal
etiqueta_subtotal = Label(panel_costos,
                          text='Subtotal',
                          font=('Segoe UI', 12, 'bold'),
                          bg='azure4',
                          fg='White')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                       font=('Segoe UI', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

# etiquetas de impuestp
etiqueta_impuesto = Label(panel_costos,
                          text='Impuestos',
                          font=('Segoe UI', 12, 'bold'),
                          bg='azure4',
                          fg='White')
etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = Entry(panel_costos,
                       font=('Segoe UI', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_impuesto)
texto_impuesto.grid(row=1, column=3, padx=41)

# etiquetas de impuesto
etiqueta_total = Label(panel_costos,
                       text='Total',
                       font=('Segoe UI', 12, 'bold'),
                       bg='azure4',
                       fg='White')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                    font=('Segoe UI', 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

# Botones
botones = ['Total', 'Recibo', 'Guardar', 'Resetear']
botones_creados = []

columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Segoe UI', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=10)
    botones_creados.append(boton)
    boton.grid(row=0,
               column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# Area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Segoe UI', 12, 'bold'),
                    bd=1,
                    width=52,
                    height=10)
texto_recibo.grid(row=0, column=0)

# Calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Segoe UI', 16, 'bold'),
                          width=39,
                          bd=1)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)
botones_calculadora = ['7', '8', '9', '+',
                       '4', '5', '6', '-',
                       '1', '2', '3', 'x',
                       'Resultado', 'Borrar', '0', '/', ]
botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Segoe UI',15, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)
    boton.grid(row=fila,
               column=columna)
    botones_guardados.append(boton)
    if columna == 3:
        fila += 1
    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda : teclear_boton('7'))
botones_guardados[1].config(command=lambda : teclear_boton('8'))
botones_guardados[2].config(command=lambda : teclear_boton('9'))
botones_guardados[3].config(command=lambda : teclear_boton('+'))
botones_guardados[4].config(command=lambda : teclear_boton('4'))
botones_guardados[5].config(command=lambda : teclear_boton('5'))
botones_guardados[6].config(command=lambda : teclear_boton('6'))
botones_guardados[7].config(command=lambda : teclear_boton('-'))
botones_guardados[8].config(command=lambda : teclear_boton('1'))
botones_guardados[9].config(command=lambda : teclear_boton('2'))
botones_guardados[10].config(command=lambda : teclear_boton('3'))
botones_guardados[11].config(command=lambda : teclear_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : teclear_boton('0'))
botones_guardados[15].config(command=lambda : teclear_boton('/'))



# Evitar el cierre de ventana
aplicacion.mainloop()
