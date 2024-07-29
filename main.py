import tkinter as tk
from tkinter import ttk


class GridApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dynamic Grid App")

        # Field dimensions (in pixels)
        self.field_width = 80
        self.field_height = 30

        # Padding between fields (in pixels)
        self.padx = 2
        self.pady = 2

        # Frame for the grid
        self.grid_frame = ttk.Frame(self)
        self.grid_frame.pack(fill="both", expand=True)

        # Store the last known grid size to avoid redundant updates
        self.last_n = 0
        self.last_m = 0

        # Bind resize event to update the grid dynamically
        self.bind("<Configure>", self.on_resize)

    def create_grid(self, n, m):
        # Clear the existing grid
        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        # Create new grid based on n and m
        for row in range(m):
            for col in range(n):
                label = ttk.Label(self.grid_frame, text=f"({row + 1},{col + 1})", borderwidth=1, relief="solid",
                                  width=10, anchor="center")
                label.grid(row=row, column=col, padx=self.padx, pady=self.pady)

    def on_resize(self, event):
        # Calculate the total width and height of one field including padding
        total_width = self.field_width + 10*self.padx
        total_height = self.field_height + 10*self.pady

        # Get the current window dimensions
        window_width = self.grid_frame.winfo_width()
        window_height = self.grid_frame.winfo_height()

        # Calculate the number of fields that fit into the current window size
        n = max(window_width // total_width, 1)
        m = max(window_height // total_height, 1)

        # Print the calculations for debugging
        print(f"Window size: {window_width}x{window_height}")
        print(f"Effective field size: {total_width}x{total_height}")
        print(f"Number of fields: {n}x{m}")

        # Only update the grid if the size has changed
        if n != self.last_n or m != self.last_m:
            self.create_grid(n, m)
            self.last_n = n
            self.last_m = m


if __name__ == "__main__":
    app = GridApp()
    app.mainloop()
