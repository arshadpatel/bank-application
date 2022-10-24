from tkinter import *
from tkinter import messagebox

def signUpclk():
    try:
        s= un.get()+".txt"
        f=open(s,"r")
        f.close()
        messagebox.showerror("Try Again","Username Already Exists. Try New Username")

    except:
        try:
            int(pw1.get())
            str(pw1.get())
            if(len(pw1.get())<5):
                if(pw1.get()==pw2.get()):
                    lbl1=Label(frame2,text="")
                    lbl1.grid(row=4,column=0,columnspan=2,padx=5,pady=5)
                    lbl1.configure(text="SignUp Successfull !!!",font=('Comic Sans MS',15))
                    s= un.get()+".txt"
                    un.delete(0,END)
                    f=open(s,"w")
                    f.write(pw1.get())
                    pw1.delete(0,END)
                    f.write("\n")
                    f.write("0")
                    f.close()
                else:
                    messagebox.showerror("Password Error","Password did not Match")
            else:
                messagebox.showerror("4-digits Only","Password should be 4 digit Only!!!")
        except:
            messagebox.showerror("Digits Only","Alphabets not Allowed in Password.Try only digits")


def signUp():
    global w2
    w2=Tk()
    global frame2
    frame2=LabelFrame(w2,bd=4,text="SignUp",bg="darkseagreen",font=("comic sans ms",12))
    frame2.pack(padx=20,pady=20)
    Label(frame2,text="Create Username : ",width=15,fg="blue",font=('Comic Sans MS',15)).grid(row=0,column=0,padx=5,pady=5)
    global un
    un=Entry(frame2,width=20,font=('Comic Sans MS',12))
    un.grid(row=0,column=1,padx=5,pady=5)
    Label(frame2,text="Create Password : ",width=15,fg="blue",font=('Comic Sans MS',15)).grid(row=1,column=0,padx=5,pady=5)
    global pw1
    pw1=Entry(frame2,show="*",width=20,font=('Comic Sans MS',12))
    pw1.grid(row=1,column=1,padx=5,pady=5)
    Label(frame2,text="Confirm Password : ",width=15,fg="blue",font=('Comic Sans MS',15)).grid(row=2,column=0,padx=5,pady=5)
    global pw2
    pw2=Entry(frame2,show="*",width=20,font=('Comic Sans MS',12))
    pw2.grid(row=2,column=1,padx=5,pady=5)
    Button(frame2,text="Submit",width=10,bg="lightblue",font=('Comic Sans MS',12),command=signUpclk).grid(row=3,column=0,columnspan=2,padx=5,pady=5)
    Button(frame2,text="Exit",width=10,bg="Antiquewhite2",font=("Comic sans ms",12),command=w2.destroy).grid(row=5,column=0,columnspan=2,padx=5,pady=5)
    w2.mainloop()

def enquiry():
    s= un.get()+".txt"
    f=open(s,"r")
    p=f.readlines()
    f.close()
    templbl=Label(frame2,text="Your Balance is : "+p[1],font=('Comic Sans MS',15))
    templbl.grid(row=4,column=1,padx=5,pady=5)

def deposit():
    def depositFun():
        Label(frame3,text="Amount Deposited Successfully!!!",font=("comic sans ms",15)).grid(row=2,column=0,columnspan=2,padx=5,pady=5)
        Label(frame3,text="Your Deposited Amount : "+da.get()+"/-",font=("comic sans ms",15)).grid(row=3,column=0,columnspan=2,padx=5,pady=5)
        s= un.get()+".txt"
        f=open(s,"r")
        p=f.readlines()
        p[1]= int(p[1])
        da1=int(da.get())
        da.delete(0,END)
        p[1]=p[1]+da1
        p[1]=str(p[1])
        f2=open(s,"w")
        f2.writelines(p)
        f2.close()
        f.close()
        Label(frame3,text="Thank You for Banking!!!",font=("comic sans ms",15)).grid(row=4,column=0,columnspan=2,padx=5,pady=5)
        Button(frame3,text="Exit",width=10,font=("comic sans ms",12),command=w3.destroy).grid(row=5,column=0,columnspan=2,padx=10,pady=10)

    w3=Tk()
    frame3=LabelFrame(w3,bd=4,text="Deposit",font=("comic sans ms",12))
    frame3.pack(padx=20,pady=20)
    Label(frame3,text="Enter Deposit Amount : ",font=("comic sans ms",15)).grid(row=0,column=0,padx=5,pady=5)
    da=Entry(frame3,font=("comic sans ms",15))
    da.grid(row=0,column=1,padx=5,pady=5)
    Button(frame3,text="Deposit",width=10,font=("comic sans ms",12),command=depositFun).grid(row=1,column=0,columnspan=2,padx=10,pady=10)
    w3.mainloop()


