#Denarnica

import tkinter as Tk
from tkinter import *
from tkinter import filedialog
import os


class Denarnica():

    def __init__(self, master):

        self.prilivi = []
        self.odlivi = []
        self.promet = []
        self.znesek = DoubleVar(master, value=0)
        self.stanje = DoubleVar(master, value = 0)
        
        menu = Menu(master)
        master.config(menu = menu)

        datoteka = Menu(menu)
        menu.add_cascade(label = 'Datoteka', menu = datoteka)

        datoteka.add_command(label='Shrani...', command = self.shrani_datoteko)
        datoteka.add_command(label='Odpri...', command = self.odpri_datoteko)
        datoteka.add_separator()
        datoteka.add_command(label='IZHOD', command=master.destroy)

        menu.add_command(label = 'Promet', command = self.skupni_promet)
        menu.add_command(label = 'Promet v dobro', command = self.promet_v_dobro)
        menu.add_command(label = 'Promet v breme', command = self.promet_v_breme)
        
        
        
        navodilo = Label(root, text='Vnesite znesek in izberite željeno transakcijo!')
        okence = Entry(master, textvariable = self.znesek)
        gumb_dvig = Button(master, text='DVIG    ', command=self.dvig)
        gumb_polog = Button(master, text= 'POLOG', command = self.polog)
        polje_znesek = Label(master, text='Znesek:')
        polje_stanje = Label(master, text = 'STANJE:')      
        
        navodilo.grid(row=0, column=0)
        okence.grid(row=1, column=1)
        gumb_dvig.grid(row=2, column=1)
        gumb_polog.grid(row=4, column=1)
        polje_znesek.grid(row=1, column=0)
        polje_stanje.grid(row=6, column=0)
        stanje = Label(master, textvariable = self.stanje)
        stanje.grid(row=6, column=1)
        Label(master, text='                   ').grid(row=5, column=1)
                
################################################################################################
        

    def dvig(self):
        znesek_dviga = float(self.znesek.get())
        print(znesek_dviga)
        print(self.stanje)
        if self.stanje.get() - znesek_dviga >= 0:
            self.stanje.set(self.stanje.get()-znesek_dviga)
            self.odlivi.append(znesek_dviga)
            self.promet.append('-' + str(znesek_dviga))
            return self.stanje.get()        
        return False

    def polog(self):
        znesek_pologa = float(self.znesek.get())
        self.stanje.set(self.stanje.get() + znesek_pologa)
        if True:
            self.prilivi.append(znesek_pologa) 
            self.promet.append('+' + str(znesek_pologa))      
        return self.stanje.get()


    def promet_v_dobro(self):
        okno = Toplevel()
        okno.title('Promet v dobro')
        promet = ""
        for znesek in self.prilivi:
            promet = promet + str('+' + str(znesek)+ '\n')
        if len(promet) == 0:
             Message(okno, text='Na računu še ni bilo prilivov.').pack()
             zapri = Button(okno, text='Zapri', command=okno.destroy).pack()
        else:
            Message(okno, text=promet).pack()
            zapri = Button(okno, text='Zapri', command=okno.destroy).pack()
        

    def promet_v_breme(self):
        okno = Toplevel()
        okno.title('Promet v breme')
        promet = ""
        for znesek in self.odlivi:
            promet = promet + str('-' + str(znesek)+ '\n')
        if len(promet) == 0:
             Message(okno, text='Na računu še ni bilo odlivov.').pack()
             zapri = Button(okno, text='Zapri', command=okno.destroy).pack()
        else:
            Message(okno, text=promet).pack()
            zapri = Button(okno, text='Zapri', command=okno.destroy).pack()

    def skupni_promet(self):
        okno = Toplevel()
        okno.title('Promet')
        promet = ""
        for znesek in self.promet:
            promet = promet + str(znesek + '\n')
        if len(promet) == 0:
             Message(okno, text='Na računu še ni bilo prometa.').pack()
             zapri = Button(okno, text='Zapri', command=okno.destroy).pack()
        else:
            Message(okno, text=promet).pack()
            zapri = Button(okno, text='Zapri', command=okno.destroy).pack()



    def odpri_datoteko(self):
        datoteka = filedialog.askopenfilename(initialdir = '/', title = 'Odpri datotoeko', filetypes = (('Text document', '*.txt'), ('all files', '*.*')))
        with open(datoteka,'r') as dat:
            for vrstica in dat:
                if '+' in vrstica:
                    self.prilivi.append(vrstica.strip())
                elif '-' in vrstica:
                    self.odlivi.append(vrstica.strip())
                else:
                    pass

    def shrani_datoteko(self):
        file_out = filedialog.asksaveasfilename(initialdir = '/', title = 'Ime datoteke', filetypes = (('Text document', '*.txt'), ('all files', '*.*')))
        with open(file_out, 'w', encoding='utf8') as dat:
            for znesek in self.prilivi:
                print('+' + str(self.znesek.get()), file = dat)
            for znesek in self.odlivi:
                print('-' + str(self.znesek.get()), file = dat)



root = Tk(className=''' Denarnica ''')
foo = Label(root, text= 'Made by Peter Kranjec')
foo.grid(row=7,column=3)

projekt = Denarnica(root)
root.mainloop()

