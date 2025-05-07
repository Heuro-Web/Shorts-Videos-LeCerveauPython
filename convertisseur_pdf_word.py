import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2docx import Converter
import os

def choisir_fichier():
    fichier = filedialog.askopenfilename(filetypes=[("Fichiers PDF", "*.pdf")])
    if fichier:
        entree_var.set(fichier)

def convertir_pdf():
    pdf = entree_var.get()
    if not pdf.endswith(".pdf"):
        messagebox.showerror("Erreur", "Veuillez choisir un fichier PDF valide.")
        return

    word = pdf.replace(".pdf", "_converted.docx")
    try:
        cv = Converter(pdf)
        cv.convert(word, start=0, end=None)
        cv.close()
        sortie_var.set(word)
        messagebox.showinfo("Succès\n\n", f"Conversion terminée !\n\nFichier : {word}")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

def ouvrir_fichier():
    fichier = sortie_var.get()
    if fichier and os.path.exists(fichier):
        os.startfile(fichier)
    else:
        messagebox.showwarning("Fichier introuvable", "Veuillez convertir un fichier d'abord.")

# Interface graphique
fenetre = tk.Tk()
fenetre.title("Convertisseur PDF vers Word")
fenetre.geometry("500x400")
fenetre.config(bg="black")

entree_var = tk.StringVar()
sortie_var = tk.StringVar()

tk.Label(fenetre, text="Fichier PDF :").pack(pady=5)
tk.Entry(fenetre, textvariable=entree_var, width=50).pack()
tk.Button(fenetre, text="Choisir un fichier",bg="green", fg="white", command=choisir_fichier).pack(pady=5)

tk.Button(fenetre, text="Convertir en Word",  command=convertir_pdf, bg="green", fg="white").pack(pady=10)

tk.Label(fenetre, text="Fichier Word :").pack(pady=5)
tk.Entry(fenetre, textvariable=sortie_var, width=50, state='readonly').pack()
tk.Button(fenetre, text="Ouvrir le fichier Word",bg="blue", fg="white", command=ouvrir_fichier).pack(pady=10)

fenetre.mainloop()