from tkinter import * 
# imported to create the GUI components
import random, string
# random is imported to generate random charecters for the password. string is imported to access various charecter set (uppercase, lowercase, digits, puntuation).

import pyperclip
# imported to copy the generated password to clipboard.
# Create the main applicatiob window.
root= Tk() # creates the main applicatiob window.
root.geometry('400x400') # sets the window size to 400x400 pixels.
root.resizable(0,0) # diables window resizing by the user.
root.title('PYTHON PROJECT- PASSWORD GENERATOR') # sets the title of the window.

# Label creates the text label in the windows.
Label(root,text='Password Generator', font='arial 10 bold').pack() # displays the title 'Password Generator' at the top
Label(root,text='Python',font='arial 15 bold').pack(side=BOTTOM) # displays 'DataFlair' at the bottom of the window.

pass_label=Label(root,text='Password Length', font='arial 10 bold').pack # creates a label prompting the user to select the password length.
pass_len= IntVar() # IntVar() is a tkinter variable class that holds integer values. It is used to store the selected password length.
length= Spinbox(root,from_=8,to=32,textvariable=pass_len,width=15).pack() # Spinbox is a widget that allows the user to select password length.
pass_str=StringVar() # StringVar() is a tkinter variable class that holds string values. It is used to store the generated password.

# Function to generate random password.
def Generator():
    password=[] # intializes an empty string to store password.
    # Ensuring atleast one charecter is there from each type (Uppercase, Lowercase, Digits, puntuations).
    if pass_len.get()>=4:
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.digits))
        password.append(random.choice(string.punctuation))
        # Fill the rest with random choices until the specified length.
        for i in range(pass_len.get()-4):
            password.append(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation))
        # Shuffel to ensure randomness
        random.shuffle(password)
    else:
        # if length is less than 4, just fill the required length with random choices.
        for _ in range(pass_len.get()):
            password.append(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation))
    # Convert list to string and set it to the variable
    pass_str.set(''.join(password)) # updates the pass_string variable with the generated password, which is displayed in the entry widget.
def Copy_password():
    pyperclip.copy(pass_str.get()) # copies the generated password to the clip board using pyperclip.copy() function.

Button(root, text='GENERATE PASSWORD', command=Generator).pack(pady=5) # calls the Generator function.
Entry(root, textvariable=pass_str).pack() # A widget that displays the generated password, which is bound to the pass_str variable.
Button(root,text='Copy To Clipboard', command=Copy_password).pack(pady=5) # calls the Copy_Password Function.

root.mainloop() # starts the tkinter event loop, which keeps the application running and responsive to user interactions.
    
    