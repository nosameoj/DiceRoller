import random
import tkinter as tk
import time

root = tk.Tk()
root.geometry('1300x1050')
root.title("Dice Roller")
root.config(bg="#36454F")

advantage = tk.IntVar()
advantage.set(3)

def d20():
    d12_b.config(command="", bg="grey")
    d10_b.config(command="", bg="grey")
    dper_b.config(command="", bg="grey")
    d8_b.config(command="", bg="grey")
    d6_b.config(command="", bg="grey")
    d4_b.config(command="", bg="grey")

    d20_r4.config(text="-",fg="#C3FBF4")

    #print(advantage.get())
    advantage2= advantage.get()

    d20_last_result=0
    d20_last_result1=0
    d20_last_result2 = 0

    if advantage2 == 3: #no advantage
       for i in range(0, 10):
           d20_last_result = random.randint(1, 20)
           d20_r.config(text=d20_last_result, fg="#C3FBF4")
           d20_r.update()
           time.sleep(0.05 + i / 25)
    elif advantage2 == 2 or advantage2 == 1: #disadvantage or advantage to roll 2 dice
        for i in range(0, 10):
            d20_last_result = random.randint(1, 20)
            d20_last_result1 = random.randint(1, 20)
            d20_r.config(text=d20_last_result, fg="#C3FBF4")
            d20_r2.config(text=d20_last_result1, fg="#C3FBF4")
            d20_r.update()
            time.sleep(0.05 + i / 25)


    # d20_last_result = random.choice([1, 20])  # force a 1/20 result
    # d20_r.config(text=d20_last_result, fg="#C3FBF4")
    if advantage2 == 2:
        if d20_last_result <= d20_last_result1:
            d20_last_result2 = d20_last_result
            d20_r4.config(text=d20_last_result2, fg="#C3FBF4")
        else:
            d20_last_result2 = d20_last_result1
            d20_r4.config(text=d20_last_result2, fg="#C3FBF4")


    if advantage2 == 1:
        if d20_last_result >= d20_last_result1:
            d20_last_result2 = d20_last_result
            d20_r4.config(text=d20_last_result2)
        else:
            d20_last_result2 = d20_last_result1
            d20_r4.config(text=d20_last_result2)

    if d20_last_result == 20:
        d20_r.config(fg="lime")
    elif d20_last_result == 1:
        d20_r.config(fg="red")

    if d20_last_result1 == 20:
        d20_r2.config(fg="lime")
    elif d20_last_result1 == 1:
        d20_r2.config(fg="red")

    if d20_last_result2 == 20:
        d20_r4.config(fg="lime")
    elif d20_last_result2 == 1:
        d20_r4.config(fg="red")


    # time.sleep(5)
    # d20_r.config(text="-")
    # d20_r.update()
    d12_b.config(command=d12, bg="#C3FBF4")
    d10_b.config(command=d10, bg="#C3FBF4")
    dper_b.config(command=dper, bg="#C3FBF4")
    d8_b.config(command=d8, bg="#C3FBF4")
    d6_b.config(command=d6, bg="#C3FBF4")
    d4_b.config(command=d4, bg="#C3FBF4")

def add():
    d20_r2.config(text="-")
    d20_r3.config(text="→")
    d20_r4.config(text="-")
    d20_r2.update()

def dis():
    d20_r2.config(text="-")
    d20_r3.config(text="→")
    d20_r4.config(text="-")
    d20_r2.update()

def none():
    d20_r2.config(text="")
    d20_r3.config(text="")
    d20_r4.config(text="")
    d20_r2.update()

