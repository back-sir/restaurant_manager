from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operator = ""
food_prc = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
drnk_prc = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
dsrt_prc = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_button(number):
    global operator
    operator = operator + number
    calc_screen.delete(0, END)
    calc_screen.insert(END, operator)


def erase():
    global operator
    operator = ""
    calc_screen.delete(0, END)


def resolve():
    global operator
    c_result = str(eval(operator))
    calc_screen.delete(0, END)
    calc_screen.insert(0, c_result)
    operator = ""


def check_cb():
    x = 0
    y = 0
    z = 0
    for c in food_sqr:
        if food_var[x].get() == 1:
            food_sqr[x].config(state=NORMAL)
            if food_sqr[x].get() == "0":
                food_sqr[x].delete(0, END)
            food_sqr[x].focus()
        else:
            food_sqr[x].config(state=DISABLED)
            food_text[x].set("0")
        x += 1

    for c in drnk_sqr:
        if drnk_var[y].get() == 1:
            drnk_sqr[y].config(state=NORMAL)
            if drnk_sqr[y].get() == "0":
                drnk_sqr[y].delete(0, END)
            drnk_sqr[y].focus()
        else:
            drnk_sqr[y].config(state=DISABLED)
            drnk_text[y].set("0")
        y += 1

    for c in dsrt_sqr:
        if dsrt_var[z].get() == 1:
            dsrt_sqr[z].config(state=NORMAL)
            if dsrt_sqr[z].get() == "0":
                dsrt_sqr[z].delete(0, END)
            dsrt_sqr[z].focus()
        else:
            dsrt_sqr[z].config(state=DISABLED)
            dsrt_text[z].set("0")
        z += 1


def total():
    food_sub_total = 0
    i = 0
    for q in food_text:
        food_sub_total = food_sub_total + float(q.get()) * food_prc[i]
        i += 1

    drnk_sub_total = 0
    i = 0
    for q in drnk_text:
        drnk_sub_total = drnk_sub_total + float(q.get()) * drnk_prc[i]
        i += 1

    dsrt_sub_total = 0
    i = 0
    for q in dsrt_text:
        dsrt_sub_total = dsrt_sub_total + float(q.get()) * dsrt_prc[i]
        i += 1

    sub_total = food_sub_total + dsrt_sub_total + drnk_sub_total
    tax = sub_total * 0.1
    mtotal = tax + sub_total

    var_prc_food.set(f"€ {round(food_sub_total, 2)}")
    var_prc_drnk.set(f"€ {round(drnk_sub_total, 2)}")
    var_prc_dsrt.set(f"€ {round(dsrt_sub_total, 2)}")
    var_subtotal.set(f"€ {round(sub_total, 2)}")
    var_tax.set(f"€ {round(tax, 2)}")
    var_total.set(f"€ {round(mtotal, 2)}")


def recipe():
    recipe_text.delete(1.0, END)
    recipe_num = f"N# - {random.randint(1000,9999)}"
    date = datetime.datetime.now()
    recipe_date = f"{date.day}/{date.month}/{date.year} - {date.hour}:{date.minute}:{date.second}"
    recipe_text.insert(END, f"Data:\t{recipe_num}\t\t{recipe_date}\n")
    recipe_text.insert(END, f"*" * 60 + "\n")
    recipe_text.insert(END, "Items\t\tQuant.\t\tPrice\n")
    recipe_text.insert(END, f"-" * 72 + "\n")

    x = 0
    for food in food_text:
        if food.get() != "0":
            recipe_text.insert(END, f"{food_list[x]}\t\t{food.get()}\t\t€ {int(food.get()) * food_prc[x]}\n")
        x += 1

    x = 0
    for drnk in drnk_text:
        if drnk.get() != "0":
            recipe_text.insert(END, f"{drinks_list[x]}\t\t{drnk.get()}\t\t€ {int(drnk.get()) * drnk_prc[x]}\n")
        x += 1

    x = 0
    for dsrt in dsrt_text:
        if dsrt.get() != "0":
            recipe_text.insert(END, f"{desserts_list[x]}\t\t{dsrt.get()}\t\t€ {int(dsrt.get()) * dsrt_prc[x]}\n")
        x += 1

    recipe_text.insert(END, f"-" * 72 + "\n")
    recipe_text.insert(END, f"Food price: \t\t\t\t{var_prc_food.get()}\n")
    recipe_text.insert(END, f"Drinks price: \t\t\t\t{var_prc_drnk.get()}\n")
    recipe_text.insert(END, f"Desserts price: \t\t\t\t{var_prc_dsrt.get()}\n")
    recipe_text.insert(END, f"-" * 72 + "\n")
    recipe_text.insert(END, f"Sub-total: \t\t\t\t{var_subtotal.get()}\n")
    recipe_text.insert(END, f"Taxes 10%: \t\t\t\t{var_tax.get()}\n")
    recipe_text.insert(END, f"Meal total: \t\t\t\t{var_total.get()}\n")
    recipe_text.insert(END, f"*" * 60 + "\n")
    recipe_text.insert(END, "We hope to see you soon!")


