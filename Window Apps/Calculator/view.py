import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
import ctypes
import math

# Adjust resolution
ctypes.windll.shcore.SetProcessDpiAwareness(1)


class VIEW(tk.Tk):
    """
    Create VIEW to manage all frames
    """

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.title("Calculator")
        self.minsize(600, 768)
        self.geometry("600x768")
        self.resizable(True, True)
        # Adjust transparent of window tkinter (0 to 1)
        self.attributes('-alpha', 1)
        # windows only (remove the minimize/maximize button)
        # self.attributes('-toolwindow', True)

        self.main_line = ""
        self.subline = ""

        self.view_rows_columns_configure()
        self.create_frames()

    def init_display(self):
        self.mainloop()

    def view_rows_columns_configure(self):
        # Rows confiure
        self.rowconfigure(0, weight=1)

        # Colums configure
        self.columnconfigure(0, weight=1)

    def create_frames(self):
        self.standard_frame = STANDARD_FRAME(self, self.controller)
        self.standard_frame.grid(row=0, column=0, sticky=NSEW)

    def insert_main_line(self, content):
        if not isinstance(content, str):
            # All following cases for better output displaying 

            if content >= 1e16 or content <= -1e16:
                self.configure_main_line_size(-10)
                try:
                    content = "{:.12e}".format(content)
                except:
                    self.error(-10, "Overflow")
                    return

            elif len(str(content)) > 10:
                if len(str(content)) > 19:
                    content = "{:,.15f}".format(content)
                else:
                    content = "{:,}".format(content)
                self.configure_main_line_size(-11)
            
            elif content < 1e-4 and len(str(content)) > 10:
                content = "{:.10e}".format(content)
                self.configure_main_line_size(-7)

            elif content > 1e-4 and content < 1 and len(str(content)) > 10:
                content = format(content, '.14f')
                self.configure_main_line_size(-7)

            else:
                content = "{:,}".format(content)
                self.configure_main_line_size(0)

        self.main_line_text = tk.StringVar()
        self.main_line_text.set(content)
        self.standard_frame.display_frame.main_line.configure(state="normal")
        self.standard_frame.display_frame.main_line.configure(
            textvariable=self.main_line_text)
        self.standard_frame.display_frame.main_line.configure(state="readonly")

    def insert_subline(self, content):
        if len(str(content)) > 33:
            self.configure_subline_size(-3)
        self.standard_frame.display_frame.subline.configure(text=content)

    def configure_main_line_size(self, change):
        new_size = self.standard_frame.display_frame.main_line_size_default + change
        self.standard_frame.display_frame.main_line['font'] = (
            "Helvetica", new_size)

    def configure_subline_size(self, change):
        new_size = self.standard_frame.display_frame.subline_size_default + change
        self.standard_frame.display_frame.subline['font'] = (
            "Helvetica", new_size)


    def error(self, size_change, error_message):
        for i in range(6):
            self.standard_frame.memory_button_frame.memory_buttons[i]['state'] = "disabled"

        for i in range(11):
            if i in [1, 2, 3]:
                continue
            self.standard_frame.calculating_button_frame.calculating_buttons[
                i]['state'] = "disabled"

        self.standard_frame.calculating_button_frame.calculating_buttons[
            20]['state'] = "disabled"
        self.standard_frame.calculating_button_frame.calculating_buttons[
            22]['state'] = "disabled"

        self.configure_main_line_size(size_change)
        self.insert_main_line(error_message)