def d12():
    d20_b.config(command="", bg="grey")
    d10_b.config(command="", bg="grey")
    dper_b.config(command="", bg="grey")
    d8_b.config(command="", bg="grey")
    d6_b.config(command="", bg="grey")
    d4_b.config(command="", bg="grey")

    for i in range(0, 10):
        d12_last_result = random.randint(1, 12)
        d12_r.config(text=d12_last_result, fg="#C3FBF4")
        d12_r.update()
        time.sleep(0.05 + i / 25)

    # d12_last_result = random.choice([1, 12])  # force a 1/12 result
    # d12_r.config(text=d20_last_result, fg="#C3FBF4")

    if d12_last_result == 12:
        d12_r.config(fg="lime")
    elif d12_last_result == 1:
        d12_r.config(fg="red")
    # time.sleep(5)
    # d12_r.config(text="-")
    # d12_r.update()
    d20_b.config(command=d20, bg="#C3FBF4")
    d10_b.config(command=d10, bg="#C3FBF4")
    dper_b.config(command=dper, bg="#C3FBF4")
    d8_b.config(command=d8, bg="#C3FBF4")
    d6_b.config(command=d6, bg="#C3FBF4")
    d4_b.config(command=d4, bg="#C3FBF4")

def d10():
    d20_b.config(command="", bg="grey")
    d12_b.config(command="", bg="grey")
    dper_b.config(command="", bg="grey")
    d8_b.config(command="", bg="grey")
    d6_b.config(command="", bg="grey")
    d4_b.config(command="", bg="grey")

    for i in range(0, 10):
        d10_last_result = random.randint(1, 10)
        d10_r.config(text=d10_last_result, fg="#C3FBF4")
        d10_r.update()
        time.sleep(0.05 + i / 25)

    # d12_last_result = random.choice([1, 12])  # force a 1/12 result
    # d12_r.config(text=d20_last_result, fg="#C3FBF4")

    if d10_last_result == 8:
        d10_r.config(fg="lime")
    elif d10_last_result == 1:
        d10_r.config(fg="red")
    # time.sleep(5)
    # d12_r.config(text="-")
    # d12_r.update()

    d20_b.config(command=d20, bg="#C3FBF4")
    d12_b.config(command=d12, bg="#C3FBF4")
    dper_b.config(command=dper, bg="#C3FBF4")
    d8_b.config(command=d8, bg="#C3FBF4")
    d6_b.config(command=d6, bg="#C3FBF4")
    d4_b.config(command=d4, bg="#C3FBF4")


def dper():
    d20_b.config(command="", bg="grey")
    d12_b.config(command="", bg="grey")
    d10_b.config(command="", bg="grey")
    d8_b.config(command="", bg="grey")
    d6_b.config(command="", bg="grey")
    d4_b.config(command="", bg="grey")

    for i in range(0, 10):
        dper_last_result = random.choice(['00', '10', '20', '30', '40', '50', '60', '70', '80', '90'])
        dper_r.config(text=dper_last_result, fg="#C3FBF4")
        dper_r.update()
        time.sleep(0.05 + i / 25)

    d20_b.config(command=d20, bg="#C3FBF4")
    d12_b.config(command=d12, bg="#C3FBF4")
    d10_b.config(command=d10, bg="#C3FBF4")
    d8_b.config(command=d8, bg="#C3FBF4")
    d6_b.config(command=d6, bg="#C3FBF4")
    d4_b.config(command=d4, bg="#C3FBF4")


def d8():
    d20_b.config(command="", bg="grey")
    d12_b.config(command="", bg="grey")
    d10_b.config(command="", bg="grey")
    dper_b.config(command="", bg="grey")
    d6_b.config(command="", bg="grey")
    d4_b.config(command="", bg="grey")

    for i in range(0, 10):
        d8_last_result = random.randint(1, 8)
        d8_r.config(text=d8_last_result, fg="#C3FBF4")
        d8_r.update()
        time.sleep(0.05 + i / 25)

    # d12_last_result = random.choice([1, 12])  # force a 1/12 result
    # d12_r.config(text=d20_last_result, fg="#C3FBF4")

    if d8_last_result == 8:
        d8_r.config(fg="lime")
    elif d8_last_result == 1:
        d8_r.config(fg="red")
    # time.sleep(5)
    # d12_r.config(text="-")
    # d12_r.update()

    d20_b.config(command=d20, bg="#C3FBF4")
    d12_b.config(command=d12, bg="#C3FBF4")
    d10_b.config(command=d10, bg="#C3FBF4")
    dper_b.config(command=dper, bg="#C3FBF4")
    d6_b.config(command=d6, bg="#C3FBF4")
    d4_b.config(command=d4, bg="#C3FBF4")

