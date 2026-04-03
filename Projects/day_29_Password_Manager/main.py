from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json

# ---------------------------- Search for Website------------------------------- #
def search_file():
    website = website_input.get().title()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)

        search_result = data.get(website)
        if website in data:
            messagebox.showinfo("Search Results", f"Website: {website}\n"
                                f"Email/Username: {search_result.get('credential')}\n"
                                f"Password: {search_result.get('password')}\n")
        else:
            messagebox.showerror("Error", "Website data does not exist")
    except FileNotFoundError:
        messagebox.showerror("Error", "File does not exist")

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
    website = website_input.get().title()
    credential = credential_input.get()
    password = password_input.get()

    new_data = {
        website: {
                "credential": credential,
                "password": password
        }
    }

    if website == "" or credential == "" or password == "":
        messagebox.showerror("Error", "Please don't leave empty fields!")
    else:
        user_accept = messagebox.askokcancel(title="Confirmation", message=f"Email: {website}\n"
                                        f"Email: {credential}\nPassword: {password}\n Are you sure you want to save?")
        if user_accept:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(window, width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", bg="white")
website_label.grid(row=1, column=0, sticky="e", padx=(0, 10), pady=5)
website_input = Entry(width=21)
website_input.grid(row=1, column=1, columnspan=1, sticky="ew", pady=5)
website_input.focus()

search_button = Button(text="Search", width = 14, command=search_file)
search_button.grid(row=1, column=2, padx=(10, 0), pady=5)

credential_label = Label(text="Email/Username: ", bg="white")
credential_label.grid(row=2, column=0, sticky="e", padx=(0, 10), pady=5)
credential_input = Entry(width=30)
credential_input.grid(row=2, column=1, columnspan=2, sticky="ew", pady=5)
credential_input.insert(0,"silverguardgithub@gmail.com")

password_label = Label(text="Password: ", bg="white")
password_label.grid(row=3, column=0, sticky=E, padx=(0, 10), pady=5)
password_input = Entry(width=21)
password_input.grid(row=3, column=1, columnspan=1, sticky="ew", pady=5)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, padx=(10, 0), pady=5)

add_password = Button(text="Add", width=35, command=save_password)
add_password.grid(row=4, column=1, columnspan=2, sticky="ew", pady=(10,0))




window.mainloop()