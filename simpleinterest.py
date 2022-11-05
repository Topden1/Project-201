from tkinter import *
window=Tk()


window.title('Simple Interest')
window.geometry("380x400")
window.configure(bg='blue')

def calculate_interest():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = Ip*r*t)/100
    interest = round(i, 2)

    Showlabel.destroy

principle_label=Label(window)
principle_label.place(x=50, y=20)

principle=Entry(window)
principle.place(x=150, y=92)

RateOfInterest_label=Label(window)
RateOfInterest_label.place(x=20, y=140)

RateOfInterest=Entry(window)
RateOfInterest.place(x=150, y=142)

Time_label=Label(window)
Time_label.place(x=40, y=60)

Time=Entry(window)
Time.place(x=150, y=120)

calculate_button=Button(window,text="CALCULATE", fg = "black", bg = "cyan",bd=4,command=calculate_interest)
calculate_button.place(x=20,y=250)

result_frame = LabelFrame(window,text="Result", bg = "grey", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

Showlabel_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), 
Showlabel_label.place(x=20,y=20)
Showlabel_label.pack()
