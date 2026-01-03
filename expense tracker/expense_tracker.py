import csv
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg

root=tk.Tk()
root.title("Expense Tracker")
root.geometry("400x400")


# """
# This script is an expense tracker that allows users to manage their expenses by adding, updating, viewing, and calculating total expenses.
# Functio"ns:
# - add_Expense(): Prompts the user for expense details (date, category, quantity, amount) and appends this information to a CSV file.
# The script checks for the existence of a CSV file named 'expenase.csv'. If the file does not exist, it creates one and writes the header row.
# The main loop presents a menu to the user with options to add expenses, update expenses, view expenses, show total expenses, or exit the program.
# The mode="a" in the open function is used to open the file in append mode, which allows new data to be added to the end of the file without overwriting the existing content.
# """

filename="expense.csv"

if not os.path.exists(filename):
    with open (filename,mode="w",newline="")as file:
        writer=csv.writer(file)
        writer.writerow(["DATE","CATEGORY","QUANTITY","AMOUNT","TOTAL"])

def add_expenses():
    # date=str(input("Enter  the date in format (DD/MM/YYYY) "))
    # category=str(input("Enter the category "))
    # qty=int(input("Enter the quantity "))
    # amt=int(input("Enter the amount "))
    date_label=tk.Label(root,text="Enter date",fg="red")
    date_label.pack()
    date=tk.Entry(root)
    date.pack()

    category_label=tk.Label(root,text="Enter category",fg="red")
    category_label.pack()
    category=tk.Entry(root)
    category.pack()

    qty_label=tk.Label(root,text="Enter quantity",fg="red")
    qty_label.pack()            
    qty=tk.Entry(root)
    qty.pack()

    amt_label=tk.Label(root,text="Enter amount",fg="red")
    amt_label.pack()
    amt=tk.Entry(root)
    amt.pack()

    def on_add():
        a=int(amt.get())
        q=int(qty.get())
        tot_amt=q*a


        with open(filename,mode="a",newline="") as file:
            writer=csv.writer(file)
            writer.writerow([date.get(),category.get(),qty.get(),amt.get(),tot_amt])
            msg.showinfo("Success","Expense added sucessfully")
        print("Expense added sucessfully")
        
    add_button=tk.Button(root,text="Add",command=on_add)
    add_button.pack()




def update_Expense():
    with open (filename,mode="r",newline="") as file:
        reader=csv.reader(file)
        data=list(reader)
    # i=int(input("Enter the row to be updated  "))
    # c=input("Select  column to be updated (0.Date 1.Category 2.Quantity 3.Amount)   ")
    # new_value=input('Enter the new value("date","cat",qty,amt):')

    row_label=tk.Label(root,text="Enetr row to be updated",fg="red")
    row_label.pack()
    row=tk.Entry(root)
    row.pack()

    column_label=tk.Label(root,text="Enter column to be updated",fg="green")
    column_label.pack()
    column=tk.Entry(root)
    column.pack()
    
    new_value=tk.Label(root,text="Enter new value",fg="green")
    new_value.pack()
    new_value=tk.Entry(root)
    new_value.pack()
    # data[1][0]="01/02/2026"
    def on_update():

        i=int(row.get())
        c=int(column.get())
        data[i][c]=new_value.get()
        # print(data[i][c])

        if  c==2 or c==3:
            data[i][4]=int(data[i][2])*int(data[i][3])
        # elif c==3:
        #     data[i][4]=int(data[i][3])*int(data[i][2])
        else:
            pass
        

        with open (filename,mode="w",newline="") as file:
            writer=csv.writer(file)
            writer.writerows(data)
        msg.showinfo("success","Expense updated sucessfully")
        # print("Expense updated sucessfully")
    update_button=tk.Button(root,text="Update",command=on_update,fg="blue")
    update_button.pack()

def view_expenses(pre_win):
    with open(filename,mode="r") as file:
        reader=csv.reader(file)
        data=list(reader)

        top = tk.Toplevel(root)
        top.title("Expenses")
        text=tk.Text(top,width=60,height=20)
        text.pack()
        # text.insert(tk.END, f"{'DATE':<15} {'CATEGORY':<15} {'QUANTITY':<10} {'AMOUNT':<10} {'TOTAL':<10}\n")

        for row in data:
            # print(f"{row[0]:<15} {row[1]:<15} {row[2]:<10} {row[3]:<10} {row[4]:<10}")
        # print(data)
            text.insert(tk.END, f"{row[0]:<15} {row[1]:<15} {row[2]:<10} {row[3]:<10} {row[4]:<10}\n")
        text.config(state="disabled")  # make it read-only
        pre_win.destroy()


def total_Expense():
    with open (filename,mode="r",newline="") as file:
        reader=csv.reader(file)
        data=list(reader)
        tot=0
        for i in range (1,len(data)):            
            v1=int(data[i][4])
            tot=tot+v1
        print("Total Exapanses is  ",tot)
         
# while True:
    # print("1.Add Expense")
    # print("2.Update Expenses")
    # print("3.View Expenses")
    # print("4.Show total expenses")
    # print("5.Exit")
    
    
choices=["Add Expenses","Update Expenses","View Expenses","Show Total Expenses","Exit"]
# choice=int(input("Enter your chooice "))
task=ttk.Combobox(root,values=choices)
task.pack()

def check_choice():
    choice=task.get()
    print(choice)
    if choice=="Add Expenses":
        add_expenses()
    elif choice=="Update Expenses":
        update_Expense()
    elif choice=="View Expenses":
        view_expenses(root)
    elif choice=="Show Total Expenses":
        total_Expense()
    elif choice=="Exit":
        pass
    else:
        pass
    # else:
    #     print("Invalid input,please try again

submit_button=tk.Button(root,text="Submit",command=check_choice)
submit_button.pack()

root.mainloop()