class STANDARD_FRAME(ttk.Frame):
    """
    Create parent frame: STANDARD_FRAME
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.setup_style()
        self.configure_rows_columns()
        self.setup_subframes()

    def setup_style(self):
        self.theme_style = ttk.Style()
        # self.theme_style.configure("Standard.TFrame", background="green")
        self.theme_style.configure("TFrame", background="#1f1f1f")

    def configure_rows_columns(self):
        # Rows confiure (5)
        # weight = 0 means no responsive
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        # Colums configure (0)
        self.columnconfigure(0, weight=1)

    def setup_subframes(self):
        self.menu_bar_frame = MENU_BAR_FRAME(self)
        self.menu_bar_frame.grid(row=0, column=0,  padx=0, pady=0, sticky=NSEW)

        self.display_frame = DISPLAY_FRAME(self)
        self.display_frame.grid(row=1, column=0,  padx=20, pady=5, sticky=NSEW)

        self.memory_button_frame = MEMORY_BUTTON_FRAME(self)
        self.memory_button_frame.grid(
            row=2, column=0,  padx=5, pady=5, sticky=NSEW)

        self.calculating_button_frame = CALCULATING_BUTTON_FRAME(
            self, self.controller)
        self.calculating_button_frame.grid(
            row=3, column=0,  padx=5, pady=5, sticky=NSEW)


class MENU_BAR_FRAME(ttk.Frame):
    """
    Create subframe 1: MENU_BAR_FRAME
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.color_on_hover = "#575757"
        self.setup_style()
        self.configure_rows_columns()
        self.setup_widgets()

    def setup_style(self):
        self.menu_bar_frame_style = ttk.Style()
        self.menu_bar_frame_style.configure(
            "Menu_bar_label.TLabel", background="#1f1f1f", foreground="white")
        # self.configure("Menu_bar_frame.TFrame")

    def configure_rows_columns(self):
        # Rows confiure (0)
        # weight = 0 means no responsive
        self.rowconfigure(0, weight=1)

        # Colums configure (4)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=10)
        self.columnconfigure(3, weight=1)

    def change_on_hover(self, button, colorOnHover, colorOnLeave):
        # adjusting backgroung of the widget
        # background on entering widget
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover))

        # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave))

    def setup_widgets(self):
        self.menu_bar_fram_bg = "#1f1f1f"
        self.menu_bar_fram_fg = "white"
        self.font = ('Arial Unicode MS', 14, "bold")
        self.menu_button = tk.Button(
            self, text="\u2630", relief="flat", font=self.font, bg=self.menu_bar_fram_bg, fg=self.menu_bar_fram_fg)
        self.menu_button.grid(row=0, column=0, ipadx=5, ipady=5, sticky=NSEW)
        self.mode_label = ttk.Label(
            self, text="Standard", font=self.font, style='Menu_bar_label.TLabel')
        self.mode_label.grid(row=0, column=1, padx=5, sticky=NSEW)

        self.extend_collapse_button = tk.Button(
            self, text="\u2197", font=self.font, relief="flat", bg=self.menu_bar_fram_bg, fg=self.menu_bar_fram_fg)
        self.extend_collapse_button.grid(row=0, column=2, sticky=W+N+S)

        self.history_button = tk.Button(
            self, text="\u21ba", font=self.font, relief="flat", bg=self.menu_bar_fram_bg, fg=self.menu_bar_fram_fg)
        self.history_button.grid(
            row=0, column=3, ipadx=5, ipady=5, sticky=N+S+E)

        # Setup hover color
        self.menu_bar_buttons = []
        self.menu_bar_buttons.append(self.menu_button)
        self.menu_bar_buttons.append(self.extend_collapse_button)
        self.menu_bar_buttons.append(self.history_button)

        for i in range(3):
            self.change_on_hover(
                self.menu_bar_buttons[i], self.color_on_hover, self.menu_bar_buttons[i]["bg"])


class DISPLAY_FRAME(ttk.Frame):
    """
    Create subframe 2: DISPLAY_FRAME
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.color_on_hover = "#575757"
        self.main_line_size_default = 37
        self.subline_size_default = 16
        self.setup_style()
        self.configure_rows_columns()
        self.setup_widgets()

    def setup_style(self):
        self.style = ttk.Style()
        # self.style.configure("Display_frame.TFrame", background="black")
        # self.style.configure("entry.TEntry", background="black")
        self.style.configure("expression.TLabel",
                             background="#1f1f1f", foreground="white")

    def configure_rows_columns(self):
        # Rows confiure (2)
        # weight = 0 means no responsive
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # Colums configure (0)
        self.columnconfigure(0, weight=1)

    def change_on_hover(self, button, colorOnHover, colorOnLeave):
        # adjusting backgroung of the widget
        # background on entering widget
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover))

        # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave))

    def setup_widgets(self):
        self.subline = ttk.Label(
            self, text="", font=("Helvetica", self.subline_size_default), style="expression.TLabel")
        self.subline.grid(row=0, column=0, sticky=N+S+E)

        self.main_line = tk.Entry(self, font=(
            "Helvetica", self.main_line_size_default), justify="right", state='readonly', fg='white', readonlybackground='#1f1f1f')  # readonlybackground='white'
        self.var = tk.StringVar()
        self.var.set('0')
        self.main_line.configure(textvariable=self.var, relief='flat')
        self.main_line.grid(row=1, column=0, sticky=N+S+E)


class MEMORY_BUTTON_FRAME(ttk.Frame):
    """
    Create subframe 3: MEMORY_BUTTON_FRAME
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.color_on_hover = "#575757"
        self.setup_style()
        self.configure_rows_columns()
        self.setup_widgets()

    def setup_style(self):
        self.style = ttk.Style()
        # self.style.configure("Memory_button_frame.TFrame", background="red")
        self.configure(style="Memory_button_frame.TFrame")

    def configure_rows_columns(self):
        # Rows confiure (1)
        # weight = 0 means no responsive
        self.rowconfigure(0, weight=1)

        # Colums configure (6)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)

    def change_on_hover(self, button, colorOnHover, colorOnLeave):
        # adjusting backgroung of the widget
        # background on entering widget
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover))

        # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave))

    def setup_widgets(self):
        self.memory_button_font = ('Arial Unicode MS', 10)
        self.memory_buttons = []
        self.memory_button_count = -1
        self.memory_button_text = ['MC', 'MR', 'M+', 'M-', 'MS', 'M']
        self.memory_button_bg = "#1f1f1f"
        self.memory_button_fg = "white"

        for i in range(6):
            self.memory_button_count += 1
            self.memory_buttons.append(tk.Button(
                self, text=self.memory_button_text[self.memory_button_count], command='1', relief="flat", font=self.memory_button_font, bg=self.memory_button_bg, fg=self.memory_button_fg))
            self.memory_buttons[self.memory_button_count].grid(
                row=0, column=i, sticky=NSEW)

            # Setup hover color
            self.change_on_hover(
                self.memory_buttons[i], self.color_on_hover, self.memory_buttons[i]["bg"])


