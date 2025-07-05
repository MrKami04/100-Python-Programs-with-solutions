print("😍 --------------------------------- 😍")  

# pip install CurrencyConverter   :  " https://pypi.org/project/CurrencyConverter/"
# a = CurrencyConverter()
# print(a.convert(12,"USD", "INR"))


from currency_converter import CurrencyConverter
import tkinter as tk

window = tk.Tk()
window.geometry("500x360")
a = CurrencyConverter()
def clicked():
    amount = int(enter1.get())
    cur1 = enter2.get()
    cur2 = enter3.get()
    data = a.convert(amount, cur1, cur2)
    label5 = tk.Label(window, text=data, font="Times 18  bold").place(x =200, y=290)

label1 = tk.Label(window, text="Currency-converter", font="Times 25  bold").place(x=100, y=0)
label2 = tk.Label(window, text = "enter amount here:",font="Times 18  bold").place(x=50, y=80)
enter1 = tk.Entry(window)

label3 = tk.Label(window, text = "enter currency:",font="Times 18  bold").place(x=50, y=130)
enter2 = tk.Entry(window)

label4 = tk.Label(window, text = "enter req currency:",font="Times 18  bold").place(x=50, y=180)
enter3 = tk.Entry(window)


enter1.place(x=300, y=90)
enter2.place(x=300, y=140)
enter3.place(x=300, y=190)

button = tk.Button(window, text="click", command= clicked).place(x = 230,y=240)
window.mainloop()



