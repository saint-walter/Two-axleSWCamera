import os
from tkinter import *
from tkinter import messagebox


def run_scripts(user_id, user_name):
    """
    Функция для запуска скриптов set_generator.py, trainer.py и LBPH.py
    с передачей ID и Name в качестве аргументов.
    """
    try:
        # Проверяем, что ID - это число
        if not user_id.isdigit():
            raise ValueError("ID must be a numeric value!")

        # Запускаем set_generator.py с ID
        os.system(f"python main/set_generator.py {user_id}")

        # Запускаем trainer.py
        os.system("python main/trainer.py")

        # Запускаем LBPH.py с ID и Name
        os.system(f"python main/LBPH.py {user_id} {user_name}")

        messagebox.showinfo("Success", "Scripts executed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def on_submit():
    """
    Обработчик кнопки Submit.
    Получает данные из полей ввода и запускает скрипты.
    """
    user_id = entry_id.get()
    user_name = entry_name.get()

    if not user_id.isdigit():
        messagebox.showerror("Input Error", "ID must be a numeric value!")
        return
    if not user_name:
        messagebox.showerror("Input Error", "Name cannot be empty!")
        return

    run_scripts(user_id, user_name)


# Создаем главное окно
root = Tk()
root.title("LBPH and Dataset Generator")
root.geometry("400x300")

# Заголовок
label_title = Label(root, text="LBPH and Dataset Generator", font=("Helvetica", 16, "bold"))
label_title.pack(pady=10)

# Поле для ввода ID
label_id = Label(root, text="Enter ID:", font=("Helvetica", 12))
label_id.pack(pady=5)
entry_id = Entry(root, width=30)
entry_id.pack(pady=5)

# Поле для ввода Name
label_name = Label(root, text="Enter Name:", font=("Helvetica", 12))
label_name.pack(pady=5)
entry_name = Entry(root, width=30)
entry_name.pack(pady=5)

# Кнопка Submit
button_submit = Button(root, text="Submit", command=on_submit, font=("Helvetica", 12))
button_submit.pack(pady=20)

# Запуск окна
root.mainloop()