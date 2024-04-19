import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

def is_armstrong_number(num):
    # Calculate the sum of the cubes of the digits
    sum_of_cubes = sum(int(digit) ** 3 for digit in str(num))
    
    # Check if the sum is equal to the number
    if sum_of_cubes == num:
        return True
    else:
        return False

def find_armstrong_numbers():
    # Get the end range value from the input box
    end = int(end_input.get())
    
    # Clear the output box
    output_box.delete('1.0', tk.END)
    
    # Check if the end value is greater than 9
    if end < 10:
        error_label.config(text='Please Enter A Number Greater Than 9')
        return
    
    # Find all the Armstrong numbers within the given range
    armstrong_numbers = [num for num in range(10, end+1) if is_armstrong_number(num)]
    
    # Display the results in the output box
    for num in armstrong_numbers:
        output_box.insert(tk.END, f'{num}\n')

    # Clear the error message
    error_label.config(text='')

# Create the main window
root = tk.Tk()
root.title('Armstrong Number Finder')

# Set the theme and font
style = ttk.Style()
font = Font(family='Consolas', size=12)
style.configure('TLabel', font=font)
style.configure('TEntry', font=font)
style.configure('TButton', font=font)
style.configure('Heading.TLabel', font=('Consolas', 16, 'bold'))

# heading for the window
heading = ttk.Label(root, text='Armstrong Number', style='Heading.TLabel')


# Create the input label and box
end_label = ttk.Label(root, text='End Number :', anchor='w')
end_input = ttk.Entry(root, width=30, font=font)

# Create the output label and box
output_label = ttk.Label(root, text='Armstrong Numbers:', anchor='w')
output_box = tk.Text(root, height=10, width=30, font=font)

# Create the find button
find_button = ttk.Button(root, text='Find', command=find_armstrong_numbers, width=40)

# Create the error label
error_label = ttk.Label(root, text='', foreground='red', font=font)

# Position the widgets on the grid
heading.grid(column=0, row=0, columnspan=2, pady=5, sticky="n")
end_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
end_input.grid(row=1, column=1, padx=5, pady=5)
output_label.grid(row=4, column=0, padx=5, pady=5, sticky='w')
output_box.grid(row=4, column=1, padx=5, pady=5)
find_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
error_label.grid(row=8, column=0, columnspan=2, sticky='s')

# Start the main loop
root.mainloop()
