import tkinter as tk
import pyperclip
from firebase import firebase
result = ""
firebase_link = " Your firebase link"
firebase = firebase.FirebaseApplication(firebase_link, None)
def push():
    """Method to push the dat into the cloud"""
    global result
    firebase.put(url=firebase_link,name="MESSAGE",data=result)
def copy():
    """ Method to copy the result"""
    global result
    pyperclip.copy(result)

def gen():
    """ Method for Encrypt the cipher """
    text = e_1.get()
    s = int(e_2.get())
    global result
    result = ""
    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    l3.config(text="")
    l3.config(text=result)

def de():
    """ Method for Decrypt the cipher"""
    text = e_11.get()
    s = int(e_21.get())
    result = ""
    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)


        else:
            result += chr((ord(char) - s - 97) % 26 + 97)

    global l31
    l31['text'] = result

#################

window = tk.Tk()
window.title("The Caesar Cipher")
window.geometry("250x250")
frame_main = tk.Frame(window)
frame_main.pack()

frame_1 = tk.Frame(frame_main)
frame_1.pack(side="left")
frame_2 = tk.Frame(frame_main)
frame_2.pack(side="left")

l1 = tk.Label(frame_1,text="Message")
l1.pack(side="top")
e_1 = tk.Entry(frame_2)
e_1.pack(side = "top")


l2 = tk.Label(frame_1,text="key(1-26)")
l2.pack(side="bottom")
e_2 = tk.Entry(frame_2)
e_2.pack(side = "bottom")

b_1 = tk.Button(window,text = "Encrypt",command =gen)
b_1.pack()
frame_main_bb = tk.Frame(window)
frame_main_bb.pack()
b_copy = tk.Button(frame_main_bb,text = "Copy",command =copy)
b_copy.pack(side = "left")
b_cloud = tk.Button(frame_main_bb,text = "Cloud",command =push)
b_cloud.pack(side = "left")

l3 = tk.Label(window,bg = "yellow")
l3.pack()


####################
frame_main_1 = tk.Frame(window)
frame_main_1.pack()

frame_11 = tk.Frame(frame_main_1)
frame_11.pack(side="left")
frame_21 = tk.Frame(frame_main_1)
frame_21.pack(side="left")

l11 = tk.Label(frame_11,text="Message")
l11.pack(side="top")
e_11 = tk.Entry(frame_21)
e_11.pack(side = "top")


l21 = tk.Label(frame_11,text="key(1-26)")
l21.pack(side="bottom")
e_21 = tk.Entry(frame_21)
e_21.pack(side = "bottom")

b_11 = tk.Button(window,text = "Dcrypt",command =de)
b_11.pack()

l31 = tk.Label(window,bg="yellow")
l31.pack()



window.mainloop()
