from tkinter import *
from playsound import playsound

def button_click(numbers):
    global operator
    playsound("../calculator/tit.wav",block=False)
    operator += str(numbers)
    text_input.set(operator)


def button_clear():
    global operator
    operator = ""
    text_input.set("")

def button_equal():
    global operator
    try:
        operator = str(eval(text_input.get()))
        text_input.set(operator)
    except:
        text_input.set("Math Error")

def main ():
    global text_input, operator 
    root = Tk()
    root.title("Calculator")
    root.resizable(height=False,width=False)
    root.minsize(height=220,width=320)
    operator = ""
    text_input = StringVar()
    screen_calc = Entry(root,width=32,font=("arial",20,"bold"),textvariable=text_input,bd=8,bg="aqua",insertwidth=4,justify="right").grid(row=0,columnspan=4)
    
    #hàng 1
    bt7=Button(root,padx=40,bd=8,pady=3,font=("arial",20,"bold"),text="7",fg="black",command=lambda:button_click(7),bg="grey").grid(row=1,column=0)
    bt8=Button(root,padx=40,bd=8,pady=3,font=("arial",20,"bold"),text="8",fg="black",command=lambda:button_click(8),bg="grey").grid(row=1,column=1)
    bt9=Button(root,padx=40,bd=8,pady=3,font=("arial",20,"bold"),text="9",fg="black",command=lambda:button_click(9),bg="grey").grid(row=1,column=2)
    bt_devision =Button(root,padx=41,bd=8,pady=3,font=("arial",20,"bold"),text="/",fg="black",command=lambda:button_click("/"),bg="red").grid(row=1,column=3)
    #hàng 2
    bt4=Button(root,padx=40,bd=8,pady=3,font=("arial",20,"bold"),text="4",fg="black",command=lambda:button_click(4),bg="grey").grid(row=2,column=0)
    bt5=Button(root,padx=40,bd=8,pady=3,font=("arial",20,"bold"),text="5",fg="black",command=lambda:button_click(5),bg="grey").grid(row=2,column=1)
    bt6=Button(root,padx=40,bd=8,pady=3,font=("arial",20,"bold"),text="6",fg="black",command=lambda:button_click(6),bg="grey").grid(row=2,column=2)
    bt_multiplication=Button(root,padx=40,bd=8,pady=3,font=("arial",20,"bold"),text="*",fg="black",command=lambda:button_click("*"),bg="red").grid(row=2,column=3)
    #hàng 3
    bt1=Button(root,padx=40,bd=8,pady=3,font=("arial",20,"bold"),text="1",fg="black",command=lambda:button_click(1),bg="grey").grid(row=3,column=0)
    bt2=Button(root,padx=40,bd=8,pady=3,font=("arial",20,"bold"),text="2",fg="black",command=lambda:button_click(2),bg="grey").grid(row=3,column=1)
    bt3=Button(root,padx=40,bd=8,pady=3,font=("arial",20,"bold"),text="3",fg="black",command=lambda:button_click(3),bg="grey").grid(row=3,column=2)
    bt_subtraction=Button(root,padx=41,bd=8,pady=4,font=("arial",18,"bold"),text="-",fg="black",command=lambda:button_click("-"),bg="red").grid(row=3,column=3)
    #hàng 4
    bt0=Button(root,padx=40,bd=8,pady=3,font=("arial",20,"bold"),text="0",fg="black",command=lambda:button_click(0),bg="grey").grid(row=4,column=0)
    bt_open_bracket=Button(root,padx=42.4,pady=3,font=("arial",20,"bold"),text="(",fg="black",command=lambda:button_click("("),bg="grey").grid(row=4,column=1)
    bt_close_bracket=Button(root,padx=42.4,pady=3,font=("arial",20,"bold"),text=")",fg="black",command=lambda:button_click(")"),bg="grey").grid(row=4,column=2)
    bt_addition=Button(root,padx=38,pady=3,font=("arial",20,"bold"),text="+",fg="black",command=lambda:button_click("+"),bg="red").grid(row=4,column=3)
    #hàng 5
    bt_clear=Button(root,padx=32,bd=8,pady=3,font=("arial",20,"bold"),text="AC",fg="black",command=button_clear,bg="grey").grid(row=5,column=0)
    bt_point=Button(root,padx=42,bd=8,pady=3,font=("arial",20,"bold"),text=".",fg="black",command=lambda:button_click("."),bg="grey").grid(row=5,column=1)
    bt_equal=Button(root,padx=90,bd=8,pady=3,font=("arial",20,"bold"),text="=",fg="black",command=button_equal,bg="orange").grid(row=5,column=2,columnspan=2)
    root.mainloop()


if __name__ == "__main__":
    main()