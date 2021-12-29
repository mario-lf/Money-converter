from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("Money converter")
window.geometry('500x650')
window.minsize(500, 650)
window.maxsize(500, 650)

# couleur boutons
couleurButton = str(994422)

# création de la frame et de la couleur de fond (degradé)
j = 0
r = 0
for i in range(100):
    c = str(222222 + r)
    Frame(window, width=10, height=650, bg='#' + c).place(x=j, y=0)
    j = j + 10
    r = r + 1

# création de la frame blanche
Frame(window, width=350, height=500, bg='white').place(x=80, y=70)


def page1():
    def page2():
        def back():  # Revenir à la première page
            LabelPage2.destroy()
            button_page2.destroy()
            LabelDollars.destroy()
            EntryDollars.destroy()
            DollarsFrame.destroy()
            page1()

        # supprimer les éléments de la premiere page
        button_page1.destroy()
        LabelPage1.destroy()
        LabelYens.destroy()
        EntryYens.destroy()
        YensFrame.destroy()

        # deuxieme page
        LabelPage2 = Label(window, text="E U R O S --> D O L L A R S", bg='white', font=("Comic Sans MS", 13))
        LabelPage2.place(x=140, y=120)
        button_page2 = Button(window, width=20, height=2, text="R E T O U R", border=0, bg='#' + couleurButton,
                              command=back)
        button_page2.place(x=180, y=500)

        # texte et champ d'entrée de "dollars"
        LabelDollars = Label(window, text="Voici le montant convertit en Dollars", bg='white', font=("", 11))
        LabelDollars.place(x=130, y=310)
        EntryDollars = Entry(window, bg='white', border=0, width=20)
        EntryDollars.place(x=190, y=350)
        DollarsFrame = Frame(window, width=122, height=2, bg='#' + couleurButton)
        DollarsFrame.place(x=190, y=366)

        # conversion
        def Dollars_convert(event):
            d = int(EntryEuros.get())
            d2 = d * 2
            EntryDollars.delete(0, END)
            EntryDollars.insert(0, d2)

        # déclenche la conversion lorque la touche entrée est pressée
        window.bind('<Return>', Dollars_convert)

    # premiere page
    LabelPage1 = Label(window, text="E U R O S --> Y E N S", bg='white', font=("Comic Sans MS", 13))
    LabelPage1.place(x=160, y=120)

    # texte et champ d'entrée de "euros"
    LabelEuros = Label(window, text="Entrez le montant en € à convertir", bg='white', font=("", 11))
    LabelEuros.place(x=140, y=180)
    EntryEuros = Entry(window, bg='white', border=0, width=20)
    EntryEuros.place(x=190, y=220)
    Frame(window, width=122, height=2, bg='#' + couleurButton).place(x=190, y=236)
    InformationEuros = Label(window, text="(pressez entrée pour convertir)", bg='white', font=("Comic Sans MS", 8))
    InformationEuros.place(x=165, y=250)

    # texte et champ d'entrée de "yens"
    LabelYens = Label(window, text="Voici le montant convertit en Yens", bg='white', font=("", 11))
    LabelYens.place(x=140, y=310)
    EntryYens = Entry(window, bg='white', border=0, width=20)
    EntryYens.place(x=190, y=350)
    YensFrame = Frame(window, width=122, height=2, bg='#' + couleurButton)
    YensFrame.place(x=190, y=366)

    # conversion
    def Yens_convert(event):
        e = int(EntryEuros.get())
        e2 = e * 129.50
        EntryYens.delete(0, END)
        EntryYens.insert(0, e2)

    # déclenche la conversion lorque la touche entrée est pressée
    window.bind('<Return>', Yens_convert)

    button_page1 = Button(window, width=20, height=2, text="S U I V A N T", border=0, bg='#' + couleurButton,
                          command=page2)
    button_page1.place(x=180, y=500)


# afficher l'image
imageLogo1 = Image.open('logo.png')
imageLogo2 = ImageTk.PhotoImage(imageLogo1)
labelLogo1 = Label(image=imageLogo2, bg='white', width=90, height=90, border=0)
labelLogo1.place(x=205, y=400)

page1()

window.mainloop()