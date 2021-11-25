import os
import time
import tkinter as tk
from tkinter import filedialog


class MODEL():
    def __init__(self, controller):
        self.controller = controller

    def open_directory(self):
        self.new_path = filedialog.askdirectory()

        if (self.new_path):
            self.ascending_sort = False
            self.list_of_extensions = []
            self.last_reorganize_type = 0
            self.path = self.new_path

            for i in self.controller.view.treeview_directory_frame.treeview_directory.get_children():
                self.controller.view.treeview_directory_frame.treeview_directory.delete(
                    i)
            root_node = self.controller.view.treeview_directory_frame.treeview_directory.insert(
                '', 'end', text=self.path, open=True)
            self.process_directory(root_node, self.path)

            self.controller.view.treeview_file_frame.entry_path.configure(
                state='textvariable')
            self.controller.view.treeview_file_frame.entry_path.delete(
                0, 'end')
            self.controller.view.treeview_file_frame.entry_path.insert(
                0, self.path)
            self.controller.view.treeview_file_frame.entry_path.configure(
                state='readonly')

            self.list_files_and_folders(self.path)

    def list_files_and_folders(self, path):
        self.directory_content = []
        for i in self.controller.view.treeview_file_frame.treeview_file.get_children():
            self.controller.view.treeview_file_frame.treeview_file.delete(i)

        files_and_folders = os.listdir(path)

        for i in range(0, len(files_and_folders)):
            abs_path = path+'/'+files_and_folders[i]
            modTimesinceEpoc = os.path.getmtime(abs_path)
            last_modified = time.strftime(
                '%m-%d-%Y %H:%M:%S', time.localtime(modTimesinceEpoc))
            file_name, file_extension = os.path.splitext(abs_path)
            size, size_in_byte = self.get_readable_size(abs_path)

            self.directory_content.append(
                (files_and_folders[i], last_modified, file_extension, size, size_in_byte))

            self.list_of_extensions.append(file_extension)

            self.controller.view.treeview_file_frame.treeview_file.insert('', tk.END, iid=i, values=(
                files_and_folders[i], last_modified, file_extension, size))

        sub_set = set(self.list_of_extensions)
        sub_set.discard('')
        self.list_of_extensions = list(sub_set)
        # print(self.list_of_extensions)

    def get_readable_size(self, abs_path):
        if (os.path.isdir(abs_path)):
            size = 0
            for path, dirs, files in os.walk(abs_path):
                for f in files:
                    fp = os.path.join(path, f)
                    size += os.stat(fp).st_size

            size_in_byte = size

        else:
            size = os.path.getsize(abs_path)
            size_in_byte = size

        if (size >= 1099511627776):
            size = str(round(size/1099511627776, 2)) + " TB"
        elif (size >= 1073741824):
            size = str(round(size/1073741824, 2)) + " GB"
        elif (size >= 1048576):
            size = str(round(size/1048576, 2)) + " MB"
        elif (size >= 1024):
            size = str(round(size/1024, 2)) + " KB"
        else:
            size = str(size) + " B"
        return [size, size_in_byte]

    def treeview_sort_column(self, option):
        # clear all items in treeview
        for item in self.controller.view.treeview_file_frame.treeview_file.get_children():
            self.controller.view.treeview_file_frame.treeview_file.delete(item)

        self.ascending_sort = not self.ascending_sort

        # creat new list for sorted content
        self.sorted_content = self.directory_content.copy()

        if (option == 1):
            self.sorted_content = sorted(
                self.sorted_content, key=lambda x: x[0].lower(), reverse=self.ascending_sort)
            for file in self.sorted_content:
                self.controller.view.treeview_file_frame.treeview_file.insert(
                    '', tk.END, values=file)

        elif (option == 2):
            self.sorted_content = sorted(
                self.sorted_content, key=lambda x: x[1], reverse=self.ascending_sort)
            for file in self.sorted_content:
                self.controller.view.treeview_file_frame.treeview_file.insert(
                    '', tk.END, values=file)

        elif (option == 3):
            self.sorted_content = sorted(
                self.sorted_content, key=lambda x: x[2], reverse=self.ascending_sort)
            for file in self.sorted_content:
                self.controller.view.treeview_file_frame.treeview_file.insert(
                    '', tk.END, values=file)

        elif (option == 4):
            self.sorted_content = sorted(
                self.sorted_content, key=lambda x: x[4], reverse=self.ascending_sort)
            for file in self.sorted_content:
                self.controller.view.treeview_file_frame.treeview_file.insert(
                    '', tk.END, values=file)

    def display_changes(self):
        # Display change in treeview_file
        self.list_files_and_folders(self.path)

        # Display change in treeview_directory
        for i in self.controller.view.treeview_directory_frame.treeview_directory.get_children():
            self.controller.view.treeview_directory_frame.treeview_directory.delete(
                i)
        root_node = self.controller.view.treeview_directory_frame.treeview_directory.insert(
            '', 'end', text=self.path, open=True)
        self.process_directory(root_node, self.path)

    def process_directory(self, parent, path):
        for p in os.listdir(path):
            abspath = os.path.join(path, p)
            isdir = os.path.isdir(abspath)
            oid = self.controller.view.treeview_directory_frame.treeview_directory.insert(
                parent, 'end', text=p, open=False)
            if isdir:
                self.process_directory(oid, abspath)

    def reorganize_files_by_extensions(self):
        self.last_reorganize_type = 1

        if self.list_of_extensions:
            for extension in self.list_of_extensions:
                if (os.path.isdir(self.path + "/" + extension) == False):
                    os.mkdir(self.path + "/" + extension)

            for file in self.directory_content:
                if file[2]:
                    os.rename(self.path + "/" +
                              file[0], self.path + "/" + file[2] + "/" + file[0])

    def execute_reorganization(self):
        if (self.controller.view.sorting_menu_frame.selected_option.get() == 1):
            self.reorganize_files_by_extensions()
            self.display_changes()
            tk.messagebox.showinfo(
                "Information", "EXECUTED: Files have been reorganized into extension folders")

    def unexecute_reorganization(self):
        if (self.last_reorganize_type == 1):
            for extension_folder in self.list_of_extensions:
                for file in os.listdir(self.path + "/" + extension_folder):
                    os.rename(self.path + "/" + extension_folder +
                              "/" + file, self.path + "/" + file)

                os.rmdir(self.path + "/" + extension_folder)

            self.display_changes()
            tk.messagebox.showinfo(
                "Information", "UNEXECUTED: Files have been restore to the main directory")

        self.last_reorganize_type = 0


def main():
    pass


if __name__ == '__main__':
    main()
