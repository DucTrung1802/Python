from tkinter import *
from tkinter import ttk


def frame1(parent):
    frame_1 = ttk.Frame(parent)

    frame_1.columnconfigure(0, weight=2)
    frame_1.columnconfigure(1, weight=3)
    button_frame1 = ttk.Label(frame_1, text="Find:")
    button_frame1.grid(column=0, row=0, pady=1, sticky=W, padx=4)
    button_frame2 = ttk.Label(frame_1, text="Replace:")
    button_frame2.grid(column=0, row=1, pady=1, sticky=W, padx=4)
    button_frame3 = ttk.Entry(frame_1)
    button_frame3.grid(column=1, row=0, pady=1, ipadx=75, padx=10)
    button_frame4 = ttk.Entry(frame_1)
    button_frame4.grid(column=1, row=1, pady=1, ipadx=75, padx=10)
    match_case = StringVar()
    check_button1 = ttk.Checkbutton(frame_1, text="Match case", variable=match_case, command=lambda: print(match_case.get()))
    check_button1.grid(column=0, row=2, pady=1,
                       padx=10, columnspan=2, sticky=W)
    wrap_around = StringVar()
    check_button2 = ttk.Checkbutton(frame_1, text="Wrap around", variable=wrap_around, command=lambda: print(wrap_around.get()))
    check_button2.grid(column=0, row=3, pady=1,
                       padx=10, columnspan=2, sticky=W)

    return frame_1


def frame2(parent):
    frame_2 = ttk.Frame(parent)

    frame_2.columnconfigure(0, weight=1)
    frame_2.columnconfigure(1, weight=3)
    button_frame1 = ttk.Button(frame_2, text="Replace")
    button_frame1.grid(column=0, row=0, pady=2)
    button_frame2 = ttk.Button(frame_2, text="Replace All")
    button_frame2.grid(column=0, row=1, pady=2)
    button_frame3 = ttk.Button(frame_2, text="Find Next")
    button_frame3.grid(column=0, row=2, pady=2)
    button_frame4 = ttk.Button(frame_2, text="Cancel")
    button_frame4.grid(column=0, row=3, pady=2)

    return frame_2


def main_window():
    root = Tk()
    root.geometry("430x130")
    root.title("Searching Box")
    root.resizable(False, False)
    root.columnconfigure(0, weight=5)
    root.columnconfigure(1, weight=1)

    input_frame1 = frame1(root)
    input_frame1.grid(column=0, row=0)

    input_frame2 = frame2(root)
    input_frame2.grid(column=1, row=0)

    root.mainloop()


if __name__ == "__main__":
    main_window()
