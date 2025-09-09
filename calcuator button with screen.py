import tkinter as tk

# Create the main window
root = tk.Tk()
root.title('Calculator Button Demo')
root.geometry('250x250')  # Slightly bigger for screen
root.configure(bg='#2c3e50')  # Dark blue-gray background

# ----- Calculator Display (screen) -----
display_var = tk.StringVar()   # Holds the text shown on screen
display = tk.Label(
    root,
    textvariable=display_var,   # Link text to StringVar
    font=('Arial', 24, 'bold'),
    bg='black',
    fg='lime',
    anchor='e',                 # Align text to the right (like real calculators)
    relief='sunken',
    width=12,
    height=2
)
display.pack(pady=10)

# ----- Function to handle button click -----
def button_clicked(num):
    current = display_var.get()      # Get current text on screen
    new_text = current + str(num)    # Append the number clicked
    display_var.set(new_text)        # Update screen

# ----- Calculator Buttons -----
calc_button = tk.Button(
    root,
    text='7',
    font=('Arial', 24, 'bold'),
    width=4,
    height=2,
    bg='#3498db',
    fg='white',
    activebackground='#2980b9',
    activeforeground='white',
    relief='raised',
    bd=3,
    command=lambda: button_clicked(7)   # Pass number 7 to function
)
calc_button.pack(pady=10)

# Info label (optional)
info_label = tk.Label(
    root,
    text='Click the calculator button!',
    font=('Arial', 12),
    bg='#2c3e50',
    fg='#ecf0f1'
)
info_label.pack()

# Start the event loop
root.mainloop()