def save():
    info_recipe = recipe_text.get(1.0, END)
    file = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    file.write(info_recipe)
    file.close()
    messagebox.showinfo("Info", "The recipe have been saved.")


def reset():
    recipe_text.delete(0.1, END)

    for text in food_text:
        text.set("0")
    for text in drnk_text:
        text.set("0")
    for text in dsrt_text:
        text.set("0")

    for sqr in food_sqr:
        sqr.config(state=DISABLED)
    for sqr in drnk_sqr:
        sqr.config(state=DISABLED)
    for sqr in dsrt_sqr:
        sqr.config(state=DISABLED)

    for v in food_var:
        v.set(0)
    for v in drnk_var:
        v.set(0)
    for v in dsrt_var:
        v.set(0)

    var_prc_food.set("")
    var_prc_drnk.set("")
    var_prc_dsrt.set("")
    var_subtotal.set("")
    var_tax.set("")
    var_total.set("")


# tkinter initialization
app = Tk()

# screen size
app.geometry("1280x640+0+0")

# avoid screen maximization
app.resizable(0, 0)

# screen title
app.title("Python Restaurant Manager")

# Background color
app.config(bg="light blue")

# Superior frame
sup_frame = Frame(app, bd=1, relief=FLAT)
sup_frame.pack(side=TOP)

# Title label
title_label = Label(sup_frame, text="Restaurant Manager", fg="azure4", font=("Dosis", 58), bg="light blue", width=20)
title_label.grid(row=0, column=0)

# Left frame
lft_frame = Frame(app, bd=1, relief=FLAT)
lft_frame.pack(side=LEFT)

# Price frame
prc_frame = Frame(lft_frame, bd=1, relief=FLAT, bg="azure4", padx=60)
prc_frame.pack(side=BOTTOM)

# Foods frame
food_frame = LabelFrame(lft_frame, text="Food", font=("Dosis", 19, "bold"), bd=1, relief=FLAT, fg="light blue")
food_frame.pack(side=LEFT)

# Drinks frame
drnk_frame = LabelFrame(lft_frame, text="Drinks", font=("Dosis", 19, "bold"), bd=1, relief=FLAT, fg="light blue")
drnk_frame.pack(side=LEFT)

# Desserts frame
dsrt_frame = LabelFrame(lft_frame, text="Desserts", font=("Dosis", 19, "bold"), bd=1, relief=FLAT, fg="light blue")
dsrt_frame.pack(side=LEFT)

# Right frame
rgt_frame = Frame(app, bd=1, relief=FLAT)
rgt_frame.pack(side=RIGHT)

# Calc frame
calc_frame = Frame(rgt_frame, bd=1, relief=FLAT, bg="light blue")
calc_frame.pack()

# Recipe frame
rcp_frame = Frame(rgt_frame, bd=1, relief=FLAT, bg="light blue")
rcp_frame.pack()

# Button frame
btn_frame = Frame(rgt_frame, bd=1, relief=FLAT, bg="light blue")
btn_frame.pack()

# Product lists
food_list = ["Pizza1", "Pizza2", "Pizza3", "Hamburger", "Hot Dog", "Fries", "Ribs", "Quesadilla"]
drinks_list = ["Water", "Wine", "Beer1", "Beer2", "Soda", "Cola", "Lemonade", "Tea"]
desserts_list = ["Apple Pie", "Cheesecake", "Chocolate cake", "Fruit", "Yogurt", "Coffee", "Macedonia", "Ice cream"]

