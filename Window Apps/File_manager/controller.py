from view import *
from model import *


class CONTROLLER:
    """
    In MVC 
    CONTROLLER is used to process logic and control MODEL and VIEW
    """

    def __init__(self):
        self.view = VIEW(self)
        self.model = MODEL(self)

    def app_style(self):
        self.style = ttk.Style()
        # self.style.configure("TFrame", background='green')

    def start_app(self):
        self.view.init_display()

    def open_directory(self):
        self.model.open_directory()

    def treeview_sort_column(self, option):
        self.model.treeview_sort_column(option)

    def execute_reorganization(self):
        self.model.execute_reorganization()

    def unexecute_reorganization(self):
        self.model.unexecute_reorganization()

def main():
    app = CONTROLLER()
    app.start_app()


if __name__ == "__main__":
    main()
