import tkinter as tk

BG_COLOR = "#070121"

class GUI():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Biblioteca")
        self.window.geometry("600x500")
        self.window.configure(bg=BG_COLOR)

        self.pages = []  # List to store references to the pages

    def run(self):
        self.window.mainloop()

    def destroy(self):
        self.window.destroy()

    def create_page(self, page_title):
        page = tk.Toplevel(self.window)
        page.title(page_title)
        page.geometry("600x500")
        page.configure(bg=BG_COLOR)
        self.pages.append(page)

    def createLabel(self, page, text):
        label = tk.Label(page, text=text, font=("Arial", 18), bg=BG_COLOR, fg="white", pady=10)
        label.pack()

    def createButton(self, page, text, command):
        button = tk.Button(page, text=text, command=command, bg="#0b0238", fg="white", font=("Arial", 12), pady=20, padx=10, bd=0)
        button.pack(pady=15)

    def createEntry(self, page):
        entry = tk.Entry(page)
        entry.pack()
        return entry

    def createText(self, page):
        text = tk.Text(page)
        text.pack()
        return text

    def createFrame(self, page):
        frame = tk.Frame(page)
        frame.pack()
        return frame

    def createListbox(self, page):
        listbox = tk.Listbox(page)
        listbox.pack()
        return listbox

    def createScrollbar(self, page, orient):
        scrollbar = tk.Scrollbar(page, orient=orient)
        scrollbar.pack()
        return scrollbar

    def createCanvas(self, page, width, height):
        canvas = tk.Canvas(page, width=width, height=height)
        canvas.pack()
        return canvas
    def createListbox(self):
        listbox = tk.Listbox(self.window)
        listbox.pack()
        return listbox
    
    def createScrollbar(self, orient):
        scrollbar = tk.Scrollbar(self.window, orient=orient)
        scrollbar.pack()
        return scrollbar
    
    def createCanvas(self, width, height):
        canvas = tk.Canvas(self.window, width=width, height=height)
        canvas.pack()
        return canvas