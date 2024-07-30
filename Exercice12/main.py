

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' par {self.author}, ({self.year})"


class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self, book):
        # Ajoute un livre à la bibliothèque.
        if not any(
            b.title == book.title and
            b.author == book.author and
            b.year == book.year
            for b in self.books
        ):
            self.books.append(book)
        else:
            print(f"\nLe livre {book.title} se trouve déjà dans la "
                  "bibliothèque")

    def remove_book(self, book_title):
        # Supprime un livre de la bibliothèque en utilisant le titre du livre.
        book_found = False
        for book in self.books:
            if book_title == book.title:
                self.books.remove(book)
                print(f"{book_title} supprimé")
                book_found = True
                break
        if not book_found:
            print(f"Erreur : Le livre '{book_title}' est introuvable")

    def borrow_book(self, book_title):
        # Emprunte un livre de la bibliothèque en utilisant le titre du livre.
        # Le livre doit être retiré de la liste des livres disponibles.
        # Il doit aussi être ajouté dans la liste des livres empruntés.
        book_found = False
        for book in self.books:
            if book_title == book.title:
                self.books.remove(book)
                self.borrowed_books.append(book)
                print(f"{book_title} emprunté")
                book_found = True
                break
        if not book_found:
            print(f"Erreur : Le livre '{book_title}' est introuvable")

    def return_book(self, book_title):
        # Rend un livre emprunté en utilisant le titre du livre.
        # Le livre doit être retiré de la liste des livres empruntés.
        # Il doit aussi être ajouté dans la liste des livres disponibles.
        book_found = False
        for book in self.borrowed_books:
            if book_title == book.title:
                self.borrowed_books.remove(book)
                self.books.append(book)
                print(f"{book_title} rendu")
                book_found = True
                break
        if not book_found:
            print(f"Erreur : Le livre '{book_title}' est introuvable")

    def display_available_books(self):
        # Renvoie une liste des livres disponibles dans la bibliothèque.
        if not self.books:
            print("La bibliothèque est vide.")
        else:
            print("\nLivres disponibles dans la bibliothèque : "
                  f"{len(self.books)}\n")
            for book in self.books:
                print(book)

    def display_borrowed_books(self):
        # Renvoie une liste des livres empruntés de la bibliothèque.
        if not self.borrowed_books:
            print("Aucun livre n'a été emprunté.")
        else:
            print("\nLivres empruntés : "
                  f"{len(self.borrowed_books)}\n")
            for book in self.borrowed_books:
                print(book)


# Instanciation de Libre
library = Library()

# Instaciation d'une liste de Book
books = [
    Book("1984", "George Orwell", 1949),
    Book("Ne tirez pas sur l'oiseau moqueur", "Harper Lee", 1960),
    Book("Orgueil et Préjugés", "Jane Austen", 1813),
    Book("Gatsby le Magnifique", "F. Scott Fitzgerald", 1925),
    Book("Moby Dick", "Herman Melville", 1851),
    Book("Guerre et Paix", "Léon Tolstoï", 1869),
    Book("L'Attrape-Cœurs", "J.D. Salinger", 1951),
    Book("Le Hobbit", "J.R.R. Tolkien", 1937),
    Book("Le Meilleur des Mondes", "Aldous Huxley", 1932),
    Book("Jane Eyre", "Charlotte Brontë", 1847)
]


print("______________________________________________________________________")
print("\nTest des méthodes add_book() et display_available_books")
print("______________________________________________________________________")
for book in books:
    library.add_book(book)
library.display_available_books()


print("______________________________________________________________________")
print("\nTest de la méthode remove_book('Moby Dick')")
print("______________________________________________________________________")
library.remove_book("Moby Dick")
print(f"Nombre de livres dans la bibliothèque : {len(library.books)}")


print("______________________________________________________________________")
print("\nTest des méthodes borrow_book('Le Hobbit') et "
      "display_borrowed_books()")
print("______________________________________________________________________")
library.borrow_book("Le Hobbit")
library.borrow_book("Gatsby le Magnifique")
print(f"\nNombre de livres dans la bibliothèque : {len(library.books)}")
library.display_borrowed_books()

print("______________________________________________________________________")
print("\nTest de la méthode return_book('Le Hobbit')")
print("______________________________________________________________________")
library.return_book("Le Hobbit")
print(f"Nombre de livres dans la bibliothèque : {len(library.books)}")
print("Nombre de livres dans la liste des emprunts : "
      f"{len(library.borrowed_books)}"
      )
