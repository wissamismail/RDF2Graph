from io import BytesIO
import requests
import tkinter as tk
from PIL import ImageTk, Image

class PhotoFrame(tk.Frame):

    def __init__(self, parent, parameter):
        super().__init__(parent)
        url = parameter

        parent.title("Graph of the data model")

        """Displays an image with scrollbars within a Tkinter frame."""
        # Load the image
        #url='https://www.w3.org/RDF/Validator/ARPServlet.tmp/servlet_11237861214816275720.png'
        self.response = requests.get(url)
        self.image_data = self.response.content
        self.image = Image.open(BytesIO(self.image_data))
        self.photo = ImageTk.PhotoImage(self.image)
        print(url)

        # Create a canvas and scrollbar
        self.canvas = tk.Canvas(self)
        self.v_scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.h_scrollbar = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set)

        # Pack canvas and scrollbars to the frame
        self.v_scrollbar.pack(side="right", fill="y")
        self.h_scrollbar.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Add image to the canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)

        # Update scroll region after the image is placed
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

