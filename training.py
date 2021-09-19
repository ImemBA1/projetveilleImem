import tkinter
import tkinter.messagebox

app = tkinter.Tk()
app.title("Projet Veille Prototype du TODO LIST")


def ajouter_tache():
    tache = entree.get()
    if tache != "":
        liste_tache.insert(tkinter.END, tache)
        entree.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Erreur Ajout", message="Vous devez entrer une tâche valide")


def supprimer_tache():
    try:
        tache = liste_tache.curselection()
        liste_tache.delete(tache)
    except ():
        tkinter.messagebox.showwarning(title="Erreur Suppression",
                                       message="Vous devez selectionner une tâche pour la supprimer")


liste_tache = tkinter.Listbox(app, height=20, width=50, bg="light blue")
entree = tkinter.Entry(app, width=50)
bouton_ajouter = tkinter.Button(app, text="Ajouter une tâche",
                                width=50, command=ajouter_tache, bg="blue", fg="white")
bouton_supp = tkinter.Button(app, text="Supprimer une tâche",
                             width=50, command=supprimer_tache, bg="blue", fg="white")

liste_tache.pack()
entree.pack()
bouton_ajouter.pack()
bouton_supp.pack()

app.mainloop()
