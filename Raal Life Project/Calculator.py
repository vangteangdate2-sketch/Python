import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.expression = ""
        self.display_text = tk.StringVar(value="0")

        self.setup_window()
        self.create_display()
        self.create_buttons()
        self.bind_keyboard()

    def setup_window(self):
        self.root.title("Simple Calculator")
        self.root.geometry("340x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#17191f")

    def create_display(self):
        title = tk.Label(
            self.root,
            text="Calculator",
            bg="#17191f",
            fg="#a8adb8",
            font=("Segoe UI", 12),
            anchor="w",
        )
        title.pack(fill="x", padx=24, pady=(22, 8))

        display = tk.Entry(
            self.root,
            textvariable=self.display_text,
            state="readonly",
            readonlybackground="#22252d",
            fg="#ffffff",
            justify="right",
            relief="flat",
            font=("Segoe UI", 28, "bold"),
        )
        display.pack(fill="x", padx=20, ipady=20)

    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg="#17191f")
        button_frame.pack(fill="both", expand=True, padx=16, pady=16)

        buttons = [
            ["AC", "⌫", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["±", "0", ".", "="],
        ]

        for row_number, row in enumerate(buttons):
            button_frame.rowconfigure(row_number, weight=1)
            for column_number, label in enumerate(row):
                button_frame.columnconfigure(column_number, weight=1)
                button = tk.Button(
                    button_frame,
                    text=label,
                    command=lambda value=label: self.press(value),
                    bg=self.button_color(label),
                    fg="#ffffff",
                    activebackground="#4b5160",
                    activeforeground="#ffffff",
                    relief="flat",
                    borderwidth=0,
                    font=("Segoe UI", 15, "bold"),
                    cursor="hand2",
                )
                button.grid(
                    row=row_number,
                    column=column_number,
                    sticky="nsew",
                    padx=4,
                    pady=4,
                )

    def button_color(self, label):
        if label == "=":
            return "#f97316"
        if label in {"÷", "×", "-", "+"}:
            return "#323844"
        if label in {"AC", "⌫", "%", "±"}:
            return "#3b404c"
        return "#292d36"

    def press(self, value):
        if value == "AC":
            self.expression = ""
        elif value == "⌫":
            self.expression = self.expression[:-1]
        elif value == "=":
            self.calculate()
            return
        elif value == "%":
            self.percent()
            return
        elif value == "±":
            self.change_sign()
            return
        elif value in {"÷", "×", "-", "+"}:
            self.add_operator(value)
        elif len(self.expression) < 24:
            self.expression += value

        self.update_display()

    def add_operator(self, operator):
        if not self.expression:
            if operator == "-":
                self.expression = "-"
            return

        if self.expression[-1] in "÷×-+":
            self.expression = self.expression[:-1] + operator
        else:
            self.expression += operator

    def calculate(self):
        try:
            result = eval(self.expression.replace("×", "*").replace("÷", "/"))
            self.expression = self.format_number(result)
        except (SyntaxError, ZeroDivisionError):
            self.expression = ""
            self.display_text.set("Error")
            return

        self.update_display()

    def percent(self):
        if not self.expression:
            return
        try:
            value = eval(self.expression.replace("×", "*").replace("÷", "/"))
            self.expression = self.format_number(value / 100)
            self.update_display()
        except (SyntaxError, ZeroDivisionError):
            self.display_text.set("Error")

    def change_sign(self):
        if not self.expression:
            self.expression = "-"
        elif self.expression.startswith("-"):
            self.expression = self.expression[1:]
        else:
            self.expression = "-" + self.expression
        self.update_display()

    def format_number(self, number):
        if isinstance(number, float) and number.is_integer():
            return str(int(number))
        return str(round(number, 10))

    def update_display(self):
        self.display_text.set(self.expression or "0")

    def bind_keyboard(self):
        self.root.bind("<Return>", lambda event: self.press("="))
        self.root.bind("<BackSpace>", lambda event: self.press("⌫"))
        self.root.bind("<Escape>", lambda event: self.press("AC"))
        self.root.bind("<Key>", self.handle_key)

    def handle_key(self, event):
        key_map = {"*": "×", "/": "÷"}
        value = key_map.get(event.char, event.char)
        if value in "0123456789.+-×÷":
            self.press(value)


if __name__ == "__main__":
    window = tk.Tk()
    Calculator(window)
    window.mainloop()



    