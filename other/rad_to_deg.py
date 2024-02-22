
import tkinter as tk

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Perform your login logic here
    # You can check the entered username and password against a database or any other authentication mechanism

    if username == "admin" and password == "password":
        print("Login successful!")
    else:
        print("Login failed!")

# Create the main window
window = tk.Tk()
window.title("Login Form")

# Create labels and entry fields
label_username = tk.Label(window, text="Username:")
label_username.pack()
entry_username = tk.Entry(window)
entry_username.pack()

label_password = tk.Label(window, text="Password:")
label_password.pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()

# Create a login button
button_login = tk.Button(window, text="Login", command=login)
button_login.pack()

# Start the Tkinter event loop
window.mainloop()