def d6():
    d20_b.config(command="", bg="grey")
    d12_b.config(command="", bg="grey")
    d10_b.config(command="", bg="grey")
    dper_b.config(command="", bg="grey")
    d8_b.config(command="", bg="grey")
    d4_b.config(command="", bg="grey")

    for i in range(0, 10):
        d6_last_result = random.randint(1, 6)
        d6_r.config(text=d6_last_result, fg="#C3FBF4")
        d6_r.update()
        time.sleep(0.05 + i / 25)

    # d12_last_result = random.choice([1, 12])  # force a 1/12 result
    # d12_r.config(text=d20_last_result, fg="#C3FBF4")

    if d6_last_result == 6:
        d6_r.config(fg="lime")
    elif d6_last_result == 1:
        d6_r.config(fg="red")
    # time.sleep(5)
    # d12_r.config(text="-")
    # d12_r.update()

    d20_b.config(command=d20, bg="#C3FBF4")
    d12_b.config(command=d12, bg="#C3FBF4")
    d10_b.config(command=d10, bg="#C3FBF4")
    dper_b.config(command=dper, bg="#C3FBF4")
    d8_b.config(command=d8, bg="#C3FBF4")
    d4_b.config(command=d4, bg="#C3FBF4")


def d4():
    d20_b.config(command="", bg="grey")
    d12_b.config(command="", bg="grey")
    d10_b.config(command="", bg="grey")
    dper_b.config(command="", bg="grey")
    d8_b.config(command="", bg="grey")
    d6_b.config(command="", bg="grey")

    for i in range(0, 10):
        d4_last_result = random.randint(1, 4)
        d4_r.config(text=d4_last_result, fg="#C3FBF4")
        d4_r.update()
        time.sleep(0.05 + i / 25)

    # d12_last_result = random.choice([1, 12])  # force a 1/12 result
    # d12_r.config(text=d20_last_result, fg="#C3FBF4")

    if d4_last_result == 4:
        d4_r.config(fg="lime")
    elif d4_last_result == 1:
        d4_r.config(fg="red")
    # time.sleep(5)
    # d12_r.config(text="-")
    # d12_r.update()

    d20_b.config(command=d20, bg="#C3FBF4")
    d12_b.config(command=d12, bg="#C3FBF4")
    d10_b.config(command=d10, bg="#C3FBF4")
    dper_b.config(command=dper, bg="#C3FBF4")
    d8_b.config(command=d8, bg="#C3FBF4")
    d6_b.config(command=d6, bg="#C3FBF4")


d20_l = tk.Label(root, text="D20", font=("comic sans ms", 64), bg="#36454F", fg="#C3FBF4")
d20_r = tk.Label(root, text="-", font=("comic sans ms", 64), bg="#36454F", fg="#C3FBF4")
d20_r2 = tk.Label(root, text="", font=("comic sans ms", 64), bg="#36454F", fg="#C3FBF4")
d20_r3 = tk.Label(root, text="", font=("comic sans ms", 64), bg="#36454F", fg="#C3FBF4")
d20_r4 = tk.Label(root, text="", font=("comic sans ms", 64), bg="#36454F", fg="#C3FBF4")
d20_b = tk.Button(root, text="Roll", font=("comic sans ms", 32), bg="#C3FBF4", fg="#36454F", command=d20, height=1)


d20_l.grid(row=2, column=5, pady=10, padx=10)
d20_r.grid(row=3, column=5, pady=10, padx=10)
d20_r2.grid(row=3, column=6, pady=10, padx=10)
d20_r3.grid(row=3, column=7, pady=10, padx=10)
d20_r4.grid(row=3, column=8, pady=10, padx=10)
d20_b.grid(row=4, column=5, pady=1, padx=10)

d12_l = tk.Label(root, text="D12", font=("comic sans ms", 64), bg="#36454F", fg="#C3FBF4")
d12_r = tk.Label(root, text="-", font=("comic sans ms", 64), bg="#36454F", fg="#C3FBF4")
d12_b = tk.Button(root, text="Roll", font=("comic sans ms", 32), bg="#C3FBF4", fg="#36454F", command=d12)

d12_l.grid(row=2, column=0, pady=10, padx=10)
d12_r.grid(row=3, column=0, pady=10, padx=10)
d12_b.grid(row=4, column=0, pady=10, padx=10)

d10_l = tk.Label(root, text="D10", font=("comic sans ms", 64), bg="#36454F", fg="#C3FBF4")
d10_r = tk.Label(root, text="-", font=("comic sans ms", 64), bg="#36454F", fg="#C3FBF4")
d10_b = tk.Button(root, text="Roll", font=("comic sans ms", 32), bg="#C3FBF4", fg="#36454F", command=d10)

d10_l.grid(row=2, column=1, pady=10, padx=10)
d10_r.grid(row=3, column=1, pady=10, padx=10)
d10_b.grid(row=4, column=1, pady=10, padx=10)

dper_l = tk.Label(root, text="D%", font=("comic sans ms", 64), bg="#36454F", fg="#C3FBF4")
dper_r = tk.Label(root, text="-", font=("comic sans ms", 64), bg="#36454F", fg="#C3FBF4")
dper_b = tk.Button(root, text="Roll", font=("comic sans ms", 32), bg="#C3FBF4", fg="#36454F", command=dper)

dper_l.grid(row=2, column=2, pady=10, padx=10)
dper_r.grid(row=3, column=2, pady=10, padx=10)
dper_b.grid(row=4, column=2, pady=10, padx=10)

d8_l = tk.Label(root, text="D8", font=("comic sans ms", 64), bg="#36454F", fg="#C3FBF4")
d8_r = tk.Label(root, text="-", font=("comic sans ms", 64), bg="#36454F", fg="#C3FBF4")
d8_b = tk.Button(root, text="Roll", font=("comic sans ms", 32), bg="#C3FBF4", fg="#36454F", command=d8)

d8_l.grid(row=5, column=0, pady=10, padx=10)
d8_r.grid(row=6, column=0, pady=10, padx=10)
d8_b.grid(row=7, column=0, pady=10, padx=10)

d6_l = tk.Label(root, text="D6", font=("comic sans ms", 64), bg="#36454F", fg="#C3FBF4")
d6_r = tk.Label(root, text="-", font=("comic sans ms", 64), bg="#36454F", fg="#C3FBF4")
d6_b = tk.Button(root, text="Roll", font=("comic sans ms", 32), bg="#C3FBF4", fg="#36454F", command=d6)

d6_l.grid(row=5, column=1, pady=10, padx=10)
d6_r.grid(row=6, column=1, pady=10, padx=10)
d6_b.grid(row=7, column=1, pady=10, padx=10)

d4_l = tk.Label(root, text="D4", font=("comic sans ms", 64), bg="#36454F", fg="#C3FBF4")
d4_r = tk.Label(root, text="-", font=("comic sans ms", 64), bg="#36454F", fg="#C3FBF4")
d4_b = tk.Button(root, text="Roll", font=("comic sans ms", 32), bg="#C3FBF4", fg="#36454F", command=d4)

d4_l.grid(row=5, column=2, pady=10, padx=10)
d4_r.grid(row=6, column=2, pady=10, padx=10)
d4_b.grid(row=7, column=2, pady=10, padx=10)

filler = filler2 = filler3 = tk.Label(root, text="  ", font=("comic sans ms", 64), bg="#36454F")
filler.grid(row=2, column=4)
filler2.grid(row=3, column=4)
filler3.grid(row=4, column=4)

plusadvantage = tk.Radiobutton(root, text="Advantage", variable=advantage, value=1, font=("comic sans ms", 16), bg="#36454F", fg="#C3FBF4", selectcolor="#36454F", command=add)
disadvantage = tk.Radiobutton(root, text="Disadvantage", variable=advantage, value=2, font=("comic sans ms", 16), bg="#36454F", fg="#C3FBF4", selectcolor="#36454F", command=dis)
noadvantage = tk.Radiobutton(root, text="No advantage modifier", variable=advantage, value=3, font=("comic sans ms", 16), bg="#36454F", fg="#C3FBF4", selectcolor="#36454F", command=none)


plusadvantage.place(x=760, y=300)
disadvantage.place(x=760, y=330)
noadvantage.place(x=760, y=360)

if __name__ == '__main__':
    root.mainloop()
