import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class osztaly:
    def listaadas(* args):
        lista = ('Hétfő', 'Kedd', 'Szerda', 'Csütörtök', 'Péntek', 'Szombat', 'Vasárnap')
        return lista
    def kiiratas(* args):
        #érték kiválasztása
        kivalasztott_ertek = listbox.curselection()
        #megkapjuk a kiválasztott értéket
        kivalasztott_pontosertek = ",".join([listbox.get(i) for i in kivalasztott_ertek])
        if kivalasztott_pontosertek == 'Hétfő':
            uzenet = f'Milyen rossz ez a: {kivalasztott_pontosertek}' + 'i nap.'
        else:
            uzenet = f'Milyen szép ez a: {kivalasztott_pontosertek}' + 'i nap.'

        showinfo(title='Információ', message=uzenet)


#képernyő létrehozása
kepernyo = tk.Tk()

kepernyo.title('Milyen nap van ma?')
kepernyo.geometry('280x80')

valtozo = tk.Variable(value=osztaly.listaadas())

listbox = tk.Listbox(
    kepernyo,
    listvariable=valtozo,
    height=6,
    selectmode=tk.EXTENDED)

listbox.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

#hozzáadunk egy csúszkát amivel tudjuk görgetni a listát
scrollbar = ttk.Scrollbar(
    kepernyo,
    orient=tk.VERTICAL,
    command=listbox.yview
)

listbox['yscrollcommand'] = scrollbar.set

scrollbar.pack(side=tk.LEFT, expand=True, fill=tk.Y)


def kivalasztott(event):
    osztaly.kiiratas()



listbox.bind('<<ListboxSelect>>', kivalasztott)

kepernyo.mainloop()