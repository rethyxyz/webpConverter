import os
from tkinter import Tk, Canvas
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image

def convert_to_png(file_path):
    try:
        img = Image.open(file_path)
        output_path = os.path.splitext(file_path)[0] + '.png'
        img.save(output_path, 'PNG')
        print(f"Converted and saved: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def on_drop(event):
    for file_path in root.tk.splitlist(event.data):
        if file_path.lower().endswith('.webp'):
            convert_to_png(file_path)
        else:
            print("Not a WEBP file. Please drop a WEBP file.")

root = TkinterDnD.Tk()
root.title('Drop WEBP and Convert to PNG')

root.geometry('200x200')
root.resizable(False, False)

canvas = Canvas(root, width=400, height=400, bg='lightgrey')
canvas.pack(fill='both', expand=True)

canvas.drop_target_register(DND_FILES)
canvas.dnd_bind('<<Drop>>', on_drop)

root.mainloop()