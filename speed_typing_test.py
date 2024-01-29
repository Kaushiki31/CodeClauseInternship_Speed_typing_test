import tkinter as tk
import random
import time

class SpeedTypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")

        self.sentences = [
            "Absence makes the heart grow fonder.",
            "She sells seashells by the seashore.",
            "Action speaks louder than words.",
            "All that glitters is not gold.",
            "The quick brown fox jumps over the lazy dog.",
            "A picture is worth a thousand words.",
            "Strike while the iron is hot.",
            "Many hands make light work.",
            "The grass is always greener on the other side of the fence.",
            "You cannot make an omelette without breaking a few eggs.",
        ]

        self.current_sentence = ""
        self.time_start = 0

        self.label_sentence = tk.Label(root, text="", font=("Helvetica", 18), wraplength=400)
        self.label_sentence.pack(pady=20)

        self.entry = tk.Entry(root, font=("Helvetica", 16))
        self.entry.pack(pady=10)

        self.label_wpm = tk.Label(root, text="WPM: 0", font=("Helvetica", 14))
        self.label_wpm.pack(pady=10)

        self.button_start = tk.Button(root, text="Start", command=self.start_game)
        self.button_start.pack(pady=10)

    def start_game(self):
        self.label_wpm.config(text="WPM: 0")
        self.time_start = time.time()
        self.next_sentence()

    def next_sentence(self):
        self.current_sentence = random.choice(self.sentences)
        self.label_sentence.config(text=self.current_sentence)
        self.entry.delete(0, tk.END)
        self.entry.focus()

    def check_input(self, event):
        user_input = self.entry.get().strip()
        if user_input == self.current_sentence:
            time_elapsed = (time.time() - self.time_start) / 60.0
            wpm = int(len(user_input) / 5 / time_elapsed)
            self.label_wpm.config(text=f"WPM: {wpm}")
            self.next_sentence()

    def run(self):
        self.root.bind("<Return>", self.check_input)
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTypingTest(root)
    app.run()
