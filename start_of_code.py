import os
from tkinter import *
from tkinter import messagebox


def run_scripts(user_id, user_name):

    try:

        if not user_id.isdigit():
            raise ValueError("ID must be a numeric value!")

        os.system(f"python main/set_generator.py {user_id}")

        os.system("python main/trainer.py")

        os.system(f"python main/LBPH.py {user_id} {user_name}")

        messagebox.showinfo("Success", "Scripts executed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def on_submit():

    user_id = entry_id.get()
    user_name = entry_name.get()

    if not user_id.isdigit():
        messagebox.showerror("Input Error", "ID must be a numeric value!")
        return
    if not user_name:
        messagebox.showerror("Input Error", "Name cannot be empty!")
        return

    run_scripts(user_id, user_name)



root = Tk()
root.title("LBPH and Dataset Generator")
root.geometry("400x300")

label_title = Label(root, text="LBPH and Dataset Generator", font=("Helvetica", 16, "bold"))
label_title.pack(pady=10)

label_id = Label(root, text="Enter ID:", font=("Helvetica", 12))
label_id.pack(pady=5)
entry_id = Entry(root, width=30)
entry_id.pack(pady=5)

label_name = Label(root, text="Enter Name:", font=("Helvetica", 12))
label_name.pack(pady=5)
entry_name = Entry(root, width=30)
entry_name.pack(pady=5)

button_submit = Button(root, text="Submit", command=on_submit, font=("Helvetica", 12))
button_submit.pack(pady=20)

root.mainloop()