def withdraw():
    def withdrawFun():
        s= un.get()+".txt"
        f=open(s,"r")
        p=f.readlines()
        p[1]= int(p[1])
        da1=int(da.get())
        if da1>p[1]:
            messagebox.showerror("Withdraw Request Rejected","Not Enough Balance\nTry again later")
        else:
            p[1]=p[1]-da1
            Label(frame3,text="Amount Withdrawn Successfully!!!",font=("comic sans ms",15)).grid(row=2,column=0,columnspan=2,padx=5,pady=5)
            Label(frame3,text="Your Withdrawn Amount : "+da.get()+"/-",font=("comic sans ms",15)).grid(row=3,column=0,columnspan=2,padx=5,pady=5)
        da.delete(0,END)
        p[1]=str(p[1])
        f2=open(un.get()+".txt","w")
        f2.writelines(p)
        f2.close()
        f.close()

    w3=Tk()
    frame3=LabelFrame(w3,bd=4,text="Withdraw",font=("comic sans ms",12))
    frame3.pack(padx=20,pady=20)
    Label(frame3,text="Enter Amount : ",font=("comic sans ms",15)).grid(row=0,column=0,padx=5,pady=5)
    da=Entry(frame3,font=("comic sans ms",15))
    da.grid(row=0,column=1,padx=5,pady=5)
    Button(frame3,text="Withdraw",width=10,font=("comic sans ms",12),command=withdrawFun).grid(row=1,column=0,padx=10,pady=10)
    Button(frame3,text="Exit",width=10,font=("comic sans ms",12),command=w3.destroy).grid(row=1,column=1,padx=10,pady=10)
    w3.mainloop()

def loginclk():
    s= un.get()+".txt"
    #un.delete(0,END)
    f=open(s,"r")
    p=f.readlines()
    f.close()
    b=pw1.get()
    b=b+"\n"
    pw1.delete(0,END)
    if(b==p[0]):
        lbl1.configure(text="Login Successfull !!!",font=('Comic Sans MS',15))
        Button(frame2,text="Enquiry",width=10,font=('Comic Sans MS',12),command=enquiry).grid(row=3,column=0,padx=10,pady=20)
        Button(frame2,text="Deposit",width=10,font=('Comic Sans MS',12),command=deposit).grid(row=3,column=1,padx=10,pady=20)
        Button(frame2,text="Withdraw",width=10,font=('Comic Sans MS',12),command=withdraw).grid(row=3,column=2,padx=10,pady=20)
        Button(frame2,text="Exit",width=10,font=('Comic Sans MS',12),command=w2.destroy).grid(row=5,column=1,padx=10,pady=10)
    else:
        messagebox.showerror("Error","Invalid Password")
    
def login():
    global w2
    w2=Tk()
    global frame2
    frame2=LabelFrame(w2,bd=4,text="Login",font=("comic sans ms",12))
    frame2.pack(padx=20,pady=20)
    frame2_in=Frame(frame2)
    frame2_in.grid(row=0,column=0,columnspan=3,padx=20,pady=20)
    Label(frame2_in,text="Enter Username : ",font=('Comic Sans MS',15)).grid(row=0,column=0,columnspan=2,padx=5,pady=5)
    global un
    un=Entry(frame2_in,width=20,font=('Comic Sans MS',12))
    un.grid(row=0,column=2,padx=5,pady=5)
    Label(frame2_in,text="Enter Password : ",font=('Comic Sans MS',15)).grid(row=1,column=0,columnspan=2,padx=5,pady=5)
    global pw1
    pw1=Entry(frame2_in,show="*",width=20,font=('Comic Sans MS',12))
    pw1.grid(row=1,column=2,padx=5,pady=5)
    Button(frame2,text="Submit",font=('Comic Sans MS',12),command=loginclk).grid(row=1,column=1,padx=5,pady=5)
    global lbl1
    lbl1=Label(frame2,text="")
    lbl1.grid(row=2,column=1,padx=5,pady=5)
    w2.mainloop()
w=Tk()
#bd--border
frame1=LabelFrame(w,bd=4,text="Welcome to Arshad Banking Services!!!",bg="lightblue2",font=('Comic Sans MS',15))
frame1.pack(padx=20,pady=20)
Label(frame1,text="Select the required option ",fg="Blue",font=('Comic Sans MS',15)).pack(padx=5,pady=5)
Button(frame1,text="SignUp",width=10,bd=2,bg="darkseagreen2",font=('Comic Sans MS',12),command=signUp).pack(padx=5,pady=10)
Button(frame1,text="Login",width=10,bd=2,bg="Lightpink2",font=('Comic Sans MS',12),command=login).pack(padx=5,pady=10)
Button(frame1,text="Exit",width=10,bd=2,bg="Antiquewhite2",font=('Comic Sans MS',12),command=w.destroy).pack(padx=5,pady=10)
w.mainloop()