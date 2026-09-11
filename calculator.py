import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        self.current_input = ""
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Поле вывода
        result_frame = tk.Frame(self.root)
        result_frame.pack(pady=10)
        
        result_entry = tk.Entry(
            result_frame, 
            textvariable=self.result_var, 
            font=("Arial", 18), 
            bd=10, 
            relief=tk.FLAT, 
            justify=tk.RIGHT,
            state='readonly'
        )
        result_entry.pack(fill=tk.BOTH, padx=10)
        
        # Кнопки
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Расположение кнопок
        buttons = [
            ('C', '±', '%', '/'),
            ('7', '8', '9', '*'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('0', '.', '=', '⌫')
        ]
        
        for i, row in enumerate(buttons):
            for j, button_text in enumerate(row):
                if button_text == '=':
                    btn = tk.Button(
                        buttons_frame, 
                        text=button_text, 
                        font=("Arial", 14, "bold"),
                        bg='#FF9500',
                        fg='white',
                        command=lambda x=button_text: self.on_button_click(x)
                    )
                elif button_text in ['C', '±', '%', '⌫']:
                    btn = tk.Button(
                        buttons_frame, 
                        text=button_text, 
                        font=("Arial", 14),
                        bg='#A5A5A5',
                        command=lambda x=button_text: self.on_button_click(x)
                    )
                elif button_text in ['/', '*', '-', '+']:
                    btn = tk.Button(
                        buttons_frame, 
                        text=button_text, 
                        font=("Arial", 14),
                        bg='#FF9500',
                        fg='white',
                        command=lambda x=button_text: self.on_button_click(x)
                    )
                else:
                    btn = tk.Button(
                        buttons_frame, 
                        text=button_text, 
                        font=("Arial", 14),
                        bg='#333333',
                        fg='white',
                        command=lambda x=button_text: self.on_button_click(x)
                    )
                
                btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
                btn.config(height=2, width=4)
        
        # Настройка веса строк и столбцов для растягивания
        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)
        for j in range(4):
            buttons_frame.columnconfigure(j, weight=1)
    
    def on_button_click(self, button_text):
        if button_text == 'C':
            self.current_input = ""
            self.result_var.set("0")
        
        elif button_text == '⌫':
            if self.current_input:
                self.current_input = self.current_input[:-1]
                self.result_var.set(self.current_input if self.current_input else "0")
        
        elif button_text == '±':
            if self.current_input and self.current_input[0] == '-':
                self.current_input = self.current_input[1:]
            elif self.current_input:
                self.current_input = '-' + self.current_input
            self.result_var.set(self.current_input if self.current_input else "0")
        
        elif button_text == '%':
            try:
                result = eval(self.current_input) / 100
                self.current_input = str(result)
                self.result_var.set(self.current_input)
            except:
                self.result_var.set("Ошибка")
                self.current_input = ""
        
        elif button_text == '=':
            try:
                # Заменяем символы для корректного вычисления
                expression = self.current_input.replace('×', '*').replace('÷', '/')
                result = eval(expression)
                self.current_input = str(result)
                self.result_var.set(self.current_input)
            except ZeroDivisionError:
                self.result_var.set("Ошибка: деление на 0")
                self.current_input = ""
            except:
                self.result_var.set("Ошибка")
                self.current_input = ""
        
        else:
            if button_text in ['+', '-', '*', '/']:
                # Заменяем символы для лучшего отображения
                display_text = button_text
                if button_text == '*':
                    display_text = '×'
                elif button_text == '/':
                    display_text = '÷'
                
                self.current_input += display_text
            else:
                self.current_input += button_text
            
            self.result_var.set(self.current_input)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()