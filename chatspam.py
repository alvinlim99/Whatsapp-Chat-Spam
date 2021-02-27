
from tkinter import *
import  random, sys, os, pyautogui, time, spam

root = Tk()
root.geometry("550x250")
root.title("CibaiPikachu Whatsapp Spam")


#Encode Message
def button_encode():
    #Retrieve And Store User Input(Plaintext) input in text file
    text = entry_plaintext.get()
    f = open("spamMessage.txt","w")
    f.write(text)


def button_spam():
        f = open("spamMessage.txt","r")
        text = f.readline()
        comments = [text]
        time.sleep(10)
        for i in range(10000):
            pyautogui.typewrite(comments[i%1])
            pyautogui.typewrite("\n")







#Define Frame For Display Location
topFrame = Frame(root)
topFrame.pack()
leftFrame = Frame(root)
leftFrame.pack(side=LEFT)
rightFrame = Frame(root)
rightFrame.pack(side=RIGHT)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


#Define Label
label_plaintext = Label(topFrame, text="Enter Spam Message     :", font="Times 12 bold", fg="black")



#Define Entry(Textboxt)
entry_plaintext = Entry(topFrame, width=50, fg="black")


#Define Button
button_encode  = Button(bottomFrame, text="Save Spam Message", font="Times 10 bold", padx=10, pady=10, command=button_encode)
button_reset   = Button(bottomFrame, text="SPAM NOW", font="Times 10 bold", padx=10, pady=10, command=button_spam)

#Display Label
#-- Display Label On The GUI Application --#
label_plaintext.grid(row=1, sticky=E)



#Display Entry(Textbox)
#-- Display Entry On The GUI Application --#
entry_plaintext.grid(row=1, column=1)


#Display Button
#-- Display Button On The GUI Application --#
button_encode.pack(side=LEFT)
button_reset.pack(side=LEFT)


#Display The Application Continously
#-- without this the application will close immediately once it run. --#
root.mainloop()
