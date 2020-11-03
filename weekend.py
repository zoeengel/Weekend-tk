from tkinter import *

#EXIT BUTTON FUNCTION
def exit_function():
    raise SystemExit
    sys.exit()

#CLEAR BUTTON FUNCTION
def clear_function():
    mytext.config(state=NORMAL)
    mytext.delete('1.0', END)


#defining my function
def weekend():
    myfile=open('/home/user/Desktop/my_weekend_activities.txt', 'w')
    myfile.write("Saturday, my friends and i went to Mixed Feelings, out of all of us that went, myself and Uzair bandswapped in.\n")
    myfile.write("Sunday i was planning to stay at home but the friends i went out with from the night before fetched me to watch the sunset at Clifton.\n")
    myfile.write("Just before we got to Clifton, we bought ice-cream at the Creamery which is in Seapoint.\n")
    myfile.write("Overall i had a great weekend!")
    myfile.close()


#display function
def display():

    quote = """
    Saturday, my friends and i went to Mixed Feelings, out of all of us that went, myself and Uzair bandswapped in.
    Sunday i was planning to stay at home but the friends i went out with from the night before fetched me to watch the sunset at Clifton.
    Just before we got to Clifton, we bought ice-cream at the Creamery which is in Seapoint.
    Overall i had a great weekend!
    """
    mytext.insert(END, quote)      #use global so that mytext can vbe accessed

#creating my window
window = Tk()
window.geometry("650x350")
window.title("Weekend Activities")
window.config(background="yellow")


#creating lable
weekendlabel=Label(text="My weekend activities", font="Arial 15")
weekendlabel.place(x=5 ,y=1)
global mytext
mytext=Text(window, height=10, width=50)
mytext.place(x=5 ,y=40)
#display button
DB=Button(window, text="Display", command=display)
DB.place(x=8, y=240)

#EXIT BUTTON
EB=Button(window, text="Exit", command=exit_function)
EB.place(x=170, y=240)

#CLEAR BUTTON
CB=Button(window, text="Clear", command = clear_function)
CB.place(x=100, y=240)
window.mainloop()
