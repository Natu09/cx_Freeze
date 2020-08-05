import numpy as np
import tkinter as tk
import pkg_resources
pkg_resources.require("numpy==`1.13.3")  # modified to use specific numpy

version = np.__version__

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

print(version)


def hello():
    label1 = tk.Label(root, text='Hello World 1! Numpy Version: ', textvariable=version, fg='green',
                      font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)


button1 = tk.Button(text='Click Me', command=hello, bg='brown', fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()
