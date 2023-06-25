import os
import tkinter as tk
from tkinter import filedialog, messagebox
import lxml.etree as ET

class MainForm(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("XML XSLT Converter")
        self.geometry("400x200")
        
        self.xml_file_path = tk.StringVar()
        self.xslt_file_path = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self, text="XML File Path:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self, textvariable=self.xml_file_path, width=40).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self, text="Select", command=self.select_xml_file).grid(row=0, column=2, padx=10, pady=10)
        
        tk.Label(self, text="XSLT File Path:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self, textvariable=self.xslt_file_path, width=40).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self, text="Select", command=self.select_xslt_file).grid(row=1, column=2, padx=10, pady=10)
        
        tk.Button(self, text="Convert", command=self.convert).grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        
    def select_xml_file(self):
        self.xml_file_path.set(filedialog.askopenfilename(filetypes=[("XML Files", "*.xml")]))
    
    def select_xslt_file(self):
        self.xslt_file_path.set(filedialog.askopenfilename(filetypes=[("XSLT Files", "*.xslt;*.xsl")]))
    
    def convert(self):
        xml_file_path = self.xml_file_path.get()
        xslt_file_path = self.xslt_file_path.get()
        
        if os.path.exists(xml_file_path) and os.path.exists(xslt_file_path):
            try:
                xml_tree = ET.parse(xml_file_path)
                
                xslt_tree = ET.parse(xslt_file_path)
                transform = ET.XSLT(xslt_tree)
                
                result_tree = transform(xml_tree)
                
                output_file_path = os.path.splitext(xml_file_path)[0] + "_output.xml"
                result_tree.write(output_file_path, pretty_print=True, encoding="utf-8")
                
                messagebox.showinfo("Success", "XML file has been converted and saved as {}".format(output_file_path))
            except Exception as ex:
                messagebox.showerror("Error", "An error occurred during conversion: {}".format(str(ex)))
        else:
            messagebox.showerror("Error", "Please select valid XML and XSLT files.")

if __name__ == "__main__":
    app = MainForm()
    app.mainloop()
