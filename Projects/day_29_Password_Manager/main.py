from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    random_length = random.randint(12, 16)
    new_password = "".join(random.choice(chars) for i in range(random_length))
    password_input.delete(0, END)
    password_input.insert(0, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    credential = credential_input.get()
    password = password_input.get()

    if website == "" or credential == "":
        messagebox.showerror("Error", "Please don't leave empty fields!")
    else:
        user_accept = messagebox.askokcancel(title="Confirmation", message=f"Email: {website}\n"
                                        f"Email: {credential}\nPassword: {password}\n Are you sure you want to save?")
        if user_accept:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {credential} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(window, width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", bg="white")
website_label.grid(row=1, column=0)
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

credential_label = Label(text="Email/Username: ", bg="white")
credential_label.grid(row=2, column=0)
credential_input = Entry(width=35)
credential_input.grid(row=2, column=1, columnspan=2)
credential_input.insert(0,"silverguardgithub@gmail.com")

password_label = Label(text="Password: ", bg="white")
password_label.grid(row=3, column=0)
password_input = Entry(width=21)
password_input.grid(row=3, column=1, columnspan=1)
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=2)

add_password = Button(text="Add", width=35, command=save_password)
add_password.grid(row=4, column=1, columnspan=2)




window.mainloop()