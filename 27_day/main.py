from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=20, pady=20)

# Labels
iqual = Label(text="is iqual to", font=("Arial", 12))
iqual.grid(column=0, row=1)
iqual.config(padx=5, pady=5)

value_km = Label(text="0", font=("Arial", 12))
value_km.grid(column=1, row=1)
value_km.config(padx=5, pady=5)

miles = Label(text="Miles", font=("Arial", 12))
miles.grid(column=2, row=0)
miles.config(padx=10, pady=10)

# Entry
input_miles = Entry(width=10)
input_miles.grid(column=1, row=0)


# Button
def button_clicked():
    value_km["text"] = round(int(input_miles.get()) * 1.609344)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()
