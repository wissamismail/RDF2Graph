import Graph
import Triples
from tkinter.font import Font
import seleniumFunctions
import tkinter as tk
from tkinter import filedialog

class MainFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create the browse button
        self.browse_button = tk.Button(window, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=0)

        # Create the text area
        self.text_area = tk.Text(window, height=10, width=50)
        self.text_area.grid(row=1, columnspan=2)

        # Create the validate button
        self.validate_button = tk.Button(window, text="Validate", command=self.validate_rdf)
        self.validate_button.grid(row=2, column=0)

        # Create the graph button
        self.graph_button = tk.Button(window, text="Graph", command=self.Open_graph)
        self.graph_button.grid(row=2, column=1)

        # Create the graph button
        self.graph_button = tk.Button(window, text="Triples", command=self.Open_Triples)
        self.graph_button.grid(row=2, column=2)

        # Create the validation label
        bold_font = Font(weight="bold")
        self.validation_label = tk.Label(window, text="", font=bold_font)
        self.validation_label.grid(row=3, columnspan=3)

        self.url = ''
        self.html = ''
    def browse_file(self):
        self.validation_label.config(text='')
        file_path = filedialog.askopenfilename(filetypes=[("RDF Files", "*.rdf"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_area.delete("1.0", tk.END)  # Clear previous content
                self.text_area.insert(tk.END, content)

    def validate_rdf(self):
        # Perform RDF validation logic here
        self.validation_label.config(text='Validation in Progress...')
        validation_text = self.text_area.get("1.0", "end")
        validation_result, image_src, htmlTable = seleniumFunctions.process_text(validation_text)
        self.validation_label.config(text=validation_result)
        if (self.validation_label == 'Fatal Error Messages'):
            self.validation_label.configure(fg="red")
        else:
            self.validation_label.configure(fg="Black")
        self.html = htmlTable
        self.url= image_src

    def Open_graph(self):
        new_window = tk.Toplevel(self.master)
        Graph_frame = Graph.PhotoFrame(new_window, self.url)
        Graph_frame.pack(expand=True, fill=tk.BOTH)

    def Open_Triples(self):
        new_window = tk.Toplevel(self.master)
        Triples_frame = Triples.TriplesFrame(new_window, self.html)
        Triples_frame.pack(expand=True, fill=tk.BOTH)


# Create the Tkinter window
window = tk.Tk()
window.title("RDF2Graph")
#window.geometry("800x550")

# Create the main frame
main_frame = MainFrame(window)

# Start the main event loop
window.mainloop()
