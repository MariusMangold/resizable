import tkinter as tk

# Define the function to be called on window resize
def on_resize(event):
    print("Hey!")

# Create the main window
root = tk.Tk()
root.title("Resize Detector")

# Bind the <Configure> event to the on_resize function
root.bind("<Configure>", on_resize)

# Set a minimum size for the window
root.minsize(300, 200)

# Start the main event loop
root.mainloop()
