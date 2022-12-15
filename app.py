import tkinter as tk

def login():
    # create the main window
    root = tk.Tk()
    root.title("Login")

    # create labels for the form fields
    mail_label = tk.Label(root, text="Mail:")
    password_label = tk.Label(root, text="Password:")

    # create the form fields
    mail_field = tk.Entry(root)
    password_field = tk.Entry(root, show="*")

    # create the submit button
    submit_button = tk.Button(root, text="Ingresar")

    # create a function to handle the form submission
    def handle_submit():
        # get the values entered in the form fields
        mail = mail_field.get()
        password = password_field.get()

        # print the values to the console
        print("Mail:", mail)
        print("Password:", password)

    # bind the submit button to the submit function
    submit_button.bind("<Button-1>", handle_submit)

    # posicionar los widgets
    mail_label.grid(row=0, column=0)
    mail_field.grid(row=0, column=1)
    password_label.grid(row=1, column=0)
    password_field.grid(row=1, column=1)
    submit_button.grid(row=2, column=1)

    # start the main loop
    root.mainloop()