# Food items generation
food_var = []
food_sqr = []
food_text = []
counter = 0
for f in food_list:
    # Check buttons
    food_var.append("")
    food_var[counter] = IntVar()
    f = Checkbutton(food_frame,
                    text=f.title(),
                    font=("Dosis", 19, "bold"),
                    onvalue=1,
                    offvalue=0,
                    variable=food_var[counter],
                    command=check_cb)
    f.grid(row=counter,
           column=0,
           sticky=W)

    # Entries
    food_sqr.append("")
    food_text.append("")
    food_text[counter] = StringVar()
    food_text[counter].set("0")
    food_sqr[counter] = Entry(food_frame,
                              font=("Dosis", 18, "bold"),
                              bd=1,
                              width=6,
                              state=DISABLED,
                              textvariable=food_text[counter])
    food_sqr[counter].grid(row=counter,
                           column=1)

    counter += 1

# Drinks items generation
drnk_var = []
drnk_sqr = []
drnk_text = []
counter = 0
for d in drinks_list:
    drnk_var.append("")
    drnk_var[counter] = IntVar()
    d = Checkbutton(drnk_frame,
                    text=d.title(),
                    font=("Dosis", 19, "bold"),
                    onvalue=1,
                    offvalue=0,
                    variable=drnk_var[counter],
                    command=check_cb)
    d.grid(row=counter,
           column=0,
           sticky=W)

    # Entries
    drnk_sqr.append("")
    drnk_text.append("")
    drnk_text[counter] = StringVar()
    drnk_text[counter].set("0")
    drnk_sqr[counter] = Entry(drnk_frame,
                              font=("Dosis", 18, "bold"),
                              bd=1,
                              width=6,
                              state=DISABLED,
                              textvariable=drnk_text[counter])
    drnk_sqr[counter].grid(row=counter,
                           column=1)

    counter += 1

# Desserts items generation
dsrt_var = []
dsrt_sqr = []
dsrt_text = []
counter = 0
for ds in desserts_list:
    dsrt_var.append("")
    dsrt_var[counter] = IntVar()
    ds = Checkbutton(dsrt_frame,
                     text=ds.title(),
                     font=("Dosis", 19, "bold"),
                     onvalue=1,
                     offvalue=0,
                     variable=dsrt_var[counter],
                     command=check_cb)
    ds.grid(row=counter,
            column=0,
            sticky=W)

    # Entries
    dsrt_sqr.append("")
    dsrt_text.append("")
    dsrt_text[counter] = StringVar()
    dsrt_text[counter].set("0")
    dsrt_sqr[counter] = Entry(dsrt_frame,
                              font=("Dosis", 18, "bold"),
                              bd=1,
                              width=6,
                              state=DISABLED,
                              textvariable=dsrt_text[counter])
    dsrt_sqr[counter].grid(row=counter,
                           column=1)

    counter += 1

# variables
var_prc_food = StringVar()
var_prc_drnk = StringVar()
var_prc_dsrt = StringVar()
var_subtotal = StringVar()
var_tax = StringVar()
var_total = StringVar()

# Price labels & Entries
prc_lbl_food = Label(prc_frame,
                     text="Food price",
                     font=("Dosis", 12, "bold"),
                     bg="azure4",
                     fg="white")
prc_lbl_food.grid(row=0, column=0)

prc_txt_food = Entry(prc_frame,
                     font=("Dosis", 12, "bold"),
                     bd=1,
                     width=10,
                     state="readonly",
                     textvariable=var_prc_food)
prc_txt_food.grid(row=0, column=1, padx=41)

prc_lbl_drnk = Label(prc_frame,
                     text="Drinks price",
                     font=("Dosis", 12, "bold"),
                     bg="azure4",
                     fg="white")
prc_lbl_drnk.grid(row=1, column=0)

prc_txt_drnk = Entry(prc_frame,
                     font=("Dosis", 12, "bold"),
                     bd=1,
                     width=10,
                     state="readonly",
                     textvariable=var_prc_drnk)
prc_txt_drnk.grid(row=1, column=1, padx=41)

prc_lbl_dsrt = Label(prc_frame,
                     text="Desserts price",
                     font=("Dosis", 12, "bold"),
                     bg="azure4",
                     fg="white")
