import tkinter as tk
from tkinter import ttk, filedialog
from alphabet import analyze_lexical

class AnalizadorLexico:
    def __init__(self, root):
        self.root = root
        #self.root.configure(bg='white')    # Cambiar color de fondo
        self.root.title("Analizador Léxico")
        self.root.geometry("1000x605")
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        self.read_button = tk.Button(self.root, text="Abrir archivo", font=("Arial", 11), command=self.open_file)
        self.read_button.pack(anchor='w', pady=15, padx=15)

        self.create_texts_frame()
        self.create_table()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

        with open(file_path, "r") as file:
            data = file.read()
        
        self.text_entry.delete(1.0, "end")
        self.text_entry.insert(1.0, data)


    def create_texts_frame(self):
        self.frame = tk.Frame(self.root, bd=2, relief="groove", padx=10)

        self.text_entry = tk.Text(self.frame, width=54, height=15, font=("Arial", 10))
        self.text_entry.grid(row=0, column=0, columnspan=2, pady=10)

        self.button = tk.Button(self.frame, text="Analizar Léxico", width=20, font=("Arial", 12), command=self.call_analyze_lexical)
        self.button.grid(row=0, column=2, pady=10, padx=10)

        self.text_output = tk.Text(self.frame, width=54, height=15, font=("Arial", 10))
        self.text_output.grid(row=0, column=3, columnspan=2, pady=10)

        self.frame.pack(fill="x", expand=True)

    def call_analyze_lexical(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        text = self.text_entry.get(1.0, "end")
        tokens = analyze_lexical(text)
        for word, token, token_value in tokens:
            self.tree.insert("", "end", values=(word, token, token_value))
        
        # Ejemplo de insertar datos en Treeview
        #self.tree.insert("", "end", values=("hola", "mundo", "cadena"))

    def create_table(self):
        self.tree = ttk.Treeview(self.root, columns=("Lexema", "Token", "Tipo"), show="headings")

        self.tree.heading('Lexema', text="Lexema")
        self.tree.heading('Token', text="Token")
        self.tree.heading('Tipo', text="#")

        self.tree.column('Lexema', anchor="center")
        self.tree.column('Token', anchor="center")
        self.tree.column('Tipo', anchor="center")

        self.tree.pack(pady=10, padx=10, fill="x", expand=True)




if __name__ == "__main__":
    root = tk.Tk()
    app = AnalizadorLexico(root)
    root.mainloop()