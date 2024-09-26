#GUI Using Python


from tkinter import *
root=Tk()
text=Text(root)
root.title("EVM")
root.geometry("700x500")
v1=0
v2=0

def voter1():
    global v1
    v1=v1+1
    print("value of v1",v1)

def voter2():
    global v2
    v2=v2+1
    print("value of v2",v2)

def result():
    if(v1>v2):
        Label(root,text="winner:Rajesh",height=2,width=20).grid(row=3,column=2)
    elif(v2>v1):
        Label(root,text="winner:Abhishek",height=2,width=20).grid(row=3,column=2)
    elif(v1==v2):
        Label(root,text="Tie",height=2,width=20).grid(row=3,column=2)

    btn1.config(state="disabled")
    btn2.config(state="disabled") 



        
   
Label(root,text="Rajesh",height=2,width=10).grid(row=1,column=1)
btn1=Button(root,text="vote",command=voter1)
btn1.grid(row=1,column=2)


Label(root,text="Abhishek",height=2,width=10).grid(row=2,column=1)
btn2=Button(root,text="vote",command=voter2)
btn2.grid(row=2,column=2)


btn3=Button(root,text="result",command=result).grid(row=3,column=3)
w=Entry(root,text="Enter name")
w.grid(row=4,column=20)


