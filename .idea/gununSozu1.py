# Günün Sözü - 2022
from random import choice
from tkinter import *

gununSozleri = ["Zor iş yoktur, başlanmayan iş vardır!", "Dost acı söylemez, yanında olur!", "Diyet her zaman Pazartesi başlar", "Sen bir pizza değilsin, kimseyi mutlu edemezsin!", "En güzel Perşembe sabahları Orçun Hocayla başlar!"]

goster = Tk()

def metinGoster():
    gununSecilenSozu = choice(gununSozleri)
    gununSozu = Label(goster, text=gununSecilenSozu)
    gununSozu.pack()

    # 2 Saniye sonra otomatik olarak sözün yok olması
    #gununSozu.after(2000, gununSozu.destroy)

gununSozuBaslik = Label(goster, text="Günün Sözünü görmek için tıklayınız")
gosterButon = Button(goster, text="Tıkla!!!", command=metinGoster)
gosterKapat = Button(goster, text="Kapat..!", command=quit)
gununSozuBaslik.pack()
gosterButon.pack()
gosterKapat.pack()

goster.mainloop()