from tkinter import Tk
from tkinter import filedialog


def select_directory():
    root = Tk()
    root.withdraw()
    current_directory = filedialog.askdirectory()
    return current_directory