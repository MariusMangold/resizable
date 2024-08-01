import customtkinter as ctk


class DynamicGridApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Dynamic Grid with Multiple Frames")

        # Field dimensions (in pixels)
        self.field_width = 80
        self.field_height = 30

        # Padding between fields (in pixels)
        self.padx = 10
        self.pady = 10

        # Padding around each frame (in pixels)
        self.frame_padx = 10
        self.frame_pady = 10

        # Total width and height of a field, including padding
        self.total_field_width = self.field_width + 2 * self.padx
        self.total_field_height = self.field_height + 2 * self.pady

        # Frame for the grids
        self.frames = []
        self.label_counts = [3, 4, 5, 6, 7]

        for count in self.label_counts:
            main_frame = ctk.CTkFrame(self)
            main_frame.pack(fill="x", expand=True, padx=self.frame_padx, pady=self.frame_pady)
            self.frames.append((main_frame, count))

        # Store the last known grid sizes to avoid redundant updates
        self.last_sizes = [0] * len(self.frames)

        # Bind resize event to update the grid dynamically
        self.bind("<Configure>", self.on_resize)

    def create_grid(self, main_frame, num_labels, n, m):
        # Clear the existing grid
        for widget in main_frame.winfo_children():
            widget.destroy()

        # Create a container frame for the labels
        container_frame = ctk.CTkFrame(main_frame)
        container_frame.pack(anchor="center")

        # Create new grid based on n and m
        for row in range(m):
            for col in range(n):
                label_index = row * n + col
                if label_index < num_labels:
                    label = ctk.CTkLabel(container_frame, text=f"Label {label_index + 1}", width=self.field_width,
                                         height=self.field_height, anchor="center")
                    label.grid(row=row, column=col, padx=self.padx, pady=self.pady)

        # Configure column weights for centering
        for col in range(n):
            container_frame.grid_columnconfigure(col, weight=1)
        for row in range(m):
            container_frame.grid_rowconfigure(row, weight=1)

    def on_resize(self, event):
        for idx, (main_frame, num_labels) in enumerate(self.frames):
            # Get the current frame dimensions
            current_frame_width = main_frame.winfo_width()

            # Calculate the number of fields that fit into the current frame width
            n = max(current_frame_width // self.total_field_width, 1)
            m = (num_labels + n - 1) // n  # Calculate number of rows needed

            # Print the calculations for debugging
            print(f"Frame {idx}: {n} columns, {m} rows")

            # Only update the grid if the size has changed
            if (n, m) != self.last_sizes[idx]:
                self.create_grid(main_frame, num_labels, n, m)
                self.last_sizes[idx] = (n, m)


if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

    app = DynamicGridApp()
    app.mainloop()
