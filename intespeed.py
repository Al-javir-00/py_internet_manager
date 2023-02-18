#AttributeError: 'NoneType' object has no attribute 'fileno'
from tkinter import *
import speedtest as sp
import os
import sys;
sys.__stderr__.fileno()
2

def r_p(re_pa):
    try:
        base_p = sys._MEIPASS
    except Exception:
        base_p = os.path.abspath(".")

    return os.path.join(base_p, re_pa)        

def speedc():
    s = sp.Speedtest()
    s.get_servers()
    dw = str(round(s.download()/(10**6),3))+" Mbps"
    up = str(round(s.upload()/(10**6),3))+ " Mbps"
    pg = str(s.results.ping)+" MS"
    sv = s.get_servers()
    l2.config(text=dw)
    l4.config(text=up)
    l6.config(text=pg)
    l9.config(text=sv)

t = Tk()
t.title("internet speedmeter")
t.geometry("950x600")
bgi = PhotoImage(file = r_p("is.png"))
p = Label(image=bgi)
p.pack()
l1 = Label(t,text="Internet Speedtest",font=("Times New Roman",30),fg=("#fa90fc"),bg="#0f003c")
l1.place(x=310,y=30,height=45,width=300)


l2 = Label(t,text="00",font=("Times New Roman",25),fg="#2adde5",bg="#130341")
l2.place(x=90,y=200,height=60,width=220)

l3 = Label(t,text="Downlod Speed",font=("Times New Roman",20),fg="#fa90fc",bg="#0f003c")
l3.place(x=90,y=270,height=45,width=220)

l4 = Label(t,text="00",font=("Times New Roman",25),fg="#2adde5",bg="#130341")
l4.place(x=650,y=200,height=60,width=220)

l5 = Label(t,text="Uplode Speed",font=("Times New Roman",20),fg="#fa90fc",bg="#0f003c")
l5.place(x=650,y=270,height=45,width=220)

l6 = Label(t,text="00",font=("Times New Roman",25),fg=("#2adde5"),bg="#130341")
l6.place(x=375,y=200,height=60,width=200)

l7 = Label(t,text="Ping",font=("Times New Roman",20),fg=("#fa90fc"),bg="#0f003c")
l7.place(x=375,y=270,height=45,width=200)

l8 = Label(t,text="Server  Name",font=("Times New Roman",20),fg=("#fa90fc"),bg="#4620b4")
l8.place(x=375,y=480,height=45,width=200)

l9 = Label(t,text="Conecting...",font=("Times New Roman",20),fg=("#130341"),bg="#2adde5")
l9.place(x=25,y=400,height=60,width=900)

b_e = Button(t,text="Check Speed",font=("Times New Roman",20),relief=RAISED,bg="#f98dfd",fg="#0f003c",command=speedc)
b_e.place(x = 385, y = 545, height=40, width=180)

t.mainloop()
