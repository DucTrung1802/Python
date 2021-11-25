import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


class VIEW(tk.Tk):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self.title("File Manager")
        self.minsize(870, 278)
        self.geometry("1230x550")
        self.resizable(True, True)
        # windows only (remove the minimize/maximize button)
        # self.attributes('-toolwindow', True)

        self.app_rows_columns_configure()
        self.create_frames()

    def init_display(self):
        self.mainloop()

    def app_rows_columns_configure(self):
        # Rows confiure
        self.rowconfigure(0, weight=1)

        # Colums configure
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)
        self.columnconfigure(2, weight=1)

    def create_frames(self):
        self.treeview_directory_frame = Treeview_Directory_Frame(
            self.controller)
        self.treeview_directory_frame.grid(
            row=0, column=0, sticky=NSEW, padx=15, pady=10)

        self.treeview_file_frame = Treeview_File_Frame(self.controller)
        self.treeview_file_frame.grid(
            row=0, column=1, sticky=NSEW, padx=15, pady=10)

        self.sorting_menu_frame = Sorting_Menu_Frame(self.controller)
        self.sorting_menu_frame.grid(
            row=0, column=2, sticky=NSEW, padx=15, pady=10)


class Treeview_Directory_Frame(ttk.Frame):
    """
    Treeview_Directory_Frame is container, used to group treeview directory
    widgets together.
    """

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.configure_rows_columns()
        self.setup_widgets()

    def configure_rows_columns(self):
        """
        Configure rows and columns for Treeview_Directory_Frame.
        """
        # Rows confiure (3)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)  # weight = 0 means no responsive
        self.rowconfigure(2, weight=0)  # weight = 0 means no responsive

        # Colums configure (2)
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=1)

    def setup_widgets(self):
        """
        Setup all widgets for Treeview_Directory_Frame.
        """
        self.treeview_directory = ttk.Treeview(self)
        self.treeview_directory_heading = self.treeview_directory.heading(
            "#0", text="Directory Tree", anchor='w')

        # LITTLE TRICK: horizontal scrollbar does not work, then we MUST have
        #  the parameter minwidth at least 1000 of column #0
        self.treeview_directory.column("#0", anchor=CENTER, minwidth=1000)
        self.treeview_directory.grid(
            row=0, column=0, sticky=NSEW, pady=0, padx=0, ipady=100)

        # Used for detecting selected item:
        # self.treeview_directory.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.treeview_directory_vertical_scrollbar = ttk.Scrollbar(
            self, orient='vertical', command=self.treeview_directory.yview)
        self.treeview_directory_vertical_scrollbar.grid(
            row=0, column=1, sticky=NSEW, pady=0, padx=0)
        self.treeview_directory['yscrollcommand'] = self.treeview_directory_vertical_scrollbar.set

        self.treeview_directory_horizontal_scrollbar = tk.Scrollbar(
            self, orient='horizontal', command=self.treeview_directory.xview)
        self.treeview_directory_horizontal_scrollbar.grid(
            row=1, column=0, sticky=NSEW, pady=0, padx=0)
        self.treeview_directory['xscrollcommand'] = self.treeview_directory_horizontal_scrollbar.set

        self.treeview_directory_browswer_button = ttk.Button(
            self, text="Choose Directory", command=self.controller.open_directory)
        self.treeview_directory_browswer_button.grid(
            row=2, column=0, sticky=NS, pady=20, padx=0, columnspan=2)


