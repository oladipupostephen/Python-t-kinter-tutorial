import tkinter as tk

# Create the main window
root = tk.Tk()
root.title('Calculator Button Demo')
root.geometry('200x150')  # Set window size
root.configure(bg='#2c3e50')  # Dark blue-gray background

# Function to handle button click
def button_clicked():
    print("Button 7 was clicked!")
    # You could also update a display or perform calculations here

# Create a colorful calculator button
calc_button = tk.Button(
    root,                           # Parent widget (from tutorial example 3)
    text='7',                       # Button text
    font=('Arial', 24, 'bold'),     # Large, bold font
    width=4,                        # Button width (from tutorial example 3)
    height=2,                       # Button height
    bg='#3498db',                   # Beautiful blue background
    fg='white',                     # White text color
    activebackground='#2980b9',     # Darker blue when pressed
    activeforeground='white',       # White text when pressed
    relief='raised',                # 3D raised effect
    bd=3,                          # Border width
    command=button_clicked          # Function to call when clicked (from tutorial example 3)
)

# Display the button using pack geometry manager (from tutorial examples)
calc_button.pack(pady=30)  # Add some padding around the button

# Add a label to show what this demonstrates (from tutorial example 2)
info_label = tk.Label(
    root,
    text='Click the calculator button!',
    font=('Arial', 12), 
    bg='#2c3e50',
    fg='#ecf0f1'  # Light gray text
)
info_label.pack()

# Start the event loop (from all tutorial examples)
root.mainloop()