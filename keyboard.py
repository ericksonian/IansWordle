import tkinter as tk


class KeyboardFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        positions = [
            ("q", 0, 0), ("w", 0, 1), ("e", 0, 2), ("r", 0, 3), ("t", 0, 4), ("y", 0, 5), ("u", 0, 6), ("i", 0, 7),
            ("o", 0, 8), ("p", 0, 9),
            ("a", 1, 0), ("s", 1, 1), ("d", 1, 2), ("f", 1, 3), ("g", 1, 4), ("h", 1, 5), ("j", 1, 6), ("k", 1, 7),
            ("l", 1, 8),
            ("ENTER", 2, 0), ("z", 2, 1), ("x", 2, 2), ("c", 2, 3), ("v", 2, 4), ("b", 2, 5), ("n", 2, 6),
            ("m", 2, 7), ("BKSP", 2, 8)
        ]

        # Create keys
        self.keys = []
        for label, row, col in positions:
            if label == 'ENTER':
                button = tk.Button(self, text=label.upper(), width=2, height=2, font=('Impact', 25))
            elif label == 'BKSP':
                button = tk.Button(self, text=label.upper(), width=2, height=2, font=('Impact', 25))
            else:
                button = tk.Button(self, text=label.upper(), width=1, height=2, font=('Impact', 30))
            button.grid(row=row, column=col, sticky="nsew")
            self.keys.append(button)

        # Set row and column weights
        for row in range(3):
            self.rowconfigure(row, weight=1)
        for col in range(10):
            self.columnconfigure(col, weight=1)

    def button_click(self, letter):
        # Handle button click event
        # Update the letter on the button based on the feedback from the game
        pass
