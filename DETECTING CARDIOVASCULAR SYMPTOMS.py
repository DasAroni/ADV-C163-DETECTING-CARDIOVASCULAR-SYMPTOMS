from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Fever Report")
root.geometry("400x400")

question1_radiobutton = StringVar(value="0")

question1 = Label(root,text="Do you experience shotness or breath during routine activities?")
question1.pack()
question1_r1 = Radiobutton(root,text="yes",variable=question1_radiobutton,value="yes")
question1_r1.pack()
question1_r2 = Radiobutton(root,text="no",variable=question1_radiobutton,value="no")
question1_r2.pack()

question2_radiobutton = StringVar(value="0")
question2 = Label(root,text="Do you have swelling in the feet/ankles/legs(shoes feel tight)or abdomen?")
question2.pack()
question2_r1 = Radiobutton(root,text="yes",variable=question2_radiobutton,value="yes")
question2_r1.pack()
question2_r2 = Radiobutton(root,text="no",variable=question2_radiobutton,value="no")
question2_r2.pack()

question3_radiobutton = StringVar(value="0")
question3 = Label(root,text="Do you feel any of this symptoms - confusion,disorientation or loss of memory?")
question3.pack()
question3_r1 = Radiobutton(root,text="yes",variable=question3_radiobutton,value="yes")
question3_r1.pack()
question3_r2 = Radiobutton(root,text="no",variable=question3_radiobutton,value="no")
question3_r2.pack()

question4_radiobutton = StringVar(value="0")
question4 = Label(root,text="Do you experience shortness of breath while at rest/lying down?")
question4.pack()
question4_r1 = Radiobutton(root,text="yes",variable=question4_radiobutton,value="yes")
question4_r1.pack()
question4_r2 = Radiobutton(root,text="no",variable=question4_radiobutton,value="no")
question4_r2.pack()

question5_radiobutton = StringVar(value="0")
question5 = Label(root,text="Do you experience presistent wheezing /coughing that produces white or pink blood tinged mucus?")
question5.pack()
question5_r1 = Radiobutton(root,text="yes",variable=question5_radiobutton,value="yes")
question5_r1.pack()
question5_r2 = Radiobutton(root,text="no",variable=question5_radiobutton,value="no")
question5_r2.pack()

def fever_report():
    score=0
    if question1_radiobutton.get()=="yes":
        score = score+20
    if question2_radiobutton.get()=="yes":
        score = score+20
    if question3_radiobutton.get()=="yes":
        score = score+20    

    if score<=20:
        messagebox.showinfo("Report","no need to check with the doctor")       
    elif score>20 and score<=40:   
        messagebox.showinfo("Report","You might perhaps have to visit a doctor")        
    else:    
        messagebox.showinfo("Report","I strongly advise you to visit a doctor")        










clickme_button = Button(root,text="Clickme",command=fever_report)
clickme_button.pack()

root.mainloop()
