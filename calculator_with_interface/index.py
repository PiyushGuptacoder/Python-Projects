import tkinter as tk
root=tk.Tk()
root.title("Calculator")
root.geometry("280x350")
root.resizable(False,False)

def click(event):
    global reset_display
    value=input_display.get()
    btn_txt=event.widget["text"]
    if btn_txt=="c":
        input_display.delete(0,tk.END)
        input_display.insert(tk.END,"0")
    elif btn_txt=="=":
        try:
            result=eval(value)
            input_display.delete(0,tk.END)
            input_display.insert(tk.END,str(result))
        



        except Exception as e:
            input_display.delete(0,tk.END)
            result="Error"
            input_display.insert(tk.END,str(result))
            
    elif btn_txt=="1":
        if value=="0":
            input_display.delete(0,tk.END)
        input_display.insert(tk.END,1)
    elif btn_txt=="2":
        if value=="0":
            input_display.delete(0,tk.END)
        input_display.insert(tk.END,2)
    elif btn_txt=="3":
        if value=="0":
            input_display.delete(0,tk.END)
        input_display.insert(tk.END,3)
    elif btn_txt=="4":
        if value=="0":
            input_display.delete(0,tk.END)
        input_display.insert(tk.END,4)
    elif btn_txt=="5":
        if value=="0":
            input_display.delete(0,tk.END)
        input_display.insert(tk.END,5)
    elif btn_txt=="6":
        if value=="0":
            input_display.delete(0,tk.END)
        input_display.insert(tk.END,6)
    elif btn_txt=="7":
        if value=="0":
            input_display.delete(0,tk.END)
        input_display.insert(tk.END,7)
    elif btn_txt=="8":
        if value=="0":
            input_display.delete(0,tk.END)
        input_display.insert(tk.END,8)
    elif btn_txt=="9":
        if value=="0":
            input_display.delete(0,tk.END)
        input_display.insert(tk.END,9)
    elif btn_txt=="0":
        if value=="0":
            input_display.delete(0,tk.END)
        input_display.insert(tk.END,0)
    elif btn_txt=="+":
        if value=="0":
            input_display.delete(0,tk.END)
        input_display.insert(tk.END,"+")
    elif btn_txt=="-":
        if value=="0":
            input_display.delete(0,tk.END)
        input_display.insert(tk.END,'-')
    elif btn_txt=="*":
        if value=="0":
            input_display.delete(0,tk.END)
        input_display.insert(tk.END,'*')
    elif btn_txt=="/":
        if value=="0":
            input_display.delete(0,tk.END)
        input_display.insert(tk.END,'/')
    elif btn_txt=="(":
        if value=="0":
            input_display.delete(0,tk.END)
        input_display.insert(tk.END,'(')
    elif btn_txt==")":
        if value=="0":
            input_display.delete(0,tk.END)
        input_display.insert(tk.END,')')
    elif btn_txt==".":
        # if value=="0":
        #     input_display.delete(0,tk.END)
        input_display.insert(tk.END,'.')





input_display=tk.Entry(root,bg="cyan",font=("Arial",20),justify="right",borderwidth=5)
input_display.pack(padx=15,pady=15)
buttons=[["c","(",")","/"],
         ["7","8","9","-"],
         ["4","5","6","+"],
         ["1","2","3","*"],
         [".","0","%","="]]
btn_frame=tk.Frame(root)
btn_frame.pack(padx=10,pady=10)
for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        btn=tk.Button(btn_frame,width=4,height=1,text=buttons[i][j],bg="grey",font=("Arial",15))
        btn.grid(row=i,column=j,padx=5,pady=5)
        btn.bind("<Button-1>",click)
input_display.insert(tk.END,"0")

root.mainloop()