class CALCULATING_BUTTON_FRAME(ttk.Frame):
    """
    Create subframe 4: CALCULATING_BUTTON_FRAME
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.color_on_hover = "#575757"
        self.color_on_hover_equal_button = "#04A8B2"
        self.setup_style()
        self.configure_rows_columns()
        self.setup_widgets()

    def setup_style(self):
        self.style = ttk.Style()
        # self.style.configure("Memory_button_frame.TFrame", background="red")
        self.configure(style="Memory_button_frame.TFrame")

    def configure_rows_columns(self):
        # Rows confiure (6)
        # weight = 0 means no responsive
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)

        # Colums configure (4)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

    def change_on_hover(self, button, colorOnHover, colorOnLeave):
        # adjusting backgroung of the widget
        # background on entering widget
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover))

        # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave))

    def setup_widgets(self):
        self.operation_button_font = ('Arial Unicode MS', 14)
        self.number_button_font = ('Arial Unicode MS', 14)
        self.equal_button_font = ('Arial Unicode MS', 14)

        self.operation_button_bg = "#131313"
        self.operation_button_fg = "white"
        self.number_button_bg = "#060606"
        self.number_button_fg = "white"
        self.equal_button_bg = "#135C61"
        self.equal_button_fg = "white"

        self.calculating_buttons = []
        self.calculating_button_count = -1
        # \u232: Erase to the Left
        # \u215f: Fraction Numerator One
        # x\u00b2: x squared
        # \u221ax: Square Root of x
        # \u00f7: Division Sign
        # \u00d7: Multiplication Sign
        # -: Minus Sign
        # +: Plus Sign
        # \u00b1: Plus-Minus Sign
        self.calculating_button_text = [
            '%', 'CE', 'C', '\u232b',
            '\u215f', 'x\u00b2', '\u221ax', '\u00f7',
            '\u00d7', '-', '+',
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '\u00b1', '0', '.',
            '='
        ]

        for i in range(4):
            self.calculating_button_count += 1
            self.calculating_buttons.append(tk.Button(
                self, text=self.calculating_button_text[self.calculating_button_count],
                command=(
                    lambda txt=self.calculating_button_text[self.calculating_button_count]: self.controller.button_trigger(txt)),
                relief="flat", font=self.operation_button_font, bg=self.operation_button_bg, fg=self.operation_button_fg))
            self.calculating_buttons[self.calculating_button_count].grid(
                row=0, column=i, padx=2, pady=2, sticky=NSEW)

        for i in range(4):
            self.calculating_button_count += 1
            self.calculating_buttons.append(tk.Button(
                self, text=self.calculating_button_text[self.calculating_button_count],
                command=(
                    lambda txt=self.calculating_button_text[self.calculating_button_count]: self.controller.button_trigger(txt)),
                relief="flat", font=self.operation_button_font, bg=self.operation_button_bg, fg=self.operation_button_fg))
            self.calculating_buttons[self.calculating_button_count].grid(
                row=1, column=i, padx=2, pady=2, sticky=NSEW)

        for i in range(3):
            self.calculating_button_count += 1
            self.calculating_buttons.append(tk.Button(
                self, text=self.calculating_button_text[self.calculating_button_count],
                command=(
                    lambda txt=self.calculating_button_text[self.calculating_button_count]: self.controller.button_trigger(txt)),
                relief="flat", font=self.operation_button_font, bg=self.operation_button_bg, fg=self.operation_button_fg))
            self.calculating_buttons[self.calculating_button_count].grid(
                row=i+2, column=3, padx=2, pady=2, sticky=NSEW)

        for i in range(12):
            self.calculating_button_count += 1
            self.calculating_buttons.append(tk.Button(
                self, text=self.calculating_button_text[self.calculating_button_count],
                command=(
                    lambda txt=self.calculating_button_text[self.calculating_button_count]: self.controller.button_trigger(txt)),
                relief="flat", font=self.number_button_font, bg=self.number_button_bg, fg=self.number_button_fg))
            self.calculating_buttons[self.calculating_button_count].grid(
                row=int(i/3)+2, column=i % 3, padx=2, pady=2, sticky=NSEW)

        self.equal_button = tk.Button(
            self, text='=',
            command=(
                lambda: self.controller.button_trigger("=")),
            relief="flat", font=self.equal_button_font, bg=self.equal_button_bg, fg=self.equal_button_fg)
        self.equal_button.grid(row=5, column=3, padx=2, pady=2, sticky=NSEW)

        # Setup hover color
        for i in range(23):
            self.change_on_hover(
                self.calculating_buttons[i], self.color_on_hover, self.calculating_buttons[i]["bg"])

        self.change_on_hover(
            self.equal_button, self.color_on_hover_equal_button, self.equal_button["bg"])


def main():
    pass


if __name__ == '__main__':
    main()
