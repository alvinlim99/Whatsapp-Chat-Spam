import  random, sys, os, pyautogui, time, spam
def spamMessage():
    f = open("spamMessage.txt","r")
    text = f.readline()
    comments = [text]
    time.sleep(10)
    for i in range(10000):
        pyautogui.typewrite(comments[i%1])
        pyautogui.typewrite("\n")