class Treeview_File_Frame(ttk.Frame):
    """
    Treeview_File_Frame is container, used to group treeview file
    widgets together.
    """

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.configure_rows_columns()
        self.setup_widgets()

    def configure_rows_columns(self):
        """
        Configure rows and columns for Treeview_File_Frame.
        """
        # Rows confiure (4)
        self.rowconfigure(0, weight=0)  # weight = 0 means no responsive
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)  # weight = 0 means no responsive
        self.rowconfigure(3, weight=0)  # weight = 0 means no responsive

        # Colums configure (4)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

    def setup_widgets(self):
        """
        Setup all widgets for Treeview_Directory_Frame.
        """
        self.label_path = ttk.Label(self, text="PATH:")
        self.label_path.grid(row=0, column=0, sticky=N,
                             pady=20, padx=0)

        self.entry_path = ttk.Entry(self)
        self.entry_path.configure(state='readonly')
        self.entry_path.grid(row=0, column=1, sticky=EW, pady=20,
                             padx=0, columnspan=3)

        columns = ('Name', 'Data Modified', 'Extension', 'Size')
        self.treeview_file = ttk.Treeview(
            self, column=columns, show='headings')

        # PROBLEM: CHANGE 'command' of each column if neccessary
        self.treeview_file.heading(
            "#1", text="Name", anchor=N, command=lambda: self.controller.treeview_sort_column(1))
        self.treeview_file.column(
            "#1", anchor=W, width=100, minwidth=70)
        self.treeview_file.heading(
            "#2", text="Data Modified", anchor=N, command=lambda: self.controller.treeview_sort_column(2))
        self.treeview_file.column(
            "#2", anchor=CENTER, width=130, minwidth=130)
        self.treeview_file.heading(
            "#3", text="Extension", anchor=N, command=lambda: self.controller.treeview_sort_column(3))
        self.treeview_file.column(
            "#3", anchor=CENTER, width=70, minwidth=70)
        self.treeview_file.heading(
            "#4", text="Size", anchor=N, command=lambda: self.controller.treeview_sort_column(4))
        self.treeview_file.column(
            "#4", anchor=E, width=80, minwidth=80)

        self.treeview_file.grid(row=1, column=0, sticky=NSEW,
                                pady=0, padx=0, ipadx=0, ipady=80, columnspan=4)

        self.vertical_scrollbar = ttk.Scrollbar(
            self, orient='vertical', command=self.treeview_file.yview)
        self.vertical_scrollbar.grid(
            row=1, column=5, sticky=NS, pady=0, padx=0)
        self.treeview_file['yscrollcommand'] = self.vertical_scrollbar.set

        self.horizontal_scrollbar = ttk.Scrollbar(
            self, orient='horizontal', command=self.treeview_file.xview)
        self.horizontal_scrollbar.grid(
            row=2, column=0, sticky=EW, pady=0, padx=0, columnspan=4)
        self.treeview_file['xscrollcommand'] = self.horizontal_scrollbar.set

        self.undo_button = ttk.Button(self, text="UNDO")
        self.undo_button.grid(row=3, column=0, sticky=N, pady=20, padx=0)

        self.copy_button = ttk.Button(self, text="COPY")
        self.copy_button.grid(row=3, column=1, sticky=N, pady=20, padx=0)

        self.cut_button = ttk.Button(self, text="CUT")
        self.cut_button.grid(row=3, column=2, sticky=N, pady=20, padx=0)

        self.paste_button = ttk.Button(self, text="PASTE")
        self.paste_button.grid(row=3, column=3, sticky=N, pady=20, padx=0)


class Sorting_Menu_Frame(ttk.Frame):
    """
    Sorting_Menu_Frame is container, used to group sorting menu
    widgets together.
    """

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.configure_rows_columns()
        self.setup_widgets()

    def configure_rows_columns(self):
        """
        Configure rows and columns for Sorting_Menu_Frame.
        """
        # Rows confiure (6)
        self.rowconfigure(0, weight=0)  # weight = 0 means no responsive
        self.rowconfigure(1, weight=0)  # weight = 0 means no responsive
        self.rowconfigure(2, weight=0)  # weight = 0 means no responsive
        self.rowconfigure(3, weight=0)  # weight = 0 means no responsive
        self.rowconfigure(4, weight=0)  # weight = 0 means no responsive
        self.rowconfigure(5, weight=0)  # weight = 0 means no responsive

        # Colums configure (4)
        self.columnconfigure(0, weight=0)   # weight = 0 means no responsive
        self.columnconfigure(1, weight=0)   # weight = 0 means no responsive

    def setup_widgets(self):
        self.selected_option = IntVar()

        # create widgets
        self.sorting_label = ttk.Label(
            self, text="REORGANIZATION TYPE:")
        self.sorting_label.grid(row=0, column=0, sticky=NSEW,
                                pady=10, padx=0, columnspan=2)

        self.option_1 = ttk.Radiobutton(
            self, text="Reorganize files by extensions", value="1", variable=self.selected_option)
        self.option_1.grid(row=1, column=0, sticky=NSEW,
                           pady=10, padx=0, columnspan=2)

        self.option_2 = ttk.Radiobutton(
            self, text="B", value="2", variable=self.selected_option)
        self.option_2.grid(row=2, column=0, sticky=NSEW,
                           pady=10, padx=0, columnspan=2)

        self.option_3 = ttk.Radiobutton(
            self, text="C", value="3", variable=self.selected_option)
        self.option_3.grid(row=3, column=0, sticky=NSEW,
                           pady=10, padx=0, columnspan=2)

        self.option_4 = ttk.Radiobutton(
            self, text="D", value="4", variable=self.selected_option)
        self.option_4.grid(row=4, column=0, sticky=NSEW,
                           pady=10, padx=0, columnspan=2)

        self.unexcute_button = ttk.Button(
            self, text="UN-EXCUTE", command=lambda: self.controller.unexecute_reorganization())
        self.unexcute_button.grid(
            row=5, column=0, sticky=EW, pady=10, padx=10)

        self.excute_button = ttk.Button(
            self, text="EXCUTE", command=lambda: self.controller.execute_reorganization())
        self.excute_button.grid(
            row=5, column=1, sticky=EW, pady=10, padx=10)


def main():
    pass


if __name__ == "__main__":
    main()
