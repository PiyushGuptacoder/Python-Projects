import csv
import os
import tkinter as tk

root=tk.Tk()
root.title("Expense Tracker")


# """
# This script is an expense tracker that allows users to manage their expenses by adding, updating, viewing, and calculating total expenses.
# Functio"ns:
# - add_expanses(): Prompts the user for expense details (date, category, quantity, amount) and appends this information to a CSV file.
# The script checks for the existence of a CSV file named 'expenase.csv'. If the file does not exist, it creates one and writes the header row.
# The main loop presents a menu to the user with options to add expenses, update expenses, view expenses, show total expenses, or exit the program.
# The mode="a" in the open function is used to open the file in append mode, which allows new data to be added to the end of the file without overwriting the existing content.
# """

filename="expenase.csv"

if not os.path.exists(filename):
    with open (filename,mode="w",newline="")as file:
        writer=csv.writer(file)
        writer.writerow(["DATE","CATEGORY","QUANTITY","AMOUNT","TOTAL"])

def add_expanses():
    date=str(input("Enter  the date in format (DD/MM/YYYY) "))
    category=str(input("Enter the category "))
    qty=int(input("Enter the quantity "))
    amt=int(input("Enter the amount "))


    # date_label=tk.Label(root,text="Enter date")
    # date_label.pack()
    # date=tk.Entry(root)
    # date.pack()

    # category_label=tk.Label(root,text="Enter category")
    # category_label.pack()
    # category=tk.Entry(root)
    # category.pack()

    # qty_label=tk.Label(root,text="Enter quantity")
    # qty_label.pack()            
    # qty=tk.Entry(root)
    # qty.pack()

    # amt_label=tk.Label(root,text="Enter amount")
    # amt_label.pack()
    # amt=tk.Entry(root)
    # amt.pack()

    # add_button=tk.Botton(root,text="Add",command=on_add)

    tot_amt=qty*amt


    with open(filename,mode="a",newline="") as file:
        writer=csv.writer(file)
        writer.writerow([date,category,qty,amt,tot_amt])
        print("Expanses added sucessfully")



def update_expanses():
    with open (filename,mode="r",newline="") as file:
        reader=csv.reader(file)
        data=list(reader)
    i=int(input("Enter the row to be updated  "))
    c=input("Select  column to be updated (0.Date 1.Category 2.Quantity 3.Amount)   ")
    new_value=input('Enter the new value("date","cat",qty,amt):')
    # data[1][0]="01/02/2026"
    co=int(c)
    data[i][co]=new_value 

    with open (filename,mode="w",newline="") as file:
        writer=csv.writer(file)
        writer.writerows(data)
    print("Expanses updated sucessfully")


def view_expenses():
    with open(filename,mode="r") as file:
        reader=csv.reader(file)
        data=list(reader)
        for row in data:
            print(f"{row[0]:<15} {row[1]:<15} {row[2]:<10} {row[3]:<10} {row[4]:<10}")
        # print(data)

def total_expanses():
    with open (filename,mode="r",newline="") as file:
        reader=csv.reader(file)
        data=list(reader)
        tot=0
        for i in range (1,len(data)):            
            v1=int(data[i][4])
            tot=tot+v1
        print("Total Exapanses is  ",tot)
         
while True:
    print("1.Add expanses")
    print("2.Update Expenses")
    print("3.View Expenses")
    print("4.Show total expenses")
    print("5.Exit")
    
    # Try:
    choice=int(input("Enter your chooice "))
    
    # except ValueError:
    #     print("Invalid input,please enter a number")
    #     continue            

    if choice==1:
        add_expanses()
    elif choice==2:
        update_expanses()
    elif choice==3:
        view_expenses()
    elif choice==4:
        total_expanses()
    elif choice==5:
        break
    else:
        print("Invalid input,please try again")