prc_lbl_dsrt.grid(row=2, column=0)

prc_txt_dsrt = Entry(prc_frame,
                     font=("Dosis", 12, "bold"),
                     bd=1,
                     width=10,
                     state="readonly",
                     textvariable=var_prc_dsrt)
prc_txt_dsrt.grid(row=2, column=1, padx=41)

lbl_subtotal = Label(prc_frame,
                     text="Subtotal",
                     font=("Dosis", 12, "bold"),
                     bg="azure4",
                     fg="white")
lbl_subtotal.grid(row=0, column=2)

txt_subtotal = Entry(prc_frame,
                     font=("Dosis", 12, "bold"),
                     bd=1,
                     width=10,
                     state="readonly",
                     textvariable=var_subtotal)
txt_subtotal.grid(row=0, column=3, padx=41)

lbl_tax = Label(prc_frame,
                text="Taxes",
                font=("Dosis", 12, "bold"),
                bg="azure4",
                fg="white")
lbl_tax.grid(row=1, column=2)

txt_tax = Entry(prc_frame,
                font=("Dosis", 12, "bold"),
                bd=1,
                width=10,
                state="readonly",
                textvariable=var_tax)
txt_tax.grid(row=1, column=3, padx=41)

lbl_total = Label(prc_frame,
                  text="Total",
                  font=("Dosis", 12, "bold"),
                  bg="azure4",
                  fg="white")
lbl_total.grid(row=2, column=2)

txt_total = Entry(prc_frame,
                  font=("Dosis", 12, "bold"),
                  bd=1,
                  width=10,
                  state="readonly",
                  textvariable=var_total)
txt_total.grid(row=2, column=3, padx=41)

# Buttons
buttons = ["total", "recipe", "save", "reset"]
c_buttons = []
columns = 0
for button in buttons:
    button = Button(btn_frame,
                    text=button.title(),
                    font=("Dosis", 14, "bold"),
                    fg="white",
                    bg="azure4",
                    bd=1,
                    width=9)

    c_buttons.append(button)

    button.grid(row=0,
                column=columns)
    columns += 1

c_buttons[0].config(command=total)
c_buttons[1].config(command=recipe)
c_buttons[2].config(command=save)
c_buttons[3].config(command=reset)

# Recipe area
recipe_text = Text(rcp_frame,
                   font=("Dosis", 12, "bold"),
                   bd=1,
                   width=42,
                   height=10)
recipe_text.grid(row=0,
                 column=0)

# calc
calc_screen = Entry(calc_frame,
                    font=("Dosis", 16, "bold"),
                    width=32,
                    bd=1)
calc_screen.grid(row=0, column=0,
                 columnspan=4)

calc_buttons = ["7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "x", "C", "0", "=", "/"]
saved_buttons = []

row = 1
column = 0
for button in calc_buttons:
    button = Button(calc_frame,
                    text=button.title(),
                    font=("Dosis", 16, "bold"),
                    fg="white",
                    bg="azure4",
                    bd=1,
                    width=8)

    saved_buttons.append(button)

    button.grid(row=row,
                column=column)

    if column == 3:
        row += 1

    column += 1

    if column == 4:
        column = 0

saved_buttons[0].config(command=lambda: click_button("7"))
saved_buttons[1].config(command=lambda: click_button("8"))
saved_buttons[2].config(command=lambda: click_button("9"))
saved_buttons[3].config(command=lambda: click_button("+"))
saved_buttons[4].config(command=lambda: click_button("4"))
saved_buttons[5].config(command=lambda: click_button("5"))
saved_buttons[6].config(command=lambda: click_button("6"))
saved_buttons[7].config(command=lambda: click_button("-"))
saved_buttons[8].config(command=lambda: click_button("1"))
saved_buttons[9].config(command=lambda: click_button("2"))
saved_buttons[10].config(command=lambda: click_button("3"))
saved_buttons[11].config(command=lambda: click_button("*"))
saved_buttons[12].config(command=lambda: erase())
saved_buttons[13].config(command=lambda: click_button("0"))
saved_buttons[14].config(command=lambda: resolve())
saved_buttons[15].config(command=lambda: click_button("/"))

# screen working
app.mainloop()
