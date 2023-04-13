import tkinter as tk
from keyboard import KeyboardFrame

class WordleUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Ian's Wordle")
        self.geometry("500x1000")

        title_label = tk.Label(text="Ian's Wordle", font=("Arial", 30))
        title_label.pack(side=tk.TOP, pady=10)

        # Top Row Frame
        self.top_row_frame = tk.Frame(self, width=480, height=100)
        self.top_row_frame.pack(side=tk.TOP, pady=10)

        for i in range(5):
            letter_label = tk.Label(self.top_row_frame, text="", font=("Arial", 30), width=2, height=1, relief=tk.RIDGE, bd=2)
            letter_label.grid(row=0, column=i, padx=5, pady=5)

        self.keyboard = KeyboardFrame(self)
        self.keyboard.pack()


if __name__ == "__main__":
    app = WordleUI()
    app.mainloop()
