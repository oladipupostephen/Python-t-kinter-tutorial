import tkinter as tk

# Create the main window
root = tk.Tk()  
root.title('Calculator')
root.geometry('300x400')
root.configure(bg='darkgray')
root.resizable(False, False)  # Make window non-resizable for better layout

# Function to handle button clicks (just displays what was clicked)
def button_click(value):
    current = display_var.get()
    if current == "0":  # Replace initial 0
        display_var.set(str(value))
    else:
        display_var.set(current + str(value))

def clear_display():
    display_var.set("0")

def delete_last():
    current = display_var.get()
    if len(current) > 1:
        display_var.set(current[:-1])
    else:
        display_var.set("0")

# Variable to hold display text
display_var = tk.StringVar()
display_var.set("0")

# Create display area (like tutorial example 2 - Label widget)
display = tk.Label(
    root,
    textvariable=display_var,
    font=('Arial', 20, 'bold'),
    bg='black',
    fg='white',
    anchor='e',  # Right-align text like real calculators
    padx=10,
    pady=10,
    relief='sunken',
    bd=2
)
display.pack(fill='x', padx=10, pady=(10, 5))

# Create main button frame
button_frame = tk.Frame(root, bg='darkgray')
button_frame.pack(fill='both', expand=True, padx=10, pady=5)

# Button styling function
def create_button(parent, text, row, col, color_type='number', command=None, colspan=1):
    # Color schemes for different button types
    colors = {
        'number': {'bg': 'lightgray', 'fg': 'black', 'active_bg': 'white'},
        'operator': {'bg': 'orange', 'fg': 'white', 'active_bg': 'darkorange'},
        'equals': {'bg': 'dodgerblue', 'fg': 'white', 'active_bg': 'darkblue'},
        'clear': {'bg': 'darkred', 'fg': 'white', 'active_bg': 'red'},
        'function': {'bg': 'dimgray', 'fg': 'white', 'active_bg': 'gray'}
    }
    
    button = tk.Button(
        parent,
        text=text,
        font=('Arial', 14, 'bold'),
        width=4,
        height=2,
        bg=colors[color_type]['bg'],
        fg=colors[color_type]['fg'],
        activebackground=colors[color_type]['active_bg'],
        activeforeground='white',
        relief='raised',
        bd=2,
        command=command
    )
    button.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2, sticky='nsew')
    return button

# Configure grid weights for responsive layout (like tutorial example 5 - grid)
for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)

# Row 0: Clear and Delete buttons
create_button(button_frame, 'C', 0, 0, 'clear', clear_display)
create_button(button_frame, '⌫', 0, 1, 'function', delete_last)
create_button(button_frame, '±', 0, 2, 'function', lambda: button_click('±'))
create_button(button_frame, '÷', 0, 3, 'operator', lambda: button_click('÷'))

# Row 1: 7, 8, 9, ×
create_button(button_frame, '7', 1, 0, 'number', lambda: button_click('7'))
create_button(button_frame, '8', 1, 1, 'number', lambda: button_click('8'))
create_button(button_frame, '9', 1, 2, 'number', lambda: button_click('9'))
create_button(button_frame, '×', 1, 3, 'operator', lambda: button_click('×'))

# Row 2: 4, 5, 6, -
create_button(button_frame, '4', 2, 0, 'number', lambda: button_click('4'))
create_button(button_frame, '5', 2, 1, 'number', lambda: button_click('5'))
create_button(button_frame, '6', 2, 2, 'number', lambda: button_click('6'))
create_button(button_frame, '−', 2, 3, 'operator', lambda: button_click('−'))

# Row 3: 1, 2, 3, +
create_button(button_frame, '1', 3, 0, 'number', lambda: button_click('1'))
create_button(button_frame, '2', 3, 1, 'number', lambda: button_click('2'))
create_button(button_frame, '3', 3, 2, 'number', lambda: button_click('3'))
create_button(button_frame, '+', 3, 3, 'operator', lambda: button_click('+'))

# Row 4: 0 (spans 2 columns), ., =
create_button(button_frame, '0', 4, 0, 'number', lambda: button_click('0'), colspan=2)
create_button(button_frame, '.', 4, 2, 'number', lambda: button_click('.'))
create_button(button_frame, '=', 4, 3, 'equals', lambda: button_click('='))

# Start the event loop (from all tutorial examples)
root.mainloop()