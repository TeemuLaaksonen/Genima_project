#GENIMA: Message Encrypter (consepts from freecodecamp.org forums)

#Requires basic understanding of Python. Base64-module is used to encode & decode messages as advised
#at freecodecamp.com. Tkinter is used to build basic UI, which has been done by using guidance from
#various websites as my knowledge of it so far has been mostly non-existent.

#The encryption process was unknown to me, so I've relied on stackoverflow.com forums for different
#encryption / decryption methods and function formats.

#I got inspiration to this program from the book "Alan Turing: The Enigma" and the movie "Imitation game".
#My future plan is to specialize in the field of cybersec and this program seemed like a suitable starting point.


#THIS IS THE BEGINNING OF THE PROGRAM CODE

#Library imports (Tkinter & Base64)

from tkinter import *
import base64

#Setting the GUI window class

window = Tk()

window.geometry("500x300") #width and height of the window
window.resizable(0,0) #fixed size, can't be resized with values 0,0
window.title("GENIMA - Encrypt / Decrypt your message") #window title
window.configure(background="black") #background color of the UI

Label(window, text="GENIMA", font="arial 20 bold",bg="Black" ,fg="ghost white").pack() #label on the upper side of window
Label(window, text="by Teemu Laaksonen", font ="arial 14 bold",bg="Black",fg="ghost white").pack(side=BOTTOM) #label on the bottom

#Setting and defining variables for actions

text = StringVar() #user's message
cipher_key = StringVar() #stores the key to encrypt / decrypt
mode = StringVar() #this selects between encrypting / decrypting
output = StringVar() #this is where the result is stored

#ENCODE FUNCTION
#The idea in this function is to loop through the text one character at a time and give each character an integer value based
#on the key lenght and the integer place of the current loop. This value is then stored to list and the list is finally
#encoded (encrypted) with base64.

def encrypt(cipher_key, text):
    encrypting = []
    for i in range(len(text)):
        x_key = cipher_key[i % len(cipher_key)]
        encrypting.append(chr((ord(text[i]) + ord(x_key)) % 256))

    return base64.urlsafe_b64encode("".join(encrypting).encode()).decode()

#DECODE FUNCTION
#The idea of this function is to perform encode-function's actions in reverse order. It takes the encrypted message, decrypts it
#with base64 and then returns the characters real values by reversing the integer-process done in encode().

def decrypt(cipher_key, text):
    decrypting = []
    text = base64.urlsafe_b64decode(text).decode()
    for i in range(len(text)):
        x_key = cipher_key[i % len(cipher_key)]
        decrypting.append(chr((256 + ord(text[i])- ord(x_key)) % 256))

    return "".join(decrypting)

#SET MODE FUNCTION
#With E the function calls encrypt(), with D it calls decrypt()

def mode_function():
    if(mode.get() == "E"):
        output.set(encrypt(cipher_key.get(), text.get()))
    elif(mode.get() == "D"):
        output.set(decrypt(cipher_key.get(), text.get()))
    else:
        output.set("MODE NOT VALID")

#RESET FUNCTION
#Clears the input fields by putting empty string in the field.

def reset():
    text.set("")
    cipher_key.set("")
    mode.set("")
    output.set("")

#INPUT AND BUTTONS GUI

#Message-label + field
Label(window, font= "arial 12 bold", text="Message", bg="black",fg="ghost white").place(x= 60,y=60)
Entry(window, font = "arial 10", textvariable = text, bg = "ghost white").place(x=290, y = 60)

#Key-label + field
Label(window, font = "arial 12 bold", text ="Key", bg="black",fg="ghost white").place(x=60, y = 90)
Entry(window, font = "arial 10", textvariable = cipher_key , bg ="ghost white").place(x=290, y = 90)

#Mode-label + field
Label(window, font = "arial 12 bold", text ="E=Encrypt / D=Decrypt", bg="black",fg="ghost white").place(x=60, y = 120)
Entry(window, font = "arial 10", textvariable = mode , bg= "ghost white").place(x=290, y = 120)

#Result-label + field
Label(window, font = "arial 12 bold", text ="Output", bg="black",fg="ghost white").place(x=60, y = 150)
Entry(window, font = "arial 10 bold", textvariable = output, bg ="ghost white").place(x=290, y = 150)

#EXECUTE BUTTON
#Calls mode_function() on button press.
Button(window, font = "arial 10 bold", text = "EXECUTE",width =7  ,padx =2,bg ="LightGreen" ,command = mode_function).place(x=80, y = 200)

#CLEAR BUTTON
#Calls reset() on button press.
Button(window, font = "arial 10 bold" ,text ="CLEAR" ,width =7, command = reset,bg = "OrangeRed", padx=2).place(x=350, y = 200)

#Starts GUI
window.mainloop()