import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    gender = gender_var.get()
    age = age_entry.get()

    if name and email and gender and age:
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Gender: {gender}")
        print(f"Age: {age}")
        messagebox.showinfo("Form Submitted", "Form submitted successfully!")
    else:
        messagebox.showwarning("Input Error", "Please fill all the fields!")

# Create the main window
window = tk.Tk()
window.title("User Information Form")
window.geometry("400x300")
window.config(bg="lightblue")

# Labels and Entry fields
tk.Label(window, text="Name:", bg="lightblue").grid(row=0, column=0, padx=10, pady=10, sticky='e')
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

tk.Label(window, text="Email:", bg="lightblue").grid(row=1, column=0, padx=10, pady=10, sticky='e')
email_entry = tk.Entry(window)
email_entry.grid(row=1, column=1)

tk.Label(window, text="Gender:", bg="lightblue").grid(row=2, column=0, padx=10, pady=10, sticky='e')
gender_var = tk.StringVar()
tk.Radiobutton(window, text="Male", variable=gender_var, value="Male", bg="lightblue").grid(row=2, column=1, sticky='w')
tk.Radiobutton(window, text="Female", variable=gender_var, value="Female", bg="lightblue").grid(row=2, column=1)

tk.Label(window, text="Age:", bg="lightblue").grid(row=3, column=0, padx=10, pady=10, sticky='e')
age_entry = tk.Entry(window)
age_entry.grid(row=3, column=1)

# Submit Button
submit_btn = tk.Button(window, text="Submit", command=submit_form)
submit_btn.grid(row=4, column=1, pady=20)

# Start the GUI loop
window.mainloop()
