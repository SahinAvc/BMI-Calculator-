from tkinter import *

#screen
window = Tk()
window.title("BMI Calculator ")
window.minsize(width=300,height=400)

#labels
labelk = Label(text="Kilogram:",font=('Ariel',15,"bold"))
labelk.place(x=50,y=75)

labelb = Label(text="Boy:",font=('Ariel',15,"bold"))
labelb.place(x=96,y=100)

#Entrys
entryk = Entry(width=5)
entryk.place(x=145,y=82)

entryb = Entry(width=5)
entryb.place(x=145,y=108)

#function
def click_button():
    try:
        boy = float(entryb.get()) / 100
        kilo = float(entryk.get())
        BMI = kilo / (boy ** 2)
        sonuc = ""

        if BMI < 18.5:
            sonuc = "Zayıf"
        elif 18.5 <= BMI <= 24.9:
            sonuc = "Optimum Aralık"
        elif 25 <= BMI <= 29.9:
            sonuc = "Fazla Kilolu"
        elif 30 <= BMI <= 34.9:
            sonuc = "Sınıf-1 Obezite"
        elif 35 <= BMI <= 39.9:
            sonuc = "Sınıf-2 Obezite"
        elif BMI >= 40:
            sonuc = "Sınıf-3 Obezite"

        resultLabel.config(text=f"BMI: {round(BMI, 2)}\nDurum: {sonuc}")
    except ValueError:
        resultLabel.config(text="Geçersiz giriş")


resultLabel = Label(text="", font=('Arial', 15, "bold"),fg="green")
resultLabel.place(x=50, y=250)

#button
button = Button(text="Calculate",bg="lightgray",command=click_button)
button.place(x=125,y=150)

window.mainloop()
