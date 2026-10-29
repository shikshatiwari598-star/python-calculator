
import tkinter as tk

def press(value):
    if value == "C":
        display.delete(0, tk.END)

    elif value == "=":
        try:
            expression = display.get()
            allowed = "0123456789+-*/.() "

            if not expression or any(
                char not in allowed for char in expression
            ):
                raise ValueError

            result = eval(expression, {"__builtins__": {}}, {})
            display.delete(0, tk.END)
            display.insert(0, str(result))

        except Exception:
            display.delete(0, tk.END)
            display.insert(0, "Error")

    else:
        display.insert(tk.END, value)


root = tk.Tk()
root.title("My Python Calculator")
root.geometry("340x440")
root.resizable(False, False)

display = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bd=5
)
display.grid(
    row=0, column=0, columnspan=4,
    padx=10, pady=15, sticky="nsew", ipady=10
)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), (".", 4, 2), ("+", 4, 3),
    ("=", 5, 0)
]

for text, row, col in buttons:
    if text == "=":
        btn = tk.Button(
            root, text=text, font=("Arial", 20),
            command=lambda v=text: press(v)
        )
        btn.grid(
            row=row, column=0, columnspan=4,
            padx=10, pady=5, sticky="nsew"
        )
    else:
        btn = tk.Button(
            root, text=text, font=("Arial", 20),
            command=lambda v=text: press(v)
        )
        btn.grid(
            row=row, column=col,
            padx=5, pady=5, sticky="nsew"
        )

for col in range(4):
    root.grid_columnconfigure(col, weight=1)

for row in range(1, 6):
    root.grid_rowconfigure(row, weight=1)

root.mainloop()
