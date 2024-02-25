import tkinter as tk
from tkhtmlview import HTMLLabel


class TriplesFrame(tk.Frame):

    def __init__(self, parent, parameter):
        super().__init__(parent)
        self.parameter = parameter
        self.parent = parent
        parent.title("Triples of the Data Model")

        #self.title("Large Image Viewer")
        self.show_Triples (parameter)

    def show_Triples(self,my_html):
        html_label = HTMLLabel(self.parent, html=my_html)
        html_label.pack(fill="both", expand=True)
        html_label.fit_height()


