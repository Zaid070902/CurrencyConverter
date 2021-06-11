import requests
from tkinter import *
from tkinter import ttk

master = Tk()
master.geometry("500x500")
master.config(bg="#111")
master.title("Currency Converter")
x = StringVar

response = requests.get("https://v6.exchangerate-api.com/v6/eb99cabf5b78d60c6e027261/latest/USD")
data = response.json()

head_lab = Label(master, text="Currency Converter", bg="#111", fg="gold")
head_lab.place(x=200, y=10)

amount_lab = Label(master, text="Enter Amount:", bg="#111", fg="gold")
amount_lab.place(x=50, y=50)

amount_ent = Entry(master, width="14")
amount_ent.place(x=200, y=50)

currency_ent = Entry(master, width="10", textvariable=x)
currency_ent.place(x=350, y=100)

currency_lab = Label(master, text="Select Currency:", bg="#111", fg="gold")
currency_lab.place(x=50, y=100)


def get():
    if comboBox.get() == data['conversion_rates'].keys():
        result = data['conversion_rates'].values()
        currency_ent.config(result)


comboBox = ttk.Combobox(master, width="14", values=list(data['conversion_rates'].keys()), textvariable=x)
comboBox.bind("<<comboBox>>", lambda event: currency_ent.config(text=data['conversion_rates'].values()[x].get()))
comboBox.place(x=200, y=100)


def currency():
    if comboBox.get() != 'USD':
        result = float(amount_ent.get()) / data['conversion_rates'].values()
        amount_lab.config(text=result)


convert_btn = Button(master, text="Convert", width="10", bg="#111", fg="gold", command=currency)
convert_btn.place(x=50, y=150)

convert_lab = Label(master, width="15", bg="gold")
convert_lab.place(x=200, y=150)

print(data)

master.mainloop()
