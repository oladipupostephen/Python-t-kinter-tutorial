import tkinter as tk
from tkinter import ttk

class KidsCalculator:
    def __init__(self):
        # Step 1: Create the main window (like opening a new notebook)
        self.window = tk.Tk()
        self.window.title("My Awesome Calculator! 🧮")
        self.window.geometry("400x600")  # width x height
        self.window.configure(bg='#2c3e50')  # Cool dark blue background
        
        # Step 2: This will hold our math expression (like "2 + 3")
        self.expression = ""
        
        # Step 3: Create the display screen
        self.create_display()
        
        # Step 4: Create all the buttons
        self.create_buttons()
    
    def create_display(self):
        """Step 3: Make the screen where numbers appear"""
        # Create a frame (like a picture frame) to hold our display
        display_frame = tk.Frame(self.window, bg='#2c3e50', pady=20)
        display_frame.pack(fill='both')
        
        # The actual display screen (like a phone screen)
        self.display = tk.Label(
            display_frame,
            text="0",  # Start with 0
            font=('Arial', 24, 'bold'),  # Big, bold letters
            bg='#34495e',  # Darker gray
            fg='#ecf0f1',  # Almost white text
            anchor='e',  # Align text to the right (like real calculators!)
            padx=20,
            pady=20,
            relief='sunken',  # Makes it look pressed in
            bd=3
        )
        self.display.pack(fill='both', padx=20)
    
    def create_buttons(self):
        """Step 4: Make all the colorful buttons"""
        # Create a frame for buttons (like a container for toys)
        button_frame = tk.Frame(self.window, bg='#2c3e50')
        button_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Button layout (like a grid pattern)
        buttons = [
            ['C', '±', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '', '.', '=']
        ]
        
        # Colors for different types of buttons
        colors = {
            'numbers': {'bg': '#3498db', 'fg': 'white'},      # Blue for numbers
            'operations': {'bg': '#e74c3c', 'fg': 'white'},   # Red for +,-,×,÷
            'special': {'bg': '#f39c12', 'fg': 'white'},      # Orange for C, ±, %
            'equals': {'bg': '#27ae60', 'fg': 'white'}        # Green for =
        }
        
        # Create buttons row by row (like building with Lego blocks)
        for row in range(5):
            for col in range(4):
                button_text = buttons[row][col]
                
                if button_text == '':  # Skip empty spots
                    continue
                
                # Choose color based on button type
                if button_text.isdigit() or button_text == '.':
                    color = colors['numbers']
                elif button_text in ['+', '-', '×', '÷']:
                    color = colors['operations']
                elif button_text == '=':
                    color = colors['equals']
                else:
                    color = colors['special']
                
                # Make the button extra wide for '0'
                colspan = 2 if button_text == '0' else 1
                
                # Create the actual button
                btn = tk.Button(
                    button_frame,
                    text=button_text,
                    font=('Arial', 18, 'bold'),
                    width=4 if button_text != '0' else 8,
                    height=2,
                    command=lambda x=button_text: self.button_click(x),
                    **color,  # Apply the colors
                    relief='raised',
                    bd=2,
                    cursor='hand2'  # Changes cursor to hand when hovering
                )
                
                # Place button in the grid
                btn.grid(row=row, column=col, columnspan=colspan, 
                        padx=2, pady=2, sticky='nsew')
        
        # Make buttons stretch when window is resized
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
    
    def button_click(self, char):
        """Step 5: Make buttons do something when clicked"""
        
        if char == 'C':
            # Clear everything (like erasing a whiteboard)
            self.expression = ""
            self.display.config(text="0")
        
        elif char == '=':
            # Do the math! (like solving a puzzle)
            try:
                # Replace symbols with Python operators
                math_expression = self.expression
                math_expression = math_expression.replace('×', '*')
                math_expression = math_expression.replace('÷', '/')
                
                # Calculate the result
                result = eval(math_expression)
                
                # Show the answer
                self.display.config(text=str(result))
                self.expression = str(result)
                
            except:
                # If something goes wrong, show error
                self.display.config(text="Error!")
                self.expression = ""
        
        elif char == '±':
            # Change positive to negative (or vice versa)
            if self.expression and self.expression[0] == '-':
                self.expression = self.expression[1:]
            else:
                self.expression = '-' + self.expression
            self.display.config(text=self.expression or "0")
        
        elif char == '%':
            # Convert to percentage
            try:
                result = float(self.expression) / 100
                self.expression = str(result)
                self.display.config(text=self.expression)
            except:
                pass
        
        else:
            # Add number or operation to our expression
            if self.display.cget("text") == "Error!":
                self.expression = ""
            
            self.expression += char
            self.display.config(text=self.expression)
    
    def run(self):
        """Step 6: Start the calculator (like turning it on!)"""
        self.window.mainloop()

# Step 7: Create and run our calculator
if __name__ == "__main__":
    calculator = KidsCalculator()
    calculator.